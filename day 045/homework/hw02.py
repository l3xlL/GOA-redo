def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    
    winning = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if winning[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"
