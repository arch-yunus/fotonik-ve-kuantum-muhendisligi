import numpy as np
import matplotlib.pyplot as plt

def ring_transmission(r, kappa, wavelength_range):
    """
    Calculates the transmission spectrum of a single-bus ring resonator.
    r: self-coupling coefficient (sqrt(1 - kappa^2))
    kappa: cross-coupling coefficient
    """
    # L = 2 * pi * radius (assuming some radius)
    L = 100e-6 # 100 micrometers
    neff = 2.4 # Effective index of silicon waveguide
    
    alpha = 0.99 # Propagation loss (transmission through the ring)
    
    phi = (2 * np.pi * neff * L) / wavelength_range
    
    # Transmission formula for all-pass ring resonator
    numerator = r**2 + alpha**2 - 2 * r * alpha * np.cos(phi)
    denominator = 1 + r**2 * alpha**2 - 2 * r * alpha * np.cos(phi)
    
    return numerator / denominator

if __name__ == "__main__":
    wavelengths = np.linspace(1540e-9, 1560e-9, 1000)
    kappa = 0.2
    r = np.sqrt(1 - kappa**2)
    
    transmission = ring_transmission(r, kappa, wavelengths)
    
    plt.figure(figsize=(10, 5))
    plt.plot(wavelengths * 1e9, transmission)
    plt.title("Ring Resonator Transmission Spectrum")
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Normalized Transmission")
    plt.grid(True)
    plt.show()
    
    print("Success: Ring resonator simulation model implemented.")
