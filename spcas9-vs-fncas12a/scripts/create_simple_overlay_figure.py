#!/usr/bin/env python3
"""
Create a simple overlay visualization figure without PyMOL.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Left panel - Structural overlay representation
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect('equal')

# Draw protein shapes (simplified representation)
# SpCas9 - bi-lobed structure
spcas9_rec = FancyBboxPatch((1, 3), 3, 4, boxstyle="round,pad=0.1", 
                           facecolor='lightblue', edgecolor='darkblue', 
                           linewidth=2, alpha=0.7)
spcas9_nuc = FancyBboxPatch((4.5, 2), 3, 5, boxstyle="round,pad=0.1",
                           facecolor='lightblue', edgecolor='darkblue',
                           linewidth=2, alpha=0.7)
ax1.add_patch(spcas9_rec)
ax1.add_patch(spcas9_nuc)

# FnCas12a - wedge structure (offset to show non-alignment)
fncas12a = patches.Polygon([[2, 1], [7, 2], [6, 7], [3, 6]], 
                          facecolor='salmon', edgecolor='darkred',
                          linewidth=2, alpha=0.7)
ax1.add_patch(fncas12a)

# Add labels
ax1.text(2.5, 8.5, 'SpCas9', fontsize=14, weight='bold', color='darkblue')
ax1.text(4.5, 0.5, 'FnCas12a', fontsize=14, weight='bold', color='darkred')
ax1.text(5, 9.5, 'Structural Overlay', fontsize=16, weight='bold', ha='center')

ax1.axis('off')

# Right panel - Metrics
ax2.axis('off')
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)

# Title
ax2.text(0.5, 0.9, 'SpCas9 vs FnCas12a Comparison', 
         fontsize=18, weight='bold', ha='center')

# Metrics box
metrics_text = """Structural Metrics:
• RMSD: 10.23 Å
• TM-score: 0.217
• Sequence Identity: 7.0%
• Aligned residues: 472

Evolutionary Pattern:
CONVERGENT EVOLUTION

Key Differences:
• Type II vs Type V systems
• Different domain architectures
• Independent evolutionary origins
• Similar function, different structure"""

ax2.text(0.5, 0.45, metrics_text, fontsize=12, ha='center', va='center',
         bbox=dict(boxstyle="round,pad=0.5", facecolor='lightyellow', 
                  edgecolor='black', linewidth=2))

# Save figure
plt.tight_layout()
plt.savefig('results/pymol/Fn_overlay.png', dpi=300, bbox_inches='tight')
print("Created overlay figure at results/pymol/Fn_overlay.png")