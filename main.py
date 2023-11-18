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
    number1='0123456789'
    lowerChar='abcdefghijklmnopqrstuvwxyz'
    result=''

    for i in range(2):
        random_char = random.choice(Char)
        result+=random_char
        random_lowerChar = random.choice(lowerChar)
        result+=lowerChar
        random_numbers = random.choice(number1)
        result+=random_numbers
      
    if result in menuList:
        pass
        
    if Choice == '1':
        name=input('Enter the item name :')
        desc=input('Enter the item description :')
        price=input('Enter the item price :')
        
      
          

    elif Choice == '2':
        serarch=input('enter the ID of the item :')
        try:
            result in menuList
            print()
        except Exception as e:
            print('its not in the menu')    
    elif Choice == '3':
         Remove1=input('Enter the Id of the item to delete it') 
         if Remove1 in menuList:
            menuList.remove(Remove1)
         else:
             print('there is something wrong try again')   
    elif Choice =='4':
            counter=1
            for i in menuList:
                    print("item",":",counter)
            for key in i:
                print("   ",key,":",i[key])
    elif Choice == '5':
        orderList=[]
        orderDic={}
        userinput1=input('enter ur name')
        userinput2=input('enter ur phone')
        userinput3=input('enter the ID of the item')
        if userinput3 in menuList:
            orderDic={
                 'name':userinput1,
                 'phone':userinput2,
                 'item':userinput3
            }
            orderList.append(orderDic)
        else:
            print('the item is not in the menu')     
    elif Choice == '6':
         counter2=1
         for i in orderList:
              print('order',':',counter2)
         for key in i:
                print("   ",key,":",i[key])
                counter+=1    
    elif Choice == '7':
        print('byee thanks for visiting our restraint')    
    break                         