To generate the reference data move to the directory data/CLAWPACK_data and run
```
python generate_data.py
```
**Requires CLAWPACK to be installed.**: https://www.clawpack.org/installing.html

### Entropy solutions

As this is implemented currently, the PINN might converge to non-entropy solutions.
The notebook SWEs.ipynb contains a trained PINN with a dam break as initial condition
that converges to an entropy violating shock. The notebook SWEs2.ipynb was trained with
an initial condition slightly advanced in time, where the rarecfaction and shock waves
emanating from the Riemann problem are already well separated. This PINN converges to
the correct entropy solution.

The code in SWEs.ipynb and SWEs2.ipynb is identical. They only differ in the training data
(initial condition).

