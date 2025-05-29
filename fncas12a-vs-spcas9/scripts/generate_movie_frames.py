#!/usr/bin/env python3
"""
Generate rotation movie frames for SpCas9 vs FnCas9
"""
from pymol import cmd
import os
import sys

# Create output directory
output_dir = "results/pymol/movie_frames"
os.makedirs(output_dir, exist_ok=True)

# Initialize PyMOL
cmd.reinitialize()

# Load structures
cmd.load("data/pdb/5F9R.pdb", "SpCas9")
cmd.load("data/pdb/5B2O.pdb", "FnCas9")

# Align structures
cmd.align("FnCas9", "SpCas9")

# Apply colors
cmd.color("firebrick", "SpCas9")
cmd.color("marine", "FnCas9")

# Display settings
cmd.hide("everything")
cmd.show("cartoon")
cmd.set("cartoon_fancy_helices", 1)
cmd.bg_color("white")
cmd.set("ray_shadows", 0)

# Orient and zoom
cmd.orient()
cmd.zoom("all", buffer=5)

# Generate frames
print(f"Generating movie frames in {output_dir}...")
for i in range(36):  # 36 frames, 10 degrees each = 360 degrees
    cmd.turn("y", 10)
    cmd.ray(800, 600)  # Smaller size for GIF
    frame_path = f"{output_dir}/frame_{i:03d}.png"
    cmd.png(frame_path)
    print(f"  Frame {i+1}/36: {frame_path}")

print(f"\nGenerated 36 frames in {output_dir}/")
print("Now you can create the GIF with:")
print(f"  python3 scripts/create_movie.py {output_dir} results/pymol/rotation.gif")