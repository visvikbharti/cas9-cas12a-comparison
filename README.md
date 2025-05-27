# cas_compare – Reproducible FnCas9 vs FnCas12a pipeline

This repo builds a high-quality multiple-sequence alignment and a
quantitative structural superposition between **Francisella novicida
Cas9 (FnCas9)** and **FnCas12a (Cpf1)** in one command.

## Quick start

```bash
git clone https://github.com/<your-org>/cas_compare.git
cd cas_compare
conda install -c conda-forge -c bioconda snakemake
snakemake -j 8 --use-conda
```

Outputs appear in `results/`:

* `alignment/cas_dual_mafft.fasta` – MAFFT alignment  
* `alignment/cas_dual_mafft.png` – coloured alignment figure  
* `struct/tmalign_stats.txt` – RMSD & TM-score  
* `pymol/Fn_overlay.png` – high-res overlay figure  
* `workflow_dag.png` – Snakemake rule graph

## Extending

* Add additional UniProt or PDB IDs to `config.yaml`; rerun Snakemake.
* All software versions are pinned in `envs/*.yaml`.

## Troubleshooting

### Conda Environment Creation Timeouts

If conda environment creation times out (especially for Java-based tools), use **mamba**:

```bash
# Install mamba (one-time)
conda install -n base -c conda-forge mamba

# Run pipeline with mamba
snakemake -j 8 --use-conda --conda-frontend mamba
```

### Alternative Alignment Visualization

The pipeline uses matplotlib for alignment visualization. For Jalview-style output:

```bash
# Option 1: Pre-create Jalview environment with mamba
mamba env create -f envs/jalview.yaml

# Option 2: Use lightweight msa_view instead
# (see envs/msa_view.yaml in project wiki)
```

## Citations

* Hirano *et al.* (2016) **Science** – PDB 5B2O
* Swarts & Jinek (2018) **Nature** – PDB 6I1K
* Katoh & Standley (2013) **MBE** – MAFFT v7