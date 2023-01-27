



Store_inventory =  {
    'apple': 25, 'banana': 30, 'pomegranate': 35, 'cucumber': 20, 'tomato':15, 'Kiwi':20, 'onion':20,
    'potato': 20, 'Pineapple': 40, 'coconut': 30, 'Aloevera':35, 'Dragon Fruit': 45, 'watermelon':30,
    'Melon': 30, 'tangerine': 25, 'pumpkin': 15, 'Eggplant': 20,
    'milk': 20, 'cheese': 45, 'yogurt': 40, 'Curd': 35, 'cream': 45, 'milk cream': 50, 'Dough':35,
    'Television': 200, 'Refrigerator': 350, 'microwave': 250, 'Agitator':70, 'dishwasher':150,
    'vacuum cleaner': 180,'discount' : 70, 'ball': 60, 'tennis rocket': 55, 'swimming glasses': 50,
    'Freshener': 40,'Fishing hooks':90, 'tennis table': 100
}
def calculate(dict,inventory,item):
    while inventory > 20:
        inventory = inventory - dict[item]
        return inventory

inventory = int(input('Please increase your balance as much as you want: '))

    

while True:
    
    item = input ('please add item:  ')
    inventory = calculate(Store_inventory,inventory,item)
    # inventory = inventory - dict[item]
    print(f'inventory = {inventory}')
    if inventory < 20:
        print('Out of credit')
        inventory = int(input('please increase : ')) 
    
