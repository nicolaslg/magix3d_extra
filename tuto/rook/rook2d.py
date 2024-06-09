# -*- coding: utf-8 -*-

import sys

import pyMagix3D as Mgx3D
ctx = Mgx3D.getStdContext()

# Création du sommet Pt0000
ctx.getGeomManager().newVertex (Mgx3D.Point(0, 0, 0))
# Création du sommet Pt0001
ctx.getGeomManager().newVertex (Mgx3D.Point(.5, 0, 0))
# Création du sommet Pt0002
ctx.getGeomManager().newVertex (Mgx3D.Point(.5, 2, 0))
# Création du sommet Pt0003
ctx.getGeomManager().newVertex (Mgx3D.Point(0, 2, 0))
# Création du segment Crb0000
ctx.getGeomManager().newSegment("Pt0000", "Pt0001")
# Création du segment Crb0001
ctx.getGeomManager().newSegment("Pt0001", "Pt0002")
# Création du segment Crb0002
ctx.getGeomManager().newSegment("Pt0002", "Pt0003")
# Création du segment Crb0003
ctx.getGeomManager().newSegment("Pt0003", "Pt0000")
# Création du sommet Pt0004
ctx.getGeomManager().newVertex (Mgx3D.Point(4, 0, 0))
# Création du sommet Pt0005
ctx.getGeomManager().newVertex (Mgx3D.Point(4, 1, 0))
# Création du segment Crb0004
ctx.getGeomManager().newSegment("Pt0001", "Pt0004")
# Création du segment Crb0005
ctx.getGeomManager().newSegment("Pt0004", "Pt0005")
# Création du segment Crb0006
ctx.getGeomManager().newSegment("Pt0005", "Pt0002")
# Création de la surface Surf0000
ctx.getGeomManager().newPlanarSurface( ["Crb0000", "Crb0001", "Crb0002", "Crb0003"] , "")
# Création de la surface Surf0001
ctx.getGeomManager().newPlanarSurface( ["Crb0004", "Crb0005", "Crb0006", "Crb0001"] , "")
# Création du sommet Pt0006
ctx.getGeomManager().newVertex (Mgx3D.Point(4.5, 0, 0))
# Création du sommet Pt0007
ctx.getGeomManager().newVertex (Mgx3D.Point(4.5, 1, 0))
# Création du segment Crb0007
ctx.getGeomManager().newSegment("Pt0004", "Pt0006")
# Création du segment Crb0008
ctx.getGeomManager().newSegment("Pt0006", "Pt0007")
# Création du segment Crb0009
ctx.getGeomManager().newSegment("Pt0007", "Pt0005")
# Création du sommet Pt0008
ctx.getGeomManager().newVertex (Mgx3D.Point(4.5, 1.5, 0))
# Création du sommet Pt0009
ctx.getGeomManager().newVertex (Mgx3D.Point(4, 1.5, 0))
# Création du segment Crb0010
ctx.getGeomManager().newSegment("Pt0007", "Pt0008")
# Création du segment Crb0011
ctx.getGeomManager().newSegment("Pt0008", "Pt0009")
# Création du segment Crb0012
ctx.getGeomManager().newSegment("Pt0009", "Pt0005")
# Création de la surface Surf0002
ctx.getGeomManager().newPlanarSurface( ["Crb0007", "Crb0008", "Crb0009", "Crb0005"] , "")
# Création de la surface Surf0003
ctx.getGeomManager().newPlanarSurface( ["Crb0009", "Crb0010", "Crb0011", "Crb0012"] , "")
# Création du sommet Pt0010
ctx.getGeomManager().newVertex (Mgx3D.Point(5.5, 1.5, 0))
# Création du sommet Pt0011
ctx.getGeomManager().newVertex (Mgx3D.Point(5.5, 2, 0))
# Création du sommet Pt0012
ctx.getGeomManager().newVertex (Mgx3D.Point(4, 2, 0))
# Création du segment Crb0013
ctx.getGeomManager().newSegment("Pt0008", "Pt0010")
# Création du segment Crb0014
ctx.getGeomManager().newSegment("Pt0010", "Pt0011")
# Création du segment Crb0015
ctx.getGeomManager().newSegment("Pt0011", "Pt0012")
# Création du segment Crb0016
ctx.getGeomManager().newSegment("Pt0012", "Pt0009")
# Création de la surface Surf0004
ctx.getGeomManager().newPlanarSurface( ["Crb0011", "Crb0013", "Crb0014", "Crb0015", "Crb0016"] , "")
# Création d'une face topologique structurée sur une géométrie (Surf0000)
ctx.getTopoManager().newStructuredTopoOnGeometry ("Surf0000")
# Création d'une face topologique structurée sur une géométrie (Surf0001)
ctx.getTopoManager().newStructuredTopoOnGeometry ("Surf0001")
# Création d'une face topologique structurée sur une géométrie (Surf0002)
ctx.getTopoManager().newStructuredTopoOnGeometry ("Surf0002")
# Création d'une face topologique structurée sur une géométrie (Surf0003)
ctx.getTopoManager().newStructuredTopoOnGeometry ("Surf0003")
# Création d'un bloc unitaire mis dans le groupe border
ctx.getTopoManager().newFreeTopoInGroup ("border", 2)
# Affectation d'une projection vers Pt0011 pour les entités topologiques Som0013
ctx.getTopoManager().setGeomAssociation (["Som0013"], "Pt0011", True)
# Affectation d'une projection vers Pt0010 pour les entités topologiques Som0010
ctx.getTopoManager().setGeomAssociation (["Som0010"], "Pt0010", True)
# Affectation d'une projection vers Pt0012 pour les entités topologiques Som0012
ctx.getTopoManager().setGeomAssociation (["Som0012"], "Pt0012", True)
# Affectation d'une projection vers Pt0009 pour les entités topologiques Som0011
ctx.getTopoManager().setGeomAssociation (["Som0011"], "Pt0009", True)
# Découpage de la face Fa0004
ctx.getTopoManager().splitFace ("Fa0004", "Ar0013", .7, True)
# Affectation d'une projection vers Pt0008 pour les entités topologiques Som0014
ctx.getTopoManager().setGeomAssociation (["Som0014"], "Pt0008", True)
# Affectation d'une projection vers Crb0014 pour les entités topologiques Ar0016
ctx.getTopoManager().setGeomAssociation (["Ar0016"], "Crb0014", True)
# Affectation d'une projection vers Crb0015 pour les entités topologiques Som0015
ctx.getTopoManager().setGeomAssociation (["Som0015"], "Crb0015", True)
# Affectation d'une projection vers Crb0015 pour les entités topologiques Ar0020 Ar0019
ctx.getTopoManager().setGeomAssociation (["Ar0020", "Ar0019"], "Crb0015", True)
# Affectation d'une projection vers Crb0016 pour les entités topologiques Ar0014
ctx.getTopoManager().setGeomAssociation (["Ar0014"], "Crb0016", True)
# Affectation d'une projection vers Crb0011 pour les entités topologiques Ar0018
ctx.getTopoManager().setGeomAssociation (["Ar0018"], "Crb0011", True)
# Modification de la position des sommets topologiques Som0015 en coordonnées cartésiennes
ctx.getTopoManager().setVertexLocation (["Som0015"], True, 4.5, True, 2, True, 0)
# Affectation d'une projection vers Surf0004 pour les entités topologiques Ar0021 Fa0006 Fa0005
ctx.getTopoManager().setGeomAssociation (["Ar0021", "Fa0006", "Fa0005"], "Surf0004", True)
# Changement de discrétisation pour Ar0019
emp = Mgx3D.EdgeMeshingPropertyUniform(10)
ctx.getTopoManager().setParallelMeshingProperty (emp,"Ar0019")
# Changement de discrétisation pour Ar0020
emp = Mgx3D.EdgeMeshingPropertyUniform(10)
ctx.getTopoManager().setParallelMeshingProperty (emp,"Ar0020")
# Fusion entre arêtes Ar0011 et Ar0018
ctx.getTopoManager().fuse2Edges ("Ar0011","Ar0018")
