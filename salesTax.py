taxRates = open("taxRates")
dic = {}
for line in taxRates:
    line = line.strip().split()
    abbrev_state = line[0]
    rates = line[1]
    dic[abbrev_state] = float(rates)








def error_message():

    print("Something went wrong!")


def calculate_sales_tax(chosenState, price):
    if chosenState in dic:
        salePrice = price + ((dic[chosenState]/100) * price)

    return salePrice





print(dic)
