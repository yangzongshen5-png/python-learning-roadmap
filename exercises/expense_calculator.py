houseRent = 0
Eats = 0
Traffic = 0
Extra = 0
def weeklyCost():
    global houseRent,Eats,Traffic,Extra
    a = float(input("Weekly houserent: "))
    houseRent+=a
    b = float(input("Weekly eats: "))
    Eats+=b
    c = float(input("Weekly traffic: "))
    Traffic+=c
    d = float(input("Weekly extra cost: "))
    Extra+=d
    return a+b+c+d
def expectedMonthlyCost(x):
    return x * 4.3
def expectedYearlyCost(x):
    return x*12
week =weeklyCost()
print("Weekly total cost: "+ str(week))
print("Monthly expected cost: "+ str(expectedMonthlyCost(week)))
print("Yearly expected cost: "+ str(expectedYearlyCost(week)))
