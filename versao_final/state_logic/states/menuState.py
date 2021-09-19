from views.menuView import MenuView
from state_logic.states.state import State
from sound_logic.musicManager import MusicManager


MUSIC_MANAGER = MusicManager()

class MenuState(State):
    def __init__(self):
        super().__init__(MenuView(), 'menu')

    def perform_actions(self, screen, **kwargs):
        MUSIC_MANAGER.game_music.stop_sound()
        MUSIC_MANAGER.menu_music.play_sound()
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)
