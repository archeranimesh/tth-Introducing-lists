# Accessing a specific element is
# zero based.

books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

print(books[0])
books[1] = "Python for Data Analysis - Wes McKinney"
print(books)
print(books[-1])
print(books[len(books) - 1])
books.insert(0, "Learning Python: Powerful object oriented Prog - Mark Lutz")
print(books)
print(books[-len(books)])
