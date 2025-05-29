"""
Enhanced PyMOL rendering script for FnCas9 vs FnCas12a structural comparison.
Generates multiple views with domain annotations and a rotation movie.

Author: Vishal Bharti
Date: 2025-05-27
"""
from pymol import cmd
import os

# Configuration
output_dir = os.path.dirname(snakemake.output[0])
basename = os.path.basename(snakemake.output[0]).replace('.png', '')

# Fresh session
cmd.reinitialize()

# Load the TM-align overlay PDB
cmd.load(snakemake.input.overlay, "overlay")

# Split into separate objects by state/model
# TM-align outputs model 1 as reference, model 2 as mobile
cmd.split_states("overlay")

# Check what objects were created
all_objects = cmd.get_object_list()
print(f"Objects after split_states: {all_objects}")

# Rename based on what's actually created
if "overlay_0001" in all_objects and "overlay_0002" in all_objects:
    cmd.set_name("overlay_0001", "FnCas9")
    cmd.set_name("overlay_0002", "FnCas12a")
elif len(all_objects) >= 2:
    # Sometimes PyMOL creates different names
    cmd.set_name(all_objects[0], "FnCas9")
    cmd.set_name(all_objects[1], "FnCas12a")
else:
    # Fallback: work with the original overlay
    cmd.create("FnCas9", "overlay and state 1")
    cmd.create("FnCas12a", "overlay and state 2")

# Delete the original overlay object
cmd.delete("overlay")

# Color schemes
cmd.color("firebrick", "FnCas9")
cmd.color("marine", "FnCas12a")

# Display settings
cmd.hide("everything", "all")
cmd.show("cartoon", "all")
cmd.set("cartoon_transparency", 0.0)
cmd.set("cartoon_fancy_helices", 1)
cmd.set("cartoon_highlight_color", "grey50")
cmd.set("cartoon_side_chain_helper", 1)

# Domain definitions for FnCas9 (approximate residue ranges based on literature)
# REC lobe: ~1-500, NUC lobe: ~500-1455
# RuvC domain: ~1-200, 500-800, HNH domain: ~800-1000
cas9_domains = {
    "REC_lobe": "FnCas9 and resi 1-500",
    "NUC_lobe": "FnCas9 and resi 501-1455",
    "RuvC": "FnCas9 and (resi 1-200 or resi 500-800)",
    "HNH": "FnCas9 and resi 800-1000"
}

# Domain definitions for FnCas12a (approximate)
# RuvC-like domain is the main catalytic domain
cas12a_domains = {
    "REC": "FnCas12a and resi 1-600",
    "NUC": "FnCas12a and resi 601-1282",
    "RuvC_like": "FnCas12a and resi 800-1100"
}

# Create domain selections
for name, selection in cas9_domains.items():
    cmd.select(f"Cas9_{name}", selection)
    
for name, selection in cas12a_domains.items():
    cmd.select(f"Cas12a_{name}", selection)

# Highlight specific domains with different shades
cmd.color("salmon", "Cas9_REC_lobe")
cmd.color("tv_red", "Cas9_NUC_lobe")
cmd.color("lightblue", "Cas12a_REC")
cmd.color("tv_blue", "Cas12a_NUC")

# Background and general settings
cmd.bg_color("white")
cmd.set("ray_shadows", 0)
cmd.set("specular", 0.2)
cmd.set("ambient", 0.4)
cmd.set("ray_trace_fog", 0)
cmd.set("depth_cue", 0)

# Function to add labels
def add_labels(view_name):
    """Add domain labels for current view"""
    # Clear previous labels
    cmd.delete("labels*")
    
    if view_name in ["front", "side"]:
        # Label major domains
        cmd.pseudoatom("label_cas9_rec", pos=cmd.get_coords("Cas9_REC_lobe", 1))
        cmd.label("label_cas9_rec", '"Cas9 REC"')
        
        cmd.pseudoatom("label_cas9_nuc", pos=cmd.get_coords("Cas9_NUC_lobe", 1))
        cmd.label("label_cas9_nuc", '"Cas9 NUC"')
        
        cmd.pseudoatom("label_cas12a", pos=cmd.get_coords("FnCas12a", 1))
        cmd.label("label_cas12a", '"Cas12a"')

