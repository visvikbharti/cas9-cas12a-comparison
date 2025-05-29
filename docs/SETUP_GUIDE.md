# Complete Setup Guide for Cas9-Cas12a Comparison Pipeline

## Overview
This pipeline performs structural and sequence comparison between Francisella novicida Cas9 (FnCas9) and Cas12a (FnCas12a/Cpf1) proteins.

## Proteins Analyzed
- **FnCas9**: UniProt A0Q5Y3, PDB 5B2O
- **FnCas12a**: UniProt A0Q7Q2, PDB 6I1K

## Prerequisites

### System Requirements
- macOS, Linux, or Windows with WSL
- At least 8GB RAM
- ~5GB free disk space

### Software Requirements
- Conda or Miniconda
- Git
- Snakemake

## Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/visvikbharti/cas9-cas12a-comparison.git
cd cas9-cas12a-comparison
```

### 2. Install Snakemake
```bash
conda install -n base -c conda-forge -c bioconda snakemake
```

### 3. Handle Environment Setup Issues

#### Issue 1: Mamba Not Found
**Problem**: `The 'mamba' command is not available`

**Solution 1**: Install mamba (recommended for speed)
```bash
conda install -n base -c conda-forge mamba
```

**Solution 2**: Use conda frontend instead
```bash
snakemake -j 8 --use-conda --conda-frontend conda
```

#### Issue 2: Environment Creation Timeout
**Problem**: Conda environments take too long to create

**Solutions**:
1. Use mamba (much faster):
   ```bash
   snakemake -j 8 --use-conda --conda-frontend mamba
   ```

2. Set channel priority:
   ```bash
   conda config --set channel_priority strict
   ```

3. For persistent timeouts, clean conda cache:
   ```bash
   conda clean --all
   ```

#### Issue 3: Directory Lock Error
**Problem**: `Directory cannot be locked`

**Solution**:
```bash
snakemake --unlock
```

#### Issue 4: Non-conda Folder Exists Error
**Problem**: `Non-conda folder exists at prefix`

**Solution**: Clean Snakemake conda environments
```bash
rm -rf .snakemake/conda/
```

## Running the Pipeline

### Basic Pipeline (Snakemake targets only)
```bash
snakemake -j 8 --use-conda --conda-frontend mamba
```

This generates:
- Sequence alignment (MAFFT)
- Structural alignment (TM-align)
- Basic overlay visualization
- Workflow DAG

### Complete Analysis (with additional visualizations)
```bash
# Run basic pipeline first
snakemake -j 8 --use-conda --conda-frontend mamba

# Generate movie frames (may take 5-10 minutes)
python scripts/generate_movie_frames.py

# Create rotation GIF
python scripts/create_movie.py

# Generate annotated figures
python scripts/create_annotated_figures.py

# Create PyMOL script
python scripts/create_colored_overlay.py
```

## Expected Outputs

### Core Outputs (from Snakemake)
```
results/
├── alignment/
│   ├── cas_dual_mafft.fasta      # MAFFT alignment
│   └── cas_dual_mafft.png        # Alignment visualization
├── struct/
│   ├── tmalign_stats.txt         # RMSD & TM-score
│   └── Fn_overlay.pdb            # Superposed structures
├── pymol/
│   └── Fn_overlay.png            # Basic overlay image
└── workflow_dag.png              # Pipeline diagram
```

### Additional Outputs (from scripts)
```
results/pymol/
├── rotation.gif                  # 360° rotation animation
├── color_overlay.pml             # PyMOL script for custom views
├── movie_frames/                 # Individual rotation frames
│   └── frame_*.png              
├── views/                        # Multiple perspective views
│   ├── front_view.png
│   ├── side_view.png
│   ├── top_view.png
│   ├── domains_colored.png
│   ├── active_site_zoom.png
│   └── structural_flexibility.png
└── annotated/                    # Publication-ready figures
    ├── domains_annotated.png
    ├── front_annotated.png
    ├── composite_panel.png
    └── publication_figure.png
```

## How PyMOL Works Programmatically

PyMOL can be controlled via Python scripts using its API. Here's how our scripts generate images:

1. **Loading Structures**: 
   ```python
   cmd.load("data/pdb/5B2O.pdb", "FnCas9")
   cmd.load("data/pdb/6I1K.pdb", "FnCas12a")
   ```

2. **Alignment**:
   ```python
   cmd.align("FnCas12a", "FnCas9")
   ```

3. **Visualization**:
   ```python
   cmd.color("firebrick", "FnCas9")
   cmd.color("marine", "FnCas12a")
   cmd.show("cartoon")
   ```

4. **Rendering**:
   ```python
   cmd.ray(1600, 1200)  # Ray-trace at high resolution
   cmd.png("output.png", dpi=300)  # Save image
   ```

The scripts run PyMOL in "headless" mode (no GUI), executing commands programmatically to generate publication-quality images.

## Troubleshooting

### PyMOL Takes Too Long
- Movie frame generation can take 5-10 minutes
- Use `timeout` parameter in scripts if needed
- Consider reducing frame count or resolution

### Missing Dependencies
If scripts fail, activate the appropriate conda environment:
```bash
# For PyMOL scripts
conda activate .snakemake/conda/552ccd508f497ea2ebadf5305ffb1000_

# For plotting scripts  
conda activate .snakemake/conda/b63fd26bd072a6b847116b8a2e7fe09c_
```

### Memory Issues
- Close other applications
- Reduce number of parallel jobs: `snakemake -j 4`
- Process one visualization at a time

## Validation

To verify results match expectations:
- TM-score should be ~0.21-0.23
- RMSD should be ~10.0 Å
- Sequence identity should be ~7.4%
- All visualization files should be generated

## Contact
For issues, please open a GitHub issue or contact the repository maintainer.