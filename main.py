#1

# class Bank:
#     def __init__(sum):
#         sum.balance = 0
#
#     def deposit(sum):
#         amount = float(input("Enter amount Deposit: "))
#         sum.balance += amount
#         print("   Deposit: ", amount)
#
#     def withdraw(sum):
#         amount = float(input("Enter amount Withdraw: "))
#         sum.balance -= amount
#         print("   Withdraw: ", amount)
#
#     def window(sum):
#         print("Balance: ", sum.balance)
#
#
# a = Bank()
# a.deposit()
# a.withdraw()
# a.window()


# 2

class Money:

    def __init__(self):
        sum.balance = 0

    def to_tng(self):
        price = float(input("Price(tng): "))
        currency = str(input("Currency: "))
        if currency == 'TNG' or 'tng':
            currency = 1
        sum1 = price*currency
        print(sum1, "TNG")

    def to_rub(self):
        price = float(input("Price(rub): "))
        currency = str(input("Currency: "))
        if currency == 'RUB' or 'rub':
            currency = 7.5
        sum2 = price*currency
        print(sum2, "TNG")

    def to_usd(self):
        price = float(input("Price(usd): "))
        currency = str(input("Currency: "))
        if currency == 'USD' or ' usd':
            currency = 475
        sum3 = price*currency
        print(sum3, "TNG")

    def to_eur(self):
        price = float(input("Price(euro): "))
        currency = str(input("Currency: "))
        if currency == 'EURO' or 'euro':
            currency = 480
        sum4 = price*currency
        print(sum4, "TNG")


a = Money()
a.to_tng()
a.to_rub()
a.to_usd()
a.to_eur()