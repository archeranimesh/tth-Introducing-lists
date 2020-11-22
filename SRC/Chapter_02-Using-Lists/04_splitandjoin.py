import time

quote = "The greatest teacher failure is"
words = quote.split()  # default seperator is space
for word in words:
    print(word)
    time.sleep(0.5)  # sleep for 0.5 sec.

attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_attendees = ["Ben J.", "Dave"]

potential_attendees = attendees + optional_attendees
print("There are", len(potential_attendees), "attendees currently")

to_line = ", ".join(attendees)  # ", "is a seperator
cc_line = ", ".join(optional_attendees)  # string
print("To: ", to_line)
print("Cc: ", cc_line)

print(to_line.split(", "))  # Split with a seperator.
