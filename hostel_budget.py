# my hostel budget calculator
# made this cuz i wanted to know how much money ill actually need in college

def welcome():
    print("\n" + "="*45)
    print("     hostel expenses calculator")
    print("     (for newton school of technology)")
    print("="*45)
    print("\nbro this will help u figure out how much")
    print("pocket money u actually need per month")
    print("(trust me, its more than u think)\n")

def get_input(prompt):
    # simple helper so i dont keep typing try-except
    try:
        return float(input(prompt))
    except:
        print("bruh enter a number please")
        return get_input(prompt)

def main():
    print("Hostel Budget Calculator")
    
    mess = float(input("Mess fee per month? (₹): "))
    hostel_rent = float(input("Hostel rent per month? (₹): "))
    travel = float(input("Travel per month? (₹): "))
    laundry = float(input("Laundry per month? (₹): "))
    stationery = float(input("Stationery per month? (₹): "))
    snacks = float(input("Snacks per week? (₹): ")) * 4
    eating_out = float(input("Eating out per month? (₹): "))
    random_shit = float(input("Random stuff per month? (₹): ")
    
    # calculations (hope this is right lol)
    fixed_total = mess + hostel_rent
    variable_total = travel + laundry + stationery
    fun_total = snacks + eating_out + random_shit
    
    grand_total = fixed_total + variable_total + fun_total
    
    # results
    print("\n" + "="*45)
    print("                 YOUR BUDGET")
    print("="*45)
    print(f"Fixed expenses:     ₹{fixed_total:.0f}")
    print(f"Variable expenses:  ₹{variable_total:.0f}")
    print(f"Fun money:          ₹{fun_total:.0f}")
    print("-"*45)
    print(f"TOTAL PER MONTH:    ₹{grand_total:.0f}")
    print("="*45)
    
    # some random advice based on total
    print("\n")
    if grand_total < 5000:
        print("damn u living like a monk or what?")
        print("either ur numbers are wrong or ur built different")
    elif grand_total < 10000:
        print("decent budget. manageable if u dont go out too much")
    elif grand_total < 15000:
        print("pretty normal. this is what most people probably spend")
    elif grand_total < 20000:
        print("ur living good bro. just dont tell ur parents the real number")
    else:
        print("bro u either rich or u added something wrong 💀")
        print("or maybe mumbai is just expensive idk")
    
    print("\n--- SAVING TIPS (if u care) ---")
    
    if eating_out > 3000:
        print("- eat out less? 3k on restaurants is crazy")
    if snacks > 2000:
        print("- chai is love but maybe 1 cup less per day?")
    if travel > 2000:
        print("- get a monthly pass instead of per trip")
    
    print("\nps - this is just an estimate. real life always costs more")
    print("keep an extra 10-15% buffer just in case\n")
    
    save = input("want to save this to a file? (y/n): ").lower()
    if save == 'y':
        with open("my_budget.txt", "w") as f:
            f.write(f"Monthly budget: ₹{grand_total:.0f}\n")
            f.write(f"Fixed: ₹{fixed_total:.0f} | Variable: ₹{variable_total:.0f} | Fun: ₹{fun_total:.0f}\n")
            f.write(f"Date calculated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}\n")
        print("saved to my_budget.txt !\n")
    else:
        print("cool, no file created\n")

if __name__ == "__main__":
    main()
