"""
Create multiple views of FnCas9 vs FnCas12a overlay with annotations.
Generates publication-quality figures with domain labels.
"""
from pymol import cmd
import os

# Output directory
output_dir = os.path.dirname(snakemake.output[0])
os.makedirs(f"{output_dir}/views", exist_ok=True)

# Fresh session
cmd.reinitialize()

# Load original PDB files
cmd.load("data/pdb/5B2O.pdb", "FnCas9")
cmd.load("data/pdb/6I1K.pdb", "FnCas12a")

# Align structures
alignment = cmd.align("FnCas12a", "FnCas9")
print(f"Alignment RMSD: {alignment[0]:.2f} Å over {alignment[1]} atoms")

# Basic display settings
cmd.hide("everything")
cmd.show("cartoon")
cmd.set("cartoon_fancy_helices", 1)
cmd.set("cartoon_transparency", 0.0)
cmd.bg_color("white")
cmd.set("ray_shadows", 0)
cmd.set("ambient", 0.4)
cmd.set("specular", 0.2)

# View 1: Front view with basic colors
cmd.color("firebrick", "FnCas9")
cmd.color("marine", "FnCas12a")
cmd.orient()
cmd.zoom("all", buffer=5)
cmd.ray(1600, 1200)
cmd.png(f"{output_dir}/views/front_view.png", dpi=300)

# View 2: Side view (90° rotation)
cmd.turn("y", 90)
cmd.ray(1600, 1200)
cmd.png(f"{output_dir}/views/side_view.png", dpi=300)

# View 3: Top view
cmd.turn("y", -90)  # Reset
cmd.turn("x", 90)
cmd.ray(1600, 1200)
cmd.png(f"{output_dir}/views/top_view.png", dpi=300)

# View 4: Domain-colored view
cmd.orient()
cmd.zoom("all", buffer=5)

# Define and color domains for FnCas9
cmd.select("Cas9_REC", "FnCas9 and resi 1-500")
cmd.select("Cas9_NUC", "FnCas9 and resi 501-1455")
cmd.select("Cas9_RuvC", "FnCas9 and (resi 1-200 or resi 500-800)")
cmd.select("Cas9_HNH", "FnCas9 and resi 800-1000")

# Define and color domains for FnCas12a
cmd.select("Cas12a_REC", "FnCas12a and resi 1-600")
cmd.select("Cas12a_NUC", "FnCas12a and resi 601-1282")
cmd.select("Cas12a_RuvC", "FnCas12a and resi 800-1100")

# Apply domain colors
cmd.color("salmon", "Cas9_REC")
cmd.color("tv_red", "Cas9_NUC")
cmd.color("lightblue", "Cas12a_REC")
cmd.color("tv_blue", "Cas12a_NUC")

cmd.ray(1600, 1200)
cmd.png(f"{output_dir}/views/domains_colored.png", dpi=300)

# View 5: Active site focus
# Reset colors
cmd.color("firebrick", "FnCas9")
cmd.color("marine", "FnCas12a")

# Known catalytic residues (approximate)
# Cas9: D10, D840, H863, N866, H986
# Cas12a: D908, E911, D1226
cmd.select("Cas9_catalytic", "FnCas9 and resi 10+840+863+866+986")
cmd.select("Cas12a_catalytic", "FnCas12a and resi 908+911+1226")

cmd.zoom("Cas9_catalytic or Cas12a_catalytic", buffer=15)
cmd.show("sticks", "Cas9_catalytic or Cas12a_catalytic")
cmd.color("yellow", "Cas9_catalytic and elem C")
cmd.color("cyan", "Cas12a_catalytic and elem C")

cmd.ray(1600, 1200)
cmd.png(f"{output_dir}/views/active_site_zoom.png", dpi=300)

# View 6: Structural differences (B-factor putty)
cmd.orient()
cmd.zoom("all", buffer=5)
cmd.hide("sticks")
cmd.cartoon("putty", "all")
cmd.set("cartoon_putty_scale_min", 0.5)
cmd.set("cartoon_putty_scale_max", 2.0)
cmd.set("cartoon_putty_radius", 0.3)

cmd.ray(1600, 1200)
cmd.png(f"{output_dir}/views/structural_flexibility.png", dpi=300)

# Reset to normal cartoon
cmd.cartoon("automatic")

# Save PyMOL session
cmd.save(f"{output_dir}/views/multiview_session.pse")

# Create main output (overview with nice orientation)
cmd.orient()
cmd.zoom("all", buffer=5)
cmd.color("firebrick", "FnCas9")
cmd.color("marine", "FnCas12a")
cmd.turn("y", 15)  # Slight rotation for better 3D effect
cmd.ray(1600, 1200)
cmd.png(snakemake.output[0], dpi=300)

# Generate rotation frames for movie
movie_dir = f"{output_dir}/movie_frames"
os.makedirs(movie_dir, exist_ok=True)

cmd.orient()
cmd.zoom("all", buffer=5)

# Generate 36 frames (every 10 degrees)
for i in range(36):
    cmd.turn("y", 10)
    cmd.ray(800, 600)
    cmd.png(f"{movie_dir}/frame_{i:03d}.png")

print(f"\nGenerated views in {output_dir}/views/:")
print("  - front_view.png")
print("  - side_view.png") 
print("  - top_view.png")
print("  - domains_colored.png")
print("  - active_site_zoom.png")
print("  - structural_flexibility.png")
print(f"\nMovie frames in {movie_dir}/")
print(f"\nPyMOL session: {output_dir}/views/multiview_session.pse")