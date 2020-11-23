shopping_list = []


def show_list():
    """
    prints the list
    """
    print("Here's your list:")
    for item in shopping_list:
        print(item)


def add_to_list(item):
    """
    adds an item to the list
    """
    shopping_list.append(item)
    print("{} is added, and List has {} items".format(item, len(shopping_list)))


def show_help():
    """
    print help
    """
    print("What should we pick up at the store?")
    print(
        """ 
    Enter 'DONE' to stop adding items.
    Enter 'SHOW' to show the list.
    Enter 'HELP' for this help.
    """
    )


show_help()


while True:
    new_item = input("> ")

    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    add_to_list(new_item)

show_list()
