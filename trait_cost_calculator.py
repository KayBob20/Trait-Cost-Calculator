import re

def process_traits(input_text):
    # Define keywords for matching trait types by rarity
    common_trait_keywords = [
        ["horn", "normal"],
        ["what's on the horn", "normal"],
        ["mouth", "normal"],
        ["heat pit", "normal"],
        ["eye", "goat"],
        ["ear", "deer"],
        ["feet", "paws"],
        ["feet", "paws + hooves"],
        ["tail", "goat on top"],
        ["tail", "snake butt"],
    ]

    uncommon_trait_keywords = [
        ["horn", "backwards"],
        ["what's on the horn", "spikey"],
        ["mouth", "canine"],
        ["heat pit", "circle"],
        ["eye", "double"],
        ["ear", "mouse"],
        ["feet", "spiked hooves"],
        ["tail", "rattlesnake"],
    ]

    rare_trait_keywords = [
        ["horn", "unicorn"],
        ["what's on the horn", "cobra"],
        ["mouth", "fanged goat"],
        ["heat pit", "split circle"],
        ["eye", "black"],
        ["ear", "rabbit"],
        ["feet", "stubs"],
        ["tail", "goat"],
    ]

    # Initialize counters
    common_traits = 0
    uncommon_traits = 0
    rare_traits = 0
    invalid_lines = []

    # Normalize input
    lines = input_text.strip().lower().splitlines()

    for line in lines:
        line = line.strip()
        line = ' '.join(line.split())  # Remove extra spaces

        matched = False

        # Extract trait type and value
        m = re.match(r"^(.*trait[s]?)\s*[:\-]?\s*(.+)$", line)
        if m:
            trait_type = m.group(1).strip()
            trait_value = m.group(2).strip()
            trait_value = re.sub(r"\s*\(.*\)$", "", trait_value).strip()
        else:
            invalid_lines.append(line)
            continue

        trait_type = trait_type.lower()
        trait_value = trait_value.lower()

        def match_trait(keyword_list):
            for keyword_type, keyword_value in keyword_list:
                if (keyword_type in trait_type) or (trait_type in keyword_type):
                    if keyword_value == trait_value:
                        return True
            return False

        if match_trait(rare_trait_keywords):
            rare_traits += 1
            matched = True
        elif match_trait(uncommon_trait_keywords):
            uncommon_traits += 1
            matched = True
        elif match_trait(common_trait_keywords):
            common_traits += 1
            matched = True

        if not matched:
            invalid_lines.append(line)

    # Prepare output
    if invalid_lines:
        error_lines = []
        for invalid in invalid_lines:
            if ":" in invalid:
                trait_detail = invalid.split(":", 1)[1].strip()
            elif "-" in invalid:
                trait_detail = invalid.split("-", 1)[1].strip()
            else:
                trait_detail = invalid
            error_lines.append(f'The trait "{trait_detail}" doesn’t exist.')
        output = (
            "There are one or more traits listed that aren’t on the traits sheet.\n\n"
            + "\n".join(error_lines)
            + "\n\nPlease ensure that all traits listed are on the trait sheet and that they are spelled correctly."
        )
        return output

    def trait_phrase(count, rarity):
        label = "trait" if count == 1 else "traits"
        return f"{count} {rarity} {label}"

    trait_summary_parts = []
    if common_traits > 0:
        trait_summary_parts.append(trait_phrase(common_traits, "common"))
    if uncommon_traits > 0:
        trait_summary_parts.append(trait_phrase(uncommon_traits, "uncommon"))
    if rare_traits > 0:
        trait_summary_parts.append(trait_phrase(rare_traits, "rare"))

    trait_summary = "\n".join(trait_summary_parts)

    if rare_traits > 0:
        rarity_label = "rare"
    elif uncommon_traits > 0:
        rarity_label = "uncommon"
    else:
        rarity_label = "common"

    # === Cost Calculation ===
    common_egg_cost = 1000
    uncommon_egg_cost = 1800
    rare_egg_cost = 3000
    uncommon_scale_cost = 600
    rare_scale_cost = 1000

    option_a_cost = rare_egg_cost
    option_a_items = f"\n1 rare egg ({rare_egg_cost})"

    option_b_cost = uncommon_egg_cost + (rare_traits * rare_scale_cost)
    option_b_items = (
        f"\n1 uncommon egg ({uncommon_egg_cost})"
        + (f"\n{rare_traits} rare scale(s) ({rare_traits * rare_scale_cost})" if rare_traits > 0 else "")
    )

    option_c_cost = (
        common_egg_cost
        + (uncommon_traits * uncommon_scale_cost)
        + (rare_traits * rare_scale_cost)
    )
    option_c_items = f"\n1 common egg ({common_egg_cost})"
    if uncommon_traits > 0:
        option_c_items += f"\n{uncommon_traits} uncommon scale(s) ({uncommon_traits * uncommon_scale_cost})"
    if rare_traits > 0:
        option_c_items += f"\n{rare_traits} rare scale(s) ({rare_traits * rare_scale_cost})"

    min_cost = min(option_a_cost, option_b_cost, option_c_cost)
    if min_cost == option_a_cost:
        items = option_a_items
        total_cost = option_a_cost
    elif min_cost == option_b_cost:
        items = option_b_items
        total_cost = option_b_cost
    else:
        items = option_c_items
        total_cost = option_c_cost

    # Final output string
    return (
        f"Your Hoofhisser is {rarity_label} and has:\n{trait_summary}\n"
        f"\nThe cheapest item(s) to make your Hoofhisser will be:\n{items}\n\nTotal Cost: {total_cost} Hisser Teeth.\n"
    )