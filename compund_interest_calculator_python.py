principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    principle = float(input("Enter the interest rate: "))
    if principle <= 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    principle = float(input("Enter the time in years: "))
    if principle <= 0:
        print("Time can't be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")