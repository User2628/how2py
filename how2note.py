# Function to display the main menu
def display_menu():
    print("""
    =========================================
              how2py Patch List
    =========================================
    1. View Patch Notes
    2. Add New Patch Note
    3. Exit
    =========================================
    """)

# Function to display patch notes
def display_patch_notes(patch_notes):
    if patch_notes:
        print("Here are the current patch notes:\n")
        for index, patch in enumerate(patch_notes, start=1):
            print(f"{index}. {patch}")
    else:
        print("No patch notes available yet.")
    input("\nPress Enter to return to the menu.")

# Function to add a new patch note
def add_patch_note(patch_notes):
    print("Enter the new patch note (or type 'back' to return to the menu):")
    while True:
        new_note = input("> ")
        if new_note.lower() == 'back':
            break
        patch_notes.append(new_note)
        print("\nPatch note added successfully!\n")
        break

# Main function to control navigation and display options
def main():
    patch_notes = []  # List to store patch notes
    while True:
        display_menu()
        choice = input("Select an option (1-3): ")

        if choice == '1':
            display_patch_notes(patch_notes)
        elif choice == '2':
            add_patch_note(patch_notes)
        elif choice == '3':
            print("Exiting the Patch List. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
