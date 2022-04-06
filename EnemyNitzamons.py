import pygame.image

from Classes.NitzamonClasses.Nitzamon import Nitzamon
import Constants

shoham_nitzamon1 = Nitzamon(Constants.TRION, 5, [Constants.PUNCH, Constants.SCRATCH, Constants.LEAFBLADE, Constants.EARTHQUAKE])
shoham_nitzamon2 = Nitzamon(Constants.DARK_SQUARION, 6, [Constants.SLASH, Constants.SCRATCH, Constants.FIREBALL, Constants.BURN])
shoham_nitzamon3 = Nitzamon(Constants.PENTAGEON, 7, [Constants.PUNCH, Constants.SLASH, Constants.EARTHQUAKE, Constants.ROCKSLIDE])


gilad_nitzamon1 = Nitzamon(Constants.COMMENTAR, 25, [Constants.PUNCH, Constants.SCRATCH, Constants.SPIT, Constants.GEYSER])
gilad_nitzamon2 = Nitzamon(Constants.SHAREE, 26, [Constants.SLASH, Constants.SCRATCH, Constants.FIREBALL, Constants.BURN])
gilad_nitzamon3 = Nitzamon(Constants.HEARTIAN, 27, [Constants.PUNCH, Constants.SLASH, Constants.FIREBALL, Constants.LASER])


adi_nitzamon1 = Nitzamon(Constants.MANAGEREON, 45, [Constants.PUNCH, Constants.SCRATCH, Constants.LEAFBLADE, Constants.EARTHQUAKE])
adi_nitzamon2 = Nitzamon(Constants.MANAGEREON, 47, [Constants.SLASH, Constants.SCRATCH, Constants.EARTHQUAKE, Constants.ROCKSLIDE])
adi_nitzamon3 = Nitzamon(Constants.HEADEA, 50, [Constants.PUNCH, Constants.SLASH, Constants.FIREBALL, Constants.LASER])