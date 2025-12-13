"""
Prompt the user to enter 5 numbers. Store them in a list.
Display the list as entered, small to large, and large to small
Calculate and display the mean and median
This is a guided practice. You can follow the video or your instructor will go
over this in class
"""

user_numbers = []

while len(user_numbers) < 5:
  y = int(input('Enter a number: '))
  user_numbers.append(y)

print(f'You entered:{user_numbers}')


#copy list
#sort method sorts in place, so you have to sort then assign
gamma = user_numbers.copy()
gamma.sort(reverse=True)

theta = user_numbers.copy()
theta.sort(reverse=False)

#Small to Large
print(f'Sorted Largest to Smallest: {gamma}')

#Larger to Small
print(f'Sorted Smallest to Largest: {theta}')

#mean
print(f'Mean: {sum(user_numbers)/len(user_numbers)}')

#median
#we can just select the middle number in the small to large sort
print(f'Median: {theta[2]}')