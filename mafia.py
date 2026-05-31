import random

# Step 1: Get players
def setup_game():
    num_players = int(input("How many players? (3-10): "))
    
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
    for player in players:
        input(f"{player['name']}, press Enter to see your role...")
        print(f"You are: {player['role']}")
        print("\n" * 3)  # Clear screen effect

# Step 4: Run the game
def main():
    print("=== MAFIA GAME ===\n")
    
    players = setup_game()
    if players is None:
        return
    
    players = assign_roles(players)
    reveal_roles(players)
    
    print("Game starting...")
    print(f"Roles assigned: {sum(1 for p in players if p['role'] == 'Mafia')} Mafia, {sum(1 for p in players if p['role'] == 'Villager')} Villagers")

if __name__ == "__main__":
    main()