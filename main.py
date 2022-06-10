from newflight import *
# Create a file for all of the state letters and pull from file to list.
destinations = ["CA", "FL", "NV", "TX", "NY", "MA"]
years = ["2019", "2020"]
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
#create a list of the different seats that show on each flight
firstClass = [["Open", "Open"], ["Open", "Open"], ["Open", "Open"], ["Open", "Open"]]
coach = [["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"]]
firstCl = tableOne(firstClass)
co = tableTwo(coach)
#subscript set to zero and answer set to N at beginning of each determination for destination, year, month, and day chosen
sub = 0
answer = "N"
destination = input("Destination? (i.e. CA, FL, TX, etc.) ")
while True:
  while sub < 6:
    if destination == destinations[sub]:
        answer = "Y"
    sub += 1
  if answer == "Y":
    break
  else:
    destination = input("Destination? (i.e. CA, FL, TX, etc.) ")
  sub = 0
year = input("Year? ")
sub = 0
answer = "N"
while True:
  while sub < 2:
    if year == years[sub]:
        answer = "Y"
    sub += 1
  if answer == "Y":
    break
  else:
    year = input("Year? ")
  sub = 0
month = input("Month? (i.e. 01, 02, 03, etc.) ")
sub = 0
answer = "N"
while True:
  while sub < 12:
    if month == months[sub]:
        answer = "Y"
    sub += 1
  if answer == "Y":
    break
  else:
    month = input("Month? (i.e. 01, 02, 03, etc.) ")
  sub = 0
day = input("Day? ")
fileName = (destination + ": " + str(month) + " " + str(day) + " " + str(year))
print(fileName)
# type in a example file, either a new one or one shown on the left pane
import os
# if statement will work on existing files from the left pane and move on to traveler info
if os.path.exists(fileName):
  print("Flight Exists")
else:
  print("New flight created.")
  f = open(fileName, "w")
  f.write("   First Class\n" + firstCl + "\n")
  f.write("   Coach\n" + co)
  f.close()

#there is no indefinite loop in place at this time
people = int(input("How many people? "))
i = 1
while i <= people:
  name = input("What is your name? ")
  classType = input("Which class would you like to sit in? First Class [FC] or Coach [C]? ")
  i += 1
  if classType == "FC":
    #this will print the seats from the chosen flight file
    f = open(fileName, "r")
    firstCl1 = f.readlines()
    f.close()
    for x in range (0,6):
      print(firstCl1[x])
    while True:
      row = int(input("Which row will you choose? "))
      seat = int(input("Which seat in that row will you choose? "))
      if firstClass[row][seat] == "Open":
        firstClass[row][seat] = name
        print(" Seat granted.\n")
        #it will overwrite in the function destined for the flight file
        firstCl = tableOne(firstClass)
        f = open(fileName, "w")
        f.write("   First Class\n" + firstCl + "\n")
        f.write("   Coach\n" + co)
        f.close()
        break
      elif firstClass[row][seat] != "Open":
        print(" Please choose another seat.\n")
      else:
        print("Invalid selection.\n")
  if classType == "C":
    f = open(fileName, "r")
    co1 = f.readlines()
    f.close()
    for x in range (7,19):
      print(co1[x])
    while True:
      row = int(input("Which row will you choose? "))
      seat = int(input("Which seat in that row will you choose? "))
      if coach[row][seat] == "Open":
        coach[row][seat] = name
        print(" Seat granted.\n")
        co = tableTwo(coach)
        f = open(fileName, "w")
        f.write("   First Class\n" + firstCl + "\n")
        f.write("   Coach\n" + co)
        f.close()
        break
      elif coach[row][seat] != "Open":
        print(" Please choose another seat.\n")
      else:
        print("Invalid selection.\n")

print(tableOne(firstClass))
print(tableTwo(coach))