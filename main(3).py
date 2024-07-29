import os

# Path to the file where allowed vehicles are stored
allowed_vehicles_file = 'AllowedVehicles.txt'


# Load allowed vehicles from the file
def load_allowed_vehicles():
  if not os.path.exists(allowed_vehicles_file):
    return []
  with open(allowed_vehicles_file, 'r') as file:
    return [line.strip() for line in file.readlines()]


# Save allowed vehicles to the file
def save_allowed_vehicles(vehicles):
  with open(allowed_vehicles_file, 'w') as file:
    for vehicle in vehicles:
      file.write(f"{vehicle}\n")


# Initialize data set from file
AllowedVehicleList = load_allowed_vehicles()


#print menu
def print_menu():
  print("********************************")
  print("AutoCountry Vehicle Finder v0.5")
  print("********************************")
  print(" Please Ender the following number below from the following menu:")
  print()
  print("1. PRINT all Allowed Vehicles")
  print("2. SEARCH for Authorized Vehicle")
  print("3. ADD Authorized Vehicle")
  print("4. DELTE Authorized Vehicle")
  print("5. EXIT")
  print("20240728_LeeAnthony_Project1.0")
  print("********************************")


#print Allowed Vehicles
def print_AllowedVehicles():
  print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
  for vehicle in AllowedVehicleList:
    print(vehicle)


#search function
def search_AllowedVehicles():
  search_term = input("Please Enter the full Vehicle Name: ")
  if search_term in AllowedVehicleList:
    print(f"{search_term} is an authorized vehicle")
  else:
    print(
        f"{search_term} is not an authorized vehicle, if you received this in error please check the spelling and try again:"
    )


#add function
def Add_AllowedVehicle():
  newVehicle = input(
      "Please Enter the full Vehicle Name you would like to add: ")
  if newVehicle in AllowedVehicleList:
    print("This Vehicle is already in the list")
  else:
    AllowedVehicleList.append(newVehicle)
    save_allowed_vehicles(AllowedVehicleList)
    print(f"You have added {newVehicle} as an authorize vehicle")


#delete function
def delete_AllowedVehicle():
  print("Please Enter the full vehicle name you would like to remove")
  deletedVehicle = input()
  if deletedVehicle in AllowedVehicleList:
    print(f"are you sure you want to remove {deletedVehicle}  from the Authorized Vehicles List")
    choice = input()
    if choice == "yes":
      AllowedVehicleList.remove(deletedVehicle)
      save_allowed_vehicles(AllowedVehicleList)
      print(f"You have REMOVED {deletedVehicle} as an authorized vehicle")
    elif choice == "no":
      pass
  else:
    print(f"{deletedVehicle} is not on the Authorized Vehicles List")


def main():
  print_menu()  
  while True:
    choice = input("Enter your choice: ").strip()
    if choice == "1":
      print_AllowedVehicles() #function to print all vehicles
    elif choice == "2":
      search_AllowedVehicles() #function to search for a vehicle
    elif choice == "3":
      Add_AllowedVehicle() #function to add a vehicle
    elif choice == "4":
      delete_vehicle() # function to delete a vehicle
    elif choice == "5":
      print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
      break
    else:
      print("Invalid choice, Enter a valid choice")
    print_menu() #Print menu after processing choice


if __name__ == "__main__":
  main()
