from .components import GrowthOption, EnergyPresenceTrack, CardPlaysPresenceTrack
from powers import Power

class Spirit:
    
    # TODO: Add special ability from bottom left of card
    def __init__(
            self, name: str, growth_options: list[GrowthOption], 
            innate_powers: dict[Power], energy_presence_track: EnergyPresenceTrack,
            card_plays_presence_track: CardPlaysPresenceTrack,
            starting_hand: dict[int, Power]) -> None:
        self.name = name
        self.growth_options = growth_options
        self.innate_powers = innate_powers
        self.energy_presence_track = energy_presence_track
        self.card_plays_presence_track = card_plays_presence_track
        self.energy = 0
        self.hand = {}
        self.discard = {}
        self.played_cards = {}

    def gain_energy(self, quantity: int) -> None:
        self.energy += quantity

    def play_power(self, power_id: int) -> None:
        self.played_cards[power_id] = (self.hand.pop(power_id))

    def reclaim_power(self, power: Power) -> None:
        self.hand[power] = self.discard.pop(power)
        
    def gain_power(self, power: Power) -> None:
        self.hand[power] = power
    
    def reclaim_all_cards(self) -> None:
        self.hand.update(self.discard)
        self.discard = {}

    def place_presence(self, track: int) -> None:
        """
        Removes presence from a track.

        Parameters
        ----------
        track : int
            The track to place presence from.
            0 = Energy Presence Track.
            1 = Card Plays Presence Track.
        """

        if track == 0:
            self.place_presence_from_energy_track()
        elif track == 1:
            self.place_presence_from_card_track()
        else:
            raise ValueError(f"Invalid track: {track}")

    def place_presence_from_energy_track(self) -> None:
        self.energy_presence_track.remove_presence()

    def place_presence_from_card_track(self) -> None:
        self.card_plays_presence_track.remove_presence()

    def get_number_of_card_plays(self) -> int:
        return self.card_plays_presence_track.get_number_of_plays()
    
    def gain_energy_from_energy_track(self) -> None:
        self.energy += self.energy_presence_track.get_energy_to_gain()

    def reset_for_next_round(self) -> None:
        self.discard.update(self.played_cards)
        self.played_cards = {}