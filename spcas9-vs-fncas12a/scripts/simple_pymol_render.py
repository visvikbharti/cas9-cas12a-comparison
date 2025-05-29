#!/usr/bin/env python3
import os

# Create PyMOL script
pymol_script = """
# Load structures
load results/struct/Fn_overlay.pdb
split_states Fn_overlay

# Style and color
hide everything
show cartoon
color lightblue, Fn_overlay_0001
color salmon, Fn_overlay_0002

# Set view
set_view (\
     0.998969078,   -0.041507259,    0.018368648,\
     0.041829307,    0.998959780,   -0.018161567,\
    -0.017624207,    0.018886993,    0.999666452,\
     0.000000000,    0.000000000, -542.166259766,\
   172.589996338,  165.830001831,  168.830001831,\
   451.758483887,  632.574035645,  -20.000000000 )

# Ray trace and save
bg_color white
set ray_opaque_background, 1
set antialias, 2
ray 2400, 1800
png results/pymol/Fn_overlay.png
"""

# Write PyMOL script
with open('results/pymol/render.pml', 'w') as f:
    f.write(pymol_script)

print("PyMOL script created at results/pymol/render.pml")
print("To generate image, run: pymol -c results/pymol/render.pml")