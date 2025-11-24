print("====Basic Expense Tracker====")
lst = []
def add_items():
    num = int(input("Enter the number of items you purchased today: "))
    for i in range(num):
        lst.append(int(input(f"Enter the cost of your {i+1}st item: ")))

def calculate_tot():
    sum=0
    for item in lst:
        sum+=item
    return sum

def calculate_avg():
    avg=0
    for item in lst:
        avg+=calculate_tot()//len(lst)
    return avg

def calculate_cheapest():
    return min(lst)
def calculate_cosliest():
    return max(lst)

def show_insight():
    print("Total expenses are worth: ₹",calculate_tot())
    print("The average of the expenses is: ₹",calculate_avg())
    print("Costliest item in list is: ₹",calculate_cosliest())
    print("Cheapest item in the list is: ₹",calculate_cheapest())


if __name__ == "__main__":
    while(1):
        print("1. Add items")
        print("2. Show Insight")

        number = int(input("Enter your choice: "))

        if number==1:
            add_items()
        elif number==2:
            show_insight()