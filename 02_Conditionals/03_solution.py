score = int(input("Enter Score : "))

if score >= 101:
    print("Wrong Score")
    exit()


if score >= 90 :
    print("A grade")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
elif score >= 60:
    print("D grade")
else:
    print("F grade")