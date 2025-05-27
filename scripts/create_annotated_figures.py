#!/usr/bin/env python3
"""
Create annotated figures with domain labels for FnCas9 vs FnCas12a comparison.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import os

# Create output directory
output_dir = "results/pymol/annotated"
os.makedirs(output_dir, exist_ok=True)

def add_annotations(image_path, output_path, annotations):
    """Add text annotations to an image."""
    # Load image
    img = Image.open(image_path)
    
    # Create figure
    fig, ax = plt.subplots(1, 1, figsize=(12, 9))
    ax.imshow(img)
    ax.axis('off')
    
    # Add annotations
    for ann in annotations:
        if ann['type'] == 'text':
            ax.text(ann['x'], ann['y'], ann['text'], 
                   fontsize=ann.get('fontsize', 14),
                   color=ann.get('color', 'black'),
                   weight=ann.get('weight', 'bold'),
                   bbox=dict(boxstyle="round,pad=0.3", 
                            facecolor=ann.get('bgcolor', 'white'),
                            alpha=0.8,
                            edgecolor='black'))
        elif ann['type'] == 'arrow':
            ax.annotate('', xy=(ann['x2'], ann['y2']), 
                       xytext=(ann['x1'], ann['y1']),
                       arrowprops=dict(arrowstyle='->', 
                                     color=ann.get('color', 'black'),
                                     lw=2))
    
    # Save figure
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Created: {output_path}")

# Annotate domain-colored view
domain_annotations = [
    {'type': 'text', 'x': 200, 'y': 100, 'text': 'FnCas9', 'fontsize': 18, 'color': 'darkred'},
    {'type': 'text', 'x': 1200, 'y': 100, 'text': 'FnCas12a', 'fontsize': 18, 'color': 'darkblue'},
    {'type': 'text', 'x': 300, 'y': 300, 'text': 'REC lobe', 'fontsize': 14, 'color': 'black', 'bgcolor': 'salmon'},
    {'type': 'text', 'x': 400, 'y': 500, 'text': 'NUC lobe', 'fontsize': 14, 'color': 'white', 'bgcolor': 'darkred'},
    {'type': 'text', 'x': 1000, 'y': 300, 'text': 'REC domain', 'fontsize': 14, 'color': 'black', 'bgcolor': 'lightblue'},
    {'type': 'text', 'x': 900, 'y': 500, 'text': 'NUC domain', 'fontsize': 14, 'color': 'white', 'bgcolor': 'darkblue'},
    {'type': 'arrow', 'x1': 350, 'y1': 330, 'x2': 400, 'y2': 380, 'color': 'black'},
    {'type': 'arrow', 'x1': 450, 'y1': 530, 'x2': 500, 'y2': 580, 'color': 'black'},
]

if os.path.exists("results/pymol/views/domains_colored.png"):
    add_annotations("results/pymol/views/domains_colored.png", 
                   f"{output_dir}/domains_annotated.png",
                   domain_annotations)

# Annotate front view with key differences
front_annotations = [
    {'type': 'text', 'x': 100, 'y': 100, 'text': 'FnCas9 vs FnCas12a Structural Overlay', 
     'fontsize': 20, 'weight': 'bold'},
    {'type': 'text', 'x': 100, 'y': 1100, 'text': 'Key Differences:', 'fontsize': 16, 'weight': 'bold'},
    {'type': 'text', 'x': 100, 'y': 1140, 'text': '• Cas9: Bilobed architecture (REC + NUC)', 'fontsize': 14},
    {'type': 'text', 'x': 100, 'y': 1170, 'text': '• Cas9: Two nuclease domains (RuvC + HNH)', 'fontsize': 14},
    {'type': 'text', 'x': 100, 'y': 1200, 'text': '• Cas12a: More compact structure', 'fontsize': 14},
    {'type': 'text', 'x': 100, 'y': 1230, 'text': '• Cas12a: Single RuvC-like domain', 'fontsize': 14},
]

if os.path.exists("results/pymol/views/front_view.png"):
    add_annotations("results/pymol/views/front_view.png",
                   f"{output_dir}/front_annotated.png",
                   front_annotations)

# Create composite figure panel
def create_composite_panel():
    """Create a multi-panel figure combining different views."""
    # Load images
    views = {
        'front': "results/pymol/views/front_view.png",
        'side': "results/pymol/views/side_view.png",
        'domains': "results/pymol/views/domains_colored.png",
        'active': "results/pymol/views/active_site_zoom.png"
    }
    
    # Check if all files exist
    if not all(os.path.exists(path) for path in views.values()):
        print("Warning: Not all view files exist")
        return
    
    # Create figure with subplots
    fig = plt.figure(figsize=(16, 12))
    
    # Panel A: Front view
    ax1 = plt.subplot(2, 2, 1)
    img1 = Image.open(views['front'])
    ax1.imshow(img1)
    ax1.set_title('A. Front View', fontsize=16, weight='bold', loc='left')
    ax1.axis('off')
    
    # Panel B: Side view
    ax2 = plt.subplot(2, 2, 2)
    img2 = Image.open(views['side'])
    ax2.imshow(img2)
    ax2.set_title('B. Side View (90° rotation)', fontsize=16, weight='bold', loc='left')
    ax2.axis('off')
    
    # Panel C: Domain colored
    ax3 = plt.subplot(2, 2, 3)
    img3 = Image.open(views['domains'])
    ax3.imshow(img3)
    ax3.set_title('C. Domain Architecture', fontsize=16, weight='bold', loc='left')
    ax3.axis('off')
    
    # Panel D: Active site
    ax4 = plt.subplot(2, 2, 4)
    img4 = Image.open(views['active'])
    ax4.imshow(img4)
    ax4.set_title('D. Active Site Residues', fontsize=16, weight='bold', loc='left')
    ax4.axis('off')
    
    # Add main title
    fig.suptitle('Structural Comparison of FnCas9 and FnCas12a', 
                 fontsize=20, weight='bold', y=0.98)
    
    # Add color legend
    legend_text = 'FnCas9 (red) | FnCas12a (blue)'
    fig.text(0.5, 0.02, legend_text, ha='center', fontsize=14)
    
    # Adjust layout
    plt.tight_layout()
    plt.subplots_adjust(top=0.94, bottom=0.05)
    
    # Save composite
    output_path = f"{output_dir}/composite_panel.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Created composite panel: {output_path}")

# Create composite panel
create_composite_panel()

# Create a publication-ready figure with detailed annotations
def create_publication_figure():
    """Create a publication-quality figure with detailed annotations."""
    fig = plt.figure(figsize=(18, 10))
    
    # Main image
    ax_main = plt.subplot(1, 2, 1)
    if os.path.exists("results/pymol/views/domains_colored.png"):
        img = Image.open("results/pymol/views/domains_colored.png")
        ax_main.imshow(img)
    ax_main.axis('off')
    
    # Annotation panel
    ax_text = plt.subplot(1, 2, 2)
    ax_text.axis('off')
    
    # Add structured annotations
    annotations_text = """
