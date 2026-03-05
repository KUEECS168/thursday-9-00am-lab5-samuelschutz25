def function ():
    choice = 0
    shop_list = []
    while choice != '4':
        print ("Welcome to your shopping list")
        print ("1) Add Item")
        print ("2) Check off itam")
        print ("3) Print list")
        print ("4) Exit")

        choice = input("Enter a choice: ")
                 


        if choice == '1':
            add = input("What will you add to the list?: ")
            shop_list.append(add)



        if choice == '2':
            off = int(input("Which item will you check off?: "))

        
            item = shop_list[off-1]

            check_off = item[0] + ('-' * (len(item) - 2)) + item [-1]
            shop_list[off-1] = check_off

            

        if choice == '3':
            for i in range (0, len(shop_list)):
                print ("\n", (i+1), ')', shop_list[i])
                i= i + 1
        
function()

print ("Goodbye!")
