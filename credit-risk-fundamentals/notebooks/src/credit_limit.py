"""
============================================================
Credit Limit Module
============================================================

This module implements a simplified Credit Limit Assignment
policy inspired by the lending practices used by financial
institutions.

Once a customer has been approved, the institution must
determine the maximum amount of credit that can be offered.

In practice, credit limits depend on many variables such
as income, debt-to-income ratio, employment stability,
internal policies and profitability.

For educational purposes, this module assigns credit
limits using only the customer's Credit Score.

Author:
    José Reyes
    
Project:
    Credit Risk Fundamentals with Python & Numpy

============================================================
"""

# ==========================================================
# Imports
# ==========================================================

from enum import Enum
import pandas as pd


# ==========================================================
# Credit Limit Tiers
# ==========================================================

class CreditTier(Enum):
    """
    Educational customer segments used to classify borrowers
    according to their Credit Score.

    These segments are only used to improve interpretability
    throughout the notebook.
    """

    EXCELLENT = "Excellent"
    VERY_GOOD = "Very Good"
    GOOD = "Good"
    FAIR = "Fair"
    LIMITED = "Limited"
    DECLINED = "Declined"

    
# ==========================================================
# Public Functions
# ==========================================================

def assign_credit_limit(customer: pd.Series) -> pd.Series:
    """
    Assign a maximum credit limit according to the customer's
    Credit Score.

    Customers that were rejected do not receive a credit offer.

    Parameters
    ----------
    customer : pandas.Series
        A row from the customer DataFrame.

    Returns
    -------
    pandas.Series

        Credit_Limit
            Maximum amount offered by the institution.

        Credit_Tier
            Educational customer segment.
    """
    
    # Rejected receive "None"
    if customer["Decision"] == "Rejected":

        return pd.Series({
            "Credit_Limit": 0,
            "Credit_Tier": CreditTier.DECLINED.value
        })
        
    # Setting credit score
    score = customer["Credit_Score"]
    
    # Lending Policy
    if score >= 800:
        limit = 500_000
        tier = CreditTier.EXCELLENT.value
        
    elif score >= 750:
        limit = 350_000
        tier = CreditTier.VERY_GOOD.value
        
    elif score >= 700:
        limit = 250_000
        tier = CreditTier.GOOD.value
        
    elif score >= 650:
        limit = 150_000
        tier = CreditTier.FAIR.value
        
    elif score >= 550:
        limit = 75_000
        tier = CreditTier.LIMITED.value
        
    else:
        limit = 0
        tier = CreditTier.DECLINED.value
        
    # Returning the limit and assigned tier
    return pd.Series({
        "Credit_Limit": limit,
        "Credit_Tier": tier
    })
