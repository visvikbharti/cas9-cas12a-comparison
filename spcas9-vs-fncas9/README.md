# SpCas9 vs FnCas9 Structural Comparison

## Overview

This repository contains a comprehensive structural and sequence comparison between **Streptococcus pyogenes Cas9 (SpCas9)** and **Francisella novicida Cas9 (FnCas9)**, two Type II-A CRISPR nucleases from different bacterial species.

## Key Finding: Divergent Evolution Within CRISPR Family

Unlike the [FnCas9 vs FnCas12a comparison](https://github.com/visvikbharti/cas9-cas12a-comparison) which showed **convergent evolution**, this analysis demonstrates **divergent evolution** within the same CRISPR family.

### Summary Results
- **RMSD**: 7.13 Å (moderate structural similarity)
- **TM-score**: 0.41 (borderline same fold)
- **Sequence Identity**: 8.9% (low but higher than unrelated proteins)
- **Aligned Length**: 710 residues (54% coverage)
- **Relationship**: Distant homologs within Type II-A family

## Scientific Significance

This analysis provides a **perfect control** for understanding CRISPR evolution:

### Convergent vs Divergent Evolution
| Comparison | Relationship | RMSD | TM-score | Seq ID | Evolutionary Pattern |
|------------|--------------|------|----------|--------|---------------------|
| **FnCas9 vs FnCas12a** | Unrelated | 10.00 Å | 0.21 | 7.4% | **Convergent Evolution** |
| **SpCas9 vs FnCas9** | Related | 7.13 Å | 0.41 | 8.9% | **Divergent Evolution** |

### Biological Insights
1. **Same function, different origins** (Cas9 vs Cas12a) vs **same family, species adaptation** (SpCas9 vs FnCas9)
2. **Quantitative validation** of structural similarity metrics
3. **Evolutionary relationships** clearly distinguished by computational methods

## Quick Start

```bash
git clone https://github.com/visvikbharti/spcas9-fncas9-comparison.git
cd spcas9-fncas9-comparison
conda install -c conda-forge -c bioconda snakemake
snakemake -j 8 --use-conda
```

## Results Overview

### Key Outputs
- `results/struct/tmalign_stats.txt` - Structural alignment metrics
- `results/alignment/cas_dual_mafft.png` - Sequence conservation plot
- `results/pymol/Fn_overlay.png` - Structural superposition
- `results/pymol/rotation.gif` - 360° rotation animation
- `results/pymol/annotated/` - Publication-ready figures

### Visual Highlights
- **Structural overlay**: Clear bi-lobed architecture similarity
- **Sequence conservation**: Many conserved blocks (unlike random distribution)
- **Domain organization**: Both proteins show REC + NUC lobe arrangement

## Documentation

### Analysis & Interpretation
- [`RESULTS_INTERPRETATION_SpCas9_FnCas9.md`](RESULTS_INTERPRETATION_SpCas9_FnCas9.md) - Detailed results interpretation
- [`COMPARATIVE_ANALYSIS_SUMMARY.md`](COMPARATIVE_ANALYSIS_SUMMARY.md) - Side-by-side comparison with Cas9 vs Cas12a
- [`PROTEIN_INFO.md`](PROTEIN_INFO.md) - Protein details and rationale

### Technical Documentation
- [`SETUP_GUIDE.md`](SETUP_GUIDE.md) - Installation and troubleshooting
- [`PYMOL_EXPLANATION.md`](PYMOL_EXPLANATION.md) - How PyMOL generates images programmatically

## Protein Information

### SpCas9 (Streptococcus pyogenes)
- **UniProt**: Q99ZW2
- **PDB**: 5F9R (2.6 Å resolution)
- **Length**: 1362 amino acids
- **Features**: Most widely used CRISPR tool

### FnCas9 (Francisella novicida)
- **UniProt**: A0Q5Y3  
- **PDB**: 5B2O (2.8 Å resolution)
- **Length**: 1455 amino acids
- **Features**: Compact, temperature-stable

## Methodology

1. **Sequence Retrieval**: UniProt database
2. **Structure Download**: PDB database
3. **Sequence Alignment**: MAFFT L-INS-i algorithm
4. **Structural Superposition**: TM-align
5. **Visualization**: PyMOL (programmatic)
6. **Analysis**: Python + matplotlib

## Related Research

### Companion Analysis
- [**FnCas9 vs FnCas12a Comparison**](https://github.com/visvikbharti/cas9-cas12a-comparison) - Demonstrates convergent evolution

### Key Contrast
This analysis shows **related proteins** adapting to different species, while the FnCas9 vs FnCas12a analysis shows **unrelated proteins** evolving similar functions.

## Applications

### For Researchers
- **Protein evolution**: Example of divergent evolution quantification
- **Method validation**: Positive control for structural comparison pipelines
- **CRISPR engineering**: Structural basis for rational design

### For Biotechnology
- **Tool selection**: Data-driven choice between SpCas9 and FnCas9
- **Engineering targets**: Conserved vs variable regions identified
- **Optimization**: Species-specific adaptations revealed

## Future Directions

1. **Complete triangle**: SpCas9 vs FnCas12a analysis
2. **Expand families**: Include other Cas proteins (Cas3, Cas13)
3. **Functional validation**: Biochemical assays of predicted differences
4. **Machine learning**: Automated CRISPR family classification

## Citation

If you use this analysis in your research, please cite:

```
SpCas9 vs FnCas9 Structural Comparison
Bharti, V. et al.
GitHub: https://github.com/visvikbharti/spcas9-fncas9-comparison
```

## Dependencies

- Snakemake (workflow management)
- MAFFT (sequence alignment)
- TM-align (structural alignment)
- PyMOL (molecular visualization)
- Python + matplotlib (plotting)

## License

MIT License - see LICENSE file for details.

## Contact

For questions or issues, please open a GitHub issue or contact the repository maintainer.

---

**Key Message**: This analysis demonstrates that computational structural biology can reliably distinguish **related proteins** (divergent evolution) from **unrelated proteins** (convergent evolution) in CRISPR systems, providing quantitative evidence for different evolutionary patterns.