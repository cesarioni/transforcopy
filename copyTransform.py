import maya.cmds

ref_obj = cmds.ls( selection=True )
print len(ref_obj)
ref_trans = []
ref_rot = []
for x in ref_obj:
    parentTranslation = cmds.getAttr (x+'.translate')
    parentRotation = maya.cmds.xform( x, q=True, ws=True, ro=True )
    ref_trans.append(parentTranslation)
    ref_rot.append(parentRotation)
   

TransXoffset = 0
TransYoffset = 0
TransZoffset = 0
RotXoffset = 0
RotYoffset = 0
RotZoffset = 0    
target_obj = cmds.ls( selection=True )
i=0
for x in target_obj:
    cmds.setAttr (x+'.translateX', ref_trans[i][0][0])
    cmds.setAttr (x+'.translateY', ref_trans[i][0][1])
    cmds.setAttr (x+'.translateZ', ref_trans[i][0][2])
   
    cmds.setAttr (x+'.rotateX',ref_rot[i][0])
    cmds.setAttr (x+'.rotateY',ref_rot[i][1])
    cmds.setAttr (x+'.rotateZ',ref_rot[i][2])
    cmds.rotate( RotXoffset, RotYoffset, RotZoffset, x, relative=True, objectSpace=True )
    cmds.move( TransXoffset, TransYoffset, TransZoffset, x, relative=True, objectSpace=True )
    i+=1

lights = cmds.ls( selection=True )
for x in lights:
    cmds.setAttr (x+'.useFarAttenuation', 1)
    cmds.setAttr (x+'.farAttenuationEnd', 70)
   
lights = cmds.ls( selection=True )
for x in lights:
    cmds.setAttr (x+'.shadowRays', 1)