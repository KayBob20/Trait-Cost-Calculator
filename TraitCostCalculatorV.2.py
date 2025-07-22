# Common trait keyword sets
common_trait_keywords = [
    ["horn", "trait", "normal"],
    ["what’s", "horn", "trait", "normal"],
    ["mouth", "trait", "normal"],
    ["heat", "pit", "traits", "normal"],
    ["eye", "trait", "goat"],
    ["ear", "trait", "deer"],
    ["feet", "trait", "paws"],
    ["tail", "trait", "goat", "on", "top"]
]

# Uncommon trait keyword sets
uncommon_trait_keywords = [
    ["horn", "trait", "backwards"],
    ["what’s", "horn", "trait", "spikey"],
    ["mouth", "trait", "canine"],
    ["heat", "pit", "traits", "circle"],
    ["eye", "trait", "double"],
    ["ear", "trait", "mouse"],
    ["feet", "trait", "spiked", "hooves"],
    ["tail", "trait", "rattlesnake"]
]

# Sample input with one invalid line
input_text = """
Horn trait - Normal
What’s on the horn trait: Normal
Mouth trait normal
Eye trait: Goat
Ear trait: Deer
Feet trait: Paws
Tail trait: Goat on top
Heat pit traits: Circle
"""

# Initialize counters and trackers
common_traits = 0
uncommon_traits = 0
invalid_lines = []

# Normalize input
lines = input_text.strip().lower().splitlines()

for line in lines:
    line = line.strip()
    matched = False

    # Check for uncommon match
    for keyword_set in uncommon_trait_keywords:
        if all(keyword in line for keyword in keyword_set):
            uncommon_traits += 1
            matched = True
            break

    # Check for common match
    if not matched:
        for keyword_set in common_trait_keywords:
            if all(keyword in line for keyword in keyword_set):
                common_traits += 1
                matched = True
                break

    # If no match, track as invalid
    if not matched:
        invalid_lines.append(line)

# Handle invalid lines
if invalid_lines:
    print("There are one or more traits listed that aren’t on the traits sheet.")
    for invalid in invalid_lines:
        # Try to extract the trait value after the colon or dash
        if ":" in invalid:
            trait_detail = invalid.split(":", 1)[1].strip()
        elif "-" in invalid:
            trait_detail = invalid.split("-", 1)[1].strip()
        else:
            trait_detail = invalid  # Fallback
        print(f'The trait "{trait_detail}" doesn’t exist.')
    print("Please ensure that all traits listed are on the trait sheet.")
else:
    # === VALID INPUTS ONLY ===

    # Determine rarity
    rarity_label = "uncommon" if uncommon_traits > 0 else "common"

    # Cost logic
    common_egg_cost = 1000
    uncommon_scale_cost = 600
    uncommon_egg_cost = 1800

    cost_option_a = uncommon_egg_cost
    cost_option_b = common_egg_cost + (uncommon_traits * uncommon_scale_cost)

    if uncommon_traits > 0:
        if cost_option_b < cost_option_a:
            items = f"one common egg ({common_egg_cost}) and {uncommon_traits} uncommon scale(s) ({uncommon_traits * uncommon_scale_cost})"
            total_cost = cost_option_b
        else:
            items = f"one uncommon egg ({uncommon_egg_cost})"
            total_cost = cost_option_a
    else:
        items = f"one common egg ({common_egg_cost})"
        total_cost = common_egg_cost

    # === Trait grammar + final output ===

    def trait_phrase(count, rarity):
        label = "trait" if count == 1 else "traits"
        return f"{count} {rarity} {label}"

    # Trait summary string (always show common first)
    trait_summary_parts = []
    if common_traits > 0:
        trait_summary_parts.append(trait_phrase(common_traits, "common"))
    if uncommon_traits > 0:
        trait_summary_parts.append(trait_phrase(uncommon_traits, "uncommon"))

    trait_summary = " and ".join(trait_summary_parts)

    # Final output
    print(f"The rarity of your Hoofhisser is {rarity_label}. You have {trait_summary}.")
    print(f"The cheapest item(s) to make your Hoofhisser will be {items} which will cost a total of {total_cost} Hisser teeth.")