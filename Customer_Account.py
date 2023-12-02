'''
By: James Burriss
The class CustomerAccount contains information about a customer account. Certain attributes are mutable.
'''

from Github.Projects.Customer_Orders.Product import *
class CustomerAccount:

    def __init__(self, firstName, lastName, identificationNumber, orders):
        '''
        A customer's account info or attributes
        :param firstName:
        :param lastName:
        :param identificationNumber:
        :param orders:
        '''
        self.firstName = firstName
        self.lastName = lastName
        self.identificationNumber = int(identificationNumber)
        self.orders = orders
        self.creditOwed = 0

    def addOrder(self, numOfOrders):
        original = self.orders
        original += numOfOrders
        count = 0
        for x in range(numOfOrders):
            print("Please enter the item ID:", end = ' ')
            try:
                identificationNumber = int(input())
                print("This item's price is", str(productDict[identificationNumber]))
                list = []
                list.append(productDict[identificationNumber])
                # for line in list:
                #     list[0] = line.strip('$')
                #     print(line)
                #     self.creditOwed += float(line)
                line = list[0].strip('$')
                # print(line)
                self.creditOwed += float(line)
            except ValueError:
                print("You can only enter numbers or a decimal. Example: 4459.32")
        self.orders = original
        return original

    def removeOrder(self, numOfOrders):
        # for x in range(numOfOrders):
        original = self.orders
        original -= numOfOrders

        if(original < 0):
            return print('Cannot have a negative amount of orders. Try again!')
        self.orders = original
        return original

    # def orderDelivered(self, numOfOrders):
    #     self.orders = 0
    #     return 'Orders are cleared the number of orders are: ', self.orders

    def accountRecievable(self):
        self.creditOwed = '$' + str(self.creditOwed)
        # amount = None
        # amount = amount.join('$',str.creditOwed)
        return print("The amount owed by", self.firstName, self.lastName, "is", self.creditOwed)
        # return amount