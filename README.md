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

## Citations

* Hirano *et al.* (2016) **Science** – PDB 5B2O
* Swarts & Jinek (2018) **Nature** – PDB 6I1K
* Katoh & Standley (2013) **MBE** – MAFFT v7