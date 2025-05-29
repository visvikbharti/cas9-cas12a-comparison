#!/bin/bash
# Complete analysis pipeline for Cas9-Cas12a comparison
# This script runs all analyses including additional visualizations

set -e  # Exit on error

echo "=== Cas9-Cas12a Complete Analysis Pipeline ==="
echo ""

# Check if mamba is available
if command -v mamba &> /dev/null; then
    CONDA_FRONTEND="mamba"
    echo "✓ Using mamba for faster environment creation"
else
    CONDA_FRONTEND="conda"
    echo "⚠ Using conda (slower). Install mamba for better performance:"
    echo "  conda install -n base -c conda-forge mamba"
fi

echo ""
echo "Step 1: Running core Snakemake pipeline..."
echo "=========================================="
snakemake -j 8 --use-conda --conda-frontend $CONDA_FRONTEND

echo ""
echo "Step 2: Generating additional visualizations..."
echo "=============================================="

# Check if all outputs already exist
if [ -f "results/pymol/rotation.gif" ] && \
   [ -f "results/pymol/annotated/publication_figure.png" ] && \
   [ -f "results/pymol/color_overlay.pml" ] && \
   [ -d "results/pymol/views" ]; then
    echo "✓ All additional outputs already exist!"
else
    echo "Running additional analysis scripts..."
    
    # Generate movie frames if needed
    if [ ! -d "results/pymol/movie_frames" ]; then
        echo "  - Generating movie frames (this may take 5-10 minutes)..."
        python scripts/generate_movie_frames.py
    fi
    
    # Create rotation GIF
    if [ ! -f "results/pymol/rotation.gif" ]; then
        echo "  - Creating rotation GIF..."
        python scripts/create_movie.py
    fi
    
    # Generate annotated figures
    if [ ! -f "results/pymol/annotated/publication_figure.png" ]; then
        echo "  - Creating annotated figures..."
        python scripts/create_annotated_figures.py
    fi
    
    # Create PyMOL script
    if [ ! -f "results/pymol/color_overlay.pml" ]; then
        echo "  - Creating PyMOL color overlay script..."
        python scripts/create_colored_overlay.py
    fi
fi

echo ""
echo "=== Analysis Complete! ==="
echo ""
echo "Key Results:"
echo "- Alignment: results/alignment/cas_dual_mafft.fasta"
echo "- TM-align stats: results/struct/tmalign_stats.txt"
echo "- Visualizations: results/pymol/"
echo ""

# Display key statistics
if [ -f "results/struct/tmalign_stats.txt" ]; then
    echo "Structural alignment statistics:"
    grep -E "(RMSD|TM-score|Seq_ID)" results/struct/tmalign_stats.txt | head -3
fi

echo ""
echo "For detailed documentation, see:"
echo "- SETUP_GUIDE.md - Installation and troubleshooting"
echo "- PYMOL_EXPLANATION.md - How PyMOL generates images"
echo "- README.md - General project information"