notes = []


def show_menu():
    print("\n............CS Notes App.............")
    print("\n")
    print("1.Add Note")
    print("2.View Notes")
    print("3.Delete Note")
    print("4.Exit")


def add_note(note):
    if note.strip() == "":
        print("Note cannot be empty.")
    else:
        notes.append(note)
        
        file = open("notes.txt", "a")
        file.write(note + "\n")
        file.close()
        
        print("Note added successfully.")
        

def view_notes(notes):
    try:
        file = open("notes.txt", "r")
        content = file.read()
        file.close()
        if content.strip() == "":
                print("No notes available.")
        else:
            print("____Your Notes____")
            print(content)

    except FileNotFoundError:
        print("No notes available.")
        


def delete_note(notes):
    if not notes:
        print("No notes available to delete.")
    else:
        view_notes(notes)
        try:
            index = int(input("Enter the note number to delete: "))
            if 1 <= index <= len(notes):
                deleted_note = notes.pop(index - 1)
                
                file = open("notes.txt", "w")
                for note in notes:
                    file.write(note + "\n")
                file.close()
                print(f"Note '{deleted_note}' deleted successfully.")
            else:
                print("Invalid note number.")
        except ValueError:
            print("Please enter a valid number.")


while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        note = input("Enter your note: ")
        add_note(note)
    elif choice == "2":
        view_notes(notes)
    elif choice == "3":
        delete_note(notes)
    elif choice == "4":
        print("Thank you for using CS Notes App. Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-4.")
