# Note Keeper App
from tabulate import tabulate
from colored import fg


def main():
    while True:
        try:
            magenta = fg('magenta')
            user_input = input(
                magenta + "Show all notes (S), Add a note (A), Delete a note(D),Search for note (E), Quit(Q): ").lower().strip()

            if user_input == "s":
                show_notes()

            elif user_input == "a":

                blue = fg('dodger_blue_1')
                print(blue+"\nAdding a note\n")
                note = input("Enter your note: ")
                add_note(note=note)
                print()

            elif user_input == "d":

                red = fg('red')
                print(red + "\nDeleting a note\n")
                note_number = input(
                    "Enter the note number you want to delete, or (all) to delete all notes, or quit(Q):")
                delete_note(note_number=note_number)
                print()

            elif user_input == "e":

                yellow = fg('yellow')
                print(yellow + "\nSearching a note\n")
                note_snip = input(
                    "Enter note snippet you want to search for: ")
                search_note(note_snip=note_snip.lower())

            elif user_input == "q":

                print("\n Bye! :) \n")

                break
        except EOFError:
            print()
            break


def number_of_notes():
    return len(open("notes.txt", "r").readlines())


def show_notes():
    notes = []
    green = fg('green')
    print(green + "\nShowing all notes.........")
    with open("notes.txt", "r") as f:
        for line in f:
            notes.append(line.split(": "))
        if notes:
            print(tabulate(notes, headers=[
                "Note", "Content"], tablefmt="fancy_grid"))
        else:
            print("There are no notes yet... add one now!")
    print()


def search_note(note_snip):
    found = []
    notes = []
    with open("notes.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if note_snip in line.lower():
                found.append(line)

    if found:
        for line in found:
            notes.append(line.split(": "))
        print(tabulate(notes, headers=[
            "Note Found", "Content"], tablefmt="fancy_grid"))
    else:
        print("\nNotes not found!\n")
        return("Notes not found!")


def add_note(note):

    with open("notes.txt", "r") as f:
        length_notes = len(f.readlines())

    with open("notes.txt", "a") as f:
        f.write("Note "+str(length_notes+1)+": " + note + "\n")
        return "Added sucessfully"


def delete_note(note_number):

    if note_number.lower() == "q":
        return
    if note_number.lower() == "all":
        with open("notes.txt", "w") as f:
            f.write("")
        return "All notes deleted"

    flag = False

    with open("notes.txt", "r") as f:
        lines = f.readlines()
    with open("notes.txt", "w") as f:
        for line in lines:
            if "Note " + str(note_number) not in line:
                f.write(line)
                # Note Found and deleted
                flag = True

    if flag:
        # reorder the notes with the correct number
        number = 1
        with open("notes.txt", "r") as f:
            lines = f.readlines()
        with open("notes.txt", "w") as f:
            for line in lines:
                if str(number) in line:
                    f.write(line)
                else:
                    f.write("Note "+str(number)+": " + line.split(":")[1])
                number += 1
        return "Deleted sucessfully"


if __name__ == "__main__":
    main()
