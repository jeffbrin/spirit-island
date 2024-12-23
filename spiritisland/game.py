from enums import Step
from spirits import Spirit
from board import Board
from gamestate import BlightPool, FearPool, InvaderBoard

class Game:
    def __init__(self, spirit: Spirit, board_choice: str):
        
        self.board = Board.choose_board(board_choice)
        self.spirit = spirit
        self.step = Step.GROWTH
        # TODO: Change size when there are multiple spirits
        self.blight_pool = BlightPool()
        self.fear_pool = FearPool()
        self.invader_actions = InvaderBoard()
    
    def run_step(self, choices: list):
        match self.step:
            case Step.GROWTH:
                ...