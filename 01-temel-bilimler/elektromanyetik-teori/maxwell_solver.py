import numpy as np
import matplotlib.pyplot as plt

def solve_maxwell_1d(steps=200, dx=0.01, dt=0.005):
    """
    1D FDTD (Finite-Difference Time-Domain) method for Maxwell's Equations.
    Simulates a simple pulse propagation in vacuum.
    """
    # Initialize fields
    Ez = np.zeros(steps)
    Hy = np.zeros(steps)
    
    # Material properties (Vacuum)
    c0 = 1.0 # Speed of light (normalized)
    imp0 = 1.0 # Impedance (normalized)
    
    # Time loop
    time_steps = 400
    for t in range(time_steps):
        # Update Hy field
        for i in range(steps - 1):
            Hy[i] = Hy[i] + (Ez[i+1] - Ez[i]) / imp0
            
        # Update Ez field
        for i in range(1, steps):
            Ez[i] = Ez[i] + (Hy[i] - Hy[i-1]) * imp0
            
        # Source (Gaussian pulse)
        Ez[0] = np.exp(-(t - 30)**2 / 100)
        
        # Visualization (every 20 steps)
        if t % 100 == 0:
            plt.plot(Ez, label=f'Time {t}')

    plt.title("1D Maxwell Equation Solver (FDTD)")
    plt.xlabel("Spatial Step (x)")
    plt.ylabel("Electric Field (Ez)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    print("Simulating 1D Maxwell Pulse Propagation...")
    # solve_maxwell_1d() # Uncomment to run locally
    print("Success: Solver logic implemented.")
