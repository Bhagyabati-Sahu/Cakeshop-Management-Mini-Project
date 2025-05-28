
from Data import Cake
from prettytable import PrettyTable
import os

class Admin:
        
    def adminlogin(self):
        admin_name = "Bhagya"
        admin_password = "bhagya90"
        name = input("\t\t\tEnter Your Name: ").strip()
        password = input("\t\t\tEnter your password: ").strip()
       
        if name == admin_name and password == admin_password:
            print(f"\t\t\tLogin successful.")
            return True
        
        print("\t\t\tInvalid admin name or password.")
        return False
        
            
    def addCake(self):
        try:
            cake_id = int(input("\t\t\tEnter Cake id: ").strip())
            flavor = input("\t\t\tEnter Cake Flover: ").strip()
            size =    input("\t\t\tEnter Cake Size: ").strip()
            quantity = int(input("\t\t\tEnter Number Of Quantity: ").strip())
            price = float(input("\t\t\tEnter Cake Price: ").strip())
            Cake_info = Cake(cake_id,flavor,size,quantity,price)

            with open("Cakedata.txt", "a") as fp:
                data = (f"{Cake_info.cake_id},{Cake_info.flavor},{Cake_info.size},{Cake_info.quantity},{Cake_info.price:.1f}\n")
                fp.write(data)
                fp.write("\n")
                print("\t\t\tCake Added successfully")
        except ValueError:
            print("\t\t\tinvalid input..")
    



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
            flavor = input("\t\t\tEnter Cake Flavor: ").strip()
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
                    
                    if Cake_info[1].strip().lower() == flavor.lower():  # Match flavor, case-insensitive
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


    def removeCake(self):
        try:
            self.viewCake()
            cake_id = int(input("\t\t\tEnter Cake ID: "))
            cakes = []
            found = False
            with open("Cakedata.txt","r+") as fp:
                for line in fp:
                    data = line.split(",")
                    if data[0] == str(cake_id):
                        found = True
                        print("Cake  has been deleted.")
                    else:
                        cakes.append(line)
            with open("Cakedata.txt","w") as fp:
                fp.write("".join(cakes))
            if not found:
                print("Cake is  not found.")
        except FileNotFoundError:
                print("An error occurred while deleting the Cake.")
        except Exception as e:
                print("Error.. ")


    def updateCake(self):
        try:
            self.viewCake()
            cake_id = input("\t\t\tEnter Cake ID to update: ").strip()
            found = False
            cakes = []
            with open("Cakedata.txt", "r") as fp:
                for line in fp:
                    data = line.strip().split(",")
                    if data[0] == str(cake_id):
                        found = True
                        print(f"\t\t\tCurrent details: {line.strip()}")

                        print("\t\t\tWhat do you want to update?")
                        print("\t\t\t1. Flavor")
                        print("\t\t\t2. Size")
                        print("\t\t\t3. Quantity")
                        print("\t\t\t4. Price")
                        print("\t\t\t5. Update All")

                        choice = input("\t\t\tEnter your choice (1-5):").strip()
                        #store values
                        flavor, size, quantity, price = data[1], data[2], data[3], float(data[4])
                        if choice == "1":
                           flavor = input("\t\t\tEnter new Cake Flavor: ").strip()
                        elif choice == "2":
                           size = input("\t\t\tEnter Cake New Size: ").strip()
                        elif choice == "3":
                            quantity = input("\t\t\tEnter new Cake Quantity: ").strip()
                        elif choice == "4":
                            price = float(input("\t\t\tEnter new Cake Price: ").strip())
                        elif choice == "5":
                            flavor = input("\t\t\tEnter new Cake Flavor: ").strip()
                            size = input("\t\t\tEnter Cake New Size: ").strip()
                            quantity = input("\t\t\tEnter new Cake Quantity: ").strip()
                            price = float(input("\t\t\tEnter new Cake Price: ").strip())
                        else:
                            print("\t\t\tInvaild choice.")
                            cakes.append(line)
                            continue

                        updated_line = f"{data[0]},{flavor},{size},{quantity},{price:.1f}\n"
                        cakes.append(updated_line)
                        print(f"\t\t\tCake  has been updated.")
                    else:
                        cakes.append(line)

            if not found:
                print(f"\t\t\tCake is not found.")
            else:
                with open("Cakedata.txt", "w") as fp:
                    fp.writelines(cakes)

        except FileNotFoundError:
            print("Error: Cake data file not found.")
        except ValueError:
            print("Error: Invalid input.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    

    def showOrderStatus(self):
        try:
            with open("Orders.txt", "r") as fp:
                orders = fp.readlines()
            
            if not orders:
                print("No orders have been placed yet.")
                return

            print("\n\t\t\t--- All Orders ---")
            current_user = None
            current_datetime = None
            table = None

            for line in orders:
                line = line.strip()
                
                if line.startswith("Name:"):
                    if current_user and table and len(table._rows) > 0:
                        print(f"\nUser: {current_user}")
                        print(f"Order Date & Time: {current_datetime if current_datetime else 'N/A'}")
                        print(table)
                        print("------------------------------------------------")
                    
                    current_user = line.split(":")[1].strip()
                    current_datetime = None  # Reset for new user
                    table = PrettyTable(["Cake Name", "Quantity", "Unit Price", "Total Price"])
                
                elif line.startswith("Order Date & Time:"):
                    current_datetime = line.split(": ", 1)[1].strip()
                
                elif "Total:" in line:
                    print(f"Total: {line.split(':')[1].strip()}")
                
                elif "GST:" in line:
                    print(f"GST: {line.split(':')[1].strip()}")
                
                elif "To Pay:" in line:
                    print(f"To Pay: {line.split(':')[1].strip()}")
                
                elif line.startswith("Cake Name:"):
                    parts = line.split(", ")
                    if len(parts) == 4:
                        cake_name = parts[0].split(":")[1].strip()
                        quantity = parts[1].split(":")[1].strip()
                        unit_price = parts[2].split(":")[1].strip()
                        total_price = parts[3].split(":")[1].strip()
                        table.add_row([cake_name, quantity, unit_price, total_price])

            # Print last user's order details
            if current_user and table and len(table._rows) > 0:
                print(f"\nUser: {current_user}")
                print(f"Order Date & Time: {current_datetime if current_datetime else 'N/A'}")
                print(table)
                print("--------------------------------------------------------")

        except FileNotFoundError:
            print("No orders found. The 'Orders.txt' file does not exist.")
        except Exception as e:
            print("An error occurred:", e)
