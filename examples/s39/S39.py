# -*- coding: utf-8 -*-

import sys

import pyMagix3D as Mgx3D
ctx = Mgx3D.getStdContext()

# Changement d'unité de longueur
ctx.setLengthUnit(Mgx3D.Unit.centimeter)
# Import STEP
ctx.getGeomManager().importSTEP("S39.step")
# Création d'un bloc topologique structuré sans projection (Vol0000)
ctx.getTopoManager().newFreeTopoOnGeometry ("Vol0000")
# Affectation d'une projection vers Pt0026 pour les entités topologiques Som0001
ctx.getTopoManager().setGeomAssociation (["Som0001"], "Pt0026", True)
# Affectation d'une projection vers Pt0018 pour les entités topologiques Som0005
ctx.getTopoManager().setGeomAssociation (["Som0005"], "Pt0018", True)
# Affectation d'une projection vers Pt0029 pour les entités topologiques Som0002
ctx.getTopoManager().setGeomAssociation (["Som0002"], "Pt0029", True)
# Affectation d'une projection vers Pt0027 pour les entités topologiques Som0000
ctx.getTopoManager().setGeomAssociation (["Som0000"], "Pt0027", True)
# Affectation d'une projection vers Pt0019 pour les entités topologiques Som0004
ctx.getTopoManager().setGeomAssociation (["Som0004"], "Pt0019", True)
# Découpage de tous les blocs suivant l'arête Ar0007
ctx.getTopoManager().splitAllBlocks ("Ar0007",.3)
# Affectation d'une projection vers Pt0022 pour les entités topologiques Som0010
ctx.getTopoManager().setGeomAssociation (["Som0010"], "Pt0022", True)
# Affectation d'une projection vers Pt0024 pour les entités topologiques Som0011
ctx.getTopoManager().setGeomAssociation (["Som0011"], "Pt0024", True)
# Affectation d'une projection vers Crb0025 pour les entités topologiques Ar0002
ctx.getTopoManager().setGeomAssociation (["Ar0002"], "Crb0025", True)
# Affectation d'une projection vers Crb0038 pour les entités topologiques Ar0000
ctx.getTopoManager().setGeomAssociation (["Ar0000"], "Crb0038", True)
# Découpage de tous les blocs suivant l'arête Ar0009
ctx.getTopoManager().splitAllBlocks ("Ar0009",.8)
# Découpage de tous les blocs suivant l'arête Ar0003
ctx.getTopoManager().splitAllBlocks ("Ar0003",.5)
# Affectation d'une projection vers Pt0028 pour les entités topologiques Som0017
ctx.getTopoManager().setGeomAssociation (["Som0017"], "Pt0028", True)
# Affectation d'une projection vers Pt0021 pour les entités topologiques Som0006
ctx.getTopoManager().setGeomAssociation (["Som0006"], "Pt0021", True)
# Affectation d'une projection vers Pt0020 pour les entités topologiques Som0018
ctx.getTopoManager().setGeomAssociation (["Som0018"], "Pt0020", True)
# Affectation d'une projection vers Pt0030 pour les entités topologiques Som0021
ctx.getTopoManager().setGeomAssociation (["Som0021"], "Pt0030", True)
# Affectation d'une projection vers Pt0023 pour les entités topologiques Som0019
ctx.getTopoManager().setGeomAssociation (["Som0019"], "Pt0023", True)
# Affectation d'une projection vers Pt0016 pour les entités topologiques Som0013
ctx.getTopoManager().setGeomAssociation (["Som0013"], "Pt0016", True)
# Affectation d'une projection vers Pt0017 pour les entités topologiques Som0012
ctx.getTopoManager().setGeomAssociation (["Som0012"], "Pt0017", True)
# Affectation d'une projection vers Pt0031 pour les entités topologiques Som0026
ctx.getTopoManager().setGeomAssociation (["Som0026"], "Pt0031", True)
# Destruction des entités topologiques Bl0014 Bl0008
ctx.getTopoManager().destroy (["Bl0014", "Bl0008"], True)
# Affectation d'une projection vers Crb0028 pour les entités topologiques Som0009 Ar0015 Ar0014
ctx.getTopoManager().setGeomAssociation (["Som0009", "Ar0015", "Ar0014"], "Crb0028", True)
# Affectation d'une projection vers Crb0032 pour les entités topologiques Som0015 Ar0033 Ar0032
ctx.getTopoManager().setGeomAssociation (["Som0015", "Ar0033", "Ar0032"], "Crb0032", True)
# Affectation d'une projection vers Crb0036 pour les entités topologiques Ar0019
ctx.getTopoManager().setGeomAssociation (["Ar0019"], "Crb0036", True)
# Affectation d'une projection vers Crb0041 pour les entités topologiques Som0008 Ar0012 Ar0013
ctx.getTopoManager().setGeomAssociation (["Som0008", "Ar0012", "Ar0013"], "Crb0041", True)
# Affectation d'une projection vers Crb0020 pour les entités topologiques Som0023 Ar0058 Ar0059
ctx.getTopoManager().setGeomAssociation (["Som0023", "Ar0058", "Ar0059"], "Crb0020", True)
# Affectation d'une projection vers Crb0026 pour les entités topologiques Ar0027
ctx.getTopoManager().setGeomAssociation (["Ar0027"], "Crb0026", True)
# Affectation d'une projection vers Crb0029 pour les entités topologiques Ar0017
ctx.getTopoManager().setGeomAssociation (["Ar0017"], "Crb0029", True)
# Affectation d'une projection vers Crb0024 pour les entités topologiques Ar0025
ctx.getTopoManager().setGeomAssociation (["Ar0025"], "Crb0024", True)
# Affectation d'une projection vers Pt0025 pour les entités topologiques Som0025
ctx.getTopoManager().setGeomAssociation (["Som0025"], "Pt0025", True)
# Affectation d'une projection vers Crb0034 pour les entités topologiques Som0020 Ar0068 Ar0050
ctx.getTopoManager().setGeomAssociation (["Som0020", "Ar0068", "Ar0050"], "Crb0034", True)
# Affectation d'une projection vers Crb0040 pour les entités topologiques Ar0038
ctx.getTopoManager().setGeomAssociation (["Ar0038"], "Crb0040", True)
# Affectation d'une projection vers Crb0046 pour les entités topologiques Ar0072
ctx.getTopoManager().setGeomAssociation (["Ar0072"], "Crb0046", True)
# Affectation d'une projection vers Crb0044 pour les entités topologiques Ar0069
ctx.getTopoManager().setGeomAssociation (["Ar0069"], "Crb0044", True)
# Affectation d'une projection vers Crb0045 pour les entités topologiques Ar0071
ctx.getTopoManager().setGeomAssociation (["Ar0071"], "Crb0045", True)
# Affectation d'une projection vers Crb0042 pour les entités topologiques Ar0053
ctx.getTopoManager().setGeomAssociation (["Ar0053"], "Crb0042", True)
# Affectation d'une projection vers Crb0039 pour les entités topologiques Ar0039
ctx.getTopoManager().setGeomAssociation (["Ar0039"], "Crb0039", True)
# Affectation d'une projection vers Crb0030 pour les entités topologiques Ar0046
ctx.getTopoManager().setGeomAssociation (["Ar0046"], "Crb0030", True)
# Affectation d'une projection vers Crb0031 pour les entités topologiques Ar0047
ctx.getTopoManager().setGeomAssociation (["Ar0047"], "Crb0031", True)
# Affectation d'une projection vers Crb0033 pour les entités topologiques Ar0064
ctx.getTopoManager().setGeomAssociation (["Ar0064"], "Crb0033", True)
# Affectation d'une projection vers Crb0043 pour les entités topologiques Ar0052
ctx.getTopoManager().setGeomAssociation (["Ar0052"], "Crb0043", True)
# Affectation d'une projection vers Crb0027 pour les entités topologiques Ar0043
ctx.getTopoManager().setGeomAssociation (["Ar0043"], "Crb0027", True)
# Affectation d'une projection vers Surf0008 pour les entités topologiques Ar0057
ctx.getTopoManager().setGeomAssociation (["Ar0057"], "Surf0008", True)
# Affectation d'une projection vers Surf0008 pour les entités topologiques Ar0045
ctx.getTopoManager().setGeomAssociation (["Ar0045"], "Surf0008", True)
# Affectation d'une projection vers Surf0012 pour les entités topologiques Ar0030 Ar0031 Ar0041 Ar0029
ctx.getTopoManager().setGeomAssociation (["Ar0030", "Ar0031", "Ar0041", "Ar0029"], "Surf0012", True)
# Affectation d'une projection vers Surf0014 pour les entités topologiques Ar0066 Ar0065
ctx.getTopoManager().setGeomAssociation (["Ar0066", "Ar0065"], "Surf0014", True)
# Affectation d'une projection vers Surf0015 pour les entités topologiques Ar0054
ctx.getTopoManager().setGeomAssociation (["Ar0054"], "Surf0015", True)
# Découpage de tous les blocs suivant l'arête Ar0024
ctx.getTopoManager().splitAllBlocks ("Ar0024",.2)
# Affectation d'une projection vers Pt0012 pour les entités topologiques Som0027
ctx.getTopoManager().setGeomAssociation (["Som0027"], "Pt0012", True)
# Affectation d'une projection vers Pt0011 pour les entités topologiques Som0032
ctx.getTopoManager().setGeomAssociation (["Som0032"], "Pt0011", True)
# Affectation d'une projection vers Crb0035 pour les entités topologiques Ar0073
ctx.getTopoManager().setGeomAssociation (["Ar0073"], "Crb0035", True)
# Affectation d'une projection vers Crb0037 pour les entités topologiques Ar0087
ctx.getTopoManager().setGeomAssociation (["Ar0087"], "Crb0037", True)
# Affectation d'une projection vers Surf0016 pour les entités topologiques Ar0097
ctx.getTopoManager().setGeomAssociation (["Ar0097"], "Surf0016", True)
# Affectation d'une projection vers Surf0015 pour les entités topologiques Ar0098
ctx.getTopoManager().setGeomAssociation (["Ar0098"], "Surf0015", True)
# Affectation d'une projection vers Surf0012 pour les entités topologiques Ar0094
ctx.getTopoManager().setGeomAssociation (["Ar0094"], "Surf0012", True)
# Affectation d'une projection vers Crb0011 pour les entités topologiques Som0029 Ar0080 Ar0090
ctx.getTopoManager().setGeomAssociation (["Som0029", "Ar0080", "Ar0090"], "Crb0011", True)
# Affectation d'une projection vers Surf0009 pour les entités topologiques Ar0083 Ar0049
ctx.getTopoManager().setGeomAssociation (["Ar0083", "Ar0049"], "Surf0009", True)
# Affectation d'une projection vers Surf0007 pour les entités topologiques Ar0060
ctx.getTopoManager().setGeomAssociation (["Ar0060"], "Surf0007", True)
# Affectation d'une projection vers Surf0011 pour les entités topologiques Ar0079
ctx.getTopoManager().setGeomAssociation (["Ar0079"], "Surf0011", True)
# Découpage de tous les blocs suivant l'arête Ar0017
ctx.getTopoManager().splitAllBlocks ("Ar0017",.3)
# Destruction des entités topologiques Bl0032 Bl0026
ctx.getTopoManager().destroy (["Bl0032", "Bl0026"], True)
# Affectation d'une projection vers Pt0010 pour les entités topologiques Som0046
ctx.getTopoManager().setGeomAssociation (["Som0046"], "Pt0010", True)
# Affectation d'une projection vers Pt0014 pour les entités topologiques Som0039
ctx.getTopoManager().setGeomAssociation (["Som0039"], "Pt0014", True)
# Affectation d'une projection vers Pt0013 pour les entités topologiques Som0041
ctx.getTopoManager().setGeomAssociation (["Som0041"], "Pt0013", True)
# Affectation d'une projection vers Pt0015 pour les entités topologiques Som0036
ctx.getTopoManager().setGeomAssociation (["Som0036"], "Pt0015", True)
# Affectation d'une projection vers Crb0013 pour les entités topologiques Som0042 Ar0124 Ar0138
ctx.getTopoManager().setGeomAssociation (["Som0042", "Ar0124", "Ar0138"], "Crb0013", True)
# Affectation d'une projection vers Crb0016 pour les entités topologiques Som0038 Ar0109 Ar0117
ctx.getTopoManager().setGeomAssociation (["Som0038", "Ar0109", "Ar0117"], "Crb0016", True)
# Affectation d'une projection vers Crb0019 pour les entités topologiques Ar0102
ctx.getTopoManager().setGeomAssociation (["Ar0102"], "Crb0019", True)
# Affectation d'une projection vers Crb0018 pour les entités topologiques Ar0111
ctx.getTopoManager().setGeomAssociation (["Ar0111"], "Crb0018", True)
# Affectation d'une projection vers Crb0010 pour les entités topologiques Ar0136
ctx.getTopoManager().setGeomAssociation (["Ar0136"], "Crb0010", True)
# Affectation d'une projection vers Crb0014 pour les entités topologiques Ar0139
ctx.getTopoManager().setGeomAssociation (["Ar0139"], "Crb0014", True)
# Affectation d'une projection vers Crb0012 pour les entités topologiques Ar0118
ctx.getTopoManager().setGeomAssociation (["Ar0118"], "Crb0012", True)
# Affectation d'une projection vers Surf0012 pour les entités topologiques Ar0137 Ar0135
ctx.getTopoManager().setGeomAssociation (["Ar0137", "Ar0135"], "Surf0012", True)
# Affectation d'une projection vers Surf0014 pour les entités topologiques Ar0129 Ar0134
ctx.getTopoManager().setGeomAssociation (["Ar0129", "Ar0134"], "Surf0014", True)
# Affectation d'une projection vers Surf0012 pour les entités topologiques Ar0115
ctx.getTopoManager().setGeomAssociation (["Ar0115"], "Surf0012", True)
# Affectation d'une projection vers Surf0008 pour les entités topologiques Ar0106 Ar0116
ctx.getTopoManager().setGeomAssociation (["Ar0106", "Ar0116"], "Surf0008", True)
# Affectation d'une projection vers Crb0015 pour les entités topologiques Ar0120
ctx.getTopoManager().setGeomAssociation (["Ar0120"], "Crb0015", True)
# Affectation d'une projection vers Surf0010 pour les entités topologiques Ar0130 Ar0119 Ar0101 Ar0103
ctx.getTopoManager().setGeomAssociation (["Ar0130", "Ar0119", "Ar0101", "Ar0103"], "Surf0010", True)
# Affectation d'une projection vers Surf0004 pour les entités topologiques Ar0108
ctx.getTopoManager().setGeomAssociation (["Ar0108"], "Surf0004", True)
# Affectation d'une projection vers Surf0002 pour les entités topologiques Ar0122
ctx.getTopoManager().setGeomAssociation (["Ar0122"], "Surf0002", True)
# Affectation d'une projection vers Surf0003 pour les entités topologiques Ar0123
ctx.getTopoManager().setGeomAssociation (["Ar0123"], "Surf0003", True)
