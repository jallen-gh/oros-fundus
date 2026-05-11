import numpy as np
from scipy.integrate import quad
from scipy.optimize import least_squares

# 1. CONSTANTS AND COSMOLOGICAL PARAMETERS
Omega_m = 0.31          
Omega_de = 1.0 - Omega_m 
z_eq = 3400.0           
		
eta_opt = 2.0 / (np.sqrt(np.pi) * (np.log(96)**2))  # Corrected: GVV normalization 
A = eta_opt / 2.0                                   
B = eta_opt / (2.0 * np.log(1.0 + z_eq))            
		
z_bins = np.array([0.0, 0.3, 0.5, 0.7, 1.1, 1.5, 1100.0])
		
# 2. THE THEORETICAL BASELINE (Logarithmic Evolution)
def f_Base(z):
    return (1.0 + z)**(-3.0 * A) * np.exp(-1.5 * B * (np.log(1.0 + z))**2)
		
def E_Base(z):
    return np.sqrt(Omega_m * (1.0 + z)**3 + Omega_de * f_Base(z))
		
def integrand_Base(z):
    return 1.0 / E_Base(z)
		
def D_M_Base(z):
    val, _ = quad(integrand_Base, 0, z)
    return val
		
# MOCK DATA GENERATION
mock_pure = np.array([D_M_Base(z) for z in z_bins])
		
mock_noisy = np.copy(mock_pure)
mock_noisy[2] *= 0.985  
mock_noisy[3] *= 0.985  
		
# Simulates the systemic bias introduced when datasets (SNe vs BAO) compete.
# Values approximate the ~3% to 4.5% distance anomalies observed in DESI LRGs.
mock_tension = np.copy(mock_pure)
mock_tension[1] *= 1.005 
mock_tension[2] *= 0.965 
mock_tension[3] *= 0.955 
		
# 3. THE CPL PARAMETERIZATION
def f_CPL(z, w0, wa):
    return (1.0+z)**(3.0*(1.0+w0+wa)) * np.exp(-3.0*wa*(z/(1.0+z)))
		
def E_CPL(z, w0, wa):
    return np.sqrt(Omega_m * (1.0 + z)**3 + Omega_de * f_CPL(z, w0, wa))
		
def D_M_CPL(z, w0, wa):
    val, _ = quad(lambda x: 1.0 / E_CPL(x, w0, wa), 0, z)
    return val
		
# 4. THE FIT
def fit_model(target_distances, description):
    def residuals(params):
        w0, wa = params
        cpl_distances = np.array([D_M_CPL(z, w0, wa) for z in z_bins])
        error = cpl_distances - target_distances
        error[-1] *= 100.0  # Heavy weight for strict CMB anchor
        return error
		
    result = least_squares(residuals, [-1.0, 0.0], method='lm')
    print("="*65)
    print(description)
    print(f"Recovered w_0 : {result.x[0]:.4f}")
    print(f"Recovered w_a : {result.x[1]:.4f}")
		
if __name__ == "__main__":
    fit_model(mock_pure, "SCENARIO 1: PURE BASELINE FIT")
    fit_model(mock_noisy, "SCENARIO 2: REALISTIC FIT (1.5% Noise)")
    fit_model(mock_tension, "SCENARIO 3: SYSTEMIC TENSION (Crisis Regime)")
