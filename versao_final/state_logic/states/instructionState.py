from state_logic.states.state import State
from views.instructionView import InstructionView


class InstructionState(State):
    def __init__(self):
        super().__init__(InstructionView(), 'instrucoes')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)