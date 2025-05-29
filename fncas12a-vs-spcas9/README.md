# FnCas12a vs SpCas9 Structural Comparison

## Overview
This analysis compares Francisella novicida Cas12a (FnCas12a) with Streptococcus pyogenes Cas9 (SpCas9), representing a comparison between Type V-A and Type II-A CRISPR systems. This comparison demonstrates **convergent evolution** - unrelated proteins that evolved similar nuclease functions independently.

## Key Results

### Structural Metrics
- **RMSD**: 10.23 Å (high structural divergence)
- **TM-score**: 0.227 (FnCas12a) / 0.217 (SpCas9) (low structural similarity)
- **Sequence Identity**: 7.0% (very low)
- **Aligned Length**: 472 residues

### Evolutionary Interpretation
These metrics confirm convergent evolution:
- Very different structural architectures (high RMSD)
- Low structural similarity (TM-score < 0.3)
- Minimal sequence conservation
- Independent evolutionary origins

## Proteins Analyzed

### FnCas12a (Type V-A)
- **UniProt**: A0Q7Q2
- **PDB**: 6I1K  
- **Organism**: Francisella novicida
- **Function**: RNA-guided DNA endonuclease
- **Size**: 1,282 residues

### SpCas9 (Type II-A)
- **UniProt**: Q99ZW2
- **PDB**: 5F9R
- **Organism**: Streptococcus pyogenes
- **Function**: RNA-guided DNA endonuclease
- **Size**: 1,362 residues

## Key Differences
1. **PAM Recognition**: FnCas12a (5'-TTTV) vs SpCas9 (3'-NGG)
2. **Cleavage Pattern**: FnCas12a (staggered cuts) vs SpCas9 (blunt ends)
3. **RNA Requirements**: FnCas12a (crRNA only) vs SpCas9 (tracrRNA + crRNA)
4. **Domain Architecture**: Completely different structural organization

## Repository Structure
```
fncas12a-vs-spcas9/
├── data/               # Input sequences and structures
├── results/            # Analysis outputs
│   ├── alignment/      # Sequence alignment results
│   ├── struct/         # Structural comparison (TM-align)
│   └── pymol/          # Visualization outputs
├── scripts/            # Analysis scripts
└── config.yaml         # Configuration file
```

## Running the Analysis
```bash
# Using Snakemake
snakemake --use-conda --cores 4

# Or using the standalone script
./run_complete_analysis.sh
```

## Outputs
- Sequence alignment visualization
- Structural overlay images
- TM-align statistics
- PyMOL session files
- Publication-ready figures