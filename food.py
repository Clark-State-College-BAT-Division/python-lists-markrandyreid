"""
Create a list
Prompt the user to enter five foods, and store the responses in the list
Display the list on one line, each item seperated by commas
Calculate how many characters were entered and display this to the user

Hint: Using the len() function will be useful here

You must use a list for this assignment. Not using a list will result in an automatic 0.

Below is a sample of what your output might look like. You do not have to follow the text exactly.

Enter a food: pizza
Enter a food: beef jerkey
Enter a food: rice triangles
Enter a food: steamed chinese bun
Enter a food: fried chicken
"""

food_list = []
food_sum = 0

while len(food_list) < 5:
  y = input('Provide a Food Item: ')
  food_list.append(y)
  food_sum += len(y)

print(f'Food List:\n{food_list}\n')
print(f'Character Sum: {food_sum}')
