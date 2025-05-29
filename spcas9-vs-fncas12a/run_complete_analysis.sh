#!/bin/bash
# Run complete SpCas9 vs FnCas12a analysis

echo "Starting SpCas9 vs FnCas12a analysis..."

# Create combined fasta
echo "Creating combined fasta file..."
cat data/fasta/Q99ZW2.fasta data/fasta/A0Q7Q2.fasta > work/combined.fasta

# Run MAFFT alignment
echo "Running MAFFT alignment..."
mafft --localpair --maxiterate 1000 work/combined.fasta > results/alignment/cas_dual_mafft.fasta

# Run TM-align
echo "Running TM-align structural comparison..."
TMalign data/pdb/5F9R.pdb data/pdb/6I1K.pdb -seq 1 > results/struct/tmalign_stats.txt

# Extract overlay structure
echo "Extracting structural overlay..."
TMalign data/pdb/5F9R.pdb data/pdb/6I1K.pdb -o results/struct/Fn_overlay.pdb

# Generate visualizations
echo "Generating PyMOL visualizations..."
python scripts/render_overlay.py
python scripts/plot_alignment.py
python scripts/create_colored_overlay.py
python scripts/render_multiview.py
python scripts/create_annotated_figures.py
python scripts/create_movie.py

# Generate workflow DAG
echo "Creating workflow diagram..."
snakemake --dag | dot -Tpng > results/workflow_dag.png 2>/dev/null || echo "Skipping DAG generation"

echo "Analysis complete! Check results/ directory for outputs."