# # Write your return_cost function here:
def return_cost(menu, item):
  if item in menu:
    return menu[item]
  return 0 
# # Write your fanciest_flavor function here:
def fanciest_flavor(menu):
  highest_cost = 0
  fanciest = ''
  for (flavor, price) in menu.items ():
    if price > highest_cost:
      fanciest = flavor
      highest_cost = price
    return fanciest
flavors = {
  'chocolate' : 0.35,
  'vanilla' : 0.35,
  'strawberry' : 0.42,
  'cookies and cream' : 0.45,
  'mint chocolate chip' : 0.42,
  'fudge chunk' : 0.45,
  'saffron' : 2.25,
  'garlic' : 0.05
}

## Set a variable called choice to the flavor you want to search for.
choice = 'vanilla'
## Use an if statement to check if choice is in the flavors dictionary.
if choice in flavors:
    cost = flavors[choice]
else:
    cost = 0
print("The cost of", choice, "is", cost)
## If it is, set another variable called cost to the value associated with choice.

## If it isn’t, set cost to 0.

# Uncomment the lines below after you code your fanciest_flavor function.
print('---')
expensive_flavor = fanciest_flavor(flavors)
print(f"The most expensive flavor we have is {expensive_flavor}.")
## Print the cost.

### Search a Dictionary Part 2:

## Initialize two variables: highest_cost to 0 and fanciest to an empty string.
highest_cost = 0 
fanciest = ''
## Loop through the flavors dictionary using a for loop.
for flavor in flavors:
   if flavors[flavor] > highest_cost:
    fanciest = flavor
    highest_cost = flavors[flavor]
## For each flavor, check if its price is higher than highest_cost.

## If it is, update fanciest to this flavor and highest_cost to its price.

## After the loop, print the most expensive flavor.