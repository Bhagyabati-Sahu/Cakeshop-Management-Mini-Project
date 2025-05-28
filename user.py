from Data import Cake
from prettytable import PrettyTable
import os
from datetime import datetime


class User:
    
    def userRegister(self):
        try:
            Name = input("\t\t\tEnter Your Name: ").strip()
            Password = input("\t\t\tSet  Password: ").strip()
            Confirm_password = input("\t\t\tComfirm Your Password: ").strip()

            if not os.path.exists("user_log.txt"):
                with open("user_log.txt", "w") as fp:
                    pass

            with open("user_log.txt","r") as fp:
                for line in fp:
                    line = line.strip().split(",")
            
            if Password != Confirm_password:
                print("\t\t\tPassword do not match..Please try again")
                return False
            
            with open("user_log.txt","a") as fp:
                fp.write(f"{Name},{Password}\n")
                print("\t\t\tRegistration successfull...\n")
                return True

        except Exception as e:
            print("\t\t\tAn error occured during registration: {e}")   
            return False        

            

    def userlogin(self):
        try:
            Name = input("\t\t\tEnter Your Name: ")
            Password = input("\t\t\tEnter Password: ")
            with open("user_log.txt","r") as fp:
                for line in fp:
                    line = line.strip().split(",")
                    if Name == line[0] and Password == line[1]:
                        self.current_user = Name
                        print(f"\t\t\tLogin successfull. Welcome, {self.current_user}!")
                        return True
            print(f"\t\t\tInvalid Name or Password.")
            return False
        except FileNotFoundError:
            print("Error: User file 'user_log.txt' not found.")
    
    

    def viewCake(self):
        try:
            with open("Cakedata.txt","r") as fp:
                data = fp.readlines()
                table = PrettyTable(["Cake ID","Cake Name"," Size","Quantity","Price"])
                table_data = []
                for line in data:
                    Cake_info = line.strip().split(",")
                    if len(Cake_info) == 5:
                        table_data.append(Cake_info)
                        table.add_row(Cake_info)
                print("\t\t\t \"\"\" CAKE MENU \"\"\"") 
                print(table)
        except FileNotFoundError:
            print("Error: File 'Cakedata.txt' not found.")


    def searchByFlavor(self):
        try:
            flavor = input("\t\t\tEnter Cake Flavor: ").strip().lower().replace(" ", "")
            with open("Cakedata.txt", "r") as fp:
                data = fp.readlines()
                table = PrettyTable(["Cake ID", "Cake Name", "Size", "Quantity", "Price"])
                table_data = []

                for line in data:
                    line = line.strip()  # Remove whitespace and newline characters
                    if not line:         # Skip empty lines
                        continue

                    Cake_info = line.split(",")  
                    if len(Cake_info) < 5:  # Check for sufficient fields
                        print(f"Skipping line: {line}")
                        continue
                    
                    
                    if Cake_info[1].strip().lower().replace(" ", "") == flavor.lower():  # Match flavor, case-insensitive
                        table_data.append(Cake_info)
                        table.add_row(Cake_info)
                if table_data:
                    print(table)
                else:
                    print("\t\t\tNo cakes found with the specified flavor.")
        except FileNotFoundError:
            print("Error: File 'Cakedata.txt' not found.")
        except Exception as e:
            print("An error occurred:", e)



    
    def place_an_order(self):
        if not hasattr(self, 'current_user') or not self.current_user:
            print("Please log in first")

        cart = []  # To store cart items
        total_bill = 0  # Total bill amount

        while True:
            self.viewCake()
            try:
                cake_id = int(input("Enter Cake ID: "))
                quantity = int(input("Enter Quantity: "))
            except ValueError:
                print("Invalid input. Please enter numbers for Cake ID and Quantity.")
                continue
            except Exception as e:
                print("An error occurred:", e)
                continue

            # Read the cake data file
            try:
                with open("Cakedata.txt", "r") as fp:
                    data = fp.readlines()
            except FileNotFoundError:
                print("Error: File 'Cakedata.txt' not found.")
                return
            except Exception as e:
                print("An error occurred:", e)
                return

            # Process the cake data
            cake_found = False
            updated_cake_data = []  # To store updated stock
            for line in data:
                cake_info = line.strip().split(",")
                if cake_info[0] == str(cake_id):
                    available_quantity = int(cake_info[3])
                    if available_quantity >= quantity:
                        cake_info[3] = str(available_quantity - quantity)  # Update stock
                        total_price = float(cake_info[4]) * quantity  # Calculate total price
                        cart.append([cake_info[1], quantity, float(cake_info[4]), total_price])  # Add to cart
                        total_bill += total_price  # Add to total bill
                        cake_found = True
                    else:
                        print("Not enough quantity available for this cake.")
                updated_cake_data.append(",".join(cake_info))

            # Update the cake data file
            if cake_found:
                with open("Cakedata.txt", "w") as fp:
                    fp.write("\n".join(updated_cake_data))
            else:
                print("Cake not found or insufficient stock.")
                continue

            # Ask user if they want to add more cakes
            try:
                add_more = input("Do you want to add more cakes (y or n)? ").strip().lower()
            except Exception as e:
                print("An error occurred:", e)
                continue

            if add_more != "y":
                break

        # Display the bill
        if cart:
            print("\t\t\t\t\t--- Your Bill ---")
            
            table = PrettyTable(["Cake Name", "Quantity", "Unit Price", "Total Price"])
            for item in cart:
                table.add_row(item)
            print(table)
            gst = round(total_bill * 0.18,2)   # Calculate GST (18%) and round to 2 decimal places
            Grand_Total = round(total_bill + gst,2)
            print("\t\t\t\t\t\t\t Total:", total_bill)
            print("\t\t\t\t\t\t\t18% GST:", gst)
            print("\t\t\t\t\t\t\tTo Pay:", Grand_Total)

            order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                with open("Orders.txt", "a") as order_file:
                    order_file.write(f"Name: {self.current_user}\n")
                    order_file.write(f"Order Date & Time: {order_time}\n")
                    order_file.write(f"Order Details:\n")
                    for item in cart:
                        order_file.write(f"Cake Name: {item[0]}, Quantity: {item[1]}, Unit Price: {item[2]}, Total Price: {item[3]}\n")
                    order_file.write(f"Total: {total_bill:.2f}, GST: {gst:.2f}, To Pay: {Grand_Total:.2f}\n")
                    order_file.write("----------\n")
            except Exception as e:
                print("An error occurred while saving the order details:", e)
        else:
            print("No items in the cart.")
       
    


    def view_order_status(self):
        if not hasattr(self, 'current_user') or not self.current_user:
            print("Please log in first!")
            return

        try:
            with open("Orders.txt", "r") as order_file:
                orders = order_file.readlines()
            
            if not orders:  
                print("\t\t\tNo previous orders found.")
                return
            
            user_orders = []
            current_order = []
            data= False

            for line in orders:
                line = line.strip()
                if line.startswith("Name:"):
                    data = (line.split(":")[1].strip().lower() == self.current_user.lower())
                    if data:
                        current_order = [line]  # Start collecting the current user's order
                    else:
                        if current_order:  # If we already collected some order, store it
                            user_orders.append(current_order)
                        current_order = []  # Reset collection
                
                elif data:
                    current_order.append(line)
            
            if current_order:
                user_orders.append(current_order)  # Save the last order
            
            if not user_orders:
                print("\t\t\tNo orders found for this user.")
                return
            
            print("\t\t\t\t--- Your Orders ---")
            
            for order in user_orders:
                for line in order:
                    print(line)
                print("------------------------------------------------")
        
        except FileNotFoundError:
            print("Error: No orders found. Place an order first.")
        except Exception as e:
            print("An unexpected error occurred:", e)
