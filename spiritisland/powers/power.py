from enums import StandardAction

class Power:
    # TODO: Implement the things I forgot
    def __init__(
            self, name: str, energy_cost: int, 
            fast: bool, actions: list[StandardAction], 
            max_times_per_action: list[int], range: int) -> None:
        """
        Initializes the power.

        Parameters
        ----------
        name : str
            The name of the power.
        energy_cost : int
            The amount of energy required to play this action.
        fast : bool
            Indicates whether the power is fast or slow.
        actions : list[StandardAction]
            The list of actions performed when this power is played.
        max_times_per_action : list[int]
            A list which mirrors actions. Each element indicates the maximum number
            of times the corresponding action can be performed.
        range : int
            The range from the player's presence that the power can be played.
        """
        self.name = name
        self.energy_cost = energy_cost
        self.fast = fast
        self.actions = actions
        self.max_times_per_action = max_times_per_action
        self.range = range