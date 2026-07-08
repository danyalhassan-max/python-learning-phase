Product_List = []

while True:

    print("____Shoping Cart____")
    print("1. Add Products")
    print("2. View Cart")
    print("3. Remove Products")
    print("4. Total Products")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Program Closed")
        break

    elif choice == "1":
        Product_name = input("Enter the product name: ")
        print()
        Product_List.append(Product_name)
        print("Product Added Successfully")

    elif choice == "2":
        if len(Product_List) == 0:
            print("Your Shopping Cart is empty")
        else:
            print("Your Shopping Cart")
            for view_Cart in Product_List:
                print(view_Cart)

    elif choice == "3":
        if len(Product_List) == 0:
            print("You have nothing like item in cart")
        else:
            remove_product_name = input("Enter the product you want to remove: ")

            if remove_product_name in Product_List:
                Product_List.remove(remove_product_name)
                print("Successfully Removed")
            else:
                print("Product Not Found")

    elif choice == "4":
        print("Total Products:", len(Product_List))

    else:
        print("Invalid Choice")
