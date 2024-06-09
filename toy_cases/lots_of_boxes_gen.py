for i in range(0, 6):
    for j in range(0, 6):
        for k in range(0, 6):
            ctx.getTopoManager().newBoxWithTopo (Mgx3D.Point(i, j, k), Mgx3D.Point(i+1, j+1, k+1), 10, 10, 10, "layer_"+str(i))


