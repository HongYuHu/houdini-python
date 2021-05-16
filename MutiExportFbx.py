def exportObject():
    obj = hou.node("/obj")
    path = r"D:\python_houdini\export_pratice\export_pratice"
    path = path.replace("\\","/")
    children = obj.children()
    
    for node in children:
        nodename = node.name()
        finalpath = path + nodename + ".fbx"
        node.parm("sopoutput").set(finalpath)
        node.parm("execute").pressButton()
        