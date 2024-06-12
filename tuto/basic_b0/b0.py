# -*- coding: utf-8 -*-

import sys

import pyMagix3D as Mgx3D
ctx = Mgx3D.getStdContext()

# Changement d'unité de longueur
ctx.setLengthUnit(Mgx3D.Unit.centimeter)
# Import STEP
ctx.getGeomManager().importSTEP("magix3d_extra/tuto/basic_b0/B0.step")
# Création d'un bloc topologique structuré sans projection (Vol0000)
ctx.getTopoManager().newFreeTopoOnGeometry ("Vol0000")
# Changement de discrétisation pour Ar0000
emp = Mgx3D.EdgeMeshingPropertyUniform(30)
ctx.getTopoManager().setParallelMeshingProperty (emp,"Ar0000")
# Changement de discrétisation pour Ar0011
emp = Mgx3D.EdgeMeshingPropertyUniform(20)
ctx.getTopoManager().setParallelMeshingProperty (emp,"Ar0011")
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
# Affectation d'une projection vers Crb0020 pour les entités topologiques Ar0005
ctx.getTopoManager().setGeomAssociation (["Ar0005"], "Crb0020", True)
# Affectation d'une projection vers Crb0002 pour les entités topologiques Ar0004
ctx.getTopoManager().setGeomAssociation (["Ar0004"], "Crb0002", True)
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
# Découpage du bloc Bl0000
ctx.getTopoManager().splitBlock ("Bl0000","Ar0002",.9)
# Découpage du bloc Bl0001
ctx.getTopoManager().splitBlock ("Bl0001","Ar0012",.1)
# Découpage de tous les blocs suivant l'arête Ar0009
ctx.getTopoManager().splitAllBlocks ("Ar0009",.8)
# Découpage en O-grid des blocs structurés Bl0008
ctx.getTopoManager().splitBlocksWithOgridV2 (["Bl0008"], ["Fa0034", "Fa0020", "Fa0035"], .5, 10)
# Destruction des entités topologiques Bl0014
ctx.getTopoManager().destroy (["Bl0014"], True)
# Découpage de tous les blocs suivant l'arête Ar0025
ctx.getTopoManager().splitAllBlocks ("Ar0025",.5)
# Affectation d'une projection vers Pt0006 pour les entités topologiques Som0024
ctx.getTopoManager().setGeomAssociation (["Som0024"], "Pt0006", True)
# Affectation d'une projection vers Pt0012 pour les entités topologiques Som0025
ctx.getTopoManager().setGeomAssociation (["Som0025"], "Pt0012", True)
# Affectation d'une projection vers Pt0010 pour les entités topologiques Som0027
ctx.getTopoManager().setGeomAssociation (["Som0027"], "Pt0010", True)
# Affectation d'une projection vers Pt0004 pour les entités topologiques Som0026
ctx.getTopoManager().setGeomAssociation (["Som0026"], "Pt0004", True)
# Affectation d'une projection vers Pt0005 pour les entités topologiques Som0037
ctx.getTopoManager().setGeomAssociation (["Som0037"], "Pt0005", True)
# Affectation d'une projection vers Pt0013 pour les entités topologiques Som0036
ctx.getTopoManager().setGeomAssociation (["Som0036"], "Pt0013", True)
# Affectation d'une projection vers Crb0005 pour les entités topologiques Som0028
ctx.getTopoManager().setGeomAssociation (["Som0028"], "Crb0005", True)
# Affectation d'une projection vers Crb0004 pour les entités topologiques Som0030
ctx.getTopoManager().setGeomAssociation (["Som0030"], "Crb0004", True)
# Affectation d'une projection vers Crb0016 pour les entités topologiques Som0031
ctx.getTopoManager().setGeomAssociation (["Som0031"], "Crb0016", True)
# Affectation d'une projection vers Crb0015 pour les entités topologiques Som0029
ctx.getTopoManager().setGeomAssociation (["Som0029"], "Crb0015", True)
# Affectation d'une projection vers Crb0017 pour les entités topologiques Ar0076
ctx.getTopoManager().setGeomAssociation (["Ar0076"], "Crb0017", True)
# Affectation d'une projection vers Crb0019 pour les entités topologiques Ar0071
ctx.getTopoManager().setGeomAssociation (["Ar0071"], "Crb0019", True)
# Affectation d'une projection vers Crb0004 pour les entités topologiques Ar0075 Ar0098
ctx.getTopoManager().setGeomAssociation (["Ar0075", "Ar0098"], "Crb0004", True)
# Affectation d'une projection vers Crb0005 pour les entités topologiques Ar0097 Ar0070
ctx.getTopoManager().setGeomAssociation (["Ar0097", "Ar0070"], "Crb0005", True)
# Affectation d'une projection vers Crb0015 pour les entités topologiques Ar0072 Ar0094
ctx.getTopoManager().setGeomAssociation (["Ar0072", "Ar0094"], "Crb0015", True)
# Affectation d'une projection vers Crb0016 pour les entités topologiques Ar0095 Ar0077
ctx.getTopoManager().setGeomAssociation (["Ar0095", "Ar0077"], "Crb0016", True)
# Affectation d'une projection vers Crb0014 pour les entités topologiques Som0010 Ar0018 Ar0063
ctx.getTopoManager().setGeomAssociation (["Som0010", "Ar0018", "Ar0063"], "Crb0014", True)
# Affectation d'une projection vers Crb0012 pour les entités topologiques Som0014 Ar0065 Ar0029
ctx.getTopoManager().setGeomAssociation (["Som0014", "Ar0065", "Ar0029"], "Crb0012", True)
# Affectation d'une projection vers Crb0009 pour les entités topologiques Som0013 Ar0026 Ar0064
ctx.getTopoManager().setGeomAssociation (["Som0013", "Ar0026", "Ar0064"], "Crb0009", True)
# Affectation d'une projection vers Crb0006 pour les entités topologiques Som0009 Ar0062 Ar0015
ctx.getTopoManager().setGeomAssociation (["Som0009", "Ar0062", "Ar0015"], "Crb0006", True)
# Affectation d'une projection vers Surf0004 pour les entités topologiques Ar0034 Fa0019 Fa0053
ctx.getTopoManager().setGeomAssociation (["Ar0034", "Fa0019", "Fa0053"], "Surf0004", True)
# Affectation d'une projection vers Surf0007 pour les entités topologiques Ar0022 Fa0048 Fa0011
ctx.getTopoManager().setGeomAssociation (["Ar0022", "Fa0048", "Fa0011"], "Surf0007", True)
# Affectation d'une projection vers Surf0005 pour les entités topologiques Ar0074 Fa0058 Fa0076
ctx.getTopoManager().setGeomAssociation (["Ar0074", "Fa0058", "Fa0076"], "Surf0005", True)
# Affectation d'une projection vers Surf0006 pour les entités topologiques Ar0073 Fa0077 Fa0057
ctx.getTopoManager().setGeomAssociation (["Ar0073", "Fa0077", "Fa0057"], "Surf0006", True)
