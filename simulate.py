from hand import Hand
from deck import Deck
amounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
poker_hands = [
    "High Card",        # 1
    "One Pair",         # 2
    "Two Pair",         # 3
    "Three of a Kind",  # 4
    "Straight",         # 5
    "Flush",            # 6
    "Full House",       # 7
    "Four of a Kind",   # 8
    "Straight Flush",   # 9
    "Royal Flush"       # 10
]

def simulate(sample_size):
    for _ in range(sample_size):
        h = Hand()
        return_value = h.draw(Deck())
        amounts[return_value-1] += 1
    return amounts

sample_size = 10000 # Change accordingly

amounts = simulate(sample_size)
print(amounts)


# ********
# PLOTTING
# ********

import matplotlib.pylab as plt

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(poker_hands, amounts, color= "blue")

ax.set_xlabel('Possible Hands')
ax.set_ylabel(f'Amount in {sample_size}')
ax.set_title("Simulating Poker Hands")
ax.set_xticks(range(len(poker_hands)))
ax.set_xticklabels(poker_hands, rotation=45)

fig.subplots_adjust(
    left=0.08,
    right=0.95, 
    top=0.93,
    bottom=0.25
)

plt.show()



