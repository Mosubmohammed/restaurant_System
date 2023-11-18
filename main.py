menuList={
    
    }

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
    if Choice == '1':
        id=input('Enter the item ID')
        name=input('Enter the item name')
        desc=input('Enter the item description')
        price=input('Enter the item price')
        
        
        print(menuList)
    elif Choice == '2':
        price('2')
    elif Choice == '3':
        price('3')
    elif Choice =='4':
        price('4')
    elif Choice == '5':
        price('5')
    elif Choice == '6':
        price('6')
    elif Choice == '7':
        print('7')                    

