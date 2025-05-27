"""
Render an overlay PNG from a TM-align superposed PDB.

Colours:
  * FnCas9 chain -> red
  * FnCas12a chain -> blue

The script receives via Snakemake:
  input.overlay : superposed PDB
  output[0]     : target PNG path
"""
from pymol import cmd

# Fresh session
cmd.reinitialize()

# Load overlay and split by model (TM-align writes model 1 & 2)
cmd.load(snakemake.input.overlay, "overlay")
models = cmd.get_object_list('overlay')  # ['overlay', 'overlay_0001'] etc.
if len(models) >= 2:
    cmd.color("red",  models[0])
    cmd.color("blue", models[1])

cmd.hide("everything")
cmd.show("cartoon")
cmd.set("cartoon_transparency", 0.15)
cmd.bg_color("white")
cmd.png(snakemake.output[0], dpi=900, ray=1, width=1600, height=1200)