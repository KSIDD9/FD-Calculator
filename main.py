# -*- coding: utf-8 -*-

from datetime import datetime

#Function to get the user inputs and process the same.
def get_user_inputs():
    
    
    #Getting the Principal Value, decimal format
    PrinVal = input("Please enter the Princial Value of the Fixed Deposit:")
    
    
    #Geting the rate of interest, decimal format
    IntRt = input("Please enter the Rate of Interest (%):")
   
    
   #Getting the start date in dd-mm-yyyy format
    while True:
        try:
            user_input = input("Please enter the Start Date of the Fixed Deposit (dd-mm-yyyy):")
            SrtDt = datetime.strptime(user_input, "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid Format, Please enter the date as dd-mm-yyyy")
            
   
    #Getting the Investment Period
    InvDur = input("Please enter the Period of Investment:")
    
    return {
        "Principal" : PrinVal,
        "Rate" : IntRt,
        "Start_Date" : SrtDt,
        "Duration" : InvDur
        }

              
def main():
   user_data = get_user_inputs()
   
   for key, value in user_data.items():
       if isinstance(value, datetime):
           print(f"{key} : {value.strftime('%d-%m-%Y')}")
       else:
           print(f"{key} : {value}")
    
    
if __name__ == "__main__":
    main()