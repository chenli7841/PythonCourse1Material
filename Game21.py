import random

cmd = input('Please press s to start: ')
while cmd != 's':
  cmd = input('Please press s to start: ')

print('')
print('Here are your initial cards:')

numberList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suiteList = ['Diamond', 'Heart', 'Spade', 'Club']
faceNumberToActualNumberMap = {
  'A': 1,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  '10': 10,
  'J': 10,
  'Q': 10,
  'K': 10
}

card1 = {
  'suite': random.choice(suiteList), 
  'faceNumber': random.choice(numberList)
}
card1['actualNumber'] = faceNumberToActualNumberMap[card1['faceNumber']]

print(card1['suite'] + ' ' + card1['faceNumber'])

card2 = {
  'suite': random.choice(suiteList), 
  'faceNumber': random.choice(numberList)
}
card2['actualNumber'] = faceNumberToActualNumberMap[card2['faceNumber']]

while (card2['suite'] + card2['faceNumber']) == (card1['suite'] + card1['faceNumber']):
  card2 = {
    'suite': random.choice(suiteList), 
    'faceNumber': random.choice(numberList)
  }
  card2['actualNumber'] = faceNumberToActualNumberMap[card2['faceNumber']]
print(card2['suite'] + ' ' + card2['faceNumber'])

print('')

totalScoreYou = card1['actualNumber']+card2['actualNumber']
print('Your total score is ' + str(totalScoreYou))

print('')

cmd = input('Press c to continue, press s to stop: ')
while cmd != 's' and cmd != 'c':
  cmd = input('Press c to continue, press s to stop: ')

print('')

if cmd == 'c':
  card3 = {
    'suite': random.choice(suiteList), 
    'faceNumber': random.choice(numberList)
  }
  card3['actualNumber'] = faceNumberToActualNumberMap[card3['faceNumber']]
  while (card3['suite']+card3['faceNumber']) == (card1['suite']+card1['faceNumber']) or (card3['suite']+card3['faceNumber']) == (card2['suite']+card2['faceNumber']):
    card3 = {
      'suite': random.choice(suiteList), 
      'faceNumber': random.choice(numberList)
    }
    card3['actualNumber'] = faceNumberToActualNumberMap[card3['faceNumber']]
  print('Your new card is ' + card3['suite'] + ' ' + card3['faceNumber'])

  print('')

  totalScoreYou = card1['actualNumber']+card2['actualNumber']+card3['actualNumber']
  if (totalScoreYou > 21):
    print('Sorry, your total score ' + str(totalScoreYou) + ' exceeds 21. You lost :(')
  else:
    print('Your total score is ' + str(totalScoreYou))

elif cmd == 's':
  print("You stopped. Player X's cards are:")
  print('')
  card1x = {
    'suite': random.choice(suiteList), 
    'faceNumber': random.choice(numberList)
  }
  card1x['actualNumber'] = faceNumberToActualNumberMap[card1x['faceNumber']]
  card2x = {
    'suite': random.choice(suiteList), 
    'faceNumber': random.choice(numberList)
  }
  card2x['actualNumber'] = faceNumberToActualNumberMap[card2x['faceNumber']]
  card3x = {
    'suite': random.choice(suiteList), 
    'faceNumber': random.choice(numberList)
  }
  print(card1x['suite']+ ' ' + card1x['faceNumber'] + ', ' + card2x['suite'] + ' ' + card2x['faceNumber'] + ', ' + card3x['suite'] + ' ' + card3x['faceNumber'])
  print('')
  card3x['actualNumber'] = faceNumberToActualNumberMap[card3x['faceNumber']]
  totalScoreX = card1x['actualNumber']+card2x['actualNumber']+card3x['actualNumber']
  print("Player X's score is: " + str(totalScoreX))
  
  # decide who wins
  if totalScoreYou > 21 and totalScoreX > 21:
    print("You both exceed 21. It's a tie. Wanna play again?")
  elif totalScoreYou < 21 and totalScoreX > 21:
    print("Congratulations, Player X has drawn too many cards and lost.")
  elif totalScoreYou > 21 and totalScoreX > 21:
    print("Too bad, you have drawn too many cards. Be careful next time!")
  else:
    if totalScoreYou < totalScoreX:
      print("Your score is too low. Please take some risk and draw more cards next time!")
    elif totalScoreYou > totalScoreX:
      print("Good job! Your score beats Player X.")
    else:
      print("What a coincidence! You both have the same score. It's a tie. Wanna play again?")


  # Now we need to calculate the total score...how???