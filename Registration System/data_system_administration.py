import pandas as po
import openpyxl

# Function to input data
def user():
    while True:
        print("\nSelect an action:")
        print("1. Register a New User")
        print("2. Update an Existing User")
        print("3. Delete a User")
        print("4. View All Users")
        print("5. Exit")
        print("6. Show Total users")

        option = input("Option: ")

        if option == '1':
            # Register a new user
            name = input("Name: ")
            number = input("Contact Number: ")
            register_user(name, number)
        elif option == '2':
            # To Update user info
            user_id = input("Enter USer ID: ")
            new_name = input("New Name: ")
            new_number = input("New Number: ")
            update_user(user_id, new_name if new_name else None, new_number if new_number else None)

        elif option == '3':
            # To Delete a user
            user_id = input("Enter User ID: ")
            delete_user(user_id)
        elif option == '4':
            view_users()
        elif option == '5':
            break
        elif option == '6':
            show_total_users()
        else:
            print("Invalid Option.")

# Get the functions to life.

def register_user(name, number):
    try:
        df = po.read_excel("users.xlsx")
    except FileNotFoundError:
        df = po.DataFrame(columns=["ID", "Name", "Number"])

    # Create a simple User ID.
    base_id = name.replace(" ", "").lower()
    user_id = f"{base_id}_{len(df) + 1}"

    # To Add user
    new_user = {"ID": user_id, "Name": name, "Contact Number": number}
    df = df._append(new_user, ignore_index=True)
    df.to_excel("users.xlsx", index=False)
    print(f"New user Added with ID: {user_id}.")

def view_users():
    try:
        df = po.read_excel("users.xlsx")
        print("\nRegistered Users:")
        print(df)
    except FileNotFoundError:
        print("User not found. Register User First")

def update_user(user_id, new_name=None, new_number=None):
    try:
        df = po.read_excel("users.xlsx")

        if user_id in df["ID"].values:
            if new_name:
                df.loc[df["ID"] == user_id, "Name"] = new_name
            if new_number:
                df.loc[df["ID"] == user_id, "Contact Number"] = new_number

            df.to_excel("users.xlsx", index=False)
            print("User Info Updated")
            print(f"New info: Name - {new_name}, Number - {new_number} ")
        else:
            print("User ID not found")
    except FileNotFoundError:
        print("No users found. Register a user first.")
    except Exception as e:
        print(f"Error updating user data: {e}")

def delete_user(user_id):
    try:
        df = po.read_excel("users.xlsx")

        if user_id in df["ID"].values:
            df = df[df["ID"] != user_id]
            df.to_excel("users.xlsx", index=False)
            print("User removed")
        else:
            print("User ID not found.")
    except FileNotFoundError:
        print("No users found. Register a user first.")
    except Exception as e:
        print(f"Error deleting user data: {e}")
def show_total_users():
    try:
        df = po.read_excel("users.xlsx")
        total_users = len(df)
        print(f"\nTotal number of users: {total_users}")
    except FileNotFoundError:
        print("No users found. Register a user first.")

# Make it work
user()
