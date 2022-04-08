import numpy as np

class Micro_Blackjack:
    def __init__(self):
        """
        Contractor for Q-learing enviroment Micro_Blackjack.
        state represents current state of the agent in the game and max_state
        the last accessible state.
        """
        self.state = 0
        self.max_state = 5


    def action(self, action):
        """
        Returns the resived reward in the current state with the chosen action.
        Action is 0: Stopp or 1: Draw.
        If draw is chosen 2, 3 or 4 cards are drawn all actions have the same probability.
        If more as 5 cards in total are drawn or the game is in state 0 stopp the reward is -5.
        If the total drawn cards <= 5 the reward is the number of drawn cards with the chosen action.
        Parameters
        ----------
        action : int
                 0: Stopp,  1: Draw
        Returns
        -------
        reward : int
                 Resived reward in the current state with the chosen action.
        """
        if action:
            action = np.random.choice([2,3,4])

        if action == 0 and self.state != 0:
            self.state = 5
            return 0

        elif action == 2 and self.state + 2 <= self.max_state:
            self.state += 2

        elif action == 3 and self.state + 3 <= self.max_state:
            self.state += 3

        elif action == 4 and self.state + 4 <= self.max_state:
            self.state += 4

        else:
            self.state = 5
            return -5

        return action
