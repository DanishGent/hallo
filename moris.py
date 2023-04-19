def sleep():
    status["sleepiness"] -= 10

def mine():
    status["sleepiness"] += 5
    status["thirst"] += 5
    status["hunger"] += 5
    status["whisky"] += 0
    status["gold"] += 5

def drink():
    status["sleepiness"] += 5
    status["thirst"] -= 6
    status["hunger"] -= 6
    status["whisky"] += 0
    status["gold"] -= 2

def dead():
    return status["sleepiness"] > 100 or status["thirst"] > 100 or status["hunger"] > 100


status = {"turn": 0, "sleepiness": 0, "thirst": 0, "hunger": 0, "whisky": 0, "gold": 0}  # dictionary

while not dead() and status["turn"] < 1000:
    status["turn"] += 1
    sleep()
    mine()
    drink()
    sleep()
    print(status)