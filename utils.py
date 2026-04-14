# -*- coding: utf-8 -*-


from dateutil.relativedelta import relativedelta

month_To_Days = 30.42
DAYS_IN_YEAR = 365

def cal_end_date(start_date, duration):
    end_date = start_date + relativedelta(years=duration["years"], months=duration["months"], days=duration["days"])
    return end_date

#logic to break the input duration string to total days
#input variabe durStrng is a string in the format "xY xM xD" eg: "2y 18m 15d"
def parse_duration(durStrng):
    durStrngList = durStrng.lower().split()
    duration_parsed = {
        "years" : 0,
        "months" : 0,
        "days" : 0}

    for x in durStrngList:
        try:
            if x.endswith('y'):
                duration_parsed["years"] = int(x[:-1])
            elif x.endswith('m'):
                duration_parsed["months"] = int(x[:-1])
            elif x.endswith('d'):
                duration_parsed["days"] = int(x[:-1])
            else:
                print(f"Invalid part: {x}")
                return None
                
        except ValueError:
            print(f"Invalid number in: {x}")
            return None
        
    duration_Dic = cal_duration_totalDays(duration_parsed)
            
    return duration_Dic

#logic to convert the Investment duration to total days from the given years, months and days.
#and also to format it into proper number of days and months in a year converting the excess to additional months or years 
#input variable is a dict with {years, months, days}
def cal_duration_totalDays(InvDur):
    formatted_InvDur = {
        "years" : 0,
        "months" : 0,
        "days" : 0,
        "total_days" : 0        
    }

    temp_total_days = (InvDur["days"] 
                       + (month_To_Days * InvDur["months"])
                        + (DAYS_IN_YEAR * InvDur["years"])
                        )

    
    formatted_InvDur["years"] = int (temp_total_days // DAYS_IN_YEAR)
    formatted_InvDur["months"] = int ((temp_total_days % DAYS_IN_YEAR) // month_To_Days)
    
    formatted_InvDur["days"] = round (temp_total_days
                                - ((formatted_InvDur["years"] * DAYS_IN_YEAR) 
                                   + (formatted_InvDur["months"] * month_To_Days)
                                   )
                                   )
    formatted_InvDur["total_days"] = round(temp_total_days)
    return formatted_InvDur


def test_parse_duration():
    test_cases = {
        "2y": {"years": 2, "months": 0, "days": 0, "total_days": 730},
        "2y 3m": {"years": 2, "months": 2, "days": 30, "total_days": 821},
        "1.5y 2m 15d": None,
        "400d": {"years": 1, "months": 1, "days": 5, "total_days": 400},
        "2y 18m 15d": {"years": 3, "months": 6, "days": 15, "total_days": 1293},
        "6m 30d": {"years": 0, "months": 6, "days": 30, "total_days": 213},
        "1y 0m 0d": {"years": 1, "months": 0, "days": 0, "total_days": 365},
        "": {"years": 0, "months": 0, "days": 0, "total_days": 0},  # empty input
        "2y abc 3m": None  # should return None for invalid input
        }
    print("Running test cases for parse_duration()...\n")
    
    for input_str, expected_output in test_cases.items():
        actual_output = parse_duration(input_str)
        if actual_output == expected_output:
            print(f"✅ PASS: '{input_str}' → {actual_output} days")
        else:
            print(f"❌ FAIL: '{input_str}' → {actual_output} (expected {expected_output})")


def main():
    test_parse_duration()


if __name__ == "__main__": 
    main()
