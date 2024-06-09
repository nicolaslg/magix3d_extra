# -*- coding: utf-8 -*-

import sys

import pyMagix3D as Mgx3D
ctx = Mgx3D.getStdContext()

# Changement d'unité de longueur
ctx.setLengthUnit(Mgx3D.Unit.centimeter)
# Import STEP
ctx.getGeomManager().importSTEP("B0.step")
# Création d'un bloc topologique structuré sans projection (Vol0000)
ctx.getTopoManager().newFreeTopoOnGeometry ("Vol0000")
# Affectation d'une projection vers Pt0008 pour les entités topologiques Som0005
ctx.getTopoManager().setGeomAssociation (["Som0005"], "Pt0008", True)
# Affectation d'une projection vers Pt0009 pour les entités topologiques Som0007
ctx.getTopoManager().setGeomAssociation (["Som0007"], "Pt0009", True)
# Affectation d'une projection vers Pt0007 pour les entités topologiques Som0001
ctx.getTopoManager().setGeomAssociation (["Som0001"], "Pt0007", True)
# Affectation d'une projection vers Pt0011 pour les entités topologiques Som0003
ctx.getTopoManager().setGeomAssociation (["Som0003"], "Pt0011", True)
# Affectation d'une projection vers Pt0003 pour les entités topologiques Som0000
ctx.getTopoManager().setGeomAssociation (["Som0000"], "Pt0003", True)
# Affectation d'une projection vers Pt0002 pour les entités topologiques Som0002
ctx.getTopoManager().setGeomAssociation (["Som0002"], "Pt0002", True)
# Affectation d'une projection vers Pt0000 pour les entités topologiques Som0004
ctx.getTopoManager().setGeomAssociation (["Som0004"], "Pt0000", True)
# Affectation d'une projection vers Pt0001 pour les entités topologiques Som0006
ctx.getTopoManager().setGeomAssociation (["Som0006"], "Pt0001", True)
# Suppression des projections pour les entités topologiques Ar0009
ctx.getTopoManager().setGeomAssociation (["Ar0009"], "", True)
# Affectation d'une projection vers Crb0007 pour les entités topologiques Ar0009
ctx.getTopoManager().setGeomAssociation (["Ar0009"], "Crb0007", True)
# Affectation d'une projection vers Crb0013 pour les entités topologiques Ar0011
ctx.getTopoManager().setGeomAssociation (["Ar0011"], "Crb0013", True)
# Affectation d'une projection vers Crb0010 pour les entités topologiques Ar0007
ctx.getTopoManager().setGeomAssociation (["Ar0007"], "Crb0010", True)
# Affectation d'une projection vers Crb0011 pour les entités topologiques Ar0003
ctx.getTopoManager().setGeomAssociation (["Ar0003"], "Crb0011", True)
# Affectation d'une projection vers Crb0008 pour les entités topologiques Ar0002
ctx.getTopoManager().setGeomAssociation (["Ar0002"], "Crb0008", True)
# Affectation d'une projection vers Crb0003 pour les entités topologiques Ar0008
ctx.getTopoManager().setGeomAssociation (["Ar0008"], "Crb0003", True)
# Affectation d'une projection vers Crb0001 pour les entités topologiques Ar0010
ctx.getTopoManager().setGeomAssociation (["Ar0010"], "Crb0001", True)
# Affectation d'une projection vers Crb0000 pour les entités topologiques Ar0006
ctx.getTopoManager().setGeomAssociation (["Ar0006"], "Crb0000", True)
# Affectation d'une projection vers Surf0002 pour les entités topologiques Fa0005
ctx.getTopoManager().setGeomAssociation (["Fa0005"], "Surf0002", True)
# Affectation d'une projection vers Surf0008 pour les entités topologiques Fa0001
ctx.getTopoManager().setGeomAssociation (["Fa0001"], "Surf0008", True)
# Affectation d'une projection vers Surf0000 pour les entités topologiques Fa0000
ctx.getTopoManager().setGeomAssociation (["Fa0000"], "Surf0000", True)
# Affectation d'une projection vers Surf0001 pour les entités topologiques Fa0002
ctx.getTopoManager().setGeomAssociation (["Fa0002"], "Surf0001", True)
# Affectation d'une projection vers Surf0003 pour les entités topologiques Fa0003
ctx.getTopoManager().setGeomAssociation (["Fa0003"], "Surf0003", True)
# Découpage en O-grid des blocs structurés Bl0000
ctx.getTopoManager().splitBlocksWithOgridV2 (["Bl0000"], ["Fa0002", "Fa0004", "Fa0003"], .5, 10)
# Destruction des entités topologiques Bl0004
ctx.getTopoManager().destroy (["Bl0004"], True)
# Découpage du bloc Bl0003
ctx.getTopoManager().splitBlock ("Bl0003","Ar0002",.5)
# Affectation d'une projection vers Pt0006 pour les entités topologiques Som0009
ctx.getTopoManager().setGeomAssociation (["Som0009"], "Pt0006", True)
# Affectation d'une projection vers Pt0012 pour les entités topologiques Som0011
ctx.getTopoManager().setGeomAssociation (["Som0011"], "Pt0012", True)
# Affectation d'une projection vers Pt0004 pour les entités topologiques Som0008
ctx.getTopoManager().setGeomAssociation (["Som0008"], "Pt0004", True)
# Affectation d'une projection vers Pt0010 pour les entités topologiques Som0010
ctx.getTopoManager().setGeomAssociation (["Som0010"], "Pt0010", True)
# Affectation d'une projection vers Pt0005 pour les entités topologiques Som0018
ctx.getTopoManager().setGeomAssociation (["Som0018"], "Pt0005", True)
# Affectation d'une projection vers Pt0013 pour les entités topologiques Som0019
ctx.getTopoManager().setGeomAssociation (["Som0019"], "Pt0013", True)
# Affectation d'une projection vers Crb0005 pour les entités topologiques Som0013
ctx.getTopoManager().setGeomAssociation (["Som0013"], "Crb0005", True)
# Affectation d'une projection vers Crb0015 pour les entités topologiques Som0015
ctx.getTopoManager().setGeomAssociation (["Som0015"], "Crb0015", True)
# Suppression des projections pour les entités topologiques Som0015
ctx.getTopoManager().setGeomAssociation (["Som0015"], "", True)
# Affectation d'une projection vers Crb0016 pour les entités topologiques Som0014
ctx.getTopoManager().setGeomAssociation (["Som0014"], "Crb0016", True)
# Affectation d'une projection vers Crb0004 pour les entités topologiques Som0012
ctx.getTopoManager().setGeomAssociation (["Som0012"], "Crb0004", True)
# Affectation d'une projection vers Crb0004 pour les entités topologiques Ar0021 Ar0037
ctx.getTopoManager().setGeomAssociation (["Ar0021", "Ar0037"], "Crb0004", True)
# Affectation d'une projection vers Crb0005 pour les entités topologiques Ar0038 Ar0025
ctx.getTopoManager().setGeomAssociation (["Ar0038", "Ar0025"], "Crb0005", True)
# Affectation d'une projection vers Crb0016 pour les entités topologiques Ar0023 Ar0040
ctx.getTopoManager().setGeomAssociation (["Ar0023", "Ar0040"], "Crb0016", True)
# Affectation d'une projection vers Crb0015 pour les entités topologiques Ar0027 Ar0041
ctx.getTopoManager().setGeomAssociation (["Ar0027", "Ar0041"], "Crb0015", True)
# Affectation d'une projection vers Crb0019 pour les entités topologiques Ar0024
ctx.getTopoManager().setGeomAssociation (["Ar0024"], "Crb0019", True)
# Affectation d'une projection vers Crb0017 pour les entités topologiques Ar0020
ctx.getTopoManager().setGeomAssociation (["Ar0020"], "Crb0017", True)
# Affectation d'une projection vers Surf0006 pour les entités topologiques Ar0026
ctx.getTopoManager().setGeomAssociation (["Ar0026"], "Surf0006", True)
# Affectation d'une projection vers Surf0005 pour les entités topologiques Ar0022
ctx.getTopoManager().setGeomAssociation (["Ar0022"], "Surf0005", True)
# Affectation d'une projection vers Crb0018 pour les entités topologiques Ar0043
ctx.getTopoManager().setGeomAssociation (["Ar0043"], "Crb0018", True)
# Affectation d'une projection vers Surf0007 pour les entités topologiques Fa0010
ctx.getTopoManager().setGeomAssociation (["Fa0010"], "Surf0007", True)
# Affectation d'une projection vers Surf0004 pour les entités topologiques Fa0006
ctx.getTopoManager().setGeomAssociation (["Fa0006"], "Surf0004", True)
# Affectation d'une projection vers Surf0005 pour les entités topologiques Fa0016 Fa0028
ctx.getTopoManager().setGeomAssociation (["Fa0016", "Fa0028"], "Surf0005", True)
# Affectation d'une projection vers Surf0006 pour les entités topologiques Fa0017 Fa0029
ctx.getTopoManager().setGeomAssociation (["Fa0017", "Fa0029"], "Surf0006", True)
