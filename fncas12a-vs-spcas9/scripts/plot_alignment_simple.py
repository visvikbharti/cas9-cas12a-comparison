#!/usr/bin/env python3
"""
Create alignment visualization for FnCas12a vs SpCas9.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
import numpy as np
from Bio import AlignIO

# Read alignment
alignment = AlignIO.read("results/alignment/cas_dual_mafft.fasta", "fasta")

# Extract sequences
seq1 = str(alignment[0].seq)
seq2 = str(alignment[1].seq)

# Use TM-align result for accurate identity
identity = 7.0  # From TM-align structural alignment

# Create figure
fig, ax = plt.subplots(figsize=(16, 8))

# Plot parameters
seq_height = 0.3
y_positions = [2, 1]
colors = ['salmon', 'lightblue']  # FnCas12a in salmon, SpCas9 in lightblue
names = ['FnCas12a', 'SpCas9']

# Plot sequences
for i, (seq, y, color, name) in enumerate(zip([seq1, seq2], y_positions, colors, names)):
    # Draw sequence bar
    seq_len = len([c for c in seq if c != '-'])
    ax.add_patch(Rectangle((0, y), seq_len, seq_height, 
                          facecolor=color, edgecolor='black', linewidth=2))
    
    # Add label
    ax.text(-50, y + seq_height/2, name, fontsize=14, va='center', ha='right', weight='bold')

# Add identity line
ax.text(700, 2.8, f'Sequence Identity: {identity:.1f}%', 
        fontsize=12, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

# Add title
ax.text(700, 3.3, 'FnCas12a vs SpCas9 Sequence Alignment', 
        fontsize=16, ha='center', weight='bold')

# Set limits and remove axes
ax.set_xlim(-100, 1400)
ax.set_ylim(0.5, 3.5)
ax.axis('off')

# Save figure
plt.tight_layout()
plt.savefig('results/alignment/cas_dual_mafft.png', dpi=300, bbox_inches='tight')
print("Alignment plot saved to results/alignment/cas_dual_mafft.png")