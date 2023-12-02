'''
James Burriss
This is a driver to start the program. Product List is predefined for simplicity. A future update could add a dataset
to be read in the program. Possibly a csv file or some other file type.
'''

from Github.Projects.Customer_Orders.Customer_Account import *
from Github.Projects.Customer_Orders.Product import *
import random

prodDictionary = {}
indDictionary = 0
prodList = []
tempList = []

filename = 'ItemList.csv'
openfile = open("ItemList.csv", 'r')
# print(openfile.read())
next(openfile)

for info in openfile:
    tempToken = info.strip().split(',')
    tempList.append(tempToken)
print(tempList)

openfile.close()
# blueTshirt = ["T-Shirt", "Blue", 53.99]
# candyBar = ["Candy", "Red Wrapper", 3.99]
# lawnMower = ["Mower", "Orange Body", 2399.99]
# prodList.extend([blueTshirt, candyBar, lawnMower])
#
#
# '''
# '''
# print(prodList[2])
#
# knownColors = ["Blue", "Red", "Yellow", "Orange", "Green", "Purple", "White", "Black", "Gray"]
# prodObjList = []
#
# while prodList:
#     item = prodList.pop()
#     print(item)
#     for color in knownColors:
#          if color in str(item):
#             # product.append(color[product])
#             itemColor = color
#             print(itemColor)
#             item[1] = itemColor
#             print(item[1])
#             prodObjList.append(Product(random.randint(100000, 999999), item[0], item[1], item[2]))
#             break
# print(prodObjList)
#
#
#
# print("Would you like to create an a Customer Account? Please respond Yes or No.")
# answerResponse = input(str())
# answerResponse = answerResponse.upper()
#
# while True:
#     if answerResponse == "Y" or answerResponse == "YES":
#         print("What is your first Name")
#         firstName = input(str())
#         print("What is your last Name")
#         lastName = input(str())
#     else:
#         print("Ok, have a nice day!")
#         break
#     while True:
#         try:
#             print("Please enter your email address")
#             emailAdd = input(str())
#             print("Please enter your email address a second time")
#             emailAdd2 = input(str())
#             if emailAdd == emailAdd2:
#                 print("Please enter your phone number")
#                 phoneNum = input(str())
#                 accountNumTemp = random.randint(10000, 99999)
#                 print(accountNumTemp)
#                 accountSelfOrd = int(0)
#                 print(accountSelfOrd)
#                 accountCreditOwed = float(0)
#                 print(accountCreditOwed)
#             else:
#                 raise ValueError("The email does not match!")
#         except ValueError as e:
#             print(e)
#         break
#     break
#
# print("Now that you have created an account please type what you would like to do?")
# purchase = str("Purchase")
# lending = str("Lending")
# support = str("Support")
#
# print("\n%-10s %-10s %-10s" % (purchase, lending, support))
# userInput = input(str())
#
# userInput = userInput.upper()
# if userInput == 'PURCHASE':
#     print("You can purchase")
#     for info in prodObjList:
#         print(info.getName())
# if userInput == 'lending':
#     print("You can purchase")
#     for info in prodObjList:
#         print()
#
# print(Product.allProducts)
# if userInput == purchase:
#

'''
Make a Customer_Account object hash table, that associates the account number with the position in the hash.
'''



# self.identificationNumber = int(identificationNumber)
#         self.orders = orders
#         self.creditOwed = 0
# print("Please create a customer account")
# print("What is your first Name")
# print("What is your last Name")

# listAccounts = [CustomerAccount.firstName(input(str()))] # Could put default value



