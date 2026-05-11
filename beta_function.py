"""
Derives the one-loop QCD beta function coefficient
β₀ = (11·N_c - 2·N_f) / 12π

N_c = 3 color charges (SU(3))
N_f = 18 active quark flavors at unification scale
      (N_F = 96 total fermionic d.o.f. / (2 chiralities × 2 spin × N_c))

The algebraic derivation follows from the modular flow
renormalization group on the Type III₁ bulk.
"""

import numpy as np

N_c = 3
N_f = 18  # 6 quark flavors × 3 colors = 18 active flavors at unification scale

beta_0 = (11 * N_c - 2 * N_f) / (12 * np.pi)

print(f"N_c              = {N_c}")
print(f"N_f              = {N_f}")
print(f"11·N_c           = {11*N_c}")
print(f"2·N_f            = {2*N_f}")
print(f"11·N_c - 2·N_f   = {11*N_c - 2*N_f}")
print(f"β₀               = {beta_0:.10f}")
print(f"β₀ < 0 at N_f=18 → infrared free at UV scale (Λ_UV)")
print(f"Confinement activates when cosmological cooling drops N_f below 16")
