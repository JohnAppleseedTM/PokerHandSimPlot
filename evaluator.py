# High card
# Pair
# Two pair
# Three of a kind
# Straight
# Flush
# Full house
# Four of a kind
# Straight flush
# Royal flush

def evaluate(players_hand, table):
      cards = players_hand + table
      suits = []
      ranks = []
      for card in cards:
           suits.append(card.suit)
           ranks.append(card.rank)

      if detect_10(cards, suits, ranks):
            print("A ROYAL FLUSH!!!!")
            return 10
      elif detect_9(cards, suits, ranks):
            print("A straight flush!!!")
            return 9
      elif detect_8(cards, ranks):
            print("A four of a kind!!")
            return 8
      elif detect_7(cards, ranks):
            print("A Full House!")
            return 7
      elif detect_6(cards, suits):
            print("A flush")
            return 6
      elif detect_5(cards, ranks):
            print("A staright")
            return 5
      elif detect_4(cards, ranks):
            print("A Three of a kind")
            return 4
      elif detect_3(cards, ranks):
            print("A two pair")
            return 3
      elif detect_2(cards, ranks):
            print("A pair")
            return 2
      else:
            print(f"High card: {max(ranks)}")
            return 1

def detect_10(cards, suits, ranks): #IS ROYAL FLUSH
      suit_ranks = {}

      for i in range(len(ranks)):
            suit = suits[i]
            rank = ranks[i]

            if suit not in suit_ranks:
                  suit_ranks[suit] = []

            suit_ranks[suit].append(rank)

      # 2. Check straight inside each suit
      for suit in suit_ranks:
            suited = suit_ranks[suit]

            if len(suited) < 5:
                  continue

            unique = sorted(set(suited), reverse=True)

            if not (14 in unique and 13 in unique and 12 in unique and 11 in unique and 10 in unique):
                  continue

            return True

      return False

def detect_9(cards, suits, ranks): #IS STRAIGHT FLUSH
    # 1. Collect ranks per suit
    suit_ranks = {}

    for i in range(len(ranks)):
        suit = suits[i]
        rank = ranks[i]

        if suit not in suit_ranks:
            suit_ranks[suit] = []

        suit_ranks[suit].append(rank)

    # 2. Check straight inside each suit
    for suit in suit_ranks:
        suited = suit_ranks[suit]

        if len(suited) < 5:
            continue

        unique = sorted(set(suited), reverse=True)

        # Ace-low straight (A,5,4,3,2)
        if 14 in unique:
            unique.append(1)

        for i in range(len(unique) - 4):
            if all(unique[i+j] == unique[i] - j for j in range(5)):
                return True

    return False

def detect_8(cards, ranks): #IS FOUR OF A KIND
      for rank in ranks:
            if ranks.count(rank) >= 4:
                  return True
      return False

def detect_7(cards, ranks): #IS FULL HOUSE
      if len(ranks) < 5: return False
      sorted_ranks = sorted(ranks, reverse=True)
      # print(sorted_ranks)
      counts = [sorted_ranks.count(x) for x in set(sorted_ranks)]
      options = [[2,3], [3,2], [3,3]]
      return any(counts[i:i+2] == option for option in options for i in range(len(counts)-1)) 

def detect_6(cards, suits): #IS FLUSH
      for suit in suits:
            if suits.count(suit) >= 5:
                  return True
      return False

def detect_5(cards, ranks): #IS STRAIGHT
      sorted_ranks = sorted(set(ranks), reverse=True)
      if 14 in sorted_ranks:
            sorted_ranks.append(1)

      for i in range(len(sorted_ranks) - 4):
            if all(sorted_ranks[i+j] == sorted_ranks[i] - j for j in range(5)):
                   return True
      return False

def detect_4(cards, ranks): #IS THREE OF A KIND
      for rank in ranks:
            if ranks.count(rank) >= 3:
                  return True
      return False

def detect_3(cards, ranks): #IS TWO PAIR
      if len(ranks) < 4: return False
      sorted_ranks = sorted(ranks, reverse=True)
      counts = [sorted_ranks.count(x) for x in set(sorted_ranks)]
      option = [2,2]
      return any(counts[i:i+2] == option for i in range(len(counts)-1)) 

def detect_2(cards, ranks): #IS PAIR
      for rank in ranks:
            if ranks.count(rank) >= 2:
                  return True
      return False
