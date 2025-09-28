def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("What item do you want to add to your list: ")
            shopping_list.append(item)

        elif choice == '2':
            item_to_rem = input("What item do you want to remove: ")
            if item_to_rem in shopping_list:
                shopping.remove(item_to_rem)
                print(f"{item_to_rem} has been removed")
            else:
                print(f"{item_to_rem} is not present in the list item")

        elif choice == '3':
            for item in shopping_list:
                print(item)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()