
#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random

p1_list = []
p2_list = []
p1_wins = 0
p2_wins = 0
ties = 0

for x in range(0,10):
    p1_list.append(random.randint(1,50))  
    p2_list.append(random.randint(1,50))

for y in range(len(p1_list)):
  if p1_list[y] > p2_list[y]:
    p1_wins += 1
  if p1_list[y] < p2_list[y]:
    p2_wins += 1
  else:
    ties += 1


print(f'Player 1 Random List: {p1_list}')
print(f'Player 2 Random List: {p2_list}')
print(f'Player 1 has won {p1_wins} times')
print(f'Player 2 has won {p2_wins} times')
print(f'Player 1 highest number is {max(p1_list)} at index {p1_list.index(max(p1_list))}')
print(f'Player 2 highest number is {max(p2_list)} at index {p2_list.index(max(p2_list))}')
print(f'Player 1 lowest number is {min(p1_list)} at index {p1_list.index(min(p1_list))}')
print(f'Player 2 lowest number is {min(p2_list)} at index {p2_list.index(min(p2_list))}')