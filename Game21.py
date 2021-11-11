import random

cmd = input('Please press s to start: ')
while cmd != 's':
  cmd = input('Please press s to start: ')

print('')
print('Here are your initial cards:')

numberList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suiteList = ['Diamond', 'Heart', 'Spade', 'Club']

card1 = random.choice(suiteList) + ' ' + random.choice(numberList)
print(card1)
card2 = random.choice(suiteList) + ' ' + random.choice(numberList)
while card2 == card1:
  card2 = random.choice(suiteList) + ' ' + random.choice(numberList)
print(card2)

print('')

cmd = input('Press c to continue, press s to stop: ')
while cmd != 's' and cmd != 'c':
  cmd = input('Press c to continue, press s to stop: ')

print('')

if cmd == 'c':
  card3 = random.choice(suiteList) + ' ' + random.choice(numberList)
  while card3 == card1 or card3 == card2:
    card3 = random.choice(suiteList) + ' ' + random.choice(numberList)
  print('Your new card is ' + card3)
  // Now we need to calculate the total score...how???