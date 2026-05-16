import numpy as np

# Temel Kuantum Kapıları (Matris Temsilleri)
I = np.array([[1, 0], [0, 1]])
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]])
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])

# 2-Kübit Kapıları
CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

def get_state_vector(qubits_states):
    """
    Kübit durumlarından toplam state vektörünü hesaplar (Tensor Product).
    Örn: [|0>, |1>] -> |01>
    """
    state = qubits_states[0]
    for i in range(1, len(qubits_states)):
        state = np.kron(state, qubits_states[i])
    return state

def apply_gate(state, gate):
    """
    Durum vektörüne kapı uygular.
    """
    return np.dot(gate, state)

if __name__ == "__main__":
    # 1. Başlangıç Durumu: |0>
    psi0 = np.array([1, 0])
    print(f"Başlangıç Durumu (|0>): {psi0}")
    
    # 2. Hadamard Kapısı Uygula (Süperpozisyon)
    psi1 = apply_gate(psi0, H)
    print(f"Hadamard Sonrası (|0> + |1>): {psi1}")
    
    # 3. Ölçüm Olasılıkları
    probs = np.abs(psi1)**2
    print(f"Ölçüm Olasılıkları: P(0)={probs[0]:.2f}, P(1)={probs[1]:.2f}")
    
    # 4. Bell Durumu Oluşturma (|00> + |11>) / sqrt(2)
    # Adım A: |0> ve |0> tensor çarpımı -> |00>
    q1 = np.array([1, 0])
    q2 = np.array([1, 0])
    bell_start = get_state_vector([q1, q2])
    
    # Adım B: İlk kübite Hadamard uygula (H ⊗ I)
    H_full = np.kron(H, I)
    bell_step1 = apply_gate(bell_start, H_full)
    
    # Adım C: CNOT uygula
    bell_final = apply_gate(bell_step1, CNOT)
    
    print("\nBell Durumu (|00> + |11>) / sqrt(2):")
    print(bell_final)
    
    bell_probs = np.abs(bell_final)**2
    print(f"Bell Ölçüm Olasılıkları: P(00)={bell_probs[0]:.2f}, P(01)={bell_probs[1]:.2f}, P(10)={bell_probs[2]:.2f}, P(11)={bell_probs[3]:.2f}")
