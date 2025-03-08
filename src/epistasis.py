import pandas as pd
from src.utils import compute_E_replicates, classify_epistasis, perform_statistical_test

def main():
    # Example input data
    example_data = {'S1': -0.5, 'S2': -0.4, 'S12': 0.3, 'E': 0.2, 'Significant': True}
    
    # Compute epistasis category
    category = classify_epistasis(example_data)
    
    # Print result
    print(f"Epistasis category: {category}")

if __name__ == "__main__":
    main()
