#Define function
def calculate_cost(width, height, cost):
  #Calculate the total floor area of the room
  total_area = width * height
  #Calculate cost of flooring for area
  total_cost = total_area * cost
  #Return calculation
  return total_cost
#Take input from user and assign to variables width, height and price
width = input("What is the length of the room in meters?")
height = input("What is the width of the room in meters?")
price = input("What is the price of flooring per meter²?")

#Output the total cost of flooring for the room by calling the function and outputting returned value
print(f"The total cost of flooring needed for this room is £{calculate_cost(int(width), int(height), int(price))}")
