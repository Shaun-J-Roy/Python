import random

inventory = [("Torch", "Tool"), ("Map", "Navigation"), ("Rope", "Tool")]
loot_items = (("Gold Coin", "Currency"), ("Magic Scroll", "Magic"))

# Tuple of classes: (name, health, attack)
character_classes = (
    ("Warrior", 100, 20),
    ("Mage", 70, 15),
    ("Rogue", 80, 12),
    ("Hybrid", 90, 18)
)

quests = (
    "Enter the Dark Forest",
    "Defeat the Goblin",
    "Find the Hidden Relic"
)

def create_character():
    print("Welcome, brave adventurer! What is your name?")
    name = input(">> ")
    print(f"\n{name}, choose your class:")

    for i, char_class in enumerate(character_classes, 1):
        print(f"{i}. {char_class[0]}")

    while True:
        choice = input("Enter the number of your class: ")
        if choice.isdigit() and 1 <= int(choice) <= len(character_classes):
            selected = character_classes[int(choice) - 1]
            return {"name": name, "class": selected[0], "health": selected[1], "attack": selected[2]}
        else:
            print("Invalid choice. Try again.")

def show_inventory():
    global inventory
    print("\nInventory (all items):", [item[0] for item in inventory])
    print("Recently Collected Items:", [item[0] for item in inventory[-2:]])

def show_quests():
    print("\nActive Quests:")
    for quest in quests:
        print("-", quest)
    print("Total Quests:", len(quests))

def encounter(player):
    print("\nYou enter a dark forest and hear something growling...")
    enemy = {"name": "Goblin", "health": 30, "attack": 5}

    while enemy["health"] > 0 and player["health"] > 0:
        print("\nWhat will you do?")
        actions = ["1. Attack", "2. Defend", "3. Run"]
        for act in actions:
            print(act)

        action = input(">> ")

        if action == "1":
            damage = player["attack"] + random.randint(-2, 2)
            enemy["health"] -= damage
            print(f"You hit the {enemy['name']} for {damage} damage!")
        elif action == "2":
            block = random.randint(2, 6)
            print(f"You brace yourself and block {block} damage.")
        elif action == "3":
            print("You try to run...")
            if random.random() > 0.5:
                print("You escaped!")
                return
            else:
                print("You failed to escape!")
        else:
            print("Invalid choice.")
            continue

        if enemy["health"] > 0:
            enemy_damage = enemy["attack"] + random.randint(-1, 3)
            if action == "2":
                enemy_damage -= block
                enemy_damage = max(enemy_damage, 0)
            player["health"] -= enemy_damage
            print(f"The {enemy['name']} hits you for {enemy_damage} damage!")

    if player["health"] > 0:
        print("\nYou defeated the goblin!")
        print("You loot some items...")
        global inventory
        inventory.extend(loot_items)
        show_inventory()
    else:
        print("\nYou have fallen in battle...")

def game_loop():
    player = create_character()
    print(f"\nWelcome {player['name']} the {player['class']}! Your adventure begins now...\n")

    show_inventory()
    show_quests()

    for i in range(3):  
        print(f"\n-- Encounter {i + 1} --")
        encounter(player)
        if player["health"] <= 0:
            print("Game Over.")
            break
        else:
            print(f"You have {player['health']} HP left.")
            print("Do you want to rest and recover 10 HP? (yes/no)")
            if input(">> ").lower() == "yes":
                player["health"] += 10
                print("You feel refreshed.")

    if player["health"] > 0:
        print(f"\nCongratulations, {player['name']}! You survived your journey.")
    else:
        print("\nBetter luck next time!")

game_loop()
