# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 16:21:31 2025

@author: kundu_33ss43d
"""

def singlePayout_calc(principal, annual_rate, total_days, comp_Factor):
    period_days = 365
    
    period_rate = (annual_rate/100) / comp_Factor
    time_Factor = (comp_Factor * total_days) / period_days
    
    maturity_amount = principal * (1 + period_rate) ** time_Factor
    total_payout = maturity_amount - principal
    
    return maturity_amount, total_payout

def multiPayout_calc(payout_frequency, principal, annual_rate, total_days):
    period_days = 365 / payout_frequency

    num_full_periods = total_days // period_days
    remaining_days = total_days % period_days

    period_rate = (annual_rate / 100) / payout_frequency
    payout_per_period = principal * period_rate

    total_payout = payout_per_period * num_full_periods

    if remaining_days > 0:
        interest_for_remaining = principal * (annual_rate/100) * (remaining_days/365)
        total_payout += interest_for_remaining
        
    return total_payout, payout_per_period


def biannualPayout_calc(principal, annual_rate, total_days):
    payout_frequency = 2
    return multiPayout_calc(payout_frequency, principal, 
                            annual_rate, total_days)

def quarterlyPayout_calc(principal, annual_rate, total_days):
    payout_frequency = 4
    return multiPayout_calc(payout_frequency, principal, 
                            annual_rate, total_days)

def monthlyPayout_calc(principal, annual_rate, total_days):
    payout_frequency = 12
    return multiPayout_calc(payout_frequency, principal, 
                            annual_rate, total_days)
    