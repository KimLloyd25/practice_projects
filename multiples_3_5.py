### THIS PRACTICE PROJECT FINDS AND LISTS ALL MULTIPLES OF 3 AND 5, UP TO AND INCLUDING 1000
### IT ALSO REMOVES ANY DUPLICATE VALUES BY CONVERTING THE LIST TO A SET

#Define function
def find_multiples(multiplier):
  #Define counter variable, i
  i = 1;
  #Sets empty list variable
  multiples = []
  #While counter is less than 1000
  while i <= 1000:
    #Check if counter divides cleanly by multiplier
    if i % multiplier == 0:
      #Add to list
      multiples.append(i)
      #Increase counter
      i = i + 1
    else:
      #Increase counter
      i = i + 1
      continue
  #Return list
  return multiples

#Assign each set of multiples to lists
multiples_of_3 = find_multiples(3)
multiples_of_5 = find_multiples(5)

#Merge lists
multiples = multiples_of_3 + multiples_of_5
#Sort in ascending order
multiples.sort()
#Print list and change to set to eliminate duplicates
print(set(multiples))
