# Presentation Slides Guide: FnCas9 vs FnCas12a Structural Comparison

## Slide Deck Structure (15-20 slides)

### Slide 1: Title Slide
**Title**: Structural Comparison of FnCas9 and FnCas12a: A Tale of Convergent Evolution
**Subtitle**: Understanding Different Architectures in CRISPR-Cas Systems
**Include**: Your name, date, institution
**Visual**: Split image - Cas9 (red) and Cas12a (blue) structures

### Slide 2: Outline
**Title**: Presentation Overview
**Content**:
1. Introduction to CRISPR-Cas Systems
2. Research Question & Motivation
3. Methodology
4. Structural Comparison Results
5. Functional Implications
6. Biotechnology Applications
7. Conclusions

### Slide 3: CRISPR Systems Background
**Title**: Two Major CRISPR-Cas Families
**Left Panel**: Type II (Cas9)
- Discovery: 2012
- Organism: *Streptococcus*, *Francisella*
- Key feature: Dual RNA guide (crRNA + tracrRNA)
- Domains: RuvC + HNH

**Right Panel**: Type V (Cas12a/Cpf1)
- Discovery: 2015
- Organism: *Francisella*, *Prevotella*
- Key feature: Single crRNA guide
- Domain: RuvC-like only

**Bottom**: Timeline showing CRISPR discovery milestones

### Slide 4: Research Question
**Title**: Central Question
**Main text**: "How do structurally different CRISPR nucleases achieve similar DNA-cutting functions?"
**Sub-questions**:
- What is the extent of structural similarity?
- Which features are conserved vs. divergent?
- What does this tell us about CRISPR evolution?

**Visual**: Question mark overlaid on faded overlay structure

### Slide 5: Proteins Studied
**Title**: FnCas9 vs FnCas12a from *Francisella novicida*
**Table format**:
| Feature | FnCas9 | FnCas12a |
|---------|--------|----------|
| PDB ID | 5B2O | 6I1K |
| UniProt | A0Q5Y3 | A0Q7Q2 |
| Length | 1455 aa | 1282 aa |
| Type | II-A | V-A |
| Year crystallized | 2016 | 2018 |

**Why these?**: Same organism allows fair comparison

### Slide 6: Methodology Overview
**Title**: Computational Analysis Pipeline
**Flowchart**:
```
Sequence Retrieval (UniProt)
    ↓
Structure Download (PDB)
    ↓
Sequence Alignment (MAFFT)
    ↓
Structural Superposition (TM-align)
    ↓
Visualization (PyMOL)
    ↓
Quantitative Analysis
```
**Side note**: Fully reproducible pipeline on GitHub

### Slide 7: Sequence Alignment Results
**Title**: Minimal Sequence Conservation
**Main visual**: `results/alignment/cas_dual_mafft.png`
**Key stats** (highlight in boxes):
- Sequence identity: **7.4%**
- Aligned length: 1798 positions
- Gap percentage: ~40%

**Interpretation**: "Despite similar function, sequences have diverged beyond recognition"

### Slide 8: Structural Superposition
**Title**: Dramatically Different 3D Structures
**Main visual**: `results/pymol/Fn_overlay.png` (large, centered)
**Key metrics** (in corner boxes):
- RMSD: **10.00 Å**
- TM-score: **0.21**
- Aligned residues: **461/~1300**

**Caption**: "Red: FnCas9 | Blue: FnCas12a"

### Slide 9: What Do These Numbers Mean?
**Title**: Interpreting Structural Similarity Metrics
**Visual**: Scale/gauge graphics

**RMSD Scale**:
```
0-2 Å: Nearly identical ✓
2-4 Å: Same fold ✓
4-8 Å: Some similarity ~
>8 Å: Different structures ✗ ← Our result (10 Å)
```

**TM-score Scale**:
```
>0.5: Same fold ✓
0.3-0.5: Maybe similar ~
<0.3: Different folds ✗ ← Our result (0.21)
```

### Slide 10: Multi-Angle Comparison
**Title**: 360° Structural View
**Layout**: 3x2 grid
- Top row: FnCas9 (Front, Side, Top)
- Bottom row: FnCas12a (Front, Side, Top)
**Or**: Show `rotation.gif` if presentation supports

**Key differences to highlight**:
- Size difference
- Domain organization
- Surface topology

### Slide 11: Domain Architecture
**Title**: Different Domain Organizations
**Visual**: `results/pymol/views/domains_colored.png`
**Annotations**:
- Cas9: Label REC lobe, NUC lobe, Bridge helix
- Cas12a: Label REC domain, NUC domain, WED domain

**Bottom comparison**:
```
Cas9:   [REC lobe]--[Bridge]--[NUC lobe (RuvC+HNH)]
Cas12a: [REC]--[WED]--[PI]--[NUC (RuvC-like)]
```

### Slide 12: Active Site Comparison
**Title**: Distinct Catalytic Mechanisms
**Visual**: `results/pymol/views/active_site_zoom.png`
**Left panel**: Cas9 active sites
- RuvC: D10, E762, D986
- HNH: D839, H843, N863

**Right panel**: Cas12a active site
- RuvC-like: D908, E993, D1226

**Bottom**: Schematic of cleavage patterns

### Slide 13: Functional Differences
**Title**: Structure Dictates Function
**Table format**:
| Feature | FnCas9 | FnCas12a |
|---------|--------|----------|
| PAM sequence | 5'-NGG-3' | 5'-TTTN-3' |
| PAM position | Upstream | Downstream |
| Cut type | Blunt | 5' overhang |
| Cut position | -3 from PAM | +18-23 from PAM |
| Guide RNA | sgRNA (dual origin) | crRNA only |
| Target | dsDNA | dsDNA + ssDNA |

### Slide 14: Evolutionary Implications
**Title**: Convergent Evolution in Action
**Visual**: Phylogenetic tree showing Type II and Type V divergence
**Key points**:
- Independent origins ~2.5 billion years ago
- Similar selective pressure → DNA cutting
- Different solutions to same problem
- No detectable homology (7.4% identity)

**Analogy**: "Like bird wings vs. bat wings"

### Slide 15: Biotechnology Applications
**Title**: Complementary Tools for Genome Editing
**Two columns**:

**When to use Cas9**:
- Need high efficiency
- Established protocols
- Mammalian cells
- Base/prime editing

**When to use Cas12a**:
- Size constraints (AAV)
- Need 5' overhangs
- T-rich PAM regions
- Multiplexing (processes own guide)

### Slide 16: Key Contributions
**Title**: What This Analysis Reveals
1. **Quantified structural differences**: First direct comparison with metrics
2. **Evolutionary insight**: Confirmed independent evolution
3. **Practical implications**: Rational choice between systems
4. **Methods development**: Reproducible pipeline for Cas comparisons

### Slide 17: Future Directions
**Title**: Next Steps
- Compare with other Cas families (Cas3, Cas13)
- Analyze DNA-bound structures
- Machine learning for Cas classification
- Engineer hybrid systems?

### Slide 18: Conclusions
**Title**: Take-Home Messages
**Three key points** (with icons):
1. 🧬 **Different structures, same function**: RMSD = 10 Å, but both cut DNA
2. 🔄 **Convergent evolution**: No homology (7.4% identity) despite functional similarity
3. 🔧 **Complementary tools**: Each has unique advantages for biotechnology

### Slide 19: Acknowledgments
**Include**:
- Funding sources
- Computational resources
- PDB/UniProt databases
- Lab members/advisors

### Slide 20: Questions?
**Visual**: Overlay structure with question marks
**Contact info**: Your email
**Resources**: 
- GitHub repo: github.com/visvikbharti/cas9-cas12a-comparison
- Further reading: Key papers

## Presentation Tips

### Visual Design
- Use consistent color scheme (Red for Cas9, Blue for Cas12a)
- White/light background for structure images
- Sans-serif fonts (Arial, Helvetica)
- Minimal text per slide
- High-resolution images (300 dpi)

### Speaking Points
- Start with "why this matters" - CRISPR revolution
- Use analogies for technical concepts
- Pause after showing complex figures
- Highlight numbers that tell the story
- End with practical applications

### Time Management (20-minute talk)
- Introduction: 3-4 minutes (slides 1-4)
- Methods: 2-3 minutes (slides 5-6)
- Results: 8-10 minutes (slides 7-13)
- Implications: 3-4 minutes (slides 14-16)
- Conclusions: 2 minutes (slides 17-19)
- Questions: 5 minutes

### Backup Slides (prepare but don't show)
- Detailed methods
- Additional statistical analyses
- Comparison with SpCas9
- Technical details of PyMOL visualization
- Full amino acid sequence alignment

### Common Audience Types & Adjustments

**For Structural Biologists**:
- Emphasize technical metrics
- Discuss methodology details
- Show multiple orientations

**For CRISPR Researchers**:
- Focus on functional differences
- Emphasize PAM and cutting patterns
- Discuss genome editing applications

**For General Biology Audience**:
- Use more analogies
- Emphasize evolution story
- Focus on big picture

**For Industry/Biotech**:
- Highlight practical applications
- Discuss IP landscape briefly
- Emphasize complementary uses