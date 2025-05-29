#!/bin/bash
# Run movie frame generation in conda environment

cd /Users/vishalbharti/Downloads/cas_compare

# Check if pymol conda environment exists
if [ -d ".snakemake/conda/117d9553db2a780b4ac9233d7a65e39f_" ]; then
    echo "Using existing PyMOL conda environment"
    source activate .snakemake/conda/117d9553db2a780b4ac9233d7a65e39f_
    python scripts/generate_movie_frames.py
else
    echo "PyMOL environment not found. Running with system Python (requires PyMOL installed)"
    python3 scripts/generate_movie_frames.py
fi