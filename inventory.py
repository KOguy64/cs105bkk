"""HW0: a game inventory. Practises Session 1: names and objects, defaults, *args, comprehensions."""

import copy

def add_item(inventory, item, count=1):
    """Return a new inventory with count more of item. Do not change inventory."""
    inventory = copy.deepcopy(inventory)
    inventory[item] = inventory.get(item, 0) + count
    return inventory

def total_items(*inventories):
    return sum([sum(i.values()) for i in inventories])


def running_low(inventory, limit=2):
    """Return the names of items with fewer than limit left, sorted A to Z."""
    return sorted([name for name in inventory if inventory.get(name, 0) < limit])