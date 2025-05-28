from admin import Admin
from user import User
from Data import Cake





def main():
    admin = Admin()
    user = User()
    choice = 0
    while choice !=3:
        print("\n***************************** WELCOME TO CAKESHOP ***********************")
        print("\t\t\t\t\t1.Admin")
        print("\t\t\t\t\t2.User")
        print("\t\t\t\t\t3.Exit")
        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            is_logged_in = False
            while True:
                
                print("\t\t\t\t\t1.Login")
                print("\t\t\t\t\t2.Logout")
                print("\t\t\t\t\t3.Home page")
                print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                choice = int(input("Enter Your Choice: "))
                if choice == 1:
                    if admin.adminlogin():
                        admin_main(admin)
                        break

                elif choice == 2:
                    if is_logged_in:
                        print(".....Logout.....")
                        is_logged_in = False
                    else:
                        print("You are not logged in.")

                    break
                elif choice == 3:
                    print("Returning to Home Page...")
                    break

                else:
                    print("Invalid Choice")

        elif choice == 2:
            while True:
                
                print("\t\t\t\t\t1.Register")
                print("\t\t\t\t\t2.Login")
                print("\t\t\t\t\t3.Logout")
                print("\t\t\t\t\t4.Home page")
                print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                choice = int(input("Enter Your Choice: "))
                if choice == 1:
                    user.userRegister()
                elif choice == 2:
                    if user.userlogin():
                        user_main(user)
                        break
                elif choice == 3:
                    if is_logged_in:
                        print(".....Logout.....")
                        is_logged_in = False
                    else:
                        print("You are not logged in.")

                    break
                elif choice == 4:
                    print("Returning to Home Page...")
                    break
                else:
                    print("Invaild Choice")


def admin_main(admin):
    while True:
        print("\n***************************** ADMIN MENU ********************************")
        print("\t\t\t\t\t1. View Cake")
        print("\t\t\t\t\t2. Add Cake")
        print("\t\t\t\t\t3. Search Cake")
        print("\t\t\t\t\t4. Remove Cake")
        print("\t\t\t\t\t5. Update Cake")
        print("\t\t\t\t\t6. OrderStatus")
        print("\t\t\t\t\t7. Home Page")
        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            admin.viewCake()
        elif choice == 2:
            admin.addCake()
        elif choice == 3:
            admin.searchByFlavor()
        elif choice == 4:
            admin.removeCake()
        elif choice == 5:
            admin.updateCake()
        elif choice == 6:
            admin.showOrderStatus()
        elif choice == 7:
            print("Returning to Home Page..")
            break
           

        





def user_main(user):
    while True:
        print("\n***************************** USER MENU ********************************")
        print("\t\t\t\t\t1. View Cake")
        print("\t\t\t\t\t2. Serach Cake")
        print("\t\t\t\t\t3. Place An Order")
        print("\t\t\t\t\t4. View Order Status")
        print("\t\t\t\t\t5. Home page")
        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            user.viewCake()
        elif choice == 2:
            user.searchByFlavor()
        elif choice == 3:
            user.place_an_order()
        elif choice == 4:
            user.view_order_status()
        elif choice == 5:
            print("Returning Home Page..")
            break



if __name__ == "__main__":
    main()

