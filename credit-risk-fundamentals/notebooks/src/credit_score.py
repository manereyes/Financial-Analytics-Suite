"""
================================================================================
Credit Scoring Module
================================================================================

This module contains the business rules used to calculate the
educational credit score throughout the project.

Author:
    José Reyes

Project:
    Credit Risk Fundamentals with Python
"""

import pandas as pd

# =============================================================================
# Payment History
# =============================================================================

def payment_history_score(late_payments: int) -> int:
    """
    Calculates the Payment History Score.

    Parameters
    ----------
    late_payments : int
        Number of late payments.

    Returns
    -------
    int
        Educational score between 20 and 100.
    """

    if late_payments == 0:
        return 100

    elif late_payments == 1:
        return 90

    elif late_payments == 2:
        return 75

    elif late_payments == 3:
        return 55

    return 20


# =============================================================================
# Credit Utilization
# =============================================================================

def utilization_score(utilization: float) -> int:
    """
    Calculates the Credit Utilization Score.

    Parameters
    ----------
    utilization : float
        Percentage of available credit currently in use.

    Returns
    -------
    int
        Educational score between 25 and 100.
    """

    if utilization < 30:
        return 100

    elif utilization < 50:
        return 80

    elif utilization < 70:
        return 60

    return 25


# =============================================================================
# Credit History Length
# =============================================================================

def credit_history_score(years: float) -> int:
    """
    Calculates the Credit History Length Score.

    Parameters
    ----------
    years : float
        Number of years the customer has maintained credit accounts.

    Returns
    -------
    int
        Educational score between 30 and 100.
    """

    if years > 10:
        return 100

    elif years >= 5:
        return 80

    elif years >= 2:
        return 60

    return 30


# =============================================================================
# Credit Mix
# =============================================================================

def credit_mix_score(products: int) -> int:
    """
    Calculates the Credit Mix Score.

    Parameters
    ----------
    products : int
        Number of active credit products.

    Returns
    -------
    int
        Educational score between 40 and 100.
    """

    if products >= 4:
        return 100

    elif products == 3:
        return 80

    elif products == 2:
        return 60

    return 40


# =============================================================================
# Recent Credit Activity
# =============================================================================

def recent_activity_score(inquiries: int) -> int:
    """
    Calculates the Recent Credit Activity Score.

    Parameters
    ----------
    inquiries : int
        Number of recent credit inquiries.

    Returns
    -------
    int
        Educational score between 30 and 100.
    """

    if inquiries == 0:
        return 100

    elif inquiries == 1:
        return 90

    elif inquiries == 2:
        return 75

    elif inquiries == 3:
        return 60

    return 30


# =============================================================================
# Raw Credit Score
# =============================================================================

def calculate_raw_score(customer: pd.Series) -> int:
    """
    Calculates the weighted educational credit score for a single customer.

    Parameters
    ----------
    customer : pandas.Series
        Customer financial information.

    Returns
    -------
    float
        Raw credit score between 0 and 100.
    """
    
    # Calculating with functions
    payment_score = payment_history_score(customer["Late_Payments"])
    utilization = utilization_score(customer["Credit_Utilization"])
    history = credit_history_score(customer["Credit_History_Years"])
    mix = credit_mix_score(customer["Credit_Mix"])
    activity = recent_activity_score(customer["Recent_Inquiries"])
    
    # Calculating raw_score
    raw_score = ((payment_score * 0.35) + (utilization * 0.30) + (history * 0.15) + (mix * 0.10) + (activity * 0.10))
    
    return round(raw_score, 2)


# =============================================================================
# Credit Score Normalization
# =============================================================================

def normalize_credit_score(raw_score: float) -> int:
    """
    Converts the educational Raw Score into a
    standardized Credit Score.

    Parameters
    ----------
    raw_score : float
        Educational score between 0 and 100.

    Returns
    -------
    int
        Educational Credit Score between 400 and 850.
    """

    credit_score = 400 + (4.5 * raw_score)

    return round(credit_score)


# =============================================================================
# Risk Categories
# =============================================================================

def assign_credit_rating(score: int) -> str:
    """
    Assigns an educational credit rating.

    Parameters
    ----------
    score : int

    Returns
    -------
    str
        Credit Rating.
    """

    if score >= 750:
        return "Excellent"

    elif score >= 650:
        return "Good"

    elif score >= 550:
        return "Fair"

    return "Poor"