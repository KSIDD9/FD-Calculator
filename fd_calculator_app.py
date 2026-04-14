# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 16:22:00 2025

@author: kundu_33ss43d
"""

import streamlit as st
from main import calculate_fd_returns

# ---------- Page Config ---------- #

st.set_page_config(
    page_title="FD Calculator", 
    layout="centered")

st.title("🧮 Fixed Deposit Calculator")
st.write("Enter the details below to calculate Fixed Deposit returns.")

# ---------- Inputs ---------- #

FD_Inputs = {}

prin_col1, prin_col2 = st.columns([1,2])

with prin_col1:
    st.write("Principal Amount (₹)")

with prin_col2:
    FD_Inputs ["principal"] = st.number_input(
        "Principal Amount (₹)", 
        min_value=0, 
        step=100,
        format="%d",
        label_visibility="collapsed")

intr_col1, intr_col2 = st.columns([1,2])

with intr_col1:
    st.write("Interest Rate (%)")

with intr_col2:
    FD_Inputs["interest_rate"] = st.number_input(
        "Interest Rate (%)", 
        min_value=0.0, 
        max_value=100.0, 
        step=0.1, 
        format="%.2f",
        label_visibility="collapsed")

st.subheader("Investment Tenure")

InvDur = {} 

Dur_col1, Dur_col2, Dur_col3 = st.columns(3)

with Dur_col1:
    InvDur["years"] = st.number_input(
        "Years",
        min_value=0,
        format="%d")

with Dur_col2:
    InvDur["months"] = st.number_input(
        "Months",
        min_value=0,
        format="%d")

with Dur_col3:
    InvDur["days"] = st.number_input(
        "Days",
        min_value=0,
        format="%d")

FD_Inputs["investment_duration"] = InvDur

strD_col1, strD_col2 = st.columns([1,2])

with strD_col1:
    st.markdown("**Start Date**")

with strD_col2:
    FD_Inputs["start_date"] = st.date_input(
        "Start Date", 
        value="today", 
        format="DD/MM/YYYY",
        label_visibility="collapsed")


st.divider()

# ---------- Validation + Calculation ---------- #

if st.button("Calculate FD"):
    if FD_Inputs["principal"] <= 0:
        st.error("Please enter a Principal Amout greater than 0")
    elif FD_Inputs["interest_rate"] <= 0:
        st.error("Please enter an Interest Rate greater than 0")
    elif FD_Inputs["investment_duration"]["years"] == 0 and FD_Inputs["investment_duration"]["months"] == 0 and FD_Inputs["investment_duration"]["days"] == 0:
        st.error("Please enter a valid Investment Duration")
    else:
        results = calculate_fd_returns(FD_Inputs)

        # ---------- Display Results ---------- #

        st.subheader("💰 FD Calculation Results")

        # Single payout
        st.markdown("### 🔹 Single Payout (Quarterly Compounding)")
        st.write(f"**Maturity Value:** ₹{results['single']['maturity_value']:,.2f}")
        st.write(f"**Total Interest:** ₹{results['single']['total_interest']:,.2f}")

        # Bi-annual payout
        st.markdown("### 🔹 Bi-Annual Payout")
        st.write(f"**Payout per Period:** ₹{results['biannual']['payout_per_period']:,.2f}")
        st.write(f"**Total Interest:** ₹{results['biannual']['total_interest']:,.2f}")

        # Quarterly payout
        st.markdown("### 🔹 Quarterly Payout")
        st.write(f"**Payout per Period:** ₹{results['quarterly']['payout_per_period']:,.2f}")
        st.write(f"**Total Interest:** ₹{results['quarterly']['total_interest']:,.2f}")

        # Monthly payout
        st.markdown("### 🔹 Monthly Payout")
        st.write(f"**Payout per Period:** ₹{results['monthly']['payout_per_period']:,.2f}")
        st.write(f"**Total Interest:** ₹{results['monthly']['total_interest']:,.2f}")

        # Dates
        st.markdown("### 📅 Dates")
        st.write(f"**Maturity Date:** {results['end_date'].strftime('%d-%m-%Y')}")
