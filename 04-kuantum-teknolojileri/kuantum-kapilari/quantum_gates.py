import numpy as np

# Single Qubit Gates
I = np.array([[1, 0], [0, 1]])
X = np.array([[0, 1], [1, 0]]) # NOT gate
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]])
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]]) # Hadamard gate

# Two Qubit Gate: CNOT
CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

def apply_gate(state, gate):
    """
    Applies a quantum gate to a state vector.
    """
    return np.dot(gate, state)

if __name__ == "__main__":
    # Initial state |0>
    psi_0 = np.array([1, 0])
    
    # Create superposition state |+> = H|0>
    psi_plus = apply_gate(psi_0, H)
    
    # Flip the state |1> = X|0>
    psi_1 = apply_gate(psi_0, X)
    
    print("Initial state |0>:", psi_0)
    print("State after Hadamard (superposition) |+>:", psi_plus)
    print("State after X (bit flip) |1>:", psi_1)
    
    # Verify Hadamard: H|+> = |0>
    psi_back = apply_gate(psi_plus, H)
    print("Verification H|+> should be |0>:", np.round(psi_back))
    
    print("Success: Basic quantum gate matrices and logic implemented.")
