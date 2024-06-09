# -*- coding: utf-8 -*-

# NE PAS MODIFIER LES LIGNES COMMENCANT PAR "!!!TAG".

import sys


# Vous avez la possibilité ici de sélectionner la version de Magix3D

import pyMagix3D as Mgx3D
ctx = Mgx3D.getStdContext()


gm = ctx.getGeomManager ()

tm = ctx.getTopoManager ()

mm = ctx.getMeshManager ()

# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 0, 0), Mgx3D.Point(1, 1, 1), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 0, 1), Mgx3D.Point(1, 1, 2), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 0, 2), Mgx3D.Point(1, 1, 3), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 0, 3), Mgx3D.Point(1, 1, 4), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 0, 4), Mgx3D.Point(1, 1, 5), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 0, 5), Mgx3D.Point(1, 1, 6), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 1, 0), Mgx3D.Point(1, 2, 1), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 1, 1), Mgx3D.Point(1, 2, 2), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 1, 2), Mgx3D.Point(1, 2, 3), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 1, 3), Mgx3D.Point(1, 2, 4), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 1, 4), Mgx3D.Point(1, 2, 5), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 1, 5), Mgx3D.Point(1, 2, 6), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 2, 0), Mgx3D.Point(1, 3, 1), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 2, 1), Mgx3D.Point(1, 3, 2), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 2, 2), Mgx3D.Point(1, 3, 3), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 2, 3), Mgx3D.Point(1, 3, 4), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 2, 4), Mgx3D.Point(1, 3, 5), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 2, 5), Mgx3D.Point(1, 3, 6), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 3, 0), Mgx3D.Point(1, 4, 1), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 3, 1), Mgx3D.Point(1, 4, 2), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 3, 2), Mgx3D.Point(1, 4, 3), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 3, 3), Mgx3D.Point(1, 4, 4), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 3, 4), Mgx3D.Point(1, 4, 5), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 3, 5), Mgx3D.Point(1, 4, 6), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 4, 0), Mgx3D.Point(1, 5, 1), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 4, 1), Mgx3D.Point(1, 5, 2), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 4, 2), Mgx3D.Point(1, 5, 3), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 4, 3), Mgx3D.Point(1, 5, 4), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 4, 4), Mgx3D.Point(1, 5, 5), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 4, 5), Mgx3D.Point(1, 5, 6), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 5, 0), Mgx3D.Point(1, 6, 1), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 5, 1), Mgx3D.Point(1, 6, 2), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 5, 2), Mgx3D.Point(1, 6, 3), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 5, 3), Mgx3D.Point(1, 6, 4), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 5, 4), Mgx3D.Point(1, 6, 5), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(0, 5, 5), Mgx3D.Point(1, 6, 6), 10, 10, 10, "layer_0")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 0, 0), Mgx3D.Point(2, 1, 1), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 0, 1), Mgx3D.Point(2, 1, 2), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 0, 2), Mgx3D.Point(2, 1, 3), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 0, 3), Mgx3D.Point(2, 1, 4), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 0, 4), Mgx3D.Point(2, 1, 5), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 0, 5), Mgx3D.Point(2, 1, 6), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 1, 0), Mgx3D.Point(2, 2, 1), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 1, 1), Mgx3D.Point(2, 2, 2), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 1, 2), Mgx3D.Point(2, 2, 3), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 1, 3), Mgx3D.Point(2, 2, 4), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 1, 4), Mgx3D.Point(2, 2, 5), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 1, 5), Mgx3D.Point(2, 2, 6), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 2, 0), Mgx3D.Point(2, 3, 1), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 2, 1), Mgx3D.Point(2, 3, 2), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 2, 2), Mgx3D.Point(2, 3, 3), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 2, 3), Mgx3D.Point(2, 3, 4), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 2, 4), Mgx3D.Point(2, 3, 5), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 2, 5), Mgx3D.Point(2, 3, 6), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 3, 0), Mgx3D.Point(2, 4, 1), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 3, 1), Mgx3D.Point(2, 4, 2), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 3, 2), Mgx3D.Point(2, 4, 3), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 3, 3), Mgx3D.Point(2, 4, 4), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 3, 4), Mgx3D.Point(2, 4, 5), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 3, 5), Mgx3D.Point(2, 4, 6), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 4, 0), Mgx3D.Point(2, 5, 1), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 4, 1), Mgx3D.Point(2, 5, 2), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 4, 2), Mgx3D.Point(2, 5, 3), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 4, 3), Mgx3D.Point(2, 5, 4), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 4, 4), Mgx3D.Point(2, 5, 5), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 4, 5), Mgx3D.Point(2, 5, 6), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 5, 0), Mgx3D.Point(2, 6, 1), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 5, 1), Mgx3D.Point(2, 6, 2), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 5, 2), Mgx3D.Point(2, 6, 3), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 5, 3), Mgx3D.Point(2, 6, 4), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 5, 4), Mgx3D.Point(2, 6, 5), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(1, 5, 5), Mgx3D.Point(2, 6, 6), 10, 10, 10, "layer_1")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 0, 0), Mgx3D.Point(3, 1, 1), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 0, 1), Mgx3D.Point(3, 1, 2), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 0, 2), Mgx3D.Point(3, 1, 3), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 0, 3), Mgx3D.Point(3, 1, 4), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 0, 4), Mgx3D.Point(3, 1, 5), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 0, 5), Mgx3D.Point(3, 1, 6), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 1, 0), Mgx3D.Point(3, 2, 1), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 1, 1), Mgx3D.Point(3, 2, 2), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 1, 2), Mgx3D.Point(3, 2, 3), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 1, 3), Mgx3D.Point(3, 2, 4), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 1, 4), Mgx3D.Point(3, 2, 5), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 1, 5), Mgx3D.Point(3, 2, 6), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 2, 0), Mgx3D.Point(3, 3, 1), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 2, 1), Mgx3D.Point(3, 3, 2), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 2, 2), Mgx3D.Point(3, 3, 3), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 2, 3), Mgx3D.Point(3, 3, 4), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 2, 4), Mgx3D.Point(3, 3, 5), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 2, 5), Mgx3D.Point(3, 3, 6), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 3, 0), Mgx3D.Point(3, 4, 1), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 3, 1), Mgx3D.Point(3, 4, 2), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 3, 2), Mgx3D.Point(3, 4, 3), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 3, 3), Mgx3D.Point(3, 4, 4), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 3, 4), Mgx3D.Point(3, 4, 5), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 3, 5), Mgx3D.Point(3, 4, 6), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 4, 0), Mgx3D.Point(3, 5, 1), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 4, 1), Mgx3D.Point(3, 5, 2), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 4, 2), Mgx3D.Point(3, 5, 3), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 4, 3), Mgx3D.Point(3, 5, 4), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 4, 4), Mgx3D.Point(3, 5, 5), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 4, 5), Mgx3D.Point(3, 5, 6), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 5, 0), Mgx3D.Point(3, 6, 1), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 5, 1), Mgx3D.Point(3, 6, 2), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 5, 2), Mgx3D.Point(3, 6, 3), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 5, 3), Mgx3D.Point(3, 6, 4), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 5, 4), Mgx3D.Point(3, 6, 5), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(2, 5, 5), Mgx3D.Point(3, 6, 6), 10, 10, 10, "layer_2")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 0, 0), Mgx3D.Point(4, 1, 1), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 0, 1), Mgx3D.Point(4, 1, 2), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 0, 2), Mgx3D.Point(4, 1, 3), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 0, 3), Mgx3D.Point(4, 1, 4), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 0, 4), Mgx3D.Point(4, 1, 5), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 0, 5), Mgx3D.Point(4, 1, 6), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 1, 0), Mgx3D.Point(4, 2, 1), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 1, 1), Mgx3D.Point(4, 2, 2), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 1, 2), Mgx3D.Point(4, 2, 3), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 1, 3), Mgx3D.Point(4, 2, 4), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 1, 4), Mgx3D.Point(4, 2, 5), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 1, 5), Mgx3D.Point(4, 2, 6), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 2, 0), Mgx3D.Point(4, 3, 1), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 2, 1), Mgx3D.Point(4, 3, 2), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 2, 2), Mgx3D.Point(4, 3, 3), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 2, 3), Mgx3D.Point(4, 3, 4), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 2, 4), Mgx3D.Point(4, 3, 5), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 2, 5), Mgx3D.Point(4, 3, 6), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 3, 0), Mgx3D.Point(4, 4, 1), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 3, 1), Mgx3D.Point(4, 4, 2), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 3, 2), Mgx3D.Point(4, 4, 3), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 3, 3), Mgx3D.Point(4, 4, 4), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 3, 4), Mgx3D.Point(4, 4, 5), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 3, 5), Mgx3D.Point(4, 4, 6), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 4, 0), Mgx3D.Point(4, 5, 1), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 4, 1), Mgx3D.Point(4, 5, 2), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 4, 2), Mgx3D.Point(4, 5, 3), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 4, 3), Mgx3D.Point(4, 5, 4), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 4, 4), Mgx3D.Point(4, 5, 5), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 4, 5), Mgx3D.Point(4, 5, 6), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 5, 0), Mgx3D.Point(4, 6, 1), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 5, 1), Mgx3D.Point(4, 6, 2), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 5, 2), Mgx3D.Point(4, 6, 3), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 5, 3), Mgx3D.Point(4, 6, 4), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 5, 4), Mgx3D.Point(4, 6, 5), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(3, 5, 5), Mgx3D.Point(4, 6, 6), 10, 10, 10, "layer_3")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 0, 0), Mgx3D.Point(5, 1, 1), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 0, 1), Mgx3D.Point(5, 1, 2), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 0, 2), Mgx3D.Point(5, 1, 3), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 0, 3), Mgx3D.Point(5, 1, 4), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 0, 4), Mgx3D.Point(5, 1, 5), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 0, 5), Mgx3D.Point(5, 1, 6), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 1, 0), Mgx3D.Point(5, 2, 1), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 1, 1), Mgx3D.Point(5, 2, 2), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 1, 2), Mgx3D.Point(5, 2, 3), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 1, 3), Mgx3D.Point(5, 2, 4), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 1, 4), Mgx3D.Point(5, 2, 5), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 1, 5), Mgx3D.Point(5, 2, 6), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 2, 0), Mgx3D.Point(5, 3, 1), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 2, 1), Mgx3D.Point(5, 3, 2), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 2, 2), Mgx3D.Point(5, 3, 3), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 2, 3), Mgx3D.Point(5, 3, 4), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 2, 4), Mgx3D.Point(5, 3, 5), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 2, 5), Mgx3D.Point(5, 3, 6), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 3, 0), Mgx3D.Point(5, 4, 1), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 3, 1), Mgx3D.Point(5, 4, 2), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 3, 2), Mgx3D.Point(5, 4, 3), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 3, 3), Mgx3D.Point(5, 4, 4), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 3, 4), Mgx3D.Point(5, 4, 5), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 3, 5), Mgx3D.Point(5, 4, 6), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 4, 0), Mgx3D.Point(5, 5, 1), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 4, 1), Mgx3D.Point(5, 5, 2), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 4, 2), Mgx3D.Point(5, 5, 3), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 4, 3), Mgx3D.Point(5, 5, 4), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 4, 4), Mgx3D.Point(5, 5, 5), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 4, 5), Mgx3D.Point(5, 5, 6), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 5, 0), Mgx3D.Point(5, 6, 1), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 5, 1), Mgx3D.Point(5, 6, 2), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 5, 2), Mgx3D.Point(5, 6, 3), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 5, 3), Mgx3D.Point(5, 6, 4), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 5, 4), Mgx3D.Point(5, 6, 5), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(4, 5, 5), Mgx3D.Point(5, 6, 6), 10, 10, 10, "layer_4")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 0, 0), Mgx3D.Point(6, 1, 1), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 0, 1), Mgx3D.Point(6, 1, 2), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 0, 2), Mgx3D.Point(6, 1, 3), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 0, 3), Mgx3D.Point(6, 1, 4), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 0, 4), Mgx3D.Point(6, 1, 5), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 0, 5), Mgx3D.Point(6, 1, 6), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 1, 0), Mgx3D.Point(6, 2, 1), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 1, 1), Mgx3D.Point(6, 2, 2), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 1, 2), Mgx3D.Point(6, 2, 3), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 1, 3), Mgx3D.Point(6, 2, 4), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 1, 4), Mgx3D.Point(6, 2, 5), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 1, 5), Mgx3D.Point(6, 2, 6), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 2, 0), Mgx3D.Point(6, 3, 1), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 2, 1), Mgx3D.Point(6, 3, 2), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 2, 2), Mgx3D.Point(6, 3, 3), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 2, 3), Mgx3D.Point(6, 3, 4), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 2, 4), Mgx3D.Point(6, 3, 5), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 2, 5), Mgx3D.Point(6, 3, 6), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 3, 0), Mgx3D.Point(6, 4, 1), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 3, 1), Mgx3D.Point(6, 4, 2), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 3, 2), Mgx3D.Point(6, 4, 3), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 3, 3), Mgx3D.Point(6, 4, 4), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 3, 4), Mgx3D.Point(6, 4, 5), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 3, 5), Mgx3D.Point(6, 4, 6), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 4, 0), Mgx3D.Point(6, 5, 1), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 4, 1), Mgx3D.Point(6, 5, 2), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 4, 2), Mgx3D.Point(6, 5, 3), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 4, 3), Mgx3D.Point(6, 5, 4), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 4, 4), Mgx3D.Point(6, 5, 5), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 4, 5), Mgx3D.Point(6, 5, 6), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 5, 0), Mgx3D.Point(6, 6, 1), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 5, 1), Mgx3D.Point(6, 6, 2), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 5, 2), Mgx3D.Point(6, 6, 3), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 5, 3), Mgx3D.Point(6, 6, 4), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 5, 4), Mgx3D.Point(6, 6, 5), 10, 10, 10, "layer_5")
# Création d'une boite avec une topologie
ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(5, 5, 5), Mgx3D.Point(6, 6, 6), 10, 10, 10, "layer_5")

