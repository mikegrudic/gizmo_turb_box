# gizmo_turb_box
Setup scripts/files for running MHD turbulent box simulations with GIZMO

# Walkthrough
## Compiling the code
Get the public version of GIZMO and copy the example `Config.sh` included in this repo to the code directory:
```bash
git clone https://bitbucket.org/gizmo-public
cp Config.sh gizmo-public
```
Now compile the code (note that you may need to go into `Makefile.systype` and uncomment the machine you are using):
```bash
cd gizmo-public
make
```

## Generating the initial condition
MakeBox.py is a simple script designed to generate GIZMO snapshot file for a uniform-density box with a uniform magnetic field, according to the specified box size, total enclosed gas mass, and magnetic field, in code units (for this repo we assume units of solar mass, pc, and μG respectively). So to generate a box 10pc in size, containing 1e4 solar mass in gas, with a 10μG initial field, resolved in 100,000 gas cells, you would run
```bash
python MakeBox.py --M=1e4 --L=10 --B=10 --N=100000
```

## Running the simulation
You now have the `hdf5` initial condition file, the compiled `GIZMO` binary in the `gizmo-public` directory, and an example parameter file `params.txt` included with this repo. To run a simulation on a single core (suitable only for very small runs, <1e5 cells), you would do

```bash
./GIZMO params.txt 0
```

The simulation will start running and output files and snapshots to the `output` directory. For details on GIZMO's outputs and related analysis tools see the [gizmo documentation](http://www.tapir.caltech.edu/~phopkins/Site/GIZMO_files/gizmo_documentation.html).

Note that the provided `params.txt` is only an example and should be adjusted based on the requirements of your simulation. Notably, you can adjust the spectrum, amplitude, compressiveness, and coherence time of the turbulent driving to get the desired properties.



# Submitting an MPI job
An example submission script for running the code with MPI on Frontera is given in `run.sh`; the exact command will vary depending on your machine.
