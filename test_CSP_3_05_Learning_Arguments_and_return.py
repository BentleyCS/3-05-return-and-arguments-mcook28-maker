#import CSP_3_05_Learning_Arguments_and_return.py as HW
def convertTemperature(temp):
    value = int(temp[:-1])       # Numeric part
    unit = temp[-1].upper()      # 'C' or 'F'
    if unit == "F":
        celsius = round((value - 32) * 5 / 9)
        return f"{celsius}C"
    elif unit == "C":
        fahrenheit = round((value * 9 / 5) + 32)
        return f"{fahrenheit}F"
    else:
        return "Invalid"
def larger(a, b):
    return a if a >= b else b
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
def fizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num
def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1
if __name__ == "__main__":
    print("Temperature Conversion 42C:", convertTemperature("42C"))  # 107F
    print("Larger of 5 and 10:", larger(5, 10))                     # 10
    print("Grade for 85:", grade(85))                                # B
    print("FizzBuzz of 15:", fizzBuzz(15))                           # FizzBuzz
    print("Collatz of 6:", collatz(6))                               # 3.0