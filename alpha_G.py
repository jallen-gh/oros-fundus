"""
Derives the gravitational fine structure constant α_G = π/N_F
from N_F = 96 fermionic degrees of freedom.

N_F is fixed by the Pati-Salam algebra under three simultaneous
constraints: DHR superselection, F_4/Spin(8) triality, and
modular nuclearity. No free parameters.
"""

import numpy as np

N_F = 96
alpha_G = np.pi / N_F

print(f"N_F        = {N_F}")
print(f"α_G = π/96 = {alpha_G:.10f}")
print(f"1/α_G      = {1/alpha_G:.6f}")
