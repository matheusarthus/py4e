hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
overTimePay = 0

if hours > 40:
    overTimePay = (hours - 40.0) * rate * 1.5

normalPay = hours * rate 
totalPay =  normalPay + overTimePay

print(totalPay)