# Landscape Navigability using Gene Expression Levels  

This repository contains code and analysis for exploring **fitness landscape navigability** using **gene expression levels**. The project aims to assess how gene expression variations influence the accessibility of high-fitness regions and the role of genetic interactions in shaping adaptive pathways.  

---

## Workflow  

### ASCII version
            +---------------------+
            |   Expression Data   |
            | (WT + 15 mutants)   |
            +----------+----------+
                       |
                       v
            +---------------------+
            |  Landscape          |
            |  Construction       |
            +----------+----------+
                       |
         +-------------+-------------+
         |                           |
         v                           v

+---------------------+ +----------------------+
| Navigability | | Epistasis Analysis |
| (adaptive walks, | | (ε calculation, |
| open-path fraction) | | RSE / SSE / ME) |
+---------------------+ +----------------------+

### Mermaid version (more visual)

```mermaid
flowchart TD
    A[Expression Data (WT + 15 mutants)] --> B[Landscape Construction]
    B --> C[Navigability<br>(adaptive walks, open paths)]
    B --> D[Epistasis Analysis<br>(ε calculation, RSE / SSE / ME)]
Global Optimal Navigability

Preprocessing: Normalization and filtering of gene expression levels.

Fitness Landscape Modeling: Constructing landscapes based on expression levels of 16 yeast genotypes (WT and 15 auxotrophic mutants).

Navigability Analysis: Assessing pathway accessibility between genotypes and the global peak by adaptive walks, under multiple statistical criteria for defining expression reduction.

Epistasis

This repository also provides code for quantifying and classifying epistasis among genetic interactions based on gene expression data.

Epistasis refers to non-additive interactions between mutations that alter expression relative to expectations under a multiplicative model. The code computes the epistasis value (ε) with propagated measurement error, performs statistical tests, and classifies the interaction type.

Epistasis Calculation

Epistasis between two mutations (A and B) is defined as:

𝜀
𝐴
𝐵
=
ln
⁡
𝐸
𝐴
𝐵
+
ln
⁡
𝐸
𝑎
𝑏
−
ln
⁡
𝐸
𝐴
𝑏
−
ln
⁡
𝐸
𝑎
𝐵
,
ε
AB
	​

=lnE
AB
	​

+lnE
ab
	​

−lnE
Ab
	​

−lnE
aB
	​

,

where:

𝐸
𝑎
𝑏
E
ab
	​

: expression level of the wild type,

𝐸
𝐴
𝑏
E
Ab
	​

, 
𝐸
𝑎
𝐵
E
aB
	​

: expression levels of the two single mutants,

𝐸
𝐴
𝐵
E
AB
	​

: expression level of the double mutant.

The standard error (SE) of 
𝜀
𝐴
𝐵
ε
AB
	​

 is estimated by error propagation across biological replicates, and significance is determined using a z-test (P < 0.05).

Epistasis Classification

Reciprocal Sign Epistasis (RSE): both inequalities satisfied, indicating strong reciprocal reversal of mutational effects.

Single Sign Epistasis (SSE): only one inequality satisfied, indicating partial reversal.

Magnitude Epistasis (ME): significant ε but without sign reversal.

Features

Computes epistasis values (ε) with error propagation.

Classifies significant interactions into RSE, SSE, or ME.

Evaluates landscape navigability by open-path fractions.

Handles replicate gene expression data and applies multiple statistical criteria for robustness.

Installation
Clone the repository
git clone https://github.com/yangli-evo/landscape_navigability.git
cd landscape_navigability
