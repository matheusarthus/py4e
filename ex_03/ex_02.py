hours = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    floatHours = float(hours)
    floatRate = float(rate)

    overTimePay = 0

    if hours > 40:
        overTimePay = (hours - 40.0) * rate * 1.5

    normalPay = hours * rate 
    totalPay =  normalPay + overTimePay

    print(totalPay)
except:
    print("Error, please enter numeric input.")

