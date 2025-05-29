"""
Render an overlay PNG from original PDB files with proper coloring.
Creates a high-quality structural comparison visualization.
"""
from pymol import cmd
import os

# Fresh session
cmd.reinitialize()

# Load original PDB files
cmd.load("data/pdb/5B2O.pdb", "FnCas9")
cmd.load("data/pdb/6I1K.pdb", "FnCas12a")

# Apply distinct colors
cmd.color("firebrick", "FnCas9")
cmd.color("marine", "FnCas12a")

# Display settings
cmd.hide("everything")
cmd.show("cartoon")
cmd.set("cartoon_fancy_helices", 1)
cmd.set("cartoon_transparency", 0.0)
cmd.bg_color("white")
cmd.set("ray_shadows", 0)
cmd.set("ambient", 0.4)
cmd.set("specular", 0.2)

# Align structures for overlay
cmd.align("FnCas12a", "FnCas9")

# Orient and zoom
cmd.orient()
cmd.zoom("all", buffer=5)

# Render high quality image
cmd.ray(1600, 1200)
cmd.png(snakemake.output[0], dpi=300)