#!/usr/bin/env python3
"""
Quick alignment visualization without Snakemake/conda dependencies.
Generates a simple conservation plot.
"""
import sys

# Check if we have matplotlib
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("Error: matplotlib not installed. Creating a text summary instead.")
    # Create a simple text summary
    with open("results/alignment/cas_dual_mafft.fasta", "r") as f:
        lines = f.readlines()
    
    seqs = []
    current_seq = ""
    for line in lines:
        if line.startswith(">"):
            if current_seq:
                seqs.append(current_seq)
            current_seq = ""
        else:
            current_seq += line.strip()
    if current_seq:
        seqs.append(current_seq)
    
    # Simple conservation analysis
    total_pos = len(seqs[0])
    identical = sum(1 for i in range(total_pos) if all(s[i] == seqs[0][i] for s in seqs))
    
    with open("results/alignment/cas_dual_mafft.png.txt", "w") as out:
        out.write("Alignment Conservation Summary\n")
        out.write("==============================\n")
        out.write(f"Total positions: {total_pos}\n")
        out.write(f"Identical positions: {identical}\n")
        out.write(f"Percent identity: {100 * identical / total_pos:.1f}%\n")
        out.write("\nNote: Install matplotlib to generate graphical output.\n")
    
    print("Created text summary at results/alignment/cas_dual_mafft.png.txt")
    sys.exit(0)

# If matplotlib is available, create the plot
alignment_file = "results/alignment/cas_dual_mafft.fasta"

# Read sequences
sequences = []
current_seq = ""
with open(alignment_file, "r") as f:
    for line in f:
        if line.startswith(">"):
            if current_seq:
                sequences.append(current_seq)
            current_seq = ""
        else:
            current_seq += line.strip()
if current_seq:
    sequences.append(current_seq)

# Calculate conservation
alignment_length = len(sequences[0])
conservation = []

for i in range(alignment_length):
    column = [seq[i] for seq in sequences]
    non_gap = [aa for aa in column if aa != '-']
    if len(non_gap) == 0:
        conservation.append(0)
    elif len(set(non_gap)) == 1:
        conservation.append(1)
    else:
        conservation.append(0.5)

# Create plot
fig, ax = plt.subplots(figsize=(16, 6))
positions = np.arange(len(conservation))
ax.bar(positions, conservation, width=1.0, edgecolor='none', color='steelblue')

ax.set_xlabel('Alignment Position', fontsize=12)
ax.set_ylabel('Conservation Score', fontsize=12)
ax.set_title(f'FnCas9 vs FnCas12a Sequence Conservation\n{len(sequences)} sequences, {alignment_length} positions', fontsize=14)
ax.set_ylim(0, 1.1)
ax.set_xlim(0, len(conservation))
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig("results/alignment/cas_dual_mafft.png", dpi=150, bbox_inches='tight')
print("Created alignment visualization at results/alignment/cas_dual_mafft.png")