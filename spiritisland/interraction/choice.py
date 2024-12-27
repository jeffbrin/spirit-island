from enums import StandardAction

class Choice:
    def __init__(self) -> None:
        pass

class GrowthChoice(Choice):
    def __init__(self, option: int) -> None:
        self.option = option

    def validate_choice_given_constraints(self, num_options: int) -> bool:
        """
        Validates that the choice is valid given the constraints of the game.

        Parameters
        ----------
        num_options : int
            The number of growth options available to the player.

        Returns
        -------
        bool
            True if the choice is valid, False otherwise.
        """

        return self.option >= 0 and self.option < num_options


class ActionChoice(Choice):
    """
    Represents a specific action a player wants to perform. There could be many actions
    which make up a power card. These actions should be joined together to form powers.
    """

    def __init__(self, target_choice: int, action: StandardAction, quantity: int) -> None:
        """
        Initializes the action choice.

        Parameters
        ----------
        target_choice : int
            For most action choices, there are multiple actions to choose from. These
            will be enumerated. target_choice is the number associated with the chosen
            target.
        action : StandardAction
            The enum value representing the chosen action.
        quantity : int
            The quantity of times to perform an action. Ex: 3 to defend 3.
        """

        self.target_choice = target_choice
        self.action = action
        self.quantity = quantity

    def validate_choice_given_constraints(
            self, target_options: list[int], max_quantity: int) -> bool:
        """
        Validates that the choice is valid given the constraints of the game.

        Parameters
        ----------
        target_options : list[int]
            The list of possible target options for the action.
        max_quantity : int
            The maximum number of times the action can be performed.

        Returns
        -------
        bool
            True if the choice is valid, False otherwise.
        """

        return self.target_choice in target_options and self.quantity <= max_quantity \
            and self.quantity > 0 and self.action in StandardAction
    