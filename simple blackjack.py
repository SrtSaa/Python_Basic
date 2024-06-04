import random


dealer_card=[]
player_card=[]

# giving two cards to dealer as well as winner
while len(dealer_card)<2:
    dealer_card.append(random.randint(2,11))
    player_card.append(random.randint(2,11))

# showing one card of dealer and two cards of player
print(dealer_card)
print('Dealer card: x &',dealer_card[random.randint(0,1)])
print('You have: ',end='')
print(*player_card,sep=', ')

# giving option to user to choose stay or hit
while sum(player_card)<21:
    choice=input('\nstay or hit: ')
    if choice=='h':
        player_card.append(random.randint(2,11))
        print('You have: ',end='')
        print(*player_card,sep=', ')
    else:
        break

# for deciding the winner showing the cards of dealer
# dealer will take card until the sum of dealer cards is greater or equal to 17
print('\nDealer has: ',end='')
print(*dealer_card,sep=', ')
while sum(dealer_card)<=16:
    dealer_card.append(random.randint(2,11))
    print('\nDealer has: ',end='')
    print(*dealer_card,sep=', ')

print("\n")
# checking for winner:
if sum(player_card)>21:
    print('Player has BUSTED!!! Dealer wins...')
elif sum(dealer_card)>21:
    print('Dealer has BUSTED!!! Player wins...')
elif sum(dealer_card)==21 and sum(player_card)==21:
    print('Both have BLACKJACK!!! Tie....')
elif sum(player_card)==21:
    print('Player has BLACKJACK!!! Player wins...')
elif sum(dealer_card)==21:
    print('Dealer has BLACKJACK!!! Dealer wins...')
elif sum(player_card)>sum(dealer_card):
    print('Player wins...')
elif sum(player_card)<sum(dealer_card):
    print('Dealer wins...')
else:
    print('Tie...')
