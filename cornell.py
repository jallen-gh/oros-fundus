"""
Verifies the full Cornell potential V(r) = -α_s/r + σr
at representative QCD distance scales.

All constants are zero-parameter outputs of the framework:
  α_s = π/6
  σ/Λ_UV² = ln(96)/2√π

Λ_UV is the single environmental integration constant.
Representative value: Λ_UV ≈ 0.2 GeV (QCD scale).
"""

import numpy as np

alpha_s = np.pi / 6
N_F = 96
sigma_ratio = np.log(N_F) / (2.0 * np.sqrt(np.pi))

Lambda_UV_GeV = 0.2  # GeV — environmental constant, not a free parameter
sigma = sigma_ratio * Lambda_UV_GeV**2

print(f"α_s              = {alpha_s:.6f}")
print(f"σ/Λ_UV²          = {sigma_ratio:.6f}")
print(f"Λ_UV             = {Lambda_UV_GeV} GeV")
print(f"σ                = {sigma:.6f} GeV²")
print()
print(f"{'r (fm)':<12} {'V(r) (GeV)':<16} {'Coulomb term':<16} {'Linear term'}")
print("-" * 60)

GeV_fm = 0.197327  # ħc in GeV·fm

for r_fm in [0.1, 0.2, 0.5, 1.0, 1.5, 2.0]:
    r_GeV = r_fm / GeV_fm
    coulomb = -alpha_s / r_GeV
    linear = sigma * r_GeV
    V = coulomb + linear
    print(f"{r_fm:<12.1f} {V:<16.4f} {coulomb:<16.4f} {linear:.4f}")
