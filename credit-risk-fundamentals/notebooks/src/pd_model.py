"""
================================================================================
Probability of Default (PD) Module
================================================================================

Educational implementation of a Probability of Default (PD) model inspired by
Logistic Regression.

This module provides reusable functions for estimating the probability that a
customer will default on a loan using manually calibrated coefficients.

The mathematical formulation follows the same principles used in banking
(Logistic Regression), although the coefficients are educational and were not
trained using historical portfolio data.

Author:
    José Reyes

Project:
    Credit Risk Fundamentals with Python & Numpy

================================================================================
"""

# =============================================================================
# Imports
# =============================================================================

import numpy as np
import pandas as pd


# =============================================================================
# Educational Model Coefficients
# =============================================================================

INTERCEPT = -3.00

BETA_PAYMENT_HISTORY = 2.20
BETA_UTILIZATION = 1.80
BETA_HISTORY = -1.00
BETA_MIX = -0.60
BETA_RECENT_ACTIVITY = 0.90


# =============================================================================
# Core Mathematical Functions
# =============================================================================

def logistic_function(z: float) -> float:
    """
    Applies the Logistic Function.

    Parameters
    ----------
    z : float
        Linear predictor.

    Returns
    -------
    float
        Probability between 0 and 1.
    """

    return 1 / (1 + np.exp(-z))


# =============================================================================
# Feature Engineering
# =============================================================================


# -----------------------------------------------------------------------------
# First... Why do we need to normalize the variables?
# -----------------------------------------------------------------------------
#
# The variables used in this educational Probability of Default model are
# measured on completely different scales.
#
# For example:
#
#     Late Payments          → 0 to 5
#     Credit Utilization     → 0 to 100 (%)
#     Credit History         → 0 to 20 years
#     Credit Mix             → 1 to 4 products
#     Recent Inquiries       → 0 to 5
#
# If we combined these variables directly, those with larger numerical values
# (such as Credit Utilization) would dominate the Logistic Regression equation,
# even if they were not necessarily the most important predictors.
#
# To make every variable comparable, we normalize them to approximately the
# same range (0–1).
#
# This educational implementation uses a simple Min-Max normalization:
#
#     normalized_value = value / maximum_expected_value
#
# This approach makes the model:
#
# • Easier to understand.
# • Easier to interpret.
# • Easier to calibrate manually.
#
# In production environments, banks often use more sophisticated techniques
# such as Standardization (Z-Score), Weight of Evidence (WoE), or Binning,
# depending on the modeling methodology.
#
# -----------------------------------------------------------------------------

def normalize_payment_history(late_payments: int) -> float:
    """
    Normalizes late payments.

    Parameters
    ----------
    late_payments : int

    Returns
    -------
    float
    """

    return min(late_payments / 5, 1)


def normalize_credit_utilization(utilization: float) -> float:
    """
    Normalizes credit utilization.

    Parameters
    ----------
    utilization : float

    Returns
    -------
    float
    """

    return utilization / 100


def normalize_credit_history(years: float) -> float:
    """
    Normalizes credit history.

    Assumes 20 years represents the maximum educational value.
    """

    return min(years / 20, 1)


def normalize_credit_mix(products: int) -> float:
    """
    Normalizes credit mix.

    Assumes four products represents maximum diversification.
    """

    return min(products / 4, 1)


def normalize_recent_activity(inquiries: int) -> float:
    """
    Normalizes recent credit inquiries.
    """

    return min(inquiries / 5, 1)


# =============================================================================
# Business Logic
# =============================================================================

def calculate_logit(customer: pd.Series) -> float:
    """
    Calculates the educational logit.

    Parameters
    ----------
    customer : pandas.Series

    Returns
    -------
    float
    """

    payment_history = normalize_payment_history(customer["Late_Payments"])

    utilization = normalize_credit_utilization(customer["Credit_Utilization"])

    history = normalize_credit_history(customer["Credit_History_Years"])

    mix = normalize_credit_mix(customer["Credit_Mix"])

    activity = normalize_recent_activity(customer["Recent_Inquiries"])

    z = (INTERCEPT + BETA_PAYMENT_HISTORY * payment_history + BETA_UTILIZATION * utilization + BETA_HISTORY * history + BETA_MIX * mix + BETA_RECENT_ACTIVITY * activity)

    return z

#  Defining a function which calculates the logit and the PD
def probability_of_default(customer: pd.Series) -> float:
    """
    Calculates Probability of Default.

    Parameters
    ----------
    customer : pandas.Series

    Returns
    -------
    float
    """

    z = calculate_logit(customer)

    return logistic_function(z)


# =============================================================================
# Business Classification
# =============================================================================

def classify_pd(pd: float) -> str:
    """
    Classifies customers according to PD.
    """

    if pd < 0.05:
        return "Very Low"

    elif pd < 0.15:
        return "Low"

    elif pd < 0.30:
        return "Medium"

    elif pd < 0.50:
        return "High"

    return "Very High"


def expected_default_flag(pd: float, threshold: float = 0.50) -> bool:
    """
    Educational expected default flag.

    Parameters
    ----------
    pd : float

    threshold : float

    Returns
    -------
    bool
    """

    return pd >= threshold