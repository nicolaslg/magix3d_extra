In this tutorial we will be creating the blocking and associate it to an imported geometruc model.


The geom model, in a STEP file format, can be found here ![Geom Model](B0.step). Choose a length unit before importing (session->unit length).
The full script is located here ![whole script](b0.py).

This is the geom model 

![2D geom Image](geom.png)

Create a free structured block associated to the volume (topo->block->create). A not free block cannot be created because the shape is too complex for magix3d to automatically associate the topo entities to the geometry. By choosing the volume the block initial position will be the bounding box of the volume.

![2D topo Image](block.png)

Change the discretization of the edges (default is 10x10x10)

![2D topo Image](discretize.png)

Associate the entites of the blocking to the geom model. Not all of them can be associated. You can associate the entities one by one or use "topo->vert/edge/face->assoc" and choose method "Vertices to geom entities". The same goes for the edges.

![split ogrid Image](assoc2.png)

Do not forget to also do it for the faces

![split ogrid Image](assoc.png)

Split the block, here at 0.9

![split ogrid Image](split_r.png)

Proceed one the other side at 0.1

![split ogrid Image](split_l.png)

And at the top, this time split all the blocks at 0.8

![split ogrid Image](split_t.png)

Apply an ogrid pattern to the central block. Ensure that it imprints itself onto three of the faces,as shown here in the preview.

![split ogrid Image](ogrid_preview.png)

Once applied, this is what the blocking looks like, for both the blocks and then edges

![split ogrid Image](ogrid_blocks.png) ![split ogrid Image](ogrid_edges.png)

Destroy the central bottom block.

![split ogrid Image](destroy.png)

And split the blocks at the top. It is necessary because at the moment we can assign an edge only to one single geometric entity, and the half circle at the bottom is composed of two curves.

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
