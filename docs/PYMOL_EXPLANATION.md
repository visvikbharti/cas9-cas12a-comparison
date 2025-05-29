# How PyMOL Generates Images Programmatically

## Overview
PyMOL is a molecular visualization system that can be controlled programmatically through Python scripts. In our pipeline, we use PyMOL to create publication-quality structural images without needing to open the GUI.

## Key Concepts

### 1. PyMOL as a Python Module
PyMOL can be imported and controlled via Python:
```python
from pymol import cmd  # cmd is the main PyMOL API
```

### 2. Headless Operation
PyMOL runs without displaying a window when called from scripts, making it perfect for automated pipelines.

## How Our Scripts Work

### Step 1: Loading Protein Structures
```python
cmd.load("data/pdb/5B2O.pdb", "FnCas9")
cmd.load("data/pdb/6I1K.pdb", "FnCas12a")
```
- Loads PDB files from disk
- Assigns names to each structure for reference

### Step 2: Structural Alignment
```python
cmd.align("FnCas12a", "FnCas9")
```
- Superimposes FnCas12a onto FnCas9
- Returns RMSD and number of aligned atoms

### Step 3: Visual Styling
```python
cmd.hide("everything")           # Hide all representations
cmd.show("cartoon")              # Show cartoon ribbons
cmd.set("cartoon_fancy_helices", 1)  # Fancy helix rendering
cmd.color("firebrick", "FnCas9")    # Color Cas9 red
cmd.color("marine", "FnCas12a")      # Color Cas12a blue
```

### Step 4: Camera Positioning
```python
cmd.orient()                     # Auto-orient to best view
cmd.zoom("all", buffer=5)        # Zoom to fit with padding
cmd.turn("y", 90)                # Rotate 90° around Y-axis
```

### Step 5: Ray Tracing & Export
```python
cmd.ray(1600, 1200)              # Ray-trace at 1600x1200
cmd.png("output.png", dpi=300)   # Save high-res PNG
```

## Example: Movie Frame Generation

Our `generate_movie_frames.py` creates a 360° rotation:

```python
for i in range(36):  # 36 frames
    cmd.turn("y", 10)  # Rotate 10° each frame
    cmd.ray(800, 600)  # Render
    cmd.png(f"frame_{i:03d}.png")  # Save frame
```

## Domain Selection & Coloring

PyMOL uses a selection language to identify specific regions:

```python
# Select by residue range
cmd.select("Cas9_REC", "FnCas9 and resi 1-500")

# Select catalytic residues
cmd.select("Cas9_catalytic", "FnCas9 and resi 10+840+863+866+986")

# Color by domain
cmd.color("salmon", "Cas9_REC")
```

## Advanced Features Used

### 1. B-factor Putty
Shows structural flexibility:
```python
cmd.cartoon("putty", "all")
cmd.set("cartoon_putty_scale_min", 0.5)
```

### 2. Stick Representation for Active Sites
```python
cmd.show("sticks", "Cas9_catalytic")
cmd.color("yellow", "Cas9_catalytic and elem C")
```

### 3. Session Saving
```python
cmd.save("session.pse")  # Save entire PyMOL session
```

## Why This Works Without GUI

1. **PyMOL Architecture**: PyMOL has separate rendering and display components
2. **Command Layer**: All GUI actions translate to commands
3. **Batch Processing**: Scripts execute commands sequentially
4. **Software Rendering**: Uses CPU/GPU for ray tracing without display

## Integration with Snakemake

Snakemake rules call PyMOL scripts in conda environments:

```yaml
rule pymol_render:
    input: overlay="results/struct/Fn_overlay.pdb"
    output: "results/pymol/Fn_overlay.png"
    conda: "envs/pymol.yaml"
    script: "scripts/render_overlay.py"
```

The conda environment ensures PyMOL and dependencies are available.

## Benefits of Programmatic Approach

1. **Reproducibility**: Exact same images every time
2. **Automation**: No manual clicking required
3. **Batch Processing**: Generate hundreds of images
4. **Version Control**: Scripts can be tracked in Git
5. **Parameter Sweeps**: Easy to test different colors/views

## Troubleshooting

### PyMOL Not Found
Ensure you're in the correct conda environment:
```bash
conda activate .snakemake/conda/552ccd508f497ea2ebadf5305ffb1000_
```

### Slow Rendering
Ray tracing is CPU-intensive. For faster previews:
```python
cmd.png("preview.png")  # Without ray tracing
```

### Memory Issues
Large structures may need optimization:
```python
cmd.set("max_threads", 4)  # Limit CPU usage
cmd.set("hash_max", 100)   # Reduce memory usage
```

## Further Reading

- [PyMOL Wiki](https://pymolwiki.org/index.php/Main_Page)
- [PyMOL Scripting Tutorial](https://pymolwiki.org/index.php/Scripting)
- [PyMOL API Documentation](https://pymol.org/pymol-command-ref.html)