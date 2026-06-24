import FreeCAD, Part

doc = FreeCAD.activeDocument()

# ── DIMENSIONS (mm) ──────────────────────────────
r_chamber = 300.0
r_throat  = 106.0
r_exit    = 629.0
L_chamber = 125.0
L_conv    = 80.0
L_div     = 400.0

# ── PREBURNER DIMENSIONS ─────────────────────────
r_pb      = 80.0    # preburner radius
L_pb      = 120.0   # preburner length
pb_offset = 280.0   # distance from centerline

# ── TURBOPUMP DIMENSIONS ─────────────────────────
r_tp      = 120.0   # turbopump housing radius
L_tp      = 300.0   # turbopump housing length
tp_offset = 500.0   # offset from centerline

# ── HELPER: make a cylinder solid ────────────────
def make_cylinder(radius, length, position, label):
    cyl = Part.makeCylinder(radius, length,
          FreeCAD.Vector(*position),
          FreeCAD.Vector(0, 1, 0))
    obj = doc.addObject("Part::Feature", label)
    obj.Shape = cyl
    return obj

# ── FUEL-RICH PREBURNER (FRP) ────────────────────
make_cylinder(r_pb, L_pb,
    (-pb_offset, 50, 0),
    "FRP_Preburner")

# ── OXIDISER-RICH PREBURNER (ORP) ───────────────
make_cylinder(r_pb, L_pb,
    (pb_offset, 50, 0),
    "ORP_Preburner")

# ── LOX TURBOPUMP ────────────────────────────────
make_cylinder(r_tp, L_tp,
    (-tp_offset, 100, 0),
    "LOX_Turbopump")

# ── CH4 TURBOPUMP ────────────────────────────────
make_cylinder(r_tp, L_tp,
    (tp_offset, 100, 0),
    "CH4_Turbopump")

# ── FEED LINES (simplified as thin cylinders) ───
def make_pipe(r, length, pos, axis, label):
    pipe = Part.makeCylinder(r, length,
           FreeCAD.Vector(*pos),
           FreeCAD.Vector(*axis))
    obj = doc.addObject("Part::Feature", label)
    obj.Shape = pipe
    return obj

# LOX feed line from LOX turbopump to ORP
make_pipe(18, 480, (-tp_offset+120, 250, 0), (1,0,0), "LOX_Feed_Line")

# CH4 feed line from CH4 turbopump to FRP
make_pipe(14, 480, (-pb_offset+80, 250, 0),  (1,0,0), "CH4_Feed_Line")

# ORP to chamber hot gas line
make_pipe(20, 120, (pb_offset, -10, 0),  (0,-1,0), "ORP_to_Chamber")

# FRP to chamber hot gas line
make_pipe(20, 120, (-pb_offset, -10, 0), (0,-1,0), "FRP_to_Chamber")

doc.recompute()
print("Clane 1 — Full engine assembly added!")
print("Components: FRP, ORP preburners + LOX/CH4 turbopumps + feed lines")