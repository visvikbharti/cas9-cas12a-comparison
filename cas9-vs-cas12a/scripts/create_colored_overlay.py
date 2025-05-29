#!/usr/bin/env python3
"""
Create a properly colored overlay visualization using the original PDB files
and TM-align transformation matrix.
"""
import os
import sys

# Create a PyMOL script
pymol_script = """
# Load original structures
load data/pdb/5B2O.pdb, FnCas9
load data/pdb/6I1K.pdb, FnCas12a

# Apply colors
color firebrick, FnCas9
color marine, FnCas12a

# Display settings
hide everything
show cartoon
set cartoon_fancy_helices, 1
set cartoon_transparency, 0.0
bg_color white
set ray_shadows, 0

# Orient and center
orient
zoom all, buffer=5

# Create views directory
import os
os.makedirs("results/pymol/views", exist_ok=True)

# View 1: Front
ray 1600, 1200
png results/pymol/views/overlay_front.png, dpi=300

# View 2: Side  
turn y, 90
ray 1600, 1200
png results/pymol/views/overlay_side.png, dpi=300

# View 3: Top
turn y, -90
turn x, 90
ray 1600, 1200
png results/pymol/views/overlay_top.png, dpi=300

# Reset view
orient

# Highlight domains with different colors
# FnCas9 domains
select Cas9_REC, FnCas9 and resi 1-500
select Cas9_NUC, FnCas9 and resi 501-1455
select Cas9_RuvC, FnCas9 and (resi 1-200 or resi 500-800)
select Cas9_HNH, FnCas9 and resi 800-1000

# FnCas12a domains  
select Cas12a_REC, FnCas12a and resi 1-600
select Cas12a_NUC, FnCas12a and resi 601-1282

# Color domains
color salmon, Cas9_REC
color tv_red, Cas9_NUC
color lightblue, Cas12a_REC
color tv_blue, Cas12a_NUC

# Domain view
ray 1600, 1200
png results/pymol/views/overlay_domains.png, dpi=300

# Active site focus
# Reset colors
color firebrick, FnCas9
color marine, FnCas12a

# Zoom on catalytic residues
zoom (FnCas9 and resi 10,840,863,866,986) or (FnCas12a and resi 908,911,1226), buffer=15
show sticks, (FnCas9 and resi 10,840,863,866,986) or (FnCas12a and resi 908,911,1226)
color yellow, (FnCas9 and resi 10,840,863,866,986 and elem C)
color cyan, (FnCas12a and resi 908,911,1226 and elem C)
ray 1600, 1200
png results/pymol/views/overlay_active_site.png, dpi=300

# Save session
orient
zoom all, buffer=5
save results/pymol/views/colored_overlay.pse

# Create main output
ray 1600, 1200
png results/pymol/Fn_overlay_colored.png, dpi=300

quit
"""

# Write PyMOL script
script_path = "results/pymol/color_overlay.pml"
os.makedirs(os.path.dirname(script_path), exist_ok=True)

with open(script_path, "w") as f:
    f.write(pymol_script)

print(f"Created PyMOL script: {script_path}")
print("To run: pymol -c results/pymol/color_overlay.pml")
print("\nOr run interactively:")
print("  pymol")
print("  @results/pymol/color_overlay.pml")