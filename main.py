import random
menuList={}
print('welcome to our restaurant')
print('--'*20)
isWhile=True
while isWhile:
    print('_'*20)
    print('1-add a item')
    print('2-search for item')
    print('3-delete a item')
    print('4list all items')
    print('5-place an order')
    print('6-view orders')
    print('7-Exit the System')
    Choice=input('Enter ur choice: ')
    Char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerChar = "abcdefghijklmnopqrstuvwxyz"
    number1 = "0123456789"
    result = ""
    for _ in range(2):
        random_char = random.choice(Char)
        result += random_char
        random_lower_char = random.choice(lowerChar)
        result += random_lower_char
        random_number = random.choice(number1)
        result += random_number
      
    if result in menuList:
        pass
        
    if Choice == '1':
        while True:
            name=input('Enter the item name :')
            desc=input('Enter the item description :')
            price=input('Enter the item price :')
            menuDic={'name':name, 'description':desc , 'price':price}
            menuList[result]=menuDic
            print(menuList)
            break
          
    elif Choice == '2':
       
            search = input('Enter the ID of the item: ')
            try:
                if search in menuList: 
                    print('Here is the item:')
                    print('#id:', search)
                    print('  - Name:', menuList[search]['name'])
                    print('  - Description:', menuList[search]['description'])
                    print('  - Price:', menuList[search]['price'])
                else:
                    print('Sorry, the item is not in the menu')
            except KeyError:
                print('sorry the item is not in the menu')

    elif Choice == '3':
         Remove1=input('Enter the Id of the item to delete it') 
         if Remove1 in menuList.keys():
            menuList.pop(Remove1)
            print('you deleted the item')
         else:
             print('there is something wrong try again') 

    elif Choice =='4':
        print('--'*20)
        print('all items')
        for i in menuList:
            print('#id:',i)
            print('  -','name:',menuList[i]['name'])
            print('  -','description:',menuList[i]['description'])
            print('  -','price:',menuList[i]['price'])
    elif Choice == '5':
        print('--'*20)
        orderList=[]
        orderDic={}
        userinput1=input('please enter ur name :')
        userinput2=input('please enter ur phone :')
        userinput3=input('please enter the ID of the item')
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
            print('--'*20)
            for i in orderList:
               print('#id:',key)
               print('  -','name:',orderList[i]['name'])
               print('  -','description:',orderList[i]['phone'])
               print('  -','price:',orderList[i]['item'])
        
    elif Choice == '7':
        
        print('byee thanks for visiting our restraint') 
        isWhile=False   

    else:
        print('wrong choice')    
                             