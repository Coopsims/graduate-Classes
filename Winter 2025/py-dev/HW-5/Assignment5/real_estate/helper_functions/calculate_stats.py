# calculate_stats.py
def cheapest(properties_dict, state_or_territory):
    """
    Retrieves cheapest property in specified state or territory.

    Args:
        properties_dict (dict): Dictionary containing property data.
        state_or_territory (str): Name of state or territory.

    Returns:
        namedtuple: Property with lowest price in the specified region,
                    or None if no valid properties are found.
    """

    group = None
    if state_or_territory in properties_dict["US States"]:
        group = "US States"
    elif state_or_territory in properties_dict["Territories"]:
        group = "Territories"
    else:
        return None

    props = properties_dict[group][state_or_territory]
    if not props:
        return None
    return min(props, key=lambda p: p.price)


def priciest(properties_dict, state_or_territory):
    """
    Retrieves most expensive property in specified state or territory.

    Args:
        properties_dict (dict): Dictionary containing property data.
        state_or_territory (str): Name of state or territory.

    Returns:
        namedtuple: Property with highest price in the specified region,
                    or None if no valid properties are found.
    """

    group = None
    if state_or_territory in properties_dict["US States"]:
        group = "US States"
    elif state_or_territory in properties_dict["Territories"]:
        group = "Territories"
    else:
        return None

    props = properties_dict[group][state_or_territory]
    if not props:
        return None
    return max(props, key=lambda p: p.price)


def dirt_cheap(properties_dict):
    """
    Retrieves cheapest property across all US States and Territories.

    Args:
        properties_dict (dict): Dictionary containing property data.

    Returns:
        namedtuple: Property with lowest price overall, or None if no
                    properties are found.
    """

    all_props = []
    for group in properties_dict.values():
        for props in group.values():
            all_props.extend(props)
    if not all_props:
        return None
    return min(all_props, key=lambda p: p.price)


def best_deal(properties_dict, state_or_territory, bedrooms, bathrooms):
    """
    Retrieves property with the best (lowest) price-per-square-foot in a given
    state or territory, filtering by the specified number of bedrooms and bathrooms.

    Args:
        properties_dict (dict): Dictionary containing property data.
        state_or_territory (str): Name of state or territory.
        bedrooms (int): Required number of bedrooms.
        bathrooms (float): Required number of bathrooms.

    Returns:
        namedtuple: Property that offers lowest price-per-square-foot
                    given specified criteria, or None if no matching
                    properties are found.
    """

    group = None
    if state_or_territory in properties_dict["US States"]:
        group = "US States"
    elif state_or_territory in properties_dict["Territories"]:
        group = "Territories"
    else:
        return None

    filtered_props = [p for p in properties_dict[group][state_or_territory]
                      if p.bed == bedrooms and p.bath == bathrooms and p.house_size > 0]
    if not filtered_props:
        return None
    return min(filtered_props, key=lambda p: p.price / p.house_size)

def budget_friendly(properties_dict, bedrooms, bathrooms, max_budget):
    """
    Retrieves best (lowest) price-per-square-foot property across all locations
    that matches the specified number of bedrooms and bathrooms, and falls within
    the given max budget.

    Args:
        properties_dict (dict): Dictionary containing property data.
        bedrooms (int): Required number of bedrooms.
        bathrooms (float): Required number of bathrooms.
        max_budget (float): Maximum allowable property price.

    Returns:
        namedtuple: Property that offers lowest price-per-square-foot
                    given specified criteria, or None if no properties are found.
    """

    all_props = []
    for group in properties_dict.values():
        for props in group.values():
            all_props.extend(props)
    filtered_props = [p for p in all_props
                      if p.bed == bedrooms and p.bath == bathrooms and p.price <= max_budget and p.house_size > 0]
    if not filtered_props:
        return None
    return min(filtered_props, key=lambda p: p.price / p.house_size)


if __name__ == "__main__":
    print("This module is intended to be imported, not run directly.")
