class Product:

    allProducts = {} # Will contain all Products.

    def __init__(self, identificationNumber, item, color, value):
        '''
        An products info or attributes. Adds to a dictionary to track a products ID and price.
        :param identificationNumber:
        :param item:
        :param value:
        '''
        self.identificationNumber = identificationNumber
        self.item = item
        self.color = color
        self.value = value
        Product.allProducts[identificationNumber] = self # Adds the product ID to the product dictionary.

    def getName(self):
        return self.item

        # productDict[identificationNumber] = value

#     # def identifyPrice(self):
#     #     '''
#     #     Building a dictionary to reference price
#     #     :return:
#     #     '''
#     #     return self.value
#
# customer1 = ['John', 'Willard', '544023', 3]
# customer1 = CustomerAccount(customer1[0], customer1[1], customer1[2], customer1[3])
#
# # productDictionary = {3671: 'suitcase', 4689: 'shirt'}
# #
# # print(productDictionary[3671])
# #
#
# productDict = {}
#
# suitcase = [3671, 'Suitcase', '$45.99']
# suitcase = Products(suitcase[0], suitcase[1], suitcase[2])
#
# shirt = [4689, 'Shirt', '$35.99']
# shirt = Products(shirt[0], shirt[1], shirt[2])
#
# print(productDict)
#
# # object(productDictionary[3671].value)
# # print(object(productDictionary[3671]))

# print(customer1.firstName, customer1.lastName, customer1.identificationNumber, customer1.orders)
# customer1.addOrder(2)
# customer1.removeOrder(6)
# print(customer1.orders)
# print(customer1.accountRecievable())




# print(customer1.orderDelivered())