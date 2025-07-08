# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 16:22:00 2025

@author: kundu_33ss43d
"""

import streamlit as st
from datetime import datetime
from utils import parse_duration, cal_end_date
import fd_calculations as fd

st.set_page_config(page_title="FD Calculator", layout="centered")

st.title("🧮 Fixed Deposit Calculator")


PrinVal = st.number_input("Enter the Principle Amout (₹)", min_value=0, step=100)

st.write(f"You have entered: ₹{PrinVal:,}")



# #Input fileds
# PrinVal = st.number_input("Enter Principal Amount (₹)", min_value=0.0, step=100.0, format="%.2f")
# IntRt = st.number_input("Enter Interest Rate (%)", min_value=0.0, max_value=100.0, step=0.1, format="%.2f")
# InvDurStrng = st.text_input("Enter Duration (e.g. 1y 6m 15d)")

# start_date_input = st.date_input("Start Date", value=None)

# # When user clicks the Calculate button
# if st.button("Calculate"):

#     duration = parse_duration(InvDurStrng)

#     if duration is None:
#         st.error("❌ Please enter a valid duration format.")
#     else:
#         total_days = duration["total_days"]

#         if start_date_input:
#             SrtDt = datetime.combine(start_date_input, datetime.min.time())
#             EndDt = cal_end_date(SrtDt, duration)
#             st.write(f"Start Date: {SrtDt.strftime('%d-%m-%Y')}")
#             st.write(f"End Date: {EndDt.strftime('%d-%m-%Y')}")

#         # Call your FD calc logic
#         mat_Val, totInt = fd.singlePayout_calc(PrinVal, IntRt, total_days, 4)
#         st.success(f"💰 Maturity Value: ₹{mat_Val:,.2f}")
#         st.info(f"Total Interest Earned: ₹{totInt:,.2f}")
