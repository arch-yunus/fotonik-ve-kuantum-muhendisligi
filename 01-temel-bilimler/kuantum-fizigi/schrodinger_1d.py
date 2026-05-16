import numpy as np
from scipy.linalg import eigh

def solve_schrodinger_well(L=1.0, N=1000, V0=0):
    """
    Solves the time-independent Schrödinger equation for a 1D well.
    Uses finite difference method to construct the Hamiltonian matrix.
    """
    x = np.linspace(0, L, N)
    dx = x[1] - x[0]
    
    # Kinetic energy matrix (Laplacian)
    # H = - (hbar^2 / 2m) * d^2/dx^2 + V
    # Normalized: hbar = 1, m = 1
    
    main_diag = 2.0 * np.ones(N) / dx**2
    off_diag = -1.0 * np.ones(N-1) / dx**2
    
    H = np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
    
    # Potential energy (Infinite well is handled by boundary conditions of the grid)
    # For a finite well, we would add V here.
    
    # Solve eigenvalue problem
    energies, wavefunctions = eigh(H)
    
    return energies, wavefunctions, x

if __name__ == "__main__":
    print("Solving 1D Schrödinger Equation for an infinite well...")
    energies, wavefunctions, x = solve_schrodinger_well()
    print(f"First 3 Energy levels: {energies[:3]}")
    print("Success: Numerical solver implemented.")
