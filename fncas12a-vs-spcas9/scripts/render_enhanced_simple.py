#!/usr/bin/env python3
"""
Enhanced PyMOL rendering - standalone version
Works directly with TM-align output
"""
from pymol import cmd
import sys

# Get input/output from command line or use defaults
pdb_file = sys.argv[1] if len(sys.argv) > 1 else "results/struct/Fn_overlay.pdb"
output_base = sys.argv[2] if len(sys.argv) > 2 else "results/pymol/enhanced"

# Initialize PyMOL
cmd.reinitialize()

# Load the structure
cmd.load(pdb_file, "overlay")

# Check if we have multiple models/chains
all_chains = cmd.get_chains("overlay")
print(f"Chains found: {all_chains}")

# TM-align often outputs structures as different chains
if len(all_chains) >= 2:
    # Create separate objects for each chain
    cmd.create("FnCas9", f"overlay and chain {all_chains[0]}")
    cmd.create("FnCas12a", f"overlay and chain {all_chains[1]}")
    cmd.delete("overlay")
else:
    # Try to work with the single structure
    # Split by B-factor or occupancy if possible
    cmd.create("structure", "overlay")
    cmd.delete("overlay")

# Get final object list
objects = cmd.get_object_list()
print(f"Final objects: {objects}")

# Color the structures
if "FnCas9" in objects and "FnCas12a" in objects:
    cmd.color("firebrick", "FnCas9")
    cmd.color("marine", "FnCas12a")
else:
    # Single structure - color by secondary structure
    cmd.color("red", "ss h")  # helices
    cmd.color("yellow", "ss s")  # sheets
    cmd.color("green", "ss l+''")  # loops

# Display settings
cmd.hide("everything", "all")
cmd.show("cartoon", "all")
cmd.set("cartoon_fancy_helices", 1)
cmd.set("cartoon_side_chain_helper", 0)
cmd.bg_color("white")
cmd.set("ray_shadows", 0)

# View 1: Overview
cmd.orient()
cmd.zoom("all", buffer=5)
cmd.ray(1600, 1200)
cmd.png(f"{output_base}_overview.png", dpi=300)

# View 2: Side view
cmd.turn("y", 90)
cmd.ray(1600, 1200)
cmd.png(f"{output_base}_side.png", dpi=300)

# View 3: Top view
cmd.turn("y", -90)
cmd.turn("x", 90)
cmd.ray(1600, 1200)
cmd.png(f"{output_base}_top.png", dpi=300)

# Save session
cmd.save(f"{output_base}.pse")

print(f"Created visualizations:")
print(f"  - {output_base}_overview.png")
print(f"  - {output_base}_side.png")
print(f"  - {output_base}_top.png")
print(f"  - {output_base}.pse")