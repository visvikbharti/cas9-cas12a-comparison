# ────────────────────────────────────────────
#  Snakemake pipeline: FnCas9 vs FnCas12a
#  Author: Vishal Bharti (2025-05-27)
#  Licence: MIT
# ────────────────────────────────────────────

import yaml, textwrap
configfile: "config.yaml"

rule all:
    """Final targets."""
    input:
        "results/pymol/Fn_overlay.png",
        "results/struct/tmalign_stats.txt",
        "results/alignment/cas_dual_mafft.fasta",
        "results/alignment/cas_dual_mafft.png",
        "results/workflow_dag.png"

# ───────────────────────── sequences ─────────────────────────
rule download_fasta:
    output: "data/fasta/{uniprot}.fasta"
    params:
        url=lambda wc: f"https://rest.uniprot.org/uniprotkb/{wc.uniprot}.fasta"
    conda: "envs/wget.yaml"
    shell: "wget -q {params.url} -O {output}"

rule concat_fasta:
    input: 
        expand("data/fasta/{uniprot}.fasta", uniprot=config['uniprot_ids'])
    output: "work/combined.fasta"
    shell: "cat {input} > {output}"

rule mafft:
    input:  "work/combined.fasta"
    output: "results/alignment/cas_dual_mafft.fasta"
    threads: 8
    conda: "envs/mafft.yaml"
    shell: 
        "mafft --localpair --maxiterate 1000 "
        "--thread {threads} {input} > {output}"

# ───────────────────────── structures ─────────────────────────
rule download_pdb:
    output: "data/pdb/{pdb}.pdb"
    params:
        url=lambda wc: f"https://files.rcsb.org/download/{wc.pdb}.pdb"
    conda: "envs/wget.yaml"
    shell: "wget -q {params.url} -O {output}"

rule tmalign:
    input:
        pdb1=f"data/pdb/{config['pdb_ids'][0]}.pdb",
        pdb2=f"data/pdb/{config['pdb_ids'][1]}.pdb"
    output:
        stats="results/struct/tmalign_stats.txt",
        overlay="results/struct/Fn_overlay.pdb"
    conda: "envs/tmalign.yaml"
    shell: 
        "TMalign {input.pdb1} {input.pdb2} "
        "-o {output.overlay} > {output.stats}"

# ───────────────────────── figure ─────────────────────────
rule pymol_render:
    input: overlay="results/struct/Fn_overlay.pdb"
    output: "results/pymol/Fn_overlay.png"
    conda: "envs/pymol.yaml"
    script: "scripts/render_overlay.py"

# ───────────────────────── alignment figure ─────────────────────────
rule alignment_png:
    input: "results/alignment/cas_dual_mafft.fasta"
    output: "results/alignment/cas_dual_mafft.png"
    conda: "envs/jalview.yaml"
    shell:
        """
        jalview -headless -open {input} \
                -imageformat PNG -out {output}
        """

rule dag_png:
    output: "results/workflow_dag.png"
    shell:
        """
        snakemake --dag | dot -Tpng -o {output}
        """