# View 1: Front view (default orientation)
cmd.orient()
cmd.zoom("all", buffer=5)
add_labels("front")
cmd.ray(1600, 1200)
cmd.png(f"{output_dir}/{basename}_front.png", dpi=300)

# View 2: Side view (90-degree rotation)
cmd.turn("y", 90)
add_labels("side")
cmd.ray(1600, 1200)
cmd.png(f"{output_dir}/{basename}_side.png", dpi=300)

# View 3: Top view
cmd.turn("y", -90)  # Reset
cmd.turn("x", 90)
cmd.ray(1600, 1200)
cmd.png(f"{output_dir}/{basename}_top.png", dpi=300)

# View 4: Active site zoom (RuvC domains)
cmd.orient()
cmd.zoom("Cas9_RuvC or Cas12a_RuvC_like", buffer=10)
cmd.hide("labels")
# Show some side chains in active site
cmd.show("sticks", "(Cas9_RuvC or Cas12a_RuvC_like) and (resn ASP+GLU+HIS)")
cmd.color("yellow", "(Cas9_RuvC or Cas12a_RuvC_like) and (resn ASP+GLU+HIS) and elem C")
cmd.ray(1600, 1200)
cmd.png(f"{output_dir}/{basename}_active_site.png", dpi=300)

# View 5: Structural differences highlighted
cmd.orient()
cmd.zoom("all", buffer=5)
cmd.hide("sticks")
# Show regions with high RMSD as thicker cartoon
cmd.cartoon("putty", "all")
cmd.set("cartoon_putty_scale_min", 0.5)
cmd.set("cartoon_putty_scale_max", 4.0)
cmd.spectrum("b", "blue_white_red", "all", minimum=0, maximum=20)
cmd.ray(1600, 1200)
cmd.png(f"{output_dir}/{basename}_rmsd.png", dpi=300)

# Reset for final overview
cmd.cartoon("automatic")
cmd.orient()
cmd.zoom("all", buffer=5)

# Add annotation text (as a separate image that can be composited)
annotation_text = """
Key Differences:
• Cas9: Bilobed architecture (REC + NUC)
• Cas9: Two nuclease domains (RuvC + HNH)
• Cas12a: More compact structure
• Cas12a: Single RuvC-like domain
• Different PAM recognition mechanisms
"""

# Save annotation info
with open(f"{output_dir}/{basename}_annotations.txt", "w") as f:
    f.write(annotation_text)

# Generate rotation movie
if True:  # Set to True to generate movie
    cmd.orient()
    cmd.zoom("all", buffer=5)
    
    # Movie settings
    frames = 360
    cmd.mset(f"1 x{frames}")
    
    # Simple Y-axis rotation
    for frame in range(frames):
        cmd.frame(frame + 1)
        cmd.turn("y", 1)
    
    # Save movie frames
    movie_dir = f"{output_dir}/movie_frames"
    os.makedirs(movie_dir, exist_ok=True)
    
    # Save key frames for GIF creation
    for i in range(0, 360, 10):  # Every 10 degrees
        cmd.frame(i + 1)
        cmd.ray(800, 600)  # Smaller size for GIF
        cmd.png(f"{movie_dir}/frame_{i:03d}.png")

# Create the main output file (overview)
cmd.orient()
cmd.zoom("all", buffer=5)
cmd.set("cartoon_transparency", 0.0)
cmd.color("firebrick", "FnCas9")
cmd.color("marine", "FnCas12a")
add_labels("front")
cmd.ray(1600, 1200)
cmd.png(snakemake.output[0], dpi=300)

# Save session for manual exploration
cmd.save(f"{output_dir}/{basename}.pse")

print(f"Generated enhanced visualizations in {output_dir}")
print("Files created:")
print(f"  - {basename}_front.png")
print(f"  - {basename}_side.png") 
print(f"  - {basename}_top.png")
print(f"  - {basename}_active_site.png")
print(f"  - {basename}_rmsd.png")
print(f"  - {basename}_annotations.txt")
print(f"  - {basename}.pse (PyMOL session)")
print(f"  - movie_frames/ (for GIF creation)")