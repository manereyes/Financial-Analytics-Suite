"""
===============================================================================
Portfolio Generator Module
===============================================================================

Educational customer portfolio generator used throughout the Credit Risk
Fundamentals project.

This module creates synthetic customer portfolios with realistic credit
behavior distributions inspired by retail banking.

The generated datasets are intended exclusively for educational purposes.

Author:
    José Reyes

Project:
    Credit Risk Fundamentals with Python & Numpy
    
===============================================================================
"""

# =============================================================================
# Imports
# =============================================================================

import numpy as np
import pandas as pd

# =============================================================================
# Defining functions
# =============================================================================

# Defining function to generate the late payments of each customer with skewed probabilities
def generate_late_payments(n_customers: int) -> np.ndarray:
    """
    Generate historical late payments.

    The distribution is intentionally skewed toward good customers,
    since most borrowers do not miss payments frequently.

    Returns
    -------
        numpy.ndarray
    """
    return np.random.choice(
        [0, 1, 2, 3, 4, 5],
        size=n_customers,
        p=[0.45, 0.25, 0.15, 0.08, 0.05, 0.02]  # This will generate more "good customers" with 0 late payments
    )

# Defining function to generate the used credit of each customer (normally distributed)
def generate_credit_utilization(n_customers: int) -> np.ndarray:
    """
    Generate Credit Utilization percentages.

    Values follow an educational normal distribution centered around
    45% utilization.
    """
    utilization = np.random.normal(loc=45, scale=18, size=n_customers)

    return np.round(utilization, 2)

# Defining function to generate the credit history of each customer
def generate_credit_history(n_customers: int) -> np.ndarray:
    """
    Generate credit history in years.
    """
    
    history = np.random.normal(loc=9, scale=4, size=n_customers)
    history = np.clip(history, 1, 20)

    return np.round(history).astype(int) # Many banks work with fractions of years, but in this educational case, we will cast to the nearest int value

# Defining function to generate a credit mix based on skewed probabilities
def generate_credit_mix(n_customers: int) -> np.ndarray:
    """
    Generate educational Credit Mix.
    """
    
    return np.random.choice(
        [1, 2, 3, 4],
        size=n_customers,
        p=[0.20, 0.40, 0.30, 0.10] # Same as the generate_late_payments
    )

# Defining function to generate recent inquiries per client
def generate_recent_inquiries(n_customers: int) -> np.ndarray:
    """
    Generate recent credit inquiries.
    """

    return np.random.choice(
        [0, 1, 2, 3, 4, 5],
        size=n_customers,
        p=[0.40, 0.30, 0.15, 0.08, 0.05, 0.02] # This will prioritize no inquiries for "good customers" profile
    )
    

# Defining the main function to generate each customer
def generate_customers(n_customers: int = 500, random_state: int = 42) -> pd.DataFrame:
    """
    Generate an educational credit portfolio.

    Parameters
    ----------
        n_customers : int
        random_state : int

    Returns
    -------
        pandas.DataFrame
    """
    
    # Defining the seed
    np.random.seed(random_state)
    
    # Generating the dataframe to return
    customers = pd.DataFrame({
        "Customer_ID":
            [
                f"C{i:04}"
                for i in range(1, n_customers + 1)
            ],
        "Late_Payments": generate_late_payments(n_customers),
        "Credit_Utilization": generate_credit_utilization(n_customers),
        "Credit_History_Years": generate_credit_history(n_customers),
        "Credit_Mix": generate_credit_mix(n_customers),
        "Recent_Inquiries": generate_recent_inquiries(n_customers)
    })
    
    return customers
    