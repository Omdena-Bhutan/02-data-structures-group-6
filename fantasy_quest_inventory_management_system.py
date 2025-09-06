# Create dictionary with character details
character_profile = {
    'name': "Alistair the Brave",
    'level': 1,
    'health': 100,
    'mana': 50,
    'gold': 50.75,
    'is_alive': True
}

# Print character's name and level
print(f"Character: {character_profile['name']} | Level: {character_profile['level']}")

# Update health
character_profile['health'] = 85

# Add experience key
character_profile['experience'] = 0

# Print updated character profile
print("Final Character Profile:", character_profile)
print("-" * 50)

# Part 2: Inventory System (Using Lists)

# Create inventory list
inventory = ['sword', 'shield', 'health potion']

# Add a new item
inventory.append('mana potion')

# Remove an item
inventory.remove('shield')

# Print all inventory items
print("Inventory Items:")
for item in inventory:
    print("-", item)

# Part 3: Character Stats (Using Tuples)

# Tuples for base stats (immutable)
base_stats = (10, 8, 12)  # (strength, dexterity, intelligence)

# Why tuple?
print("Tuples are used for base stats because they are immutable and cannot be changed accidentally.")

# Access intelligence value
print("Intelligence:", base_stats[2])

# Challenge: Try to change a tuple value (will raise an error if uncommented)
# base_stats[0] = 15  # Uncomment this line to see TypeError

# Part 4: Quest Log (Using Sets)

# Create set of quests
quest_log = {'Defeat the Goblin King', 'Find the Lost Amulet'}

# Add a new quest
quest_log.add('Deliver the Old Scroll')

# Add a duplicate quest (set ignores duplicates)
quest_log.add('Defeat the Goblin King')

# Remove completed quest
quest_log.remove('Find the Lost Amulet')

# Print final quest log
print("Quest Log:", quest_log)
print("-" * 50)

# Part 5: Putting it all together

# Combine everything into one dictionary
character_sheet = {
    'profile': character_profile,
    'inventory': inventory,
    'stats': base_stats,
    'quests': quest_log
}

# Print full character sheet
print("Complete Character Sheet:")
print(character_sheet)