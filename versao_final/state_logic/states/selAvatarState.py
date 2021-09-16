from state_logic.states.state import State
from views.avatarView import AvatarView


class SelAvatarState(State):
    def __init__(self):
        super().__init__(AvatarView(), 'sel_avatar')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)
