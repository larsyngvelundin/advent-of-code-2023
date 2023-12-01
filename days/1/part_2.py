import re
from time import time

from data import calibration_values

new_pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

digit_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def get_full_number(first, last):
    if(len(first)> 1):
        first = digit_dict[first]
    if(len(last)> 1):
        last = digit_dict[last]
    return first + last


def main():
    sum = 0
    for value in calibration_values:
        digits = re.findall(new_pattern, value)
        full_number = get_full_number(digits[0], digits[-1])
        sum += int(full_number)

    print(f"main sum: {sum}")

def main_alt(): #broken due to combined words, but slightly faster
    #'eightwo' will be converted to 'eigh2' instead of '82'
    sum = 0
    for value in calibration_values:
        value = value.replace(
            'one', '1').replace(
            'two', '2').replace(
            'three', '3').replace(
            'four', '4').replace(
            'five', '5').replace(
            'six', '6').replace(
            'seven', '7').replace(
            'eight', '8').replace(
            'nine', '9')
        
        digits = re.findall(r'\d', value)
        full_number = digits[0] + digits[-1]
        sum += int(full_number)
    print(f"alt sum: {sum}")

if (__name__ == "__main__"):
    start_time_total = time()
    main()
    end_time = time()
    elapsed_time = end_time - start_time_total
    print(f"- Total time: {elapsed_time:.3f}")

    start_time_total = time()
    main_alt()
    end_time = time()
    elapsed_time = end_time - start_time_total
    print(f"- Total time: {elapsed_time:.3f}")