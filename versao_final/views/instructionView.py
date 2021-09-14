from settings.gameColors import GameColors
from settings.gameSettings import GameSettings
from views.backHomeView import ViewWithHomeButton
from views.instruction.powers import PowersContent
from views.instruction.controls import ControlsContent
from views.instruction.objectives import ObjectivesContent
from views.buttons import RightArrowButton, LeftArrowButton


class InstructionView(ViewWithHomeButton):
    def __init__(self):
        super().__init__(GameColors.AZUL)
        self.__contents = [ObjectivesContent(), ControlsContent(), PowersContent()]
        self.__pos = 0
        self.__currentContent = self.__contents[self.__pos]
        self.__buttons = [LeftArrowButton(100, 70, (20, GameSettings.HEIGHT/2)),
                          RightArrowButton(100, 70, (GameSettings.WIDTH - 100 - 30, GameSettings.HEIGHT/2)) ]

    def display(self, screen, mouse_up):
        s0 = super().display(screen, mouse_up)
        self.__currentContent.display(screen)
        self.manage_arrow_buttons(screen, mouse_up)
        self.__currentContent = self.__contents[self.__pos]
        return self.button_states_handler('instrucoes',[s0])

    def manage_arrow_buttons(self, screen, mouse_up):
        if self.__pos == 0:
            self.__buttons[1].draw(screen)
            self.__buttons[1].hover()
            self.__pos = self.__buttons[1].click(self.__pos, mouse_up)
        elif self.__pos == len(self.__contents) - 1:
            self.__buttons[0].draw(screen)
            self.__buttons[0].hover()
            self.__pos = self.__buttons[0].click(self.__pos, mouse_up)
        else:
            for btn in self.__buttons:
                btn.draw(screen)
                btn.hover()
                self.__pos = btn.click(self.__pos, mouse_up)
