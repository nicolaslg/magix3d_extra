# -*- coding: utf-8 -*-

import sys

import pyMagix3D as Mgx3D
ctx = Mgx3D.getStdContext()

# Changement d'unité de longueur
ctx.setLengthUnit(Mgx3D.Unit.centimeter)
# Import STEP
ctx.getGeomManager().importSTEP("magix3d_extra/examples/s45/S45.step")
# Création d'un bloc unitaire mis dans le groupe box
ctx.getTopoManager().newFreeTopoInGroup ("box", 3)
# Affectation d'une projection vers Pt0021 pour les entités topologiques Som0005
ctx.getTopoManager().setGeomAssociation (["Som0005"], "Pt0021", True)
# Affectation d'une projection vers Pt0029 pour les entités topologiques Som0001
ctx.getTopoManager().setGeomAssociation (["Som0001"], "Pt0029", True)
# Affectation d'une projection vers Pt0018 pour les entités topologiques Som0004
ctx.getTopoManager().setGeomAssociation (["Som0004"], "Pt0018", True)
# Affectation d'une projection vers Pt0017 pour les entités topologiques Som0000
ctx.getTopoManager().setGeomAssociation (["Som0000"], "Pt0017", True)
# Affectation d'une projection vers Pt0022 pour les entités topologiques Som0007
ctx.getTopoManager().setGeomAssociation (["Som0007"], "Pt0022", True)
# Affectation d'une projection vers Pt0019 pour les entités topologiques Som0006
ctx.getTopoManager().setGeomAssociation (["Som0006"], "Pt0019", True)
# Affectation d'une projection vers Pt0030 pour les entités topologiques Som0003
ctx.getTopoManager().setGeomAssociation (["Som0003"], "Pt0030", True)
# Affectation d'une projection vers Pt0016 pour les entités topologiques Som0002
ctx.getTopoManager().setGeomAssociation (["Som0002"], "Pt0016", True)
# Affectation d'une projection vers Crb0021 pour les entités topologiques Ar0002
ctx.getTopoManager().setGeomAssociation (["Ar0002"], "Crb0021", True)
# Affectation d'une projection vers Crb0022 pour les entités topologiques Ar0007
ctx.getTopoManager().setGeomAssociation (["Ar0007"], "Crb0022", True)
# Affectation d'une projection vers Crb0018 pour les entités topologiques Ar0006
ctx.getTopoManager().setGeomAssociation (["Ar0006"], "Crb0018", True)
# Affectation d'une projection vers Crb0043 pour les entités topologiques Ar0000
ctx.getTopoManager().setGeomAssociation (["Ar0000"], "Crb0043", True)
# Affectation d'une projection vers Crb0040 pour les entités topologiques Ar0009
ctx.getTopoManager().setGeomAssociation (["Ar0009"], "Crb0040", True)
# Affectation d'une projection vers Crb0017 pour les entités topologiques Ar0008
ctx.getTopoManager().setGeomAssociation (["Ar0008"], "Crb0017", True)
# Affectation d'une projection vers Surf0014 pour les entités topologiques Fa0002
ctx.getTopoManager().setGeomAssociation (["Fa0002"], "Surf0014", True)
# Affectation d'une projection vers Surf0013 pour les entités topologiques Fa0004
ctx.getTopoManager().setGeomAssociation (["Fa0004"], "Surf0013", True)
# Affectation d'une projection vers Surf0012 pour les entités topologiques Fa0001
ctx.getTopoManager().setGeomAssociation (["Fa0001"], "Surf0012", True)
# Affectation d'une projection vers Surf0003 pour les entités topologiques Fa0005
ctx.getTopoManager().setGeomAssociation (["Fa0005"], "Surf0003", True)
# Affectation d'une projection vers Surf0002 pour les entités topologiques Fa0000
ctx.getTopoManager().setGeomAssociation (["Fa0000"], "Surf0002", True)
# Découpage du bloc Bl0000
ctx.getTopoManager().splitBlock ("Bl0000","Ar0008",.3)
# Affectation d'une projection vers Pt0020 pour les entités topologiques Som0009
ctx.getTopoManager().setGeomAssociation (["Som0009"], "Pt0020", True)
# Affectation d'une projection vers Pt0028 pour les entités topologiques Som0010
ctx.getTopoManager().setGeomAssociation (["Som0010"], "Pt0028", True)
# Affectation d'une projection vers Crb0042 pour les entités topologiques Ar0017
ctx.getTopoManager().setGeomAssociation (["Ar0017"], "Crb0042", True)
# Affectation d'une projection vers Crb0020 pour les entités topologiques Ar0014
ctx.getTopoManager().setGeomAssociation (["Ar0014"], "Crb0020", True)
# Affectation d'une projection vers Crb0038 pour les entités topologiques Ar0023
ctx.getTopoManager().setGeomAssociation (["Ar0023"], "Crb0038", True)
# Affectation d'une projection vers Surf0015 pour les entités topologiques Fa0012
ctx.getTopoManager().setGeomAssociation (["Fa0012"], "Surf0015", True)
# Création d'un bloc unitaire mis dans le groupe middle
ctx.getTopoManager().newFreeTopoInGroup ("middle", 3)
# Changement de discrétisation pour Ar0033
emp = Mgx3D.EdgeMeshingPropertyUniform(7)
ctx.getTopoManager().setParallelMeshingProperty (emp,"Ar0033")
# Fusion entre les 2 sommets Som0010 et Som0013
ctx.getTopoManager().fuse2Vertices ("Som0010","Som0013")
# Fusion entre les 2 sommets Som0007 et Som0017
ctx.getTopoManager().fuse2Vertices ("Som0007","Som0017")
# Fusion entre les 2 sommets Som0009 et Som0012
ctx.getTopoManager().fuse2Vertices ("Som0009","Som0012")
# Fusion entre les 2 sommets Som0006 et Som0016
ctx.getTopoManager().fuse2Vertices ("Som0006","Som0016")
# Affectation d'une projection vers Pt0025 pour les entités topologiques Som0014
ctx.getTopoManager().setGeomAssociation (["Som0014"], "Pt0025", True)
# Affectation d'une projection vers Pt0026 pour les entités topologiques Som0018
ctx.getTopoManager().setGeomAssociation (["Som0018"], "Pt0026", True)
# Affectation d'une projection vers Pt0013 pour les entités topologiques Som0015
ctx.getTopoManager().setGeomAssociation (["Som0015"], "Pt0013", True)
# Affectation d'une projection vers Pt0012 pour les entités topologiques Som0019
ctx.getTopoManager().setGeomAssociation (["Som0019"], "Pt0012", True)
# Affectation d'une projection vers Crb0037 pour les entités topologiques Ar0029
ctx.getTopoManager().setGeomAssociation (["Ar0029"], "Crb0037", True)
# Affectation d'une projection vers Crb0034 pour les entités topologiques Ar0031
ctx.getTopoManager().setGeomAssociation (["Ar0031"], "Crb0034", True)
# Affectation d'une projection vers Crb0035 pour les entités topologiques Ar0030
ctx.getTopoManager().setGeomAssociation (["Ar0030"], "Crb0035", True)
# Affectation d'une projection vers Crb0036 pour les entités topologiques Ar0028
ctx.getTopoManager().setGeomAssociation (["Ar0028"], "Crb0036", True)
# Affectation d'une projection vers Surf0010 pour les entités topologiques Fa0019
ctx.getTopoManager().setGeomAssociation (["Fa0019"], "Surf0010", True)
# Affectation d'une projection vers Surf0008 pour les entités topologiques Fa0020
ctx.getTopoManager().setGeomAssociation (["Fa0020"], "Surf0008", True)
# Affectation d'une projection vers Surf0009 pour les entités topologiques Fa0015
ctx.getTopoManager().setGeomAssociation (["Fa0015"], "Surf0009", True)
# Affectation d'une projection vers Surf0011 pour les entités topologiques Fa0016
ctx.getTopoManager().setGeomAssociation (["Fa0016"], "Surf0011", True)
# Affectation d'une projection vers Crb0031 pour les entités topologiques Ar0027
ctx.getTopoManager().setGeomAssociation (["Ar0027"], "Crb0031", True)
# Affectation d'une projection vers Crb0029 pour les entités topologiques Ar0025
ctx.getTopoManager().setGeomAssociation (["Ar0025"], "Crb0029", True)
# Création d'un bloc unitaire mis dans le groupe top
ctx.getTopoManager().newFreeTopoInGroup ("top", 3)
# Modification de la position des sommets topologiques Som0024 en coordonnées cartésiennes
ctx.getTopoManager().setVertexLocation (["Som0024"], True, -1.55099427700043, True, 2.19584083557129, True, 6.87393856048584)
# Modification de la position des sommets topologiques Som0026 en coordonnées cartésiennes
ctx.getTopoManager().setVertexLocation (["Som0026"], True, -1.46092331409454, True, 5.0877251625061, True, 5.28282880783081)
# Modification de la position des sommets topologiques Som0025 en coordonnées cartésiennes
ctx.getTopoManager().setVertexLocation (["Som0025"], True, 1.50011718273163, True, 2.21543765068054, True, 6.90788125991821)
# Modification de la position des sommets topologiques Som0027 en coordonnées cartésiennes
ctx.getTopoManager().setVertexLocation (["Som0027"], True, 1.60463070869446, True, 5.03190088272095, True, 5.18613815307617)
# Affectation d'une projection vers Pt0011 pour les entités topologiques Som0021
ctx.getTopoManager().setGeomAssociation (["Som0021"], "Pt0011", True)
# Affectation d'une projection vers Pt0014 pour les entités topologiques Som0023
ctx.getTopoManager().setGeomAssociation (["Som0023"], "Pt0014", True)
# Modification de la position des sommets topologiques Som0022 en coordonnées cartésiennes
ctx.getTopoManager().setVertexLocation (["Som0022"], True, -1.70718777179718, True, 3.16019654273987, True, 1.94425141811371)
# Modification de la position des sommets topologiques Som0020 en coordonnées cartésiennes
ctx.getTopoManager().setVertexLocation (["Som0020"], True, -1.66096723079681, True, 2.81245470046997e-1, True, 3.55776190757751)
# Changement de discrétisation pour Ar0040
emp = Mgx3D.EdgeMeshingPropertyUniform(9)
ctx.getTopoManager().setParallelMeshingProperty (emp,"Ar0040")
# Découpage du bloc Bl0004
ctx.getTopoManager().splitBlock ("Bl0004","Ar0045",.5)
# Affectation d'une projection vers Pt0010 pour les entités topologiques Som0030
ctx.getTopoManager().setGeomAssociation (["Som0030"], "Pt0010", True)
# Affectation d'une projection vers Pt0008 pour les entités topologiques Som0029
ctx.getTopoManager().setGeomAssociation (["Som0029"], "Pt0008", True)
# Affectation d'une projection vers Pt0015 pour les entités topologiques Som0028
ctx.getTopoManager().setGeomAssociation (["Som0028"], "Pt0015", True)
# Affectation d'une projection vers Crb0014 pour les entités topologiques Som0031
ctx.getTopoManager().setGeomAssociation (["Som0031"], "Crb0014", True)
# Affectation d'une projection vers Surf0001 pour les entités topologiques Fa0026
ctx.getTopoManager().setGeomAssociation (["Fa0026"], "Surf0001", True)
# Affectation d'une projection vers Surf0001 pour les entités topologiques Fa0028
ctx.getTopoManager().setGeomAssociation (["Fa0028"], "Surf0001", True)
# Affectation d'une projection vers Surf0001 pour les entités topologiques Fa0030
ctx.getTopoManager().setGeomAssociation (["Fa0030"], "Surf0001", True)
# Affectation d'une projection vers Surf0001 pour les entités topologiques Fa0029
ctx.getTopoManager().setGeomAssociation (["Fa0029"], "Surf0001", True)
# Affectation d'une projection vers Surf0005 pour les entités topologiques Fa0027
ctx.getTopoManager().setGeomAssociation (["Fa0027"], "Surf0005", True)
# Affectation d'une projection vers Crb0010 pour les entités topologiques Ar0053
ctx.getTopoManager().setGeomAssociation (["Ar0053"], "Crb0010", True)
# Affectation d'une projection vers Crb0024 pour les entités topologiques Ar0036
ctx.getTopoManager().setGeomAssociation (["Ar0036"], "Crb0024", True)
# Affectation d'une projection vers Crb0024 pour les entités topologiques Ar0050
ctx.getTopoManager().setGeomAssociation (["Ar0050"], "Crb0024", True)
# Affectation d'une projection vers Crb0028 pour les entités topologiques Ar0037
ctx.getTopoManager().setGeomAssociation (["Ar0037"], "Crb0028", True)
# Affectation d'une projection vers Crb0028 pour les entités topologiques Ar0048
ctx.getTopoManager().setGeomAssociation (["Ar0048"], "Crb0028", True)
# Affectation d'une projection vers Crb0014 pour les entités topologiques Ar0049
ctx.getTopoManager().setGeomAssociation (["Ar0049"], "Crb0014", True)
# Affectation d'une projection vers Crb0014 pour les entités topologiques Ar0039
ctx.getTopoManager().setGeomAssociation (["Ar0039"], "Crb0014", True)
# Affectation d'une projection vers Crb0014 pour les entités topologiques Ar0055 Ar0056
ctx.getTopoManager().setGeomAssociation (["Ar0055", "Ar0056"], "Crb0014", True)
# Affectation d'une projection vers Crb0009 pour les entités topologiques Ar0054 Ar0038 Ar0051
ctx.getTopoManager().setGeomAssociation (["Ar0054", "Ar0038", "Ar0051"], "Crb0009", True)
# Affectation d'une projection vers Surf0004 pour les entités topologiques Fa0032 Fa0031
ctx.getTopoManager().setGeomAssociation (["Fa0032", "Fa0031"], "Surf0004", True)
# Affectation d'une projection vers Surf0007 pour les entités topologiques Fa0034 Fa0033
ctx.getTopoManager().setGeomAssociation (["Fa0034", "Fa0033"], "Surf0007", True)
# Découpage en O-grid des blocs structurés Bl0006 Bl0005
ctx.getTopoManager().splitBlocksWithOgridV2 (["Bl0006", "Bl0005"], ["Fa0032", "Fa0031", "Fa0033", "Fa0035", "Fa0034"], .5, 10)
# Affectation d'une projection vers Surf0006 pour les entités topologiques Fa0057 Fa0059 Fa0056
ctx.getTopoManager().setGeomAssociation (["Fa0057", "Fa0059", "Fa0056"], "Surf0006", True)
# Affectation d'une projection vers Surf0000 pour les entités topologiques Fa0063 Fa0064 Fa0062
ctx.getTopoManager().setGeomAssociation (["Fa0063", "Fa0064", "Fa0062"], "Surf0000", True)
# Destruction des entités topologiques Bl0010 Bl0014
ctx.getTopoManager().destroy (["Bl0010", "Bl0014"], True)
# Affectation d'une projection vers Surf0004 pour les entités topologiques Som0038 Ar0066 Som0037 Ar0065
ctx.getTopoManager().setGeomAssociation (["Som0038", "Ar0066", "Som0037", "Ar0065"], "Surf0004", True)
# Découpage de tous les blocs suivant l'arête Ar0040
ctx.getTopoManager().splitAllBlocks ("Ar0040",.9)
# Découpage de tous les blocs suivant l'arête Ar0092
ctx.getTopoManager().splitAllBlocks ("Ar0092",.1)
# Fusion entre les 2 sommets Som0014 et Som0044
ctx.getTopoManager().fuse2Vertices ("Som0014","Som0044")
# Fusion entre les 2 sommets Som0015 et Som0054
ctx.getTopoManager().fuse2Vertices ("Som0015","Som0054")
# Fusion entre les 2 sommets Som0018 et Som0056
ctx.getTopoManager().fuse2Vertices ("Som0018","Som0056")
# Fusion entre les 2 sommets Som0019 et Som0066
ctx.getTopoManager().fuse2Vertices ("Som0019","Som0066")
# Affectation d'une projection vers Crb0025 pour les entités topologiques Som0033 Som0032
ctx.getTopoManager().setGeomAssociation (["Som0033", "Som0032"], "Crb0025", True)
# Affectation d'une projection vers Crb0032 pour les entités topologiques Som0035 Som0034
ctx.getTopoManager().setGeomAssociation (["Som0035", "Som0034"], "Crb0032", True)
