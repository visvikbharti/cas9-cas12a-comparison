# Troubleshooting Guide

## Common Issues and Solutions

### 1. Conda Environment Creation Timeouts

**Problem**: Large conda environments (especially Java-based tools like Jalview) can timeout during creation.

**Solutions**:

#### Use Mamba (Recommended)
Mamba is a drop-in replacement for conda with 10-100x faster dependency resolution:

```bash
# Install mamba once
conda install -n base -c conda-forge mamba

# Run pipeline with mamba
snakemake -j 8 --use-conda --conda-frontend mamba

# Or pre-create all environments
snakemake --use-conda --conda-frontend mamba --conda-create-envs-only
```

#### Pre-create Environments
Create environments outside of Snakemake to avoid timeouts:

```bash
# Create specific environment
mamba env create -p .snakemake/conda/jalview -f envs/jalview.yaml

# Then run pipeline normally
snakemake -j 8 --use-conda
```

### 2. Alternative Visualization Tools

The pipeline includes multiple options for alignment visualization:

#### Current Implementation (matplotlib)
- Lightweight, pure Python solution
- Creates conservation plots
- No Java dependencies

#### Jalview (original design)
- Professional alignment viewer
- Requires Java environment
- Use with mamba to avoid timeouts

#### MSA Viewer (lightweight alternative)
Create `envs/msa_view.yaml`:
```yaml
name: msa-view
channels: [conda-forge, bioconda]
dependencies:
  - python=3.10
  - msa_view=1.0.3
  - pillow
```

Then modify Snakefile rule:
```python
rule alignment_png:
    input: "results/alignment/cas_dual_mafft.fasta"
    output: "results/alignment/cas_dual_mafft.png"
    conda: "envs/msa_view.yaml"
    shell:
        "msa_view {input} --coloring clustalx --format png -o {output}"
```

### 3. UniProt URL Changes

**Problem**: UniProt occasionally changes API endpoints.

**Solution**: Update the download URL in Snakefile:
```python
# Current (as of 2025)
url=lambda wc: f"https://rest.uniprot.org/uniprotkb/{wc.uniprot}.fasta"

# Legacy format
url=lambda wc: f"https://www.uniprot.org/uniprot/{wc.uniprot}.fasta"
```

### 4. PyMOL Rendering Issues

**Problem**: PyMOL may fail in headless environments.

**Solutions**:
- Ensure `pymol-open-source` is used (not commercial PyMOL)
- Add virtual display for CI/CD:
  ```bash
  xvfb-run -a snakemake pymol_render --use-conda
  ```

### 5. Missing Graphviz

**Problem**: DAG visualization requires graphviz.

**Solution**:
```bash
# macOS
brew install graphviz

# Linux
sudo apt-get install graphviz

# Conda
conda install -c conda-forge graphviz
```

### 6. Lock File Issues

**Problem**: "Directory cannot be locked" error.

**Solution**:
```bash
snakemake --unlock
```

### 7. Memory Issues

For large alignments or structures:
```bash
# Increase Java heap for Jalview
export _JAVA_OPTIONS="-Xmx4g"

# Run with more resources
snakemake -j 1 --resources mem_mb=8000
```

## Performance Tips

1. **Use mamba** for all conda operations
2. **Pre-download databases** if working offline
3. **Parallelize** appropriately: `-j 4` for most systems
4. **Cache conda packages**: `conda config --set pkgs_dirs ~/.conda/pkgs`

## Getting Help

- Check the [GitHub Issues](https://github.com/visvikbharti/cas9-cas12a-comparison/issues)
- Review Snakemake logs: `.snakemake/log/`
- Enable verbose output: `snakemake -j 4 --verbose`

## Environment Details

Tested on:
- macOS 14+ (Apple Silicon & Intel)
- Ubuntu 20.04+
- Snakemake 7.32+
- Python 3.9+