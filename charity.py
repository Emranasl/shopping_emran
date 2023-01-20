


from dataclasses import dataclass
import price_list

# # def Product_discount(func):
# #     def inner(*args, **kwargs):
# #         print('Buying more than 5 products has a bigger discount.')
# #         func(*args, **kwargs)
# #         print('There are long term installment terms for home appliances')
# # #         return 
# #     return inner


# # @Product_discount
# # def discount(name):
# #     print(f'{name} are discounted in this store')
# # discount(['Ball', 'tennis rocket', 'swimming glasses','Freshener', 'Fishing hooks', 'tennis table'])  


# class charity:
#     def __init__(self,_name,_lastname,_inventory):
#         self._name = _name
#         self._lastname = _lastname
#         self._inventory = _inventory
# ch1 = charity('john', 'makenzi', '1000')
# ch2 = charity('jan', 'kawely', '1100')
# ch3 = charity('nik', 'sualmon', '900')




fruts_price = {
    'apple': 25, 'banana': 30, 'pomegranate': 35, 'cucumber': 20, 'tomato':15, 'Kiwi':20, 'onion':20,
    'potato': 20, 'Pineapple': 40, 'coconut': 30, 'Aloevera':35, 'Dragon Fruit': 45, 'watermelon':30,
    'Melon': 30, 'tangerine': 25, 'pumpkin': 15, 'Eggplant': 20
}

dairy_price ={
    'milk': 20, 'cheese': 45, 'yogurt': 40, 'Curd': 35, 'cream': 45, 'milk cream': 50, 'Dough':35
}


home_appliances_price = {
    'Television': 200, 'Refrigerator': 350, 'microwave': 250, 'Agitator':70, 'dishwasher':150,
    'vacuum cleaner': 180
}
sport_price = {
    'discount' : 70, 'ball': 60, 'tennis rocket': 55, 'swimming glasses': 50,'Freshener': 40,
    'Fishing hooks':90, 'tennis table': 100
}
@dataclass
class charity:
    '''Inventory class for poor people'''
    _name: str
    _lastname: str
    _inventory: int
    def Inventory_charge(self):
        if _inventory < 20:
            _inventory += 500

ch1 = charity('john', 'makenzi', 1000)
ch2 = charity('jan', 'kawely', 1100)
ch3 = charity('nik', 'sualmon', 800)

def calculate(item,myDict):
    # global inventory
    if item in myDict:
        first_inv = ch1._inventory
        cash = ch1._inventory - myDict[item]
        ch1._inventory = ch1._inventory - myDict[item]
        # if (first_inv != ch1._inventory):
        print(f'inventory = {cash}')
    elif item not in myDict:
        print(f'{item} not in shop')
    if ch1._inventory <= 10:
        print('Please increase your inventory')
print(fruts_price.items())
print(dairy_price.items())
print(sport_price.items())
print(home_appliances_price.items())
while True:
    item = input('pleas enter your list: ')
    calculate(item,fruts_price)
    calculate(item,dairy_price)
    calculate(item,sport_price)
    calculate(item, home_appliances_price)

