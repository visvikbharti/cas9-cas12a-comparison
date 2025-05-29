#!/usr/bin/env python3
"""
Create an animated GIF from PyMOL movie frames.
Requires: pip install pillow
"""
import os
import sys
from PIL import Image
import glob

def create_gif(frames_dir, output_path, duration=100):
    """Create animated GIF from PNG frames."""
    # Get all frame files
    frame_files = sorted(glob.glob(os.path.join(frames_dir, "frame_*.png")))
    
    if not frame_files:
        print(f"No frames found in {frames_dir}")
        return False
    
    # Load images
    images = []
    for f in frame_files:
        img = Image.open(f)
        images.append(img)
    
    # Save as GIF
    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0
    )
    
    print(f"Created GIF: {output_path}")
    print(f"Frames: {len(images)}")
    print(f"Duration: {duration}ms per frame")
    return True

if __name__ == "__main__":
    # Default paths
    frames_dir = "results/pymol/movie_frames"
    output_gif = "results/pymol/Fn_overlay_rotation.gif"
    
    if len(sys.argv) > 1:
        frames_dir = sys.argv[1]
    if len(sys.argv) > 2:
        output_gif = sys.argv[2]
    
    create_gif(frames_dir, output_gif)