def required_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def positive_integer(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
            if number > 0:
                return number
        except ValueError:
            pass
        print("Please enter a positive whole number.")


def find_by_id(data, item_id):
    for item in data:
        if item["id"] == item_id:
            return item
    return None


def read_id(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid numeric ID.")
