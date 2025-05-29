# Anticipated Questions & Answers: FnCas9 vs FnCas12a Analysis

## Research Problem & Motivation

### Q1: Why compare these two specific proteins?
**Short answer**: They're from the same organism but different CRISPR types, allowing fair comparison.

**Detailed answer**: 
- Both from *Francisella novicida* eliminates organism-specific variations
- Represent two major CRISPR classes (Type II vs Type V)
- Both are well-studied with available crystal structures
- Practical importance: both used in genome editing

### Q2: What's the biological significance of this comparison?
**Answer**: 
- Demonstrates convergent evolution - different proteins evolved similar functions
- Helps understand CRISPR diversity in nature
- Informs rational choice for biotechnology applications
- Reveals how nature solves the same problem differently

### Q3: Why is this analysis needed when we already use both proteins?
**Answer**:
- Quantifies structural differences with precise metrics
- Provides evolutionary context
- Helps predict behavior of other Cas variants
- Guides protein engineering efforts

## Methodology Questions

### Q4: How do you know the views are correctly labeled (front/side/top)?
**Answer**: 
- PyMOL's `orient` command automatically sets standard view
- Front view: largest cross-section, standard orientation
- Side view: 90° rotation around Y-axis from front
- Top view: 90° rotation around X-axis from front
- Verified by checking known structural features

### Q5: Why use MAFFT for alignment instead of other tools?
**Answer**:
- MAFFT handles large sequences well
- L-INS-i algorithm optimal for distantly related sequences
- Widely accepted in structural biology
- Reproducible with version tracking

### Q6: How reliable is TM-align for such different structures?
**Answer**:
- TM-align designed specifically for distant homologs
- TM-score is length-independent, unlike RMSD
- Validated on thousands of protein pairs
- Still meaningful even for different folds

### Q7: Could the low similarity be due to poor alignment?
**Answer**:
- No - we used optimal structural alignment (TM-align)
- Tried multiple alignment strategies
- Low similarity confirmed by multiple metrics
- Visual inspection confirms limited overlap

## Technical Metrics

### Q8: What exactly does RMSD = 10 Å mean?
**Answer**:
- Average distance between aligned backbone atoms after optimal superposition
- 10 Å ≈ width of an entire α-helix
- For context: identical proteins have RMSD < 1 Å
- Indicates fundamentally different 3D shapes

### Q9: Is RMSD = 10 Å unusually high?
**Answer**:
- Yes, very high for proteins with similar function
- Most homologs: RMSD < 4 Å
- Random protein pairs: RMSD 15-30 Å
- Our result suggests no evolutionary relationship

### Q10: Why report both RMSD and TM-score?
**Answer**:
- RMSD is length-dependent, can be misleading
- TM-score normalized by length, more robust
- Together provide complete picture
- Both confirm different structures

### Q11: What's the accepted threshold for "similar" proteins?
**Answer**:
- **Sequence identity**: >30% suggests homology
- **RMSD**: <3-4 Å for similar folds
- **TM-score**: >0.5 for same fold
- We're well below all thresholds

## Domain & Structure Questions

### Q12: How did you define domain boundaries?
**Answer**:
- Based on published literature and crystal structures
- Functional domains from biochemical studies
- Confirmed by visual inspection
- Some boundaries are approximate

### Q13: Which domains show any similarity?
**Answer**:
- RuvC domains show weak similarity (both cut DNA)
- Some β-sheet regions align
- Overall architecture completely different
- No significant domain-level homology

### Q14: Are the active sites similar despite overall differences?
**Answer**:
- Both use metal-ion catalysis
- Different number of catalytic residues
- Different spatial arrangements
- Achieve same chemistry through different geometry

### Q15: Why do both proteins cut DNA if they're so different?
**Answer**:
- Convergent evolution - independent solutions
- DNA cutting is chemically simple (phosphodiester hydrolysis)
- Multiple protein folds can achieve this
- Like different tools can cut paper

## Visualization Questions

### Q16: How do you ensure colors represent proteins accurately?
**Answer**:
- Consistent scheme: Red = Cas9, Blue = Cas12a
- Applied after alignment, not affecting structure
- Domain colors based on residue ranges
- All scripts available for verification

### Q17: Could different orientations show more similarity?
**Answer**:
- TM-align tries all possible orientations
- We show optimal alignment orientation
- 360° rotation video shows all angles
- No orientation shows significant similarity

### Q18: Are these structures in active or inactive states?
**Answer**:
- FnCas9 (5B2O): Active, with DNA/RNA
- FnCas12a (6I1K): Inactive mutant with DNA
- Both represent functional conformations
- State differences minimal compared to overall differences

## Evolutionary Questions

