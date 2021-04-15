def computepay(hours, rate):
    floatHours = float(hours)
    floatRate = float(rate)

    overTimePay = 0

    if floatHours > 40:
        overTimePay = (floatHours - 40.0) * floatRate * 1.5

    normalPay = floatHours * floatRate 
    totalPay =  normalPay + overTimePay

    return totalPay

hours = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    pay = computepay(hours, rate)
    print(pay)
except:
    print("Error, please enter numeric input.")