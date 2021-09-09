import pygame
import os
from pygame.font import Font

pygame.font.init()
fontPath = os.path.join(os.getcwd(),'settings', 'fonts')

#Poppins
class GameFonts:
    BOLD_SMALL = Font(os.path.join(fontPath,"Poppins-Bold.ttf"), 20)
    BOLD_LARGE = Font(os.path.join(fontPath,"Poppins-Bold.ttf"), 40)
    SEMIBOLD_LARGE = Font(os.path.join(fontPath,"Poppins-SemiBold.ttf"), 40)
    SEMIBOLD_SMALL = Font(os.path.join(fontPath,"Poppins-SemiBold.ttf"), 20)
    REGULAR_LARGE = Font(os.path.join(fontPath,"Poppins-Regular.ttf"), 40)
    REGULAR_SMALL = Font(os.path.join(fontPath,"Poppins-Regular.ttf"), 20)
    LIGHT_LARGE = Font(os.path.join(fontPath,"Poppins-ExtraLight.ttf"), 40)
    LIGHT_SMALL = Font(os.path.join(fontPath,"Poppins-ExtraLight.ttf"), 20)
