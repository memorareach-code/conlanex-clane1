# conlanex-clane1
Clane 1 rocket engine — physics-derived FFSC LOX/CH4 engine design. ConlaneX
# Clane 1 — ConlaneX Rocket Engine

Full-flow staged combustion (FFSC) LOX/CH₄ rocket engine.
Physics-derived design from first principles.

## Target Specifications
| Parameter | Value |
|---|---|
| Thrust (vacuum) | 2,500 kN |
| Isp (vacuum) | 363 s |
| Chamber pressure | 350 bar |
| Propellants | LOX / CH₄ |
| Cycle | Full-Flow Staged Combustion |
| TWR | 227:1 |
| Injector elements | 600 |

## Files
- `clane1.py` — 1D performance model (mass flow, nozzle sizing, pump power)
- `clane1_full.py` — Full engine assembly (preburners, turbopumps, feed lines)
- `clane1_injector.py` — Injector plate with 600 coaxial elements

## Status
- [x] Physics model complete
- [x] 3D CAD assembly (FreeCAD)
- [x] CFD simulation running (SimScale)
- [ ] FEA structural analysis
- [ ] R&D document
- [ ] Sub-scale test

## About ConlaneX
Building the machines that leave Earth.
