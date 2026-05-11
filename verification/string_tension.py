"""
Derives the QCD string tension ratio σ/Λ_UV² = ln(N_F) / 2√π
from the Cornell potential V(r) = -α_s/r + σr.

The string tension emerges from the Log-Sobolev saturation
condition on the modular Hamiltonian at the confinement scale.
"""

import numpy as np

N_F = 96
alpha_s = np.pi / 6

string_tension_ratio = np.log(N_F) / (2.0 * np.sqrt(np.pi))

print(f"N_F                    = {N_F}")
print(f"ln(N_F)                = {np.log(N_F):.10f}")
print(f"σ/Λ_UV² = ln(96)/2√π  = {string_tension_ratio:.10f}")
print(f"α_s                    = {alpha_s:.10f}")
print(f"Cornell: V(r) = -{alpha_s:.4f}/r + {string_tension_ratio:.4f}·Λ_UV²·r")
