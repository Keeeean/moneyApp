taxRates = open("taxRates")
dic = {}
for line in taxRates:
    line = line.strip().split(',')
    abbrev_state = line[0]
    rates = line[1]
    dic[abbrev_state] = rates

def error_message():

    print("Something went wrong!")

def calculate_sales_tax(chosenState, price):
    if chosenState in dic:
        chosen_rate = dic[chosenState]
        price = ((float(chosen_rate)/100)*price)+price
    return price




