
contacts = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid input. Please try again."

    return wrapper


# Функція для виведення привітання


def hello():
    return "How can I help you?"


# Функція для додавання нового контакту
@input_error
def add_contact(input_str):
    parts = input_str.split()
    name = parts[1]
    phone = parts[2]
    contacts[name] = phone
    return f"Contact '{name}' with phone '{phone}' added successfully."


# Функція для зміни номеру телефону контакту
@input_error
def change_phone(input_str):
    parts = input_str.split()
    name = parts[1]
    phone = parts[2]
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for '{name}' updated to '{phone}'."
    else:
        return f"Contact '{name}' not found."


# Функція для отримання номеру телефону за іменем контакту
@input_error
def get_phone(input_str):
    name = input_str.split()[1]
    if name in contacts:
        return f"The phone number for '{name}' is '{contacts[name]}'."
    else:
        return f"Contact '{name}' not found."


# Функція для виведення всіх контактів


def show_all():
    if not contacts:
        return "No contacts found."
    else:
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result


# Функція завершення роботи бота


def goodbye():
    return "Good bye!"


# Головна функція взаємодії з користувачем


def main():
    while True:
        command = input("Enter a command: ").strip().lower()

        if command == "hello":
            print(hello())
        elif command.startswith("add"):
            print(add_contact(command))
        elif command.startswith("change"):
            print(change_phone(command))
        elif command.startswith("phone"):
            print(get_phone(command))
        elif command == "show all":
            print(show_all())
        elif command in ["good bye", "close", "exit"]:
            print(goodbye())
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
