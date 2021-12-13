#!/bin/bash
#SBATCH -J MHD_BOX -p development -N 1 --ntasks-per-node 56 -t 00:10:00 -A AST21002
source $HOME/.bashrc
ibrun ./GIZMO ./params.txt 0 1>gizmo.out 2>gizmo.err
