# Landscape Navigability using Gene Expression Levels  
This repository contains code and analysis for exploring **fitness landscape navigability** using **gene expression levels**. The project aims to assess how gene expression variations influence movement across fitness landscapes and the accessibility of high-fitness regions.

### Global Optimal Navigability
- **Preprocessing:** Normalization and filtering of gene expression levels.  
- **Fitness Landscape Modeling:** Constructing landscapes based on expression levels and fitness values.  
- **Navigability Analysis:** Assessing pathway accessibility between fitness peaks. 

## Workflow  
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


### Epistasis

This repository also contains code for analyzing and classifying **epistasis** between genetic interactions based on fitness data. It computes the epistasis value `ε` and classifies the type of epistasis based on the results.


Epistasis refers to the interaction between different genetic loci that influence an organism's fitness. The goal of this project is to analyze genetic interactions and classify them into different categories such as **Reciprocal Sign Epistasis (RSE)**, **Simple Sign Epistasis (SSE)**, **Positive Epistasis (PE)**, and **Negative Epistasis (NE)**.

### **Epistasis Calculation Formula**

The epistasis value `ε` is calculated using the following formula:

$$
\epsilon = ln E_{AB} - ln E_{aB} - ln E_{Ab} + ln E_{ab}
$$

Where:
- E<sub>AB</sub> is the fitness value of the genotype with both alleles.
- E<sub>aB</sub> and E<sub>Ab</sub> represent the fitness values of the other genotypes formed by different allele combinations.
- E<sub>ab</sub> is the fitness value of widetype genotype.

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
