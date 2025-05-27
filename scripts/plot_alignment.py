"""
Generate alignment visualization using matplotlib.
Creates a conservation plot showing sequence identity along the alignment.
"""
import matplotlib
matplotlib.use('Agg')  # For headless operation
import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO

# Read alignment
alignment_file = snakemake.input[0]
sequences = list(SeqIO.parse(alignment_file, "fasta"))

# Calculate conservation score at each position
alignment_length = len(sequences[0].seq)
conservation = []

for i in range(alignment_length):
    column = [seq.seq[i] for seq in sequences]
    # Skip gap positions
    non_gap = [aa for aa in column if aa != '-']
    if len(non_gap) == 0:
        conservation.append(0)
    elif len(set(non_gap)) == 1:
        conservation.append(1)  # Identical
    else:
        conservation.append(0.5)  # Similar but not identical

# Create plot
fig, ax = plt.subplots(1, 1, figsize=(16, 6))

# Plot conservation as bar chart
positions = np.arange(len(conservation))
ax.bar(positions, conservation, width=1.0, edgecolor='none')

# Customize plot
ax.set_xlabel('Alignment Position', fontsize=12)
ax.set_ylabel('Conservation Score', fontsize=12)
ax.set_title(f'FnCas9 vs FnCas12a Sequence Conservation\n{len(sequences)} sequences, {alignment_length} positions', fontsize=14)
ax.set_ylim(0, 1.1)
ax.set_xlim(0, len(conservation))

# Add grid
ax.grid(True, alpha=0.3, axis='y')

# Color scheme
ax.set_facecolor('#f5f5f5')
fig.patch.set_facecolor('white')

# Save figure
plt.tight_layout()
plt.savefig(snakemake.output[0], dpi=150, bbox_inches='tight')
plt.close()