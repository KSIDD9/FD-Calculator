# -*- coding: utf-8 -*-

from datetime import datetime
from utils import cal_end_date, parse_duration
import fd_calculations as fdc

#Function to get the user inputs and process the same.
def get_user_inputs():
    
    #Getting the Principal Value, decimal format
    PrinVal = int(input("Please enter the Princial Value of the Fixed Deposit:"))
    
    
    #Geting the rate of interest, decimal format
    IntRt = float(input("Please enter the Rate of Interest (%):"))
    
    #Getting the Investment Period
    while True:
        InvDurStrng = input("Please enter the Period of Investment as xY xM xD:")
        InvDur = parse_duration(InvDurStrng)
        if InvDur is not None:
            break
        else:
            print("❌ Please enter a valid duration format.\n")
     
    
    #Getting the start date in dd-mm-yyyy format
    while True:
        try:
            user_Dtinput = input("Enter Start Date (dd-mm-yyyy) or type '0' to skip:")
            if user_Dtinput == "0":
                SrtDt = EndDt = None
            else:
                SrtDt = datetime.strptime(user_Dtinput, "%d-%m-%Y")
                EndDt = cal_end_date(SrtDt, InvDur)
            break
        except ValueError:
            print("Invalid Format, Please enter the date as dd-mm-yyyy")           
               
    
    return {
        "Principal" : PrinVal,
        "Rate" : IntRt,
        "Duration" : InvDur,
        "Start_Date" : SrtDt,
        "End_Date" : EndDt
        }

            
              
def main():
   user_data = get_user_inputs()
   
   for key, value in user_data.items():
       if isinstance(value, datetime):
           print(f"{key} : {value.strftime('%d-%m-%Y')}")
       else:
           print(f"{key} : {value}")
    
   mat_Val, totInt = fdc.singlePayout_calc(user_data["Principal"], user_data["Rate"], user_data["Duration"]["total_days"], 4)
   print(f"Maturity Value is ₹{mat_Val:.2f} and the total interest is ₹{totInt:.2f}")
   
   tot_interest, int_payout = fdc.biannualPayout_calc(user_data["Principal"], user_data["Rate"], user_data["Duration"]["total_days"])
   print(f"For Bi-Annual Payout, each payout is ₹{int_payout:.2f} and total interest earned is ₹{tot_interest:.2f}")
   
   tot_interest, int_payout = fdc.quarterlyPayout_calc(user_data["Principal"], user_data["Rate"], user_data["Duration"]["total_days"])
   print(f"For Quarterly Payout, each payout is ₹{int_payout:.2f} and total interest earned is ₹{tot_interest:.2f}")
   
   tot_interest, int_payout = fdc.monthlyPayout_calc(user_data["Principal"], user_data["Rate"], user_data["Duration"]["total_days"])
   print(f"For Monthly Payout, each payout is ₹{int_payout:.2f} and total interest earned is ₹{tot_interest:.2f}")
    
if __name__ == "__main__":
    
    main()