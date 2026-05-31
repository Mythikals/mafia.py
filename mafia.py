import random

# Step 1: Get players
def setup_game():
   try:
    num_players = int(input("How many players? (3-10): "))
except ValueError:
    print("Please enter a number!")
    return None
    
    if num_players < 3 or num_players > 10:
        print("Need 3-10 players!")
        return None
    
    players = []
    for i in range(num_players):
        name = input(f"Player {i+1} name: ")
        players.append({
            "name": name,
            "role": None,
            "alive": True
        })
    
    return players

# Step 2: Assign random roles
def assign_roles(players):
    num_players = len(players)
    num_mafia = max(1, num_players // 3)  # 1 mafia per 3 players
    
    roles = ["Mafia"] * num_mafia + ["Villager"] * (num_players - num_mafia)
    random.shuffle(roles)
    
    for i, player in enumerate(players):
        player["role"] = roles[i]
    
    return players

# Step 3: Show everyone their secret role
def reveal_roles(players):
    def day_phase(players):
    print("\n=== DAY PHASE ===")

    alive_players = [p for p in players if p["alive"]]

    print("\nAlive players:")
    for player in alive_players:
        print("-", player["name"])

    vote = input("\nWho should be eliminated? ")

    for player in players:
        if player["name"].lower() == vote.lower() and player["alive"]:
            player["alive"] = False
            print(f"{player['name']} has been eliminated!")
            return

    print("Player not found!")
    def check_winner(players):
    mafia = 0
    villagers = 0

    for player in players:
        if player["alive"]:
            if player["role"] == "Mafia":
                mafia += 1
            else:
                villagers += 1

    if mafia == 0:
        print("\nVillagers win!")
        return True

    if mafia >= villagers:
        print("\nMafia wins!")
        return True

    return False
    for player in players:
        input(f"{player['name']}, press Enter to see your role...")
        print(f"You are: {player['role']}")
        print("\n" * 50)  # Clear screen effect

# Step 4: Run the game
def main():
   def main():
    print("=== MAFIA GAME ===\n")

    players = setup_game()

    if players is None:
        return

    players = assign_roles(players)

    reveal_roles(players)

    while True:
        day_phase(players)

        if check_winner(players):
            break
