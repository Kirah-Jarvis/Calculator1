print("1.*")
print("2.+")
print("3.-")
print("4./")
print("select one")
print("or Exit by 7")
num1 = float(input(":"))
num2 = float(input(":"))
i = int(input(":"))

if i == 1:
    print(f":{num1 * num2}")
elif i == 2:
    print(f":{num1 + num2}")
elif i == 3:
    print(f":{num1 - num2}")
elif i == 4:
    if num2 == 0:
        print("Math Error")
    else:
        print(f":{num1 / num2}")
elif i == 7:
    print("Thank you")
else:
    print("Error")
