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
        self.__contents = [PowersContent(), ControlsContent(), ObjectivesContent()]
        self.__pos = 0
        self.__currentContent = self.__contents[self.__pos]
        self.__buttons = [LeftArrowButton(150, 50, (100, GameSettings.HEIGHT/2)),
                          RightArrowButton(150, 50, (GameSettings.WIDTH - 150 - 100, GameSettings.HEIGHT/2)) ]

    def display(self, screen, mouse_up):
        super().display(screen)
        self.__currentContent.display(screen)
        self.manage_buttons(screen)
        self.__currentContent = self.__contents[self.__pos]

    def manage_buttons(self, screen):
        if self.__pos == 0:
            self.__buttons[1].draw(screen)
            self.__buttons[1].hover()
            self.__pos = self.__buttons[1].click(self.__pos)
        elif self.__pos == len(self.__contents) - 1:
            self.__buttons[0].draw(screen)
            self.__buttons[0].hover()
            self.__pos = self.__buttons[0].click(self.__pos)
        else:
            for btn in self.__buttons:
                btn.draw(screen)
                btn.hover()
                self.__pos = btn.click(self.__pos)
