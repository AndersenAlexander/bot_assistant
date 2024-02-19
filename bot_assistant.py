def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.lower(), args

def add_contact(contacts):
    user_input = input("Enter username and phone number separated by a space: ")
    args = user_input.split()
    if len(args) != 2:
        return "Invalid input format. Please enter a username and a phone number separated by a space."

    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2 or args[0] not in contacts:
        return "Invalid input or contact not found."
    name, new_phone = args
    contacts[name] = new_phone
    return "Contact updated."

def show_phone(args, contacts):
    if not args or args[0] not in contacts:
        return "Contact not found."
    return contacts[args[0]]

def show_all(contacts):
    return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)exit

        if command in ["close", "exit", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
