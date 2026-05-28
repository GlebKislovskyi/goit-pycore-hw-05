def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError:
            return "Введіть ім'я та номер телефону."

        except KeyError:
            return "Контакт не знайдено."

        except IndexError:
            return "Введіть аргумент для команди."

    return inner


@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Контакт додано."


@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    name, phone = args[0], args[1]

    if name not in contacts:
        raise KeyError

    contacts[name] = phone
    return "Контакт оновлено."


@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        raise IndexError
    name = args[0]

    if name not in contacts:
        raise KeyError

    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "Контакти відсутні."

    result = ""

    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return result.strip()


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower()

    return cmd, args


def main():
    contacts = {}

    print("Вітаю! Я бот-помічник.")

    while True:
        user_input = input("Введіть команду: ")

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break

        elif command == "hello":
            print("Чим можу допомогти?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Невідома команда.")


if __name__ == "__main__":
    main()
