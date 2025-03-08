# Epistasis

This repository contains code for analyzing and classifying **epistasis** between genetic interactions based on fitness data. It computes the epistasis value `ε` and classifies the type of epistasis based on the results.

## **Overview**

Epistasis refers to the interaction between different genetic loci that influence an organism's fitness. The goal of this project is to analyze genetic interactions and classify them into different categories such as **Reciprocal Sign Epistasis (RSE)**, **Simple Sign Epistasis (SSE)**, **Positive Epistasis (PE)**, and **Negative Epistasis (NE)**.

### **Epistasis Calculation Formula**

The epistasis value `ε` is calculated using the following formula:

$$
\epsilon = E_{AB} - E_{aB} - E_{Ab} + E_{ab}
$$

Where:
- E<sub>AB</sub> is the fitness value of the genotype with both alleles.
- E<sub>aB</sub>, E<sub>Ab</sub>, and E<sub>ab</sub> represent the fitness values of the other genotypes formed by different allele combinations.

The program computes this value for all combinations of genetic variants and classifies the interactions based on the significance of `ε`.

## **Installation**

### **Clone the repository**

```bash
git clone https://github.com/yangli-evo/epistasis.git
cd epistasis-analysis

## Features
- Computes **epistasis values (E)** from genetic interaction data.
- Classifies interactions into **RSE, SSE, PE, or NE** based on statistical criteria.
- Handles **replicate data** and **statistical significance testing**.

## Installation
### Prerequisites
Make sure you have Python 3 installed along with the required libraries:

```bash
pip install pandas numpy scipy

