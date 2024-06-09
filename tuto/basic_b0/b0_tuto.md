In this tutorial we will be creating the blocking and associate it to an imported geometruc model.


The geom model, in a STEP file format, can be found here ![Geom Model](B0.step). Choose a length unit before importing (session->unit length).
The full script is located here ![whole script](b0.py).

This is the geom model 

![2D geom Image](geom.png)

Create a free structured block. An associated block cannot be created because the shape is too complex for magix3d to automatically associate the topo entities to the geometry.

![2D topo Image](block.png)

Associate the entites of the blocking to the geom model. Not all of them can be associated.

![split ogrid Image](assoc2.png)

Do not forget to also do it for the faces

![split ogrid Image](assoc.png)

Apply an ogrid pattern to the block. Ensure that it imprints itself onto three of the faces,as shown here in the preview.

![split ogrid Image](ogrid_preview.png)

Once applied, this is what the blocking looks like, both faces and edges

![split ogrid Image](ogrid_faces.png) ![split ogrid Image](ogrid_edges.png)

Destroy the central bottom block.

![split ogrid Image](destroy.png)

And split the block at the top.

![split ogrid Image](split.png)

Associate the topo vertices to geom points.

![split ogrid Image](assoc_vert.png)

Associate the remaing vertices and topo edges to geom curves.

![split ogrid Image](assoc_edges.png)

Also associate the last edges to surfaces.

![split ogrid Image](assoc_edges_surf.png)

Finally do the same for the faces

![split ogrid Image](assoc_faces.png)

This is the resulting mesh.

![split ogrid Image](mesh.png)
