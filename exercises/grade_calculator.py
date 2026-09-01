scores = []
for name in ["aScore","bScore","cScore"]:
    while True:
        try:
            score = float(input(name+": "))
            scores.append(score)
            break
        except ValueError:
            print("Invalid input, please enter a number!")
a = scores[0]
b = scores[1]
c = scores[2]

averageScore = (a+b+c)/3
if averageScore<50:
    print("Fail!!")
elif averageScore>=50 and averageScore<=64:
    print("Pass!!")
elif averageScore>=65 and averageScore<=74:
    print("Credit")
elif averageScore>=75 and averageScore<=84:
    print("Distinction")
else:
    print("High Distinction")