
import os
import logging 
from dataclasses import dataclass
from enum import Enum
#defin function for
class EXIT_COMMANDS(Enum):
    exit = "exit"
    ex = "ex"
    q = "q"
    quit = "quit"
    ex_key = 'ex_key'
EXIT_COMMANDS = ["q", "quit", "ex", "exit"]
shopping_list = list()
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


# defin decorator for discount
def Product_discount(func):
    def inner(*args, **kwargs):
        print('Buying more than 5 products has a bigger discount.')
        func(*args, **kwargs)
        print('There are long term installment terms for home appliances')
    return inner
@Product_discount
def discount(name):
    print(f'{name} are discounted in this store')
#defin function beautify
def beautify_list(shopp_list):
    for item in shopp_list:
        print(f"> {item} ")
#defin function show for help
def show_help():
    print("enter 'quit' to exit the app and see your list")
    print("enter 'help' to see help ")
    print("enter 'remove' the item you want to remove")
    print("enter 'search' the item you want to search ")
    print("enter 'ds' the item you want to discount")
#defin function for add in list
def add_item(shopp_list, item):
    shopp_list.append(item)
    return shopp_list
#defin function for remove item from list
def remove_item(shopp_list, item):
    if item not in shopp_list:
        print("item that you are trying to remove is not in the list")
    else:
        shopp_list.remove(item)
    return shopp_list
#defin function for search
def show_search():
    for item in shopping_list:
        if item in shopping_list:
            print(f"search True , {item}")
        else:
            print("search_false")
def clear_screen():
    return os.system("cls")
def calculate(item,myDict):
    # global inventory
    if item in myDict:
        cash = ch1._inventory - myDict[item]
        ch1._inventory = ch1._inventory - myDict[item]
        print(f'inventory = {cash}')
    elif item not in myDict:
        print(f'{item} not in shop')
    if ch1._inventory <= 10:
        print('Please increase your inventory')
users = {
    'sepehr':'123456',
    'emran':'456789',
    'mohammad': '987654'
}
enter_username = input('please enter your username: ')
enter_password = input('please entar your password: ')
while enter_username not in users or users[enter_username] != enter_password:
    print('your username or password is wrong!')
    enter_username = input('enter your usename again: ')
    enter_password = input('enter your password again: ')
print('you loged in !')
ex_key = False
while True:
    item = input('please add your list : ').strip().casefold()
    for com in EXIT_COMMANDS:
        if item == com:
            ex_key = True
    if ex_key is True:
        break    
    try:
        item in EXIT_COMMANDS
    except :
        print('you exit of program')
        logging.error
    #input your item
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.info(item)
    clear_screen()
    # define iidiscount
    if item == 'ds':
        (discount(['discount : ','Ball', 'tennis rocket', 'swimming glasses','Freshener', 'Fishing hooks', 'tennis table']))
    #define show situation
    elif item == "show":
        beautify_list(shopping_list)
    #define help situation
    elif item == "help":
        show_help()
        logging.info(item)
    #define remove situation
    elif item == "remove":
        item_to_remove = input("pleas enter the item you want to remove: ")
        remove_item(shopping_list, item_to_remove)
        logging.info(item)
    elif item == "search":
        show_search()
        logging.info(item)
    else:
        if item in shopping_list:
            print(input('item is already in your list '))
        else:
            add_item(shopping_list, item)
            print(f"{item} add to your list and ther are {len(shopping_list)} item in your list ")
