"""
============================================================
Pricing Module
============================================================

This module implements a simplified pricing strategy used
to assign an interest rate to a customer based on their
estimated Probability of Default (PD).

In real financial institutions, pricing models consider
many additional variables such as funding costs,
competition, profitability targets and regulatory
requirements.

For educational purposes, this module uses a simplified
rule-based pricing policy.

Author:
    José Reyes
    
Project:
    Credit Risk Fundamentals with Python & Numpy

============================================================
"""

# ==========================================================
# Imports
# ==========================================================

import pandas as pd
from enum import Enum


# ==========================================================
# Pricing Policy
# ==========================================================

# Educational pricing policy based on Probability of Default.
#
# Lower PD
#     ↓
# Lower Interest Rate
#
# Higher PD
#     ↓
# Higher Interest Rate


# ==========================================================
# Decision Enumeration
# ==========================================================

class PricingTier(Enum):
    VERY_LOW = "Very Low Risk"
    LOW = "Low Risk"
    MODERATE = "Moderate Risk"
    HIGH = "High Risk"
    VERY_HIGH = "Very High Risk"
    MANUAL = "Manual Review"


# ==========================================================
# Public Functions
# ==========================================================

# Defining a function to assign interest rate based on PD
def assign_interest_rate(customer: pd.Series) -> float | None:
    """
    Assign an annual interest rate according to the customer's
    estimated Probability of Default.

    Customers that have been rejected do not receive a loan
    offer and therefore no interest rate is assigned.

    Parameters
    ----------
        customer: pandas.Series
            A row from the customer DataFrame.

    Returns
    -------
        float | None
            Annual interest rate expressed as a decimal.

            Examples
            --------
            0.09 = 9%

            Returns None when the customer is rejected.
    """

    # Rejected customers do not receive an offer.
    if customer["Decision"] == "Rejected":
        return None

    # Setting the user PD into pd_value
    pd_value = customer["Probability_of_Default"]

    ## Interest Calculator ##
    if pd_value <= 0.05:
        return pd.Series({
            "Interest_Rate": 0.09,
            "Pricing_Tier": PricingTier.VERY_LOW.value
            })
    elif pd_value <= 0.10:
        return pd.Series({
            "Interest_Rate": 0.11,
            "Pricing_Tier": PricingTier.LOW.value
            })
    # Moderate Risk
    elif pd_value <= 0.20:
        return pd.Series({
            "Interest_Rate": 0.13,
            "Pricing_Tier": PricingTier.MODERATE.value
            })
    # High Risk
    elif pd_value <= 0.30:
        return pd.Series({
            "Interest_Rate": 0.16,
            "Pricing_Tier": PricingTier.HIGH.value
            })
    # Very High Risk
    elif pd_value <= 0.40:
        return pd.Series({
            "Interest_Rate": 0.20,
            "Pricing_Tier": PricingTier.VERY_HIGH.value
            })
    # Manual Review
    elif pd_value <= 0.60:
        return pd.Series({
            "Interest_Rate": 0.24,
            "Pricing_Tier": PricingTier.MANUAL.value
            })

    # Outside Lending Policy
    return None