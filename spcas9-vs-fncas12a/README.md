# SpCas9 vs FnCas12a Structural Comparison

## Overview
This analysis compares Streptococcus pyogenes Cas9 (SpCas9) with Francisella novicida Cas12a (FnCas12a), representing a comparison between Type II-A and Type V-A CRISPR systems. This comparison demonstrates **convergent evolution** - unrelated proteins that evolved similar nuclease functions independently.

## Key Results

### Structural Metrics
- **RMSD**: 10.23 Å (high structural divergence)
- **TM-score**: 0.217 (SpCas9) / 0.227 (FnCas12a) (low structural similarity)
- **Sequence Identity**: 7.0% (very low)
- **Aligned Length**: 472 residues

### Evolutionary Interpretation
These metrics confirm convergent evolution:
- Very different structural architectures (high RMSD)
- Low structural similarity (TM-score < 0.3)
- Minimal sequence conservation
- Independent evolutionary origins

## Proteins Analyzed

### SpCas9 (Type II-A)
- **UniProt**: Q99ZW2
- **PDB**: 5F9R
- **Organism**: Streptococcus pyogenes
- **Function**: RNA-guided DNA endonuclease
- **Size**: 1,362 residues

### FnCas12a (Type V-A)
- **UniProt**: A0Q7Q2
- **PDB**: 6I1K  
- **Organism**: Francisella novicida
- **Function**: RNA-guided DNA endonuclease
- **Size**: 1,282 residues

## Key Differences
1. **PAM Recognition**: SpCas9 (3'-NGG) vs FnCas12a (5'-TTTV)
2. **Cleavage Pattern**: SpCas9 (blunt ends) vs FnCas12a (staggered cuts)
3. **RNA Requirements**: SpCas9 (tracrRNA + crRNA) vs FnCas12a (crRNA only)
4. **Domain Architecture**: Completely different structural organization

## Repository Structure
```
spcas9-vs-fncas12a/
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