import numpy as np

def mzi_unit(theta, phi):
    """
    Simulates a single Mach-Zehnder Interferometer (MZI) transformation matrix.
    Used as a basic building block for unitary matrices in ONNs.
    """
    matrix = 0.5 * np.array([
        [np.exp(1j*phi) * (np.exp(1j*theta) - 1), 1j * np.exp(1j*phi) * (np.exp(1j*theta) + 1)],
        [1j * (np.exp(1j*theta) + 1), -(np.exp(1j*theta) - 1)]
    ])
    return matrix

def simulate_onn_layer(input_vector, weights_matrix):
    """
    Simulates a linear layer in an Optical Neural Network.
    y = W * x
    """
    return np.dot(weights_matrix, input_vector)

if __name__ == "__main__":
    # Example input: 2-element vector (e.g., light intensities/phases in 2 waveguides)
    input_v = np.array([1.0 + 0j, 0.0 + 0j])
    
    # Unitary matrix from a single MZI
    W = mzi_unit(theta=np.pi/2, phi=0)
    
    output_v = simulate_onn_layer(input_v, W)
    
    print("Input Vector:", input_v)
    print("MZI Transformation Matrix:\n", W)
    print("Output Vector (after MZI):", output_v)
    print("Success: ONN basic simulation logic implemented.")
