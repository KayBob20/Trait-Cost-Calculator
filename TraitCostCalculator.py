trait_rarity = {
    # Horn Traits
    "Normal (Horn)": "common",
    "Thunderbolt": "common",
    "Backwards": "uncommon",
    "Up High": "uncommon",
    "Straight": "uncommon",
    "Twist": "uncommon",
    "Unicorn": "rare",
    "Tall": "rare",
    "Crossed": "rare",
    "Ibex": "rare",
    "Curled Back": "rare",

    # What’s on the Horn Traits
    "Normal (On Horn)": "common",
    "Spikey": "uncommon",
    "Cobra": "rare",
    "Large": "rare",

    # Mouth Traits
    "Normal (Mouth)": "common",
    "Canine": "uncommon",
    "Shark": "uncommon",
    "Fanged Goat": "rare",
    "Outwards": "rare",
    "Outside": "rare",
    "Small Tusks": "rare",

    # Heat Pit Traits
    "Normal (Heat Pit)": "common",
    "Circle": "uncommon",
    "Oval": "uncommon",
    "Teardrop": "uncommon",
    "Split Circle": "rare",
    "Heart": "rare",
    "Diamond": "rare",

    # Eye Traits
    "Snake": "common",
    "Goat (Eye)": "common",
    "Double": "uncommon",
    "Black": "rare",

    # Ear Traits
    "Deer": "common",
    "Goat Alt.": "common",
    "Mouse": "uncommon",
    "Rabbit": "rare",
    "Bat": "rare",

    # Feet Traits
    "Paws": "common",
    "Hooves": "common",
    "Split Hooves": "common",
    "Spiked Hooves": "uncommon",
    "Designed Hooves": "uncommon",
    "Stubs": "rare",

    # Tail Traits
    "Goat on Top": "common",
    "Snake Butt": "common",
    "Rattlesnake": "uncommon",
    "Split End": "uncommon",
    "Extra Long": "uncommon",
    "Goat (Tail)": "rare",
    "Fat": "rare",
    "Crocodile": "rare",
    "Spines": "rare",
    "Mallet": "rare",
    "Ankylosaurus": "rare",
    "Thunderbolt": "rare",
    "Curled": "rare"
}

rarity_cost = {
    "common": 1,
    "uncommon": 2,
    "rare": 3,
    "ultra rare": 4,
    "mythical": 5
}

item_options = {
    "common egg": {"covers": ["common"], "cost": 1000},
    "uncommon egg": {"covers": ["common", "uncommon"], "cost": 1800},
    "rare egg": {"covers": ["common", "uncommon", "rare"], "cost": 3000},
    "ultra rare egg": {"covers": ["common", "uncommon", "rare", "ultra rare"], "cost": 4200},
    "mythicale egg": {"covers": ["common", "uncommon", "rare", "ultra rare", "mythical"], "cost": 6000},
}

# --- Get raw user input ---
print("Paste your trait list below (press Enter twice to finish):")
input_lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    input_lines.append(line.strip())

# --- Process the pasted input ---
user_traits = {}

for line in input_lines:
    if ":" not in line:
        continue  # Skip header lines like "Traits:" or "——"

    # Normalize smart punctuation
    line = line.replace("’", "'").replace("“", "\"").replace("”", "\"")

    label, value = line.split(":", 1)
    label = label.strip().lower()
    value = value.strip()

    if not value:  # Skip blank values
        continue

    # Handle custom naming for correct rarity lookups
    if "what's on the horn" in label and value.lower() == "normal":
        value = "Normal (On Horn)"
    elif "horn trait" in label and value.lower() == "normal":
        value = "Normal (Horn)"
    elif "mouth" in label and value.lower() == "normal":
        value = "Normal (Mouth)"
    elif "heat pit" in label and value.lower() == "normal":
        value = "Normal (Heat Pit)"
    elif "eye" in label and value.lower() == "goat":
        value = "Goat (Eye)"
    elif "tail" in label and value.lower() == "goat":
        value = "Goat (Tail)"

    user_traits[label] = value


from collections import Counter

rarities = []

for trait, value in user_traits.items():
    sub_traits = value.split(" + ")  # handle multiple traits
    for t in sub_traits:
        cleaned = t.strip()
        if not cleaned:
            continue
        if cleaned not in trait_rarity:
            raise ValueError(f"Trait not found in rarity list: '{cleaned}'")
        rarity = trait_rarity[cleaned]
        print(f"[DEBUG] Trait: '{cleaned}', Rarity: {rarity}")
        rarities.append(rarity)

rarity_counts = Counter(rarities)
print("\nYour Hoofhisser has:")
for rarity in ["common", "uncommon", "rare", "ultra rare", "mythical"]:
    count = rarity_counts.get(rarity, 0)
    if count > 0:
        trait_word = "trait" if count == 1 else "traits"
        print(f"{count} {rarity} {trait_word}")

required_rarities = set(rarity_counts.keys())
cheapest = None

for item, details in item_options.items():
    if required_rarities.issubset(details["covers"]):
        if cheapest is None or details["cost"] < item_options[cheapest]["cost"]:
            cheapest = item

print(f"\nUse a {cheapest} for the cheapest result: {item_options[cheapest]['cost']} Hisser teeth.")