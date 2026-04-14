# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 16:21:31 2025

@author: kundu_33ss43d
"""

DAYS_IN_YEAR = 365
QUARTERLY = 4
BIANNUAL = 2
PER_MONTH = 12

# ---------- Core Calculations ---------- #

def singlePayout_calc(principal, annual_rate, total_days, comp_Factor):
    period_rate = (annual_rate/100) / comp_Factor
    time_Factor = (comp_Factor * total_days) / DAYS_IN_YEAR
    
    maturity_amount = principal * (1 + period_rate) ** time_Factor
    total_interest = maturity_amount - principal
    
    return maturity_amount, total_interest

def multiPayout_calc(payout_frequency, principal, annual_rate, total_days):
    period_days = DAYS_IN_YEAR / payout_frequency

    num_full_periods = int (total_days // period_days)
    remaining_days = total_days % period_days

    period_rate = (annual_rate / 100) / payout_frequency
    payout_per_period = principal * period_rate

    total_interest = payout_per_period * num_full_periods

    if remaining_days > 0:
        interest_for_remaining = principal * (annual_rate/100) * (remaining_days/DAYS_IN_YEAR)
        total_interest += interest_for_remaining
        
    return total_interest, payout_per_period


def biannualPayout_calc(principal, annual_rate, total_days):
    payout_frequency = BIANNUAL
    return multiPayout_calc(payout_frequency, principal, 
                            annual_rate, total_days)

def quarterlyPayout_calc(principal, annual_rate, total_days):
    payout_frequency = QUARTERLY
    return multiPayout_calc(payout_frequency, principal, 
                            annual_rate, total_days)

def monthlyPayout_calc(principal, annual_rate, total_days):
    payout_frequency = PER_MONTH
    return multiPayout_calc(payout_frequency, principal, 
                            annual_rate, total_days)
    