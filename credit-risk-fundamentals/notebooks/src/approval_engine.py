"""
============================================================
Approval Engine Module
===============================================================================
This module implements a simplified Credit Decision Engine
inspired by the approval workflow used by financial
institutions.

Using a customer's Credit Score, Probability of Default
(PD) and Credit Utilization, the module determines whether
the customer should be:

    • Approved
    • Rejected
    • Sent to Manual Review
    
The objective of this module is educational. The business
rules implemented here are simplified and should not be
interpreted as real lending policies.

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
# Decision Enumeration
# ==========================================================

class Decision(Enum):
    """
    Possible outcomes produced by the Credit Decision Engine.

    Using an Enum avoids hardcoding text strings throughout the
    project and reduces the possibility of typing mistakes.
    """

    APPROVED = "Approved"
    REJECTED = "Rejected"
    MANUAL_REVIEW = "Manual Review"

# ==========================================================
# Business Rules (public vars)
# ==========================================================

MIN_APPROVAL_SCORE = 550
MAX_APPROVAL_PD = 0.40
MAX_MANUAL_REVIEW_PD = 0.60
MAX_UTILIZATION = 95

# ==========================================================
# Utility Functions
# ==========================================================

# Defininf the function that approves or rejects a customer based on ther C.S and P.D
def approve_customer(customer: pd.Series) -> bool:
    """
    Determine whether a customer satisfies the minimum
    requirements for automatic approval.

    Business Rules
    --------------
        • Credit Score must be at least 550.
        • Probability of Default must not exceed 40%.

    Parameters
    ----------
        customer: pandas.Series
            A row from the customer DataFrame.

    Returns
    -------
        bool:
            True if the customer satisfies the approval rules.
    """

    score = customer["Credit_Score"]
    pd_value = customer["Probability_of_Default"]

    return (score >= MIN_APPROVAL_SCORE and pd_value <= MAX_APPROVAL_PD) # Returns True or False

# Defining the function that categorizes a customer into "manual review" depending of their P.D and Credit Utilization
def manual_review(customer: pd.Series) -> bool:
    """
    Determine whether a customer should be evaluated by a
    credit analyst instead of receiving an automatic decision.

    Customers are sent to Manual Review when:
        • Their Probability of Default falls into an intermediate
        risk range.
    OR
        • Their Credit Utilization is extremely high.

    Parameters
    ----------
        customer : pandas.Series

    Returns
    -------
        bool
    """

    pd_value = customer["Probability_of_Default"]
    utilization = customer["Credit_Utilization"]

    return (
        (MAX_APPROVAL_PD < pd_value <= MAX_MANUAL_REVIEW_PD) or (utilization >= MAX_UTILIZATION)
    )

# --- #

# Building the decision tree
def decision_reason(customer: pd.Series) -> str:
    """
    Explain why the customer received a particular decision.

    Providing an explanation improves transparency and mimics
    the behaviour of many real-world Decision Engines.

    Parameters
    ----------
        customer: pandas.Series

    Returns
    -------
        str:
            Human-readable explanation.
    """

    score = customer["Credit_Score"]
    pd_value = customer["Probability_of_Default"]
    utilization = customer["Credit_Utilization"]

    # We will generate a "reason" for every decision
    if score < MIN_APPROVAL_SCORE:
        return "Credit Score below minimum policy."

    if pd_value > MAX_MANUAL_REVIEW_PD:
        return "Probability of Default is too high."

    if utilization >= MAX_UTILIZATION:
        return "Very high credit utilization."

    if MAX_APPROVAL_PD < pd_value <= MAX_MANUAL_REVIEW_PD:
        return "Intermediate risk requires manual review."

    return "Customer satisfies approval policy."


# ==========================================================
# Public Functions to call
# ==========================================================


def generate_decision(customer: pd.Series) -> pd.Series:
    """
    Generate the final lending decision.

    This function represents the public interface of the module
    and is the only function that should normally be called
    from the notebook.

    Parameters
    ----------
        customer: pandas.Series

    Returns
    -------
        pandas.Series

    Output
    ------
        Decision
            Approved / Rejected / Manual Review

    Decision_Reason
        Business explanation of the decision.
    """

    if approve_customer(customer):
        decision = Decision.APPROVED.value

    elif manual_review(customer):
        decision = Decision.MANUAL_REVIEW.value

    else:
        decision = Decision.REJECTED.value

    return pd.Series({
        "Decision": decision,
        "Decision_Reason": decision_reason(customer)
        })

