import re

from data import calibration_values

def main():
    sum = 0
    for value in calibration_values:
        digits = re.findall(r'\d', value)
        full_number = digits[0] + digits[-1]
        sum += int(full_number)
    print(sum)

if (__name__ == "__main__"):
    main()