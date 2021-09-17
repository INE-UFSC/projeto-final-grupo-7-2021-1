from state_logic.states.state import State
from views.endgameView import EndgameView
from sound_logic.musicManager import MusicManager


MUSIC_MANAGER = MusicManager()

class EndgameState(State):
    def __init__(self):
        super().__init__(EndgameView(), 'endgame')

    def perform_actions(self, screen, **kwargs):
        MUSIC_MANAGER.game_music.stop_sound()
        final_score = kwargs['final_score']
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, final_score, mouse_up)