ctx.getGeomManager().glue(['Vol0000', 'Vol0001', 'Vol0002', 'Vol0003', 'Vol0004', 'Vol0005', 'Vol0006', 'Vol0007', 'Vol0008', 'Vol0009', 'Vol0010', 'Vol0011', 'Vol0012', 'Vol0013', 'Vol0014', 'Vol0015', 'Vol0016', 'Vol0017', 'Vol0018', 'Vol0019', 'Vol0020', 'Vol0021', 'Vol0022', 'Vol0023', 'Vol0024', 'Vol0025', 'Vol0026', 'Vol0027', 'Vol0028', 'Vol0029', 'Vol0030', 'Vol0031', 'Vol0032', 'Vol0033', 'Vol0034', 'Vol0035', 'Vol0036', 'Vol0037', 'Vol0038', 'Vol0039', 'Vol0040', 'Vol0041', 'Vol0042', 'Vol0043', 'Vol0044', 'Vol0045', 'Vol0046', 'Vol0047', 'Vol0048', 'Vol0049', 'Vol0050', 'Vol0051', 'Vol0052', 'Vol0053', 'Vol0054', 'Vol0055', 'Vol0056', 'Vol0057', 'Vol0058', 'Vol0059', 'Vol0060', 'Vol0061', 'Vol0062', 'Vol0063', 'Vol0064', 'Vol0065', 'Vol0066', 'Vol0067', 'Vol0068', 'Vol0069', 'Vol0070', 'Vol0071', 'Vol0072', 'Vol0073', 'Vol0074', 'Vol0075', 'Vol0076', 'Vol0077', 'Vol0078', 'Vol0079', 'Vol0080', 'Vol0081', 'Vol0082', 'Vol0083', 'Vol0084', 'Vol0085', 'Vol0086', 'Vol0087', 'Vol0089', 'Vol0090', 'Vol0091', 'Vol0092', 'Vol0093', 'Vol0094', 'Vol0095', 'Vol0096', 'Vol0097', 'Vol0098', 'Vol0099', 'Vol0100', 'Vol0101', 'Vol0102', 'Vol0103', 'Vol0104', 'Vol0105', 'Vol0106', 'Vol0107', 'Vol0108', 'Vol0109', 'Vol0110', 'Vol0111', 'Vol0112', 'Vol0113', 'Vol0114', 'Vol0115', 'Vol0116', 'Vol0117', 'Vol0118', 'Vol0119', 'Vol0120', 'Vol0121', 'Vol0122', 'Vol0123', 'Vol0124', 'Vol0125', 'Vol0126', 'Vol0127', 'Vol0128', 'Vol0129', 'Vol0130', 'Vol0131', 'Vol0132', 'Vol0133', 'Vol0134', 'Vol0135', 'Vol0136', 'Vol0137', 'Vol0138', 'Vol0139', 'Vol0140', 'Vol0141', 'Vol0142', 'Vol0143', 'Vol0144', 'Vol0145', 'Vol0146', 'Vol0147', 'Vol0148', 'Vol0149', 'Vol0150', 'Vol0151', 'Vol0152', 'Vol0153', 'Vol0154', 'Vol0155', 'Vol0156', 'Vol0157', 'Vol0158', 'Vol0159', 'Vol0160', 'Vol0161', 'Vol0162', 'Vol0163', 'Vol0164', 'Vol0165', 'Vol0166', 'Vol0167', 'Vol0168', 'Vol0169', 'Vol0170', 'Vol0171', 'Vol0172', 'Vol0173', 'Vol0174', 'Vol0175', 'Vol0176', 'Vol0177', 'Vol0178', 'Vol0179', 'Vol0180', 'Vol0181', 'Vol0182', 'Vol0183', 'Vol0184', 'Vol0185', 'Vol0186', 'Vol0187', 'Vol0188', 'Vol0189', 'Vol0190', 'Vol0191', 'Vol0192', 'Vol0193', 'Vol0194', 'Vol0195', 'Vol0196', 'Vol0197', 'Vol0198', 'Vol0199', 'Vol0200', 'Vol0201', 'Vol0202', 'Vol0203', 'Vol0204', 'Vol0205', 'Vol0206', 'Vol0207', 'Vol0208', 'Vol0209', 'Vol0210', 'Vol0211', 'Vol0212', 'Vol0213', 'Vol0214', 'Vol0215'])

# Création du maillage pour tous les blocs
ctx.getMeshManager().newAllBlocksMesh()
