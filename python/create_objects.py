print("+++++++++++++++++instantiate inertia objects++++++++++++++++++++++++")

import FreeCAD as f
#for objects
import sys,os

scrDir=os.path.dirname(os.path.abspath(__file__))+os.sep

if scrDir not in sys.path:
	print(f"not in path -> {scrDir}, adding")
	print(sys.path)
	sys.path.append(scrDir)
elif scrDir in sys.path:
	print(f"in path -> {scrDir}")
else:
	print("??confusing path situation")

import cycleTester_objects as objs

doc=f.getDocument("inertia_cylinder_custom")

properties_sheet=doc.getObjectsByLabel("properties")[0]
fixedParameters_sheet=doc.getObjectsByLabel("fixedParameters")[0]
calculatedParameters_sheet=doc.getObjectsByLabel("calculatedParameters")[0]
inertia_sheet=doc.getObjectsByLabel("inertia")[0]

#setup objects
#contact drum
setup_objects={
	"tube":{},
	"cylinder":{},
	"cuboid":{}
}
aliases={
	"tube":["radiusInner","radiusOuter","length","density"],
	"cylinder":["radius","height","density"],
	"cuboid":["length","width","height","density"]
	}
types={
	"tube":["contactDrum","disk","flywheel","hub","extendingDrum"],
	"cylinder":["threadedShaft"],
	"cuboid":["wp_ed_key1","wp_ed_key2"]
	}
for objType in types:
	for objI in range(0,len(types[objType])):
		objInstance=getattr(objs,objType)
		args=[]
		for prop in aliases[objType]:
			print(objType, objI,types[objType][objI], prop, types[objType][objI]+"_"+prop)
			args.append( objs.get_obj( calculatedParameters_sheet , types[objType][objI]+"_"+prop ) )
		setup_objects[objType][types[objType][objI]]=	objInstance(*args)

# set moi in spreadsheet
for objType in setup_objects:
	print(objType)
	for objects in setup_objects[objType]:
		print(objects)
		moi=setup_objects[objType][objects].momentOfInertia

		alias_targetCell='moi_'+objects
		alias_radiusInner=f"<<calculatedParameters>>.{objects}.radiusInner"
		alias_radiusOuter=f"<<calculatedParameters>>.{objects}.radiusOuter"
		alias_mass=f"<<calculatedParameters>>.{objects}_mass"
		expression=f'={alias_radiusOuter}*{alias_radiusOuter}*{alias_mass}*0.5 - {alias_radiusInner}*{alias_radiusInner}*{alias_mass}*0.5'
		print(expression)
		inertia_sheet.setExpression("C2",expression)
