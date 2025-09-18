# Landscape Navigability using gene expression data
This repository provides code and analysis pipelines for studying **adaptive landscape navigability** and **epistasis** using gene expression levels in yeast.  

> Li, Yang & Zhang, Jianzhi (2025) *Navigability of thousands of adaptive landscapes of RNA and protein expressions by trans-regulatory mutations* 【submitted】  

## 🌐 Background
Adaptive (fitness) landscapes describe the mapping between genotypes and phenotypes or fitness.  
> This project focuses on **gene expression landscapes**, using transcriptomic and proteomic data from 16 yeast genotypes MET15 (ΔM), HIS3 (ΔH), LEU2 (ΔL), URA3 (ΔU), and their combinations (ΔHM, ΔLM, ΔUM, ΔHL, ΔHU, ΔLU, ΔHLM, ΔHUM, ΔLUM, ΔHLU, and ΔHLUM).

Key scientific questions:  
- How navigable are gene expression landscapes when altered by **trans-regulatory mutations**?  
- How does navigability differ between **mRNA** and **protein** expression landscapes?  
- What role does **epistasis** play in shaping accessibility to global optima?  
- How do empirical landscapes compare to **maximally rugged landscapes** and **cis-regulatory (TF binding affinity) landscapes**?

### Global Optimal Navigability
- **Preprocessing:** Normalization and filtering of gene expression levels.  
- **Fitness Landscape Modeling:** Constructing landscapes based on expression levels and fitness values.  
- **Navigability Analysis:** Assessing pathway accessibility between fitness peaks. 

## 📊 Features
- **Landscape constructio**n from transcriptomic & proteomic data.
- Navigability analysis: compute fraction of open paths to global peaks under multiple statistical criteria.
- Epistasis detection: compute ε with error propagation, test significance, and classify as: **Reciprocal Sign Epistasis (RSE)**, **Simple Sign Epistasis (SSE)**, **Positive Epistasis (PE)**, and **Negative Epistasis (NE)**.
### Comparison modules:
- Empirical vs. maximally rugged landscapes
- mRNA vs. protein landscapes (buffering effect)
- Trans- vs. cis-regulatory landscapes (TF binding affinity data)

### **🧮 Epistasis Calculation**

The epistasis value `ε` is calculated using the following formula:

$$
\epsilon = ln E_{AB} - ln E_{aB} - ln E_{Ab} + ln E_{ab}
$$

Where:
- E<sub>AB</sub> is the fitness value of the genotype with both alleles.
- E<sub>aB</sub> and E<sub>Ab</sub> represent the fitness values of the other genotypes formed by different allele combinations.
- E<sub>ab</sub> is the fitness value of widetype genotype.
The standard error (SE) of ε is propagated from replicate variance.
A z-score is computed and significance is tested at P < 0.05.

The program computes this value for all combinations of genetic variants and classifies the interactions based on the significance of `ε`.

## **Installation**

### **Clone the repository**

```bash
git clone https://github.com/yangli-evo/landscape_navigability.git
cd landscape_navigability
```
## Features
- Computes **epistasis values (E)** from genetic interaction data.
- Classifies interactions into **RSE, SSE, PE, or NE** based on statistical criteria.
- Handles **replicate data** and **statistical significance testing**.

## Installation
### Prerequisites
Make sure you have Python 3 installed along with the required libraries:

```bash
pip install pandas numpy scipy
```
