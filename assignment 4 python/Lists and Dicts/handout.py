def main():
    # Problem #1: List Practice
    # Create a list called fruit_list with the given fruits.
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list
    print("Length of the fruit list:", len(fruit_list))

    # Add 'mango' at the end of the list
    fruit_list.append('mango')

    # Print the updated list
    print("Updated fruit list:", fruit_list)
    
    # Problem #2: Index Game
    # Initialize a list for the game
    my_list = [5, 'apple', 42, 'banana', 18]
    
    print("\nWelcome to the Index Game!")
    print("Your current list:", my_list)
    
    while True:
        # Ask the user to choose an operation
        print("\nSelect an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        operation = input("Enter the operation number (1-4): ")

        if operation == '1':
            # Access an element
            index = int(input("Enter the index of the element to access: "))
            if 0 <= index < len(my_list):
                print("Element at index", index, "is:", my_list[index])
            else:
                print("Index out of range!")

        elif operation == '2':
            # Modify an element
            index = int(input("Enter the index of the element to modify: "))
            new_value = input("Enter the new value: ")
            if 0 <= index < len(my_list):
                my_list[index] = new_value
                print("Updated list:", my_list)
            else:
                print("Index out of range!")

        elif operation == '3':
            # Slice the list
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            if 0 <= start < len(my_list) and 0 <= end <= len(my_list) and start < end:
                print("Sliced list:", my_list[start:end])
            else:
                print("Invalid slice indices!")

        elif operation == '4':
            # Exit the game
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()







