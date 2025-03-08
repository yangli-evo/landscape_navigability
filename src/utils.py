import numpy as np
from scipy import stats

def compute_E_replicates(ab, Ab, aB, AB):
    """Compute epistasis values (E) based on replicate fitness data."""
    E_vals = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    E = AB[i] - aB[j] - Ab[k] + ab[l]
                    E_vals.append(E)
    return E_vals

def classify_epistasis(row):
    """Classifies epistasis into RSE, SSE, PE, NE, or NO."""
    if not row['Significant']:
        return 'NO'
    if row['E'] == 0:
        return 'NO'
    if (np.sign(row['S1']) < 0 and np.sign(row['S2']) < 0 and row['S12'] > row['S1'] and row['S12'] > row['S2']) or \
       (np.sign(row['S1']) > 0 and np.sign(row['S2']) > 0 and row['S12'] < row['S1'] and row['S12'] < row['S2']):
        return 'RSE'
    if (np.sign(row['S1']) != np.sign(row['S2']) and abs(row['S12']) > abs(row['S1']) and abs(row['S12']) > abs(row['S2'])) or \
       (np.sign(row['S1']) == np.sign(row['S2']) and row['S12'] < row['S1'] and row['S12'] > row['S2']):
        return 'SSE'
    return 'PE' if row['E'] > 0 else 'NE'

def perform_statistical_test(values):
    """Performs a t-test on given values to determine significance."""
    t_stat, p_value = stats.ttest_1samp(values, 0)
    return p_value < 0.05  # Returns True if significant
