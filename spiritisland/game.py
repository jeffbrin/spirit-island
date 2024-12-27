from enums import Step
from spirits import Spirit, GrowthComponent
from board import Board
from gamestate import BlightPool, FearPool, InvaderBoard
from interraction import Choice, GrowthChoice, ActionChoice, PlayCardChoice
from powers import Power

from typing import Optional

class Game:
    def __init__(self, spirit: Spirit, board_choice: str, minor_powers: list[Power]):
        
        self.board = Board.choose_board(board_choice)
        self.spirit = spirit
        self.step = Step.GROWTH
        # TODO: Change size when there are multiple spirits
        self.blight_pool = BlightPool()
        self.fear_pool = FearPool()
        self.invader_actions = InvaderBoard()
        self.minor_powers = minor_powers
        # TODO: Add major powers
        self.major_powers = []
        self.rejected_minor_powers = []
        self.rejected_major_powers = []
    
    def run(self) -> None:
        while not self.is_game_over():
            choices = self.get_choices_for_step(self.step)
            self.run_step(self.step, choices, self.spirit)
            self.next_step()

    def next_step(self) -> None:
        match self.step:
            case Step.GROWTH:
                self.step = Step.PLAY_CARDS
            case Step.PLAY_CARDS:
                self.step = Step.PICK_FAST_CARDS_ORDER
            case Step.PICK_FAST_CARDS_ORDER:
                self.step = Step.PERFORM_ACTIONS
            case Step.PERFORM_FAST_ACTIONS:
                self.step = Step.PICK_SLOW_CARDS_ORDER
            case Step.PICK_SLOW_CARDS_ORDER:
                self.step = Step.PERFORM_SLOW_ACTIONS
            case Step.PERFORM_SLOW_ACTIONS:
                self.step = Step.GROWTH

    def get_choices_for_step(self, step: Step) -> list[Choice]:
        # TODO: Communicate with the model to get their choices for the current step, and
        # return them.
        ...

    def run_step(self, step: Step, choices: list[Choice], 
                 spirit: Optional[Spirit] = None) -> None:
        """
        Once the user has made their choices, perform the tasks they chose.
        While performing some of the tasks, we may call the get_choices_for_step and
        run_step method for a different step. This is because some tasks require the user
        to make choices during the task.

        Parameters
        ----------
        spirit : Spirit
            The spirit performing the tasks.
        choices : list[Choice]
            The list of choices made by the player.
        """        

        match step:
            case Step.PLAY_CARDS:
                self.play_cards(spirit, choices)
            case Step.PICK_FAST_CARDS_ORDER:
                self.pick_fast_cards_order(spirit, choices)
            case Step.PERFORM_FAST_ACTIONS:
                self.perform_power_actions(spirit, choices)
                # TODO: After performing actions, let the invaders do their thing.
            case Step.PERFORM_SLOW_ACTIONS:
                self.perform_power_actions(spirit, choices)
            case Step.PICK_BLIGHT_LAND:
                self.place_blight(choices)
            case Step.PICK_INVADERS_TO_KILL_ON_LAND:
                self.kill_invaders_on_land(choices)
            case Step.PICK_SLOW_CARDS_ORDER:
                self.pick_slow_cards_order(spirit, choices)
            case Step.PICK_LAND_FOR_PRESENCE:
                self.place_presence(spirit, choices)
            case Step.PICK_ONE_OF_4_MINOR_CARDS:
                self.add_power_card_to_hand(spirit, choices)
            case Step.PICK_PRESENCE_TRACK:
                pass
            case Step.PICK_GROWTH_OPTION:
                pass

    def perform_growth(self, spirit: Spirit, choices: list[GrowthChoice]) -> None:
        if not all([isinstance(choice, GrowthChoice) for choice in choices]):
            raise ValueError(
                f"All choices must be growth choices. Received: {choices}")
        
        if len(choices) != 1:
            raise ValueError(
                f"Only one growth choice is allowed, received {len(choices)}")
        
        choice = choices[0]
        if not choice.validate_choice_given_constraints(len(spirit.growth_options)):
            raise ValueError(f"Invalid growth choice: {choice.option}.")
        
        # Growth Option
        for growth_option in spirit.growth_options[choice.option].actions:
            match growth_option[0]:
                case GrowthComponent.RECLAIM_CARDS:
                    spirit.reclaim_all_cards()
                case GrowthComponent.GAIN_POWER_CARD:
                    spirit.gain_power(self.pick_power_card())
                case GrowthComponent.PLACE_PRESENCE:
                    spirit.place_presence(growth_option[1])
                case GrowthComponent.GAIN_ENERGY:
                    spirit.gain_energy(growth_option[1])

    def play_cards(self, spirit: Spirit, choices: list[PlayCardChoice]) -> None:
        if not all([isinstance(choice, PlayCardChoice) for choice in choices]):
            raise TypeError(f"Expected only PlayCardChoice, received {choices}")
        
        for choice in choices:
            if not choice.validate_choice_given_constraints(list(spirit.hand.keys())):
                raise ValueError(f'Received invalid card choice: {choice.card_id}. Available: {[x for x in spirit.hand.keys()]}')

            spirit.play_power(choice.card_id)

    def pick_power_card(self) -> Power:
        raise NotImplementedError("Need to implement power card picking")