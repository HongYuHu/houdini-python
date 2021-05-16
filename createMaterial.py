def createTexture():
    mat = hou.node("/mat")
    matnode = mat.createNode("redshift_vopnet","wood_mat")
    txBasecolor = matnode.createNode("redshift::TextureSampler","tx_basecolor")
    txcolorcorrect =matnode.createNode("redshift::RSColorCorrection","colorCorrection")
    material = matnode.createNode("redshift::Material","Material")
    material.setInput(1,txBasecolor,0)
    #nodename = node.name()
    