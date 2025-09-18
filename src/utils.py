import numpy as np
import itertools
from scipy import stats
from statsmodels.stats.multitest import multipletests
import glob

epsilon = 1e-10
def threshold_func(x):
    return np.where(x > 1, 1, 0)

def classify_epistasis(P_value, E, S1, S2, S12):
    if E == 0:
        return 'NO'
    if (S1*(S12-S2) < 0) and (S2*(S12-S1) < 0):
        return 'RSE'
    # Simple Sign Epistasis (SE)
    if (S1*(S12-S2) < 0) or (S2*(S12-S1) < 0):
        return 'SSE'
    # Positive Epistasis (PE) 或 Negative Epistasis (NE)
    if E > 0:
        return 'PE'
    if E < 0:
        return 'NE'

def classify_epistasis_P_N(row):
    if not row['Significant']:
        return 'NO'
    if row['E'] == 0:
        return 'NO'
    if row['E'] > 0:
        return 'PE'
    if row['E'] < 0:
        return 'NE'


def get_P(ab, Ab, aB, AB):
    ab_mean = np.mean(ab)
    ab_se = np.std(ab, ddof=1)/np.sqrt(len(ab))
    Ab_mean = np.mean(Ab)
    Ab_se = np.std(Ab, ddof=1)/np.sqrt(len(Ab))
    aB_mean = np.mean(aB)
    aB_se = np.std(aB, ddof=1)/np.sqrt(len(aB))
    AB_mean = np.mean(AB)
    AB_se = np.std(AB, ddof=1)/np.sqrt(len(AB))
    m = np.log((AB_mean+epsilon)/(ab_mean+epsilon)) - np.log((Ab_mean+epsilon)/(ab_mean+epsilon)) - np.log((aB_mean+epsilon)/(ab_mean+epsilon))
    var = (AB_se**2 / (AB_mean + epsilon)**2 +
           ab_se**2 / (ab_mean + epsilon)**2 +
           Ab_se**2 / (Ab_mean + epsilon)**2 +
           aB_se**2 / (aB_mean + epsilon)**2)
    z = np.abs(m/(np.sqrt(var)+epsilon))
    P = 2 * stats.norm.sf(z)
    return P

def get_cv(ab, Ab, aB, AB):
    ab_mean = np.mean(ab)
    ab_se = np.std(ab, ddof=1)/np.sqrt(len(ab))
    Ab_mean = np.mean(Ab)
    Ab_se = np.std(Ab, ddof=1)/np.sqrt(len(Ab))
    aB_mean = np.mean(aB)
    aB_se = np.std(aB, ddof=1)/np.sqrt(len(aB))
    AB_mean = np.mean(AB)
    AB_se = np.std(AB, ddof=1)/np.sqrt(len(AB))
    var = (AB_se**2 / (AB_mean + epsilon)**2 +
           ab_se**2 / (ab_mean + epsilon)**2 +
           Ab_se**2 / (Ab_mean + epsilon)**2 +
           aB_se**2 / (aB_mean + epsilon)**2)
    return var
