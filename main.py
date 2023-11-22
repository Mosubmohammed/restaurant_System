import random
menuList={}
print('welcome to our restaurant')
print('--'*20)
isWhile=True
orderList=[]
orderDic={}
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
    for i in range(2):
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
            while True:
                try:
                    price=int(input('Enter the item price :'))
                    break
                except Exception as e:
                    print('please enter a valid number')
                    continue
            
            menuDic={'name':name, 'description':desc , 'price':price}
            menuList[result]=menuDic
            print('you just added a new item')
            break
          
    elif Choice == '2':
        while True:
            search = input('Enter the ID of the item: ')
            try:
                if search in menuList:
                    print('Here is the item:')
                    print('#id:', search)
                    print('  - Name:', menuList[search]['name'])
                    print('  - Description:', menuList[search]['description'])
                    print('  - Price:', menuList[search]['price'])
                    break
                else:
                    print('Sorry, the item is not in the menu try again')
            except Exception as e:
                print('An error occurred:', e)

    elif Choice == '3':
         ishere=True
         while ishere:
            Remove1=input('Enter the Id of the item you want delete :') 
            if Remove1 in menuList.keys():
                menuList.pop(Remove1)
                print('successfully deleted')
                ishere=False
            else:
                print('there is something wrong try again') 

    elif Choice =='4':
        if menuList!={}:
            print('--'*20)
            print('all items:')
            for i in menuList:
                print('#id:',i)
                print('  -','name:',menuList[i]['name'])
                print('  -','description:',menuList[i]['description'])
                print('  -','price:',menuList[i]['price'])
        else:
            print('--'*7)
            print('there is no items')        
    elif Choice == '5':
        print('--'*20)
        
        userinput1=input('please enter ur name :')
        while True:
            try:
                userinput2=int(input('please enter ur phone :'))
                break
            except Exception as e:
                print('please enter a valid number')
                continue       
        userinput3=input('please enter the ID of the item :')
        while True:
            if userinput3 in menuList:
                orderDic={
                    'name':userinput1,
                    'phone':userinput2,
                    'item':userinput3
                }
                break
            else:
                print('the item is not in the menu')
                userinput3=input('please enter the ID of the item again:')
        orderList.append(orderDic)
        print('thank you for adding a order')
             

    elif Choice == '6':
            if orderList!=[]:
                print('--'*20)
                print('the orders :')
                for i in orderList:
                    print('*******')
                    print('  -','name:',i['name'])
                    print('  -','phone:',i['phone'])
                    print('  -','item ID:',i['item'])
                    print('---- Item details:')
                    print('    - Name:', menuDic['name'])
                    print('    - Description:', menuDic['description'])
                    print('    - Price:', menuDic['price'])  
            else:
                print('--'*7)
                print('there is no orders')         
    elif Choice == '7':
        Exit=input('are you sure u wanna exit the system , enter YES or NO :')
        if Exit=='yes':
            print('byee thanks for visiting our restraint') 
            isWhile=False 
        else:
            continue      

    else:
        print('--'*7)
        print('wrong choice')    
                             