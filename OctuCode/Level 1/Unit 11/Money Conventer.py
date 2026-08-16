import os
import time
import sys

def clear_screen():
  os.system("cls") if os.name == "nt" else os.system("clear")
  
def showing():
    clear_screen()
    
    print("""\n\n|====================================================================||
  ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
  ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
  ||\\$//        ~         '------========--------'                \\$//||
  ||<< /        /$\              // ____ \\                         \ >>||
  ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
  ||<<|        \\ //           || <||  >\  ||                        |>>||
  ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||""")

showing()

print("\n________________________________________________________________________________\n")

print("""
      USD = 1.0
      EUR = 0.87
      EGP = 50.17
      RMB = 6.75""")

rates = {
    "USD": 1.0,
    "EUR": 0.87,
    "EGP": 50.17,
    "RMB": 6.75
}

user_currency = input("\nChoose a currency to convert from: ").upper()

def conversion():
  
    global user_currency
  
    amount = float(input("\nEnter the amount: "))
    if input(f"\nYou entered {amount} {user_currency}. Confirm? (Y/N): ").upper() != "Y":
      conversion()
    else:
        clear_screen()
        showing()
        print("\n________________________________________________________________________________\n")
        print("""
              USD = 1.0
              EUR = 0.87
              EGP = 50.17
              RMB = 6.75""")
        target_currency = input("\nChoose a currency to convert to: ").upper()
        print("\nAnalyzing your request... Please wait.")
        time.sleep(2)
        print(f"Checking for {target_currency}'s best rates available... Please wait.")
        time.sleep(2)
        print(f"Getting a discount price for {user_currency}... Please wait.")
        time.sleep(2)
        
        clear_screen()
        
        print(f"Preparing the deal from {user_currency} to {target_currency}... Please wait.\n")
        time.sleep(2)
        
        if user_currency not in rates or target_currency not in rates:
            print("Invalid currency. Conversion Canceled.")
            time.sleep(3)
            clear_screen()
            showing()
            print("\n________________________________________________________________________________\n")
            print("""
                  USD = 1.0
                  EUR = 0.87
                  EGP = 50.17
                  RMB = 6.75""")
            user_currency = input("\nChoose a currency to convert from: ").upper()
            conversion()

        if rates[user_currency] < rates[target_currency]:
            exchange_rate = rates[target_currency] / rates[user_currency]
            final_amount = amount * exchange_rate
        else:
            exchange_rate = amount / (rates[user_currency] / rates[target_currency])
            final_amount = rates[target_currency] / rates[user_currency]

        print(f"\nExchange Rate: 1 {user_currency} = {exchange_rate} {target_currency}")
        print(f"\n{amount} {user_currency} is equal to {final_amount} {target_currency}")

        
        if input("\nDo you accept this transaction? (Y/N): ").upper() != "Y":
          print("Transaction Canceled.")
          if input("\nDo you want to perform another conversion? (Y/N): ").upper() != "Y":
            sys.exit()
          else:
            user_currency = input("Choose a currency to convert from: ").upper()
            conversion()
        else:
          print("Transaction Completed!")
          if input("\nDo you want to perform another conversion? (Y/N): ").upper() != "Y":
            sys.exit()
          else:
            user_currency = input("Choose a currency to convert from: ").upper()
            conversion()

conversion()