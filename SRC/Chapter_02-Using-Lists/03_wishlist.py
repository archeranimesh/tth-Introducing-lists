video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]
books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

print("Suggested gift: {}".format(books[0]))

print("Books:")
for book in books:
    print("* " + book)


def display_wishlist(display_name, wishes):
    # copy the original list coming in.
    items = wishes.copy()
    """
    displays a wishlist as per the param passed.
    """
    print(display_name + " :")
    suggested_gift = items.pop(0)
    print("=======>", suggested_gift, "<==========")
    for wish in items:
        print("* " + wish)
    print()


display_wishlist("Books", books)
display_wishlist("Video Games", video_games)
display_wishlist("Video Games", video_games)
display_wishlist("Video Games", video_games)
print(video_games)
# display_wishlist("Video Games", video_games)

# list and for loops
inventory = ["shield", "apple", "sword", "bow", "boomerang"]
# remove an element by value.
inventory.remove("apple")
print(inventory)
for item in inventory:
    print(inventory, "item", item)
    inventory.remove(item)
