# -*- coding: utf-8 -*-


# Création d'une sphère avec une topologie
ctx.getTopoManager().newSphereWithTopo (Mgx3D.Point(0, 0, 0), 1, Mgx3D.Portion.ENTIER, True, .5, 10, 10)
# Translation de la topologie seule Som0006
ctx.getTopoManager().translate (["Som0006"], Mgx3D.Vector(0, 1, 0), False)
# Création du maillage pour tous les blocs
ctx.getMeshManager().newAllBlocksMesh()
