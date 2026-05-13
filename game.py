import time

def validateInt(prompt, low, high):
    while True:
        try:
            val = int(input(prompt))
            if low <= val <= high:
                return val
            print(f"Enter number between {low} and {high}")
        except ValueError:
            print("Enter a valid number")

def validateYesNo(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ["yes", "no"]:
            return ans
        print("Enter yes or no")

def showSticks(count):
    print(f"Sticks left ({count}): {'|' * count}")

def computerMove(sticks):
    print("🤖 Computer's turn...")
    time.sleep(1)
    
    if sticks % 4 == 0:
        take = 1
    else:
        take = sticks % 4
    
    print(f"Computer takes {take} stick(s)")
    return sticks - take

def playerMove(sticks):
    take = validateInt("Your turn (1-3): ", 1, 3)
    while take > sticks:
        print(f"Only {sticks} sticks left")
        take = validateInt("Pick again (1-3): ", 1, 3)
    return sticks - take

def play():
    print("=== STICK GAME ===")
    print("Players take turns picking 1-3 sticks.")
    print("The player who takes the last stick WINS.\n")
    
    sticks = validateInt("Number of sticks: ", 1, 100)
    showSticks(sticks)
    
    first = validateYesNo("Go first? (yes/no): ")
    
    turn = "player" if first == "yes" else "computer"
    
    while sticks > 0:
        print()
        if turn == "player":
            sticks = playerMove(sticks)
            turn = "computer"
        else:
            sticks = computerMove(sticks)
            turn = "player"
        showSticks(sticks)
    
    winner = "You" if turn == "computer" else "Computer"
    print(f"\n{winner} win!")

if __name__ == "__main__":
    play()
