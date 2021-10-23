"""
swarm.py
some file for swarm intelligence

"""
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms import Swarm


def gather_swarm():
    pass


options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
# Call instance of PSO
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)
# Perform optimization
best_cost, best_pos = optimizer.optimize(fx.sphere, iters=100)