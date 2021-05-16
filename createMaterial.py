def createTexture():
    obj = hou.node("/obj")
    matnet = obj.createNode("matnet","matnet",exact_type_name = matnet)
    matnode = matnet.createNode("redshift_vopnet","wood_mat",exact_type_name=1)
    #childen = matnode.childen()
    #childen.destroy()

    txBasecolor = matnode.createNode("redshift::TextureSampler","tx_basecolor")    
    txcolorcorrect =matnode.createNode("redshift::RSColorCorrection","colorCorrection")
    material = matnode.createNode("redshift::Material","Material1")
    shader = matnode.createNode("redshift_material","redshift_material1")
    shader.setInput(0,material,0)
    material.setInput(1,txBasecolor,0)
    #nodename = node.name()
    
