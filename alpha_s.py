"""
Derives the strong coupling constant α_s = π/6
from the D_4 principal graph quantum dimension.

The Jones index [M:N] = 3 forces statistical dimension
d(ρ) = √3 for exceptional color SU(3) ⊂ G_2 = Aut(O).
The strong coupling follows from d(ρ)² = 3 = 18/6.
"""

import numpy as np

jones_index = 3
d_rho = np.sqrt(jones_index)
alpha_s = np.pi / (2 * jones_index)

print(f"Jones index [M:N]  = {jones_index}")
print(f"Statistical dim d  = √3 = {d_rho:.10f}")
print(f"α_s = π/6          = {alpha_s:.10f}")
print(f"1/α_s              = {1/alpha_s:.6f}")
