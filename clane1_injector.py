import FreeCAD, Part, math

doc = FreeCAD.activeDocument()

# ── INJECTOR PLATE ───────────────────────────────
# Flat disc sitting at top of combustion chamber
r_injector   = 300.0   # same as chamber radius mm
thickness    = 25.0    # plate thickness mm
y_position   = 125.0   # sits at top of chamber

plate = Part.makeCylinder(
    r_injector, thickness,
    FreeCAD.Vector(0, y_position, 0),
    FreeCAD.Vector(0, 1, 0))

# ── DRILL 600 INJECTOR HOLES ─────────────────────
# Arranged in concentric rings
# LOX hole d=7.14mm, CH4 hole d=2.79mm
# Alternating LOX/CH4 across 3 rings

hole_positions = []
rings = [
    (60,  18),   # ring 1: radius 60mm,  18 elements
    (130, 54),   # ring 2: radius 130mm, 54 elements
    (210, 120),  # ring 3: radius 210mm, 120 elements
    (270, 180),  # ring 4: radius 270mm, 180 elements
    (290, 228),  # ring 5: radius 290mm, 228 elements
]

holes = []
for ring_r, count in rings:
    for i in range(count):
        angle = 2 * math.pi * i / count
        x = ring_r * math.cos(angle)
        z = ring_r * math.sin(angle)
        # alternate LOX and CH4 holes
        if i % 2 == 0:
            r_hole = 3.57   # LOX radius (d=7.14mm)
        else:
            r_hole = 1.395  # CH4 radius (d=2.79mm)
        hole = Part.makeCylinder(
            r_hole, thickness + 2,
            FreeCAD.Vector(x, y_position - 1, z),
            FreeCAD.Vector(0, 1, 0))
        holes.append(hole)

# Cut all holes from plate
print(f"Cutting {len(holes)} injector holes...")
for i, hole in enumerate(holes):
    plate = plate.cut(hole)
    if i % 100 == 0:
        print(f"  {i}/{len(holes)} done...")

obj = doc.addObject("Part::Feature", "Injector_Plate")
obj.Shape = plate
doc.recompute()

print("Injector plate complete!")
print(f"Total holes: {sum(c for _,c in rings)}")
print("LOX orifice: 7.14mm | CH4 orifice: 2.79mm")