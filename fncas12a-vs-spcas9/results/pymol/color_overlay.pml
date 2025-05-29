# PyMOL script for FnCas12a vs SpCas9 overlay visualization
# Generated for convergent evolution comparison

# Clear everything and load structures
reinitialize

# Load the overlay file from TM-align
load results/struct/Fn_overlay.pdb
split_states Fn_overlay

# Style settings
hide everything
show cartoon
set cartoon_fancy_helices, 1
set cartoon_fancy_sheets, 1

# Color scheme
# FnCas12a in salmon
color salmon, Fn_overlay_0001
# SpCas9 in light blue
color lightblue, Fn_overlay_0002

# Set transparency for better visualization
set cartoon_transparency, 0.1, Fn_overlay_0001
set cartoon_transparency, 0.1, Fn_overlay_0002

# Background and display settings
bg_color white
set ray_opaque_background, 1
set depth_cue, 0
set specular, 0.3
set antialias, 2

# Optimal view
orient
zoom complete, 5

# Save image
ray 2400, 1800
png results/pymol/Fn_overlay.png

# Print completion message
print "Overlay visualization complete!"
print "Image saved as: results/pymol/Fn_overlay.png"