STRUCTURAL COMPARISON

Francisella novicida Cas9 (FnCas9)
• Type II-A CRISPR nuclease
• 1,455 amino acids
• Bilobed architecture:
  - REC lobe (residues 1-500)
  - NUC lobe (residues 501-1455)
• Two nuclease domains:
  - RuvC (1-200, 500-800)
  - HNH (800-1000)
• PAM: 5'-NGG-3'
• Cleavage: Blunt ends

Francisella novicida Cas12a (FnCas12a)
• Type V-A CRISPR nuclease  
• 1,282 amino acids
• Compact architecture:
  - REC domain (1-600)
  - NUC domain (601-1282)
• Single RuvC-like domain
• PAM: 5'-TTN-3'
• Cleavage: Staggered (5' overhang)

Key Structural Differences
• Overall fold divergence
• Different domain organization
• Distinct PAM recognition
• Alternative cleavage mechanisms
"""
    
    ax_text.text(0.05, 0.95, annotations_text, 
                transform=ax_text.transAxes,
                fontsize=12, 
                verticalalignment='top',
                fontfamily='monospace',
                bbox=dict(boxstyle="round,pad=0.5", 
                         facecolor='lightgray',
                         alpha=0.8))
    
    plt.suptitle('FnCas9 vs FnCas12a: Structural and Functional Comparison', 
                fontsize=18, weight='bold')
    
    output_path = f"{output_dir}/publication_figure.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Created publication figure: {output_path}")

create_publication_figure()

print(f"\nAll annotated figures created in {output_dir}/")
print("Files created:")
print("  - domains_annotated.png (with domain labels)")
print("  - front_annotated.png (with key differences)")
print("  - composite_panel.png (4-panel view)")
print("  - publication_figure.png (detailed comparison)")