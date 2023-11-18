import random


menuList={}

print('welcome to our restaurant')
while True:
    print('_'*20)
    print('1-add a item')
    print('2-search for item')
    print('3-delete a item')
    print('4list all items')
    print('5-place an order')
    print('6-view orders')
    print('7-Exit the System')
    Choice=input('Enter ur choice: ')
    Char='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number1='1 2 3 4 5 6 7 8 9 '
    result=''
    for i in range(0,2):
        Char.random()
        result+=random.random(Char)
        result+=random.random(number1)
    print(result)    
    if Choice == '1':
        name=input('Enter the item name')
        desc=input('Enter the item description')
        price=input('Enter the item price')
        
      
          

    # elif Choice == '2':
    #     pass
    # elif Choice == '3':
    #     price('3')
    # elif Choice =='4':
    #     price('4')
    # elif Choice == '5':
    #     price('5')
    # elif Choice == '6':
    #     price('6')
    # elif Choice == '7':
    #     print('7')                    

