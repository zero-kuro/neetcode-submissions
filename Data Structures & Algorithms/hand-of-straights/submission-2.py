class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        store = {}
        for i in hand:
            store[i] = store.get(i,0) + 1
        while store:
            start = min(store)

            for j in range(groupSize):
                card = start + j

                if card not in store:
                    return False

                else:
                    store[card] -= 1
                    if store[card] == 0:
                        store.pop(card)
        return True
