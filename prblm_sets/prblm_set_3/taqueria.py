#ask user for items
#after every entry show total cost(round off to 2 decimal)
#ignore any item not on the list
menu ={"Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}



def main():
    total_cost = 0
    while True:
        try:
            item = input("Item: ").title().strip()
        except EOFError: #if user use ctrl+d to exit
            print(end="\n") #move to newline and break
            break
        if item in menu:
           total_cost=total_cost+ menu[item]
            #frmatting to two decimals
           print(f"${total_cost:.2f}")
        else:continue
main()