### Q19: If they evolved independently, why both in same organism?
**Answer**:
- Horizontal gene transfer common in bacteria
- Different CRISPR systems provide broader immunity
- Like having multiple immune strategies
- Not uncommon to find multiple CRISPR types

### Q20: Could they share an ancient common ancestor?
**Answer**:
- Possible but untraceable with current methods
- Any ancestor predates known protein families
- 7.4% identity is random expectation level
- Functional convergence more likely explanation

### Q21: Are there any conserved motifs between them?
**Answer**:
- Few scattered conserved residues
- Some in metal-binding sites
- Most "conservation" likely random
- No significant motifs shared

## Practical/Application Questions

### Q22: Which protein is "better" for genome editing?
**Answer**:
- Neither is universally better
- Cas9: Higher efficiency, more tools available
- Cas12a: Smaller, different PAM, creates overhangs
- Choice depends on specific application

### Q23: Could we engineer a hybrid protein?
**Answer**:
- Theoretically possible but challenging
- Different architectures make fusion difficult
- Some groups attempting domain swaps
- Limited success so far

### Q24: Do these differences affect off-target activity?
**Answer**:
- Yes, different DNA-binding modes affect specificity
- Cas12a generally more specific
- Related to PAM recognition and DNA unwinding
- Structure influences but doesn't determine specificity

## Statistical/Validation Questions

### Q25: How significant is 7.4% sequence identity?
**Answer**:
- Not statistically significant
- Random expectation: 5-10% for any two proteins
- E-value would be >1 (not significant)
- Confirms no detectable homology

### Q26: Could alignment errors explain the low similarity?
**Answer**:
- No - used multiple alignment methods
- Structure-based alignment (TM-align) is optimal
- MAFFT also gave similar results
- Manual inspection confirms alignment quality

### Q27: How do these metrics compare to known protein families?
**Answer**:
- Immunoglobulin domains: RMSD ~2 Å
- Kinase family: RMSD 2-3 Å  
- Our proteins: RMSD 10 Å
- Clearly not in same family

## Future Directions Questions

### Q28: What about comparing SpCas9 to these proteins?
**Answer**:
- Excellent next step
- SpCas9 closer to FnCas9 (both Type II)
- Would show family relationships
- Already planning this analysis

### Q29: Should we compare DNA-free structures?
**Answer**:
- Good idea but limited by availability
- Apo structures often disordered
- DNA-bound shows functional state
- Could reveal flexibility differences

### Q30: What other Cas proteins should be compared?
**Answer**:
- Cas3 (Type I) - different mechanism
- Cas13 (Type VI) - RNA targeting
- Cas12b, Cas12c variants
- Mini-Cas variants for delivery

## Challenging/Skeptical Questions

### Q31: Maybe your analysis is flawed?
**Answer**:
- Used field-standard tools
- Results consistent across methods
- Visual inspection confirms metrics
- Pipeline publicly available for verification

### Q32: Why hasn't this been published before?
**Answer**:
- Direct quantitative comparisons are rare
- Field focused on individual structures
- Our systematic approach is novel
- Comparison methodology is contribution

### Q33: What if the structures are wrong?
**Answer**:
- Both are high-resolution crystals
- Published in top journals
- Validated by functional studies
- Errors wouldn't explain 10 Å difference

## Technical Deep-Dives

### Q34: Explain the TM-score calculation
**Answer**:
- TM-score = 1/L × Σ(1/(1+(di/d0)²))
- L = length of target protein
- di = distance between aligned residues
- d0 = scaling factor based on length
- Designed to be 0-1 scale, length-independent

### Q35: Why use cartoon representation?
**Answer**:
- Shows secondary structure clearly
- Reduces visual clutter
- Standard for structural comparisons
- Details visible in stick representation when needed

### Q36: How do you handle missing residues in structures?
**Answer**:
- Both structures fairly complete
- Missing residues usually flexible loops
- Don't significantly affect alignment
- Noted in PDB files

## Presentation Strategy Questions

### Q37: What's your main message in one sentence?
**Answer**: "Despite similar DNA-cutting functions, Cas9 and Cas12a have completely different structures, demonstrating convergent evolution in CRISPR systems."

### Q38: Who is your target audience?
**Answer**: 
- Primary: Structural biologists and CRISPR researchers
- Secondary: General molecular biologists
- Tertiary: Biotech industry professionals
- Adjusted technical level accordingly

### Q39: What's the broader impact?
**Answer**:
- Evolutionary: Proves convergent evolution at molecular level
- Practical: Guides rational choice of CRISPR tools
- Theoretical: Challenges structure-function assumptions
- Technical: Provides reproducible comparison framework

### Q40: What's next after this work?
**Answer**:
- Expand to more Cas protein families
- Include functional assays with structural data
- Machine learning for Cas classification
- Engineer improved variants based on insights