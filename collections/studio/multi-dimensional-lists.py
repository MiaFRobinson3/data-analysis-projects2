food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_list = food.split(',')
print(food_list)
print('You need to buy:')
for item in food_list:     
    print('\t' + item) 
food_list.sort()
print(food_list)
equipment_list = equipment.split(',')
equipment_list.sort()
print(equipment_list)
pets_list = pets.split(',')
pets_list.sort()
print(pets_list)
sleep_aids_list = sleep_aids.split(',')
sleep_aids_list.sort()
print(sleep_aids_list)

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [['chocolate', 'meal packs', 'snacks', 'water bottles'],
['jet packs', 'space suits', 'thermal detonators', 'tool belts'],
['alien eggs', 'cats', 'moose', 'parrots'],
['alarm clocks', 'blankets', 'eyepatches', 'pillows']]
print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
user_input = input("Select a cabinet in the cargo hold (0-3):")
cabinet_index=int(user_input)
if 0 <= cabinet_index < len(cargo_hold):
    print(cargo_hold[cabinet_index])
else:
    print("Invalid Selection")

# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.



# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
user_input = input("Select a cabinet in the cargo hold (0-3):")
cabinet_index=int(user_input)
if 0 <= cabinet_index < len(cargo_hold):
    print(f"The contents of cabinet", {cabinet_index}, "are", {cargo_hold[cabinet_index]})
else:
    print("Invalid Selection")