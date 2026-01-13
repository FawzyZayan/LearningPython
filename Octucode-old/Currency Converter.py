import os
import time


def clear():
  os.system("cls") if os.name == "nt" else os.system("clear")


def printing():
   print ("""
   USD: 1.0
   EUR: 0.93
   EGP: 47.56
   CNY: 7.25""")


printing()

def money():
    currency = input("Choose a currency to convert from: ")
    if currency == "USD":
        amount = input("Enter the amount: ")
        y_n = input(f"\nYou entered {amount} {currency}. Confirm? (Y/N): ").lower()
        if y_n == "n":
            money()
        else:
            clear()
            printing()
            changed_currency = input("Choose a currency to convert to: ")
            if changed_currency == "EGP":
                print ("Analyzing your request... Please wait.")
                time.sleep(3)
                print (f"Checking for {changed_currency}'s best rates available... Please wait.")
                time.sleep(3)
                print (f"Getting a discout price for {currency}... Please wait.")
                time.sleep(2)
                clear()
                print (f"Preparing the deal from USD to EGP... Please wait.")
                print("\nExchange Rate: 1 USD = 47.56 EGP")
                calculating_money = float(amount) * 47.56
                print(f"\n{amount} USD is equal to {calculating_money} EGP")

            elif changed_currency == "EUR":
                print ("Analyzing your request... Please wait.")
                time.sleep(3)
                print(f"Checking for {changed_currency}'s best rates available... Please wait.")
                time.sleep(3)
                print (f"Getting a discout price for {currency}... Please wait.")
                time.sleep(2)
                clear()
                print (f"Preparing the deal from USD to EUR... Please wait.")
                print("\nExchange Rate: 1 USD = 0.93 EUR")
                calculating_money = float(amount) / 0.93
                print(f"\n{amount} USD is equal to {calculating_money} EUR")

            elif changed_currency == "CNY":
                print ("Analyzing your request... Please wait.")
                time.sleep(3)
                print(f"Checking for {changed_currency}'s best rates available... Please wait.")
                time.sleep(3)
                print (f"Getting a discout price for {currency}... Please wait.")
                time.sleep(2)
                clear()
                print (f"Preparing the deal from USD to CNY... Please wait.")
                print("\nExchange Rate: 1 USD = 7.25 EUR")
                calculating_money = float(amount) * 7.25
                print(f"\n{amount} USD is equal to {calculating_money} EUR")
            else:
                print("Invalid choice!")

    elif currency == "EUR":
        amount = input("Enter the amount: ")
        y_n = input(f"\nYou entered {amount} {currency}. Confirm? (Y/N): ").lower()
        if y_n == "n":
            money()
        else:
            clear()
            printing()
            changed_currency = input("Choose a currency to convert to: ")
            if changed_currency == "USD":
                print ("Analyzing your request... Please wait.")
                time.sleep(3)
                print (f"Checking for {changed_currency}'s best rates available... Please wait.")
                time.sleep(3)
                print (f"Getting a discout price for {currency}... Please wait.")
                time.sleep(2)
                clear()
                print (f"Preparing the deal from EUR to USD... Please wait.")
                print("Exchange Rate: 1 EUR = 1.07 USD")
                calculating_money = float(amount) * 1.07
                print(f"{amount} EUR is equal to {calculating_money} USD")

            elif changed_currency == "EGP":
                print ("Analyzing your request... Please wait.")
                time.sleep(3)
                print (f"Checking for {changed_currency}'s best rates available... Please wait.")
                time.sleep(3)
                print (f"Getting a discout price for {currency}... Please wait.")
                time.sleep(2)
                clear()
                print (f"Preparing the deal from EUR to EGP... Please wait.")
                EURtoEGP = 1 * 1.07 * 47.56
                print(f"Exchange Rate: 1 EUR = {EURtoEGP} EGP")
                calculating_money = float(amount) * EURtoEGP
                print(f"{amount} EUR is equal to {calculating_money} EGP")

            elif changed_currency == "CNY":
                print ("Analyzing your request... Please wait.")
                time.sleep(3)
                print (f"Checking for {changed_currency}'s best rates available... Please wait.")
                time.sleep(3)
                print (f"Getting a discout price for {currency}... Please wait.")
                time.sleep(2)
                clear()
                print (f"Preparing the deal from EUR to CNY... Please wait.")
                EURtoCNY = 1 * 1.07 * 7.25
                print(f"Exchange Rate: 1 EUR = {EURtoCNY} CNY")
                calculating_money = float(amount) * EURtoCNY
                print(f"{amount} EUR is equal to {calculating_money} CNY")

    elif currency == "EGP":
        amount = input("Enter the amount: ")
        y_n = input(f"\nYou entered {amount} {currency}. Confirm? (Y/N): ").lower()

        if y_n == "n":
            money()
        else:
            clear()
            printing()
            changed_currency = input("Choose a currency to convert to: ")
            if changed_currency == "USD":
                print ("Analyzing your request... Please wait.")
                time.sleep(3)
                print (f"Checking for {changed_currency}'s best rates available... Please wait.")
                time.sleep(3)
                print (f"Getting a discout price for {currency}... Please wait.")
                time.sleep(2)
                clear()
                print (f"Preparing the deal from EGP to USD... Please wait.")
                print(f"Exchange Rate: 1 EGP = {1 / 47.56} USD")
                calculating_money = float(amount) / 47.56
                print(f"{amount} EGP is equal to {calculating_money} USD")

            elif changed_currency == "EUR":
                print ("Analyzing your request... Please wait.")
                time.sleep(3)
                print (f"Checking for {changed_currency}'s best rates available... Please wait.")
                time.sleep(3)
                print (f"Getting a discout price for {currency}... Please wait.")
                time.sleep(2)
                clear()
                print (f"Preparing the deal from EGP to EUR... Please wait.")
                print(f"Exchange Rate: 1 EGP = {1 / 47.56 / 1.07} EUR")
                calculating_money = float(amount) / 47.56 / 1.07
                print(f"{amount} EGP is equal to {calculating_money} EUR")

            elif changed_currency == "CNY":
                print ("Analyzing your request... Please wait.")
                time.sleep(3)
                print (f"Checking for {changed_currency}'s best rates available... Please wait.")
                time.sleep(3)
                print (f"Getting a discout price for {currency}... Please wait.")
                time.sleep(2)
                clear()
                print (f"Preparing the deal from EGP to CNY... Please wait.")
                print("Exchange Rate: 1 EGP = {1 / 47.56 * 7.25}CNY")
                calculating_money = float(amount) / 47.56 * 7.25
                print(f"{amount} EGP is equal to {calculating_money} CNY")

    elif currency == "CNY":
        amount = input("Enter the amount: ")
        y_n = input(f"\nYou entered {amount} {currency}. Confirm? (Y/N): ").lower()
        if y_n == "n":
            money()
        else:
            clear()
            printing()
            changed_currency = input("Choose a currency to convert to: ")
            if changed_currency == "USD":
                print ("Analyzing your request... Please wait.")
                time.sleep(3)
                print (f"Checking for {changed_currency}'s best rates available... Please wait.")
                time.sleep(3)
                print (f"Getting a discout price for {currency}... Please wait.")
                time.sleep(2)
                clear()
                print (f"Preparing the deal from CNY to USD... Please wait.")
                print("Exchange Rate: 1 CNY = {1 / 7.25} USD")
                calculating_money = float(amount) / 7.25
                print(f"{amount} CNY is equal to {calculating_money} USD")

            elif changed_currency == "EUR":
                print ("Analyzing your request... Please wait.")
                time.sleep(3)
                print (f"Checking for {changed_currency}'s best rates available... Please wait.")
                time.sleep(3)
                print (f"Getting a discout price for {currency}... Please wait.")
                time.sleep(2)
                clear()
                print (f"Preparing the deal from CNY to EUR... Please wait.")
                print("Exchange Rate: 1 CNY = {1 / 7.25 / 1.07} EUR")
                calculating_money = float(amount) / 7.25 / 1.07
                print(f"{amount} CNY is equal to {calculating_money} EUR")

            elif changed_currency == "EGP":
                print ("Analyzing your request... Please wait.")
                time.sleep(3)
                print (f"Checking for {changed_currency}'s best rates available... Please wait.")
                time.sleep(3)
                print (f"Getting a discout price for {currency}... Please wait.")
                time.sleep(2)
                clear()
                print (f"Preparing the deal from CNY to EGP... Please wait.")
                print("Exchange Rate: 1 CNY =  {1 / 7.25 * 47.56} EGP")
                calculating_money = float(amount) / 7.25 * 47.56
                print(f"{amount} CNY is equal to {calculating_money} EGP")
    
    else:
        print ("Invaled Choice!")
        time.sleep(2)
        clear()
        printing()
        money()


money()