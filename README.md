# gizmo_turb_box
Setup scripts/files for running MHD turbulent box simulations with GIZMO

# Walkthrough
## Compiling the code
Get the public version of GIZMO:
```bash
git clone https://bitbucket.org/gizmo_public
```

## Generating the initial condition
MakeBox.py is a simple script designed to generate GIZMO snapshot file for a uniform-density box with a uniform magnetic field, according to the specified box size, total enclosed gas mass, and magnetic field, in code units (for this repo we assume units of solar mass, pc, and μG respectively). So to generate a box 10pc in size, containing 1e4 solar mass in gas, with a 10μG initial field, resolved in 100,000 gas cells, you would run
```bash
python MakeBox.py --M=1e4 --L=10 --B=10 --N=100000
```
## Running the simulation

