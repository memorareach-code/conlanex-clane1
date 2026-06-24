import FreeCAD, Part

doc = FreeCAD.newDocument("Clane1_Chamber")

r_chamber = 300.0
r_throat  = 106.0
r_exit    = 629.0
L_chamber = 125.0
L_conv    = 80.0
L_div     = 400.0

pts = [
    FreeCAD.Vector(0,         0,                              0),
    FreeCAD.Vector(r_chamber, 0,                              0),
    FreeCAD.Vector(r_chamber, -L_chamber,                     0),
    FreeCAD.Vector(r_throat,  -L_chamber - L_conv,            0),
    FreeCAD.Vector(r_exit,    -L_chamber - L_conv - L_div,    0),
    FreeCAD.Vector(0,         -L_chamber - L_conv - L_div,    0),
]

edges = []
for i in range(len(pts) - 1):
    edges.append(Part.makeLine(pts[i], pts[i+1]))
edges.append(Part.makeLine(pts[-1], pts[0]))

wire  = Part.Wire(edges)
face  = Part.Face(wire)
solid = face.revolve(FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,1,0), 360)

obj = doc.addObject("Part::Feature", "Clane1_Nozzle")
obj.Shape = solid
doc.recompute()

print("Clane 1 nozzle created!")