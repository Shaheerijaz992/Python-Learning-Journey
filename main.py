MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def process_coins():
    print("Insert the Coins")
    quarters = int(input("Insert the number of quarters: "))
    dimes = int(input("Insert the number of dimes: "))
    nickles = int(input("Insert the number of nickles: "))
    pennies = int(input("Insert the number of pennies: "))
    quarter_value=0.25*quarters
    dime_value=0.1*dimes
    nickle_value=0.05*nickles
    pennies_value=0.01*pennies
    total_value=quarter_value + dime_value + nickle_value + pennies_value
    return total_value
def check_transection_success(flavour,money_inserted):
    drink_cost = MENU[flavour]["cost"]
    if money_inserted >= drink_cost:
        print(f"Here is your {flavour} Enjoy!")
        change = round(money_inserted - drink_cost, 2)
        print(f"Here is your extra money ${change}")
        return True
    else:
        return False


def print_report():
    print(f"water:{resources['water']} milk:{resources['milk']} coffee:{resources['coffee']}")
report_decision=input("Do you want to print the report?(y/n): ")
if report_decision=="y":
    print_report()

chosen_flavour=input("What would you like? (espresso,latte,cappuccino) ")
if chosen_flavour=="espresso":
    if resources["water"]>=MENU["espresso"]["ingredients"]["water"]  and resources["coffee"]>=MENU["espresso"]["ingredients"]["coffee"]:
        inserted_money = process_coins()
        if check_transection_success(chosen_flavour,inserted_money):
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]

    else:
        print("Sorry,there is not enough resources left")
elif chosen_flavour=="latte":
    if resources["water"]>=MENU["latte"]["ingredients"]["water"] and resources["milk"]>=MENU["latte"]["ingredients"]["milk"] and resources["coffee"]>=MENU["latte"]["ingredients"]["coffee"]:
        inserted_money = process_coins()
        if check_transection_success(chosen_flavour,inserted_money):
            resources["water"]-=MENU["latte"]["ingredients"]["water"]
            resources["milk"]-=MENU["latte"]["ingredients"]["milk"]
            resources["coffee"]-=MENU["latte"]["ingredients"]["coffee"]
    else:
        print("Sorry,there is not enough resources left")
elif chosen_flavour=="cappuccino":
    if resources["water"]>=MENU["cappuccino"]["ingredients"]["water"] and resources["milk"]>=MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"]>=MENU["Cappuccino"]["ingredients"]["coffee"]:
        inserted_money = process_coins()
        if check_transection_success(chosen_flavour,inserted_money):
            resources["water"]-=MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"]-=MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"]-=MENU["cappuccino"]["ingredients"]["coffee"]
    else:
        print("Sorry,there is not enough resources left")
