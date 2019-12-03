amount = float(input("Enter the amount(PLN): "))

EUR = 4.2900    #Euro
USD = 3.8706    #U.S. Dollar
CHF = 3.9126    #Swiss franc
RUB = 0.0604    #Russian ruble
CZK = 0.1679    #The Czech crown
UAH = 0.1617    #Ukrainian hryvnia


currency = input("Choose your currency EUR, USD, CHF, RUB, CZK, UAH: ")

if currency == "EUR":
    score = amount / 4.2900
    print(amount,"PLN =", round(score, 2),"EUR")

elif currency == "USD":
    score = amount / 3.8706
    print(amount, "PLN =", round(score, 2), "USD")

elif currency == "CHF":
    score = amount / 3.9126
    print(amount, "PLN =", round(score, 2), "CHF")

elif currency == "RUB":
    score = amount / 0.0604
    print(amount, "PLN =", round(score, 2), "RUB")

elif currency == "CZK":
    score = amount / 0.1679
    print(amount, "PLN =", round(score, 2), "CZK")

elif currency == "UAH":
    score = amount / 0.1617
    print(amount, "PLN =", round(score, 2), "UAH")

