#!/usr/bin/env python
"""                                                                            
Usage: MakeBox.py [options]

Options:                                                                       
   -h --help            Show this screen.
   --L=<pc>             Size of the box in code units (e.g. pc) [default: 10.0]
   --M=<msun>           Total mass in the box in code units (e.g. msun) [default: 2e4]
   --B=<f>              Initial magnetic field strength in code units (e.g. microgauss) [default: 10]
   --N=<N>              Number of gas cells in the box [default: 125000]
"""


import numpy as np
import h5py
from docopt import docopt

arguments = docopt(__doc__)
Lbox = float(arguments["--L"])
M_gas = float(arguments["--M"])
N_gas = int(float(arguments["--N"])+0.5)
B = float(arguments["--B"])


filename = "BOX_M%3.2g_L%g_B%g_N%d.hdf5"%(M_gas, Lbox, B, N_gas)
filename = filename.replace("+","").replace("e0","e")

mgas = np.repeat(M_gas/N_gas, N_gas)
x = np.random.rand(N_gas,3)*Lbox
v = np.zeros_like(x)
B = np.ones_like(x) * B

print("Writing snapshot...")

F=h5py.File(filename, 'w')
F.create_group("PartType0")
F.create_group("Header")
F["Header"].attrs["NumPart_ThisFile"] = [N_gas] + 5*[0]
F["Header"].attrs["NumPart_Total"] = [N_gas] + 5 * [0]
F["Header"].attrs["MassTable"] = [M_gas/N_gas] + 5*[0]
F["Header"].attrs["BoxSize"] = Lbox
F["Header"].attrs["Time"] = 0.0
F["PartType0"].create_dataset("Masses", data=mgas)
F["PartType0"].create_dataset("Coordinates", data=x)
F["PartType0"].create_dataset("Velocities", data=v)
F["PartType0"].create_dataset("ParticleIDs", data=1+np.arange(N_gas))
F["PartType0"].create_dataset("MagneticField", data=B)
F.close()
