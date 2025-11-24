import random
while (1):
    num = int(input("Enter the number you want to enter "))
    rand_num = random.randint(1,10)

    if 0<=num<=10:
        if num>6: print("Greater")
        elif num==5: print("Fine")
        else: print("Smaller")
    else: print("Number should be between 1 and 10")
