# list can store any type of data type.
temperatures = []

# add at the end.
temperatures.append(98.6)
temperatures.append(98.7)
print(temperatures)
er_temps = [102.2, 103.5]

# extends the original list.
temperatures.extend(er_temps)
print(temperatures)

# Concatenate
primary_care_doctors = ["Dr. Scholls", "Dr. Pepper"]
er_doctor = ["Doug", "Susan"]

all_doctors = primary_care_doctors + er_doctor
print(all_doctors)

hello = ["How", "are", "you"]
hello.extend("hello")
print(hello)
