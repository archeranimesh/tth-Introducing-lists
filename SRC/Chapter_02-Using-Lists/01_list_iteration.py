# List is iterable.
# for in loop can be used as List is iterable
attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_attendees = ["Ben J.", "Dave"]

potential_attendees = attendees + optional_attendees
print("There are", len(potential_attendees), "attendees currently")

print(attendees)

# for in loop for list
for attendee in attendees:
    print(attendee)


# the local variable attendee is still avaible.
print(attendee)

# in key word
print("Ken" in attendees)
