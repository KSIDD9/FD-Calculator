# -*- coding: utf-8 -*-

#logic to implement break the input duration string to total days
def parse_duration(durStrng):
    durStrngList = durStrng.lower().split()
    total_days = 0.0
    for x in durStrngList:
        try:
            if x.endswith('y'):
                total_days += float(x[:-1])*365
            elif x.endswith('m'):
                total_days += float(x[:-1])*30.42
            elif x.endswith('d'):
                total_days += int(x[:-1])
            else:
                print(f"Invalid part: {x}")
                return None
                
        except ValueError:
            print(f"Invalid number in: {x}")
            return None
            
    return round(total_days)


def test_parse_duration():
    test_cases = {
        "2y": 730,
        "2y 3m": 821,
        "1.5y 2m 15d": 623,
        "400d": 400,
        "2y 18m 15d": 1293,
        "6m 30d": 213,
        "1y 0m 0d": 365,
        "": 0,  # empty input
        "2y abc 3m": 821  # should ignore invalid parts like 'abc'
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