"""
Derives η_opt = 2 / (√π · (ln N_F)²)
from the GVV half-normal normalization on the TFD bipartite split.

η_opt controls the dark energy equation of state:
  w(z=0) = -1 - η_opt ≈ -1.054  (instantaneous)
  w_eff  = -1 - η_opt/2 ≈ -1.027 (time-averaged)
"""

import numpy as np

N_F = 96
eta_opt = 2.0 / (np.sqrt(np.pi) * (np.log(N_F))**2)

w_instantaneous = -1.0 - eta_opt
w_eff = -1.0 - eta_opt / 2.0

print(f"N_F              = {N_F}")
print(f"ln(N_F)          = {np.log(N_F):.10f}")
print(f"η_opt            = {eta_opt:.10f}")
print(f"w(z=0)           = {w_instantaneous:.6f}")
print(f"w_eff (averaged) = {w_eff:.6f}")
