books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

print("Suggested gift: {}".format(books[0]))
# del deletes the label from the object.
craigs_lunch = "\N{TACO}"
print(craigs_lunch)
carne_asada = craigs_lunch
print(carne_asada)
del craigs_lunch
# print(craigs_lunch) # NameError
print(carne_asada)

recommendation = books[0]
del books[0]
# the value of book[0] will not be garbage collected as it still has a reference in recommendation.
print("Suggested gift: {}".format(books[0]))
# LIFO, pop()
last_book = books.pop()
print(last_book)
print(books)

# specific index
print(books.pop(0))
