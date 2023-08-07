price = 50
prompt = "Insert Coin: "
while price != 0:
    amount = print("Amount Due: " + str(price))
    coin = input(prompt)
    if coin == "25" or coin == "10" or coin == "5":
        bal = price - int(coin)
        price = bal
    if price < 0:
        change = -1 * price
        amount = print("Change owed: " + str(change))
        break

while price == 0:
    change = price
    print("Change owed: " + str(change))
    break
