import os
import sys
import pandas as pd
from itertools import combinations
import numpy as np
import itertools
from scipy import stats

def compute_E_replicates(ab, Ab, aB, AB):
    E_vals = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    E = AB[i] - aB[j] - Ab[k] + ab[l]
                    E_vals.append(E)
    return E_vals

def classify_epistasis(row):
    # If E is not significant, return 'NO'
    if not row['Significant']:
        return 'NO'
    # Check if E is exactly 0 (boundary case)
    if row['E'] == 0:
        return 'NO'
    # Reciprocal Sign Epistasis (RSE)
    if (np.sign(row['S1']) < 0 and np.sign(row['S2']) < 0 and row['S12'] > row['S1'] and row['S12'] > row['S2']) or \
       (np.sign(row['S1']) > 0 and np.sign(row['S2']) > 0 and row['S12'] < row['S1'] and row['S12'] < row['S2']):
        return 'RSE'
    # Simple Sign Epistasis (SSE)
    if (np.sign(row['S1']) != np.sign(row['S2']) and abs(row['S12']) > abs(row['S1']) and abs(row['S12']) > abs(row['S2'])) or \
       (np.sign(row['S1']) != np.sign(row['S2']) and abs(row['S12']) > abs(row['S2']) and abs(row['S12']) > abs(row['S1'])):
        return 'SSE'
    if (np.sign(row['S1']) == np.sign(row['S2']) and row['S12'] < row['S1'] and row['S12'] > row['S2']) or \
       (np.sign(row['S1']) == np.sign(row['S2']) and row['S12'] < row['S2'] and row['S12'] > row['S1']):
        return 'SSE'
    # Positive Epistasis (PE) or Negative Epistasis (NE)
    if row['E'] > 0:
        return 'PE'
    if row['E'] < 0:
        return 'NE'
