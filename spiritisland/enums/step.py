from enum import Enum

class Step(Enum):
    # Make Growth Decisions
    GROWTH = 0
    # When placing presence, pick where to place it
    PICK_LAND_FOR_PRESENCE = 7
    # Pick one of the 4 minor cards when picking new cards
    PICK_ONE_OF_4_MINOR_CARDS = 8
    # Play cards from your hand
    PLAY_CARDS = 1
    # Pick the order in which fast action cards will be resolved
    PICK_FAST_CARDS_ORDER = 2
    # Given a list of (Pull, Push, Damage, ...), decide how to use them.
    PERFORM_FAST_ACTIONS = 3
    PERFORM_SLOW_ACTIONS = 9
    # Pick a land to place blight on
    PICK_BLIGHT_LAND = 4
    # When doing damage to invaders, pick how many cities, dahan, towns to kill
    PICK_INVADERS_TO_KILL_ON_LAND = 5
    # Pick the order in which slow cards will be resolved
    PICK_SLOW_CARDS_ORDER = 6
    # Pick the Presence track to take presence off of
    PICK_PRESENCE_TRACK = 10
    # Pick the growth option from the top of the spirit card
    PICK_GROWTH_OPTION = 11
    # Pick power card
    PICK_POWER_CARD = 12
    