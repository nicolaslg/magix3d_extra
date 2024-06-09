# -*- coding: utf-8 -*-


# Création du sommet Pt0000
ctx.getGeomManager().newVertex (Mgx3D.Point(0, 0, 0))
ctx.getGeomManager().newVertex (Mgx3D.Point(1, 0, 0))
ctx.getGeomManager().newVertex (Mgx3D.Point(1, 1, 0))
ctx.getGeomManager().newVertex (Mgx3D.Point(0, 1, 0))
ctx.getGeomManager().newVertex (Mgx3D.Point(1+1e-3, 0, 0))
ctx.getGeomManager().newVertex (Mgx3D.Point(1+1e-3, 1, 0))
ctx.getGeomManager().newVertex (Mgx3D.Point(1+2e-3, 0, 0))
ctx.getGeomManager().newVertex (Mgx3D.Point(1+2e-3, 1, 0))
ctx.getGeomManager().newVertex (Mgx3D.Point(2, 0, 0))
ctx.getGeomManager().newVertex (Mgx3D.Point(2, 1, 0))
# Création du segment Crb0000
ctx.getGeomManager().newSegment("Pt0000", "Pt0001")
ctx.getGeomManager().newSegment("Pt0001", "Pt0002")
ctx.getGeomManager().newSegment("Pt0002", "Pt0003")
ctx.getGeomManager().newSegment("Pt0003", "Pt0000")
ctx.getGeomManager().newSegment("Pt0001", "Pt0004")
ctx.getGeomManager().newSegment("Pt0004", "Pt0005")
ctx.getGeomManager().newSegment("Pt0005", "Pt0002")
ctx.getGeomManager().newSegment("Pt0004", "Pt0006")
ctx.getGeomManager().newSegment("Pt0006", "Pt0007")
ctx.getGeomManager().newSegment("Pt0007", "Pt0005")
ctx.getGeomManager().newSegment("Pt0006", "Pt0008")
ctx.getGeomManager().newSegment("Pt0008", "Pt0009")
ctx.getGeomManager().newSegment("Pt0009", "Pt0007")
# Création de la surface Surf0000
ctx.getGeomManager().newPlanarSurface( ["Crb0000", "Crb0001", "Crb0002", "Crb0003"] , "")
ctx.getGeomManager().newPlanarSurface( ["Crb0004", "Crb0005", "Crb0006", "Crb0001"] , "")
ctx.getGeomManager().newPlanarSurface( ["Crb0007", "Crb0008", "Crb0009", "Crb0005"] , "")
ctx.getGeomManager().newPlanarSurface( ["Crb0010", "Crb0011", "Crb0012", "Crb0008"] , "")

# Création d'une face topologique structurée sur une géométrie (Surf0000)
ctx.getTopoManager().newStructuredTopoOnGeometry ("Surf0000")
ctx.getTopoManager().newStructuredTopoOnGeometry ("Surf0003")
ctx.getTopoManager().newStructuredTopoOnGeometry ("Surf0001")
ctx.getTopoManager().newStructuredTopoOnGeometry ("Surf0002")

# Changement de discrétisation pour les arêtes Ar0008 Ar0011 Ar0010 Ar0012
emp = Mgx3D.EdgeMeshingPropertyUniform(1)
ctx.getTopoManager().setMeshingProperty (emp,["Ar0008", "Ar0011", "Ar0010", "Ar0012"])

# Changement de discrétisation pour les arêtes Ar0009
emp = Mgx3D.EdgeMeshingPropertyGeometric(10,1.5)
ctx.getTopoManager().setMeshingProperty (emp,["Ar0009"])

# Création du maillage pour toutes les faces
ctx.getMeshManager().newAllFacesMesh()
