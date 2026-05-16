import numpy as np

# Kapı tanımları
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])
I = np.eye(2)
X = np.array([[0, 1], [1, 0]])
CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])

def create_bell_state(initial_bits='00'):
    """
    Belirli bir başlangıç durumundan Bell durumu üretir.
    '00' -> |Phi+> = (|00> + |11>) / sqrt(2)
    '10' -> |Phi-> = (|00> - |11>) / sqrt(2)
    '01' -> |Psi+> = (|01> + |10>) / sqrt(2)
    '11' -> |Psi-> = (|01> - |10>) / sqrt(2)
    """
    # Başlangıç vektörünü oluştur
    v1 = np.array([1, 0]) if initial_bits[0] == '0' else np.array([0, 1])
    v2 = np.array([1, 0]) if initial_bits[1] == '0' else np.array([0, 1])
    psi_in = np.kron(v1, v2)
    
    # 1. İlk kübite Hadamard uygula
    H_total = np.kron(H, I)
    psi_mid = np.dot(H_total, psi_in)
    
    # 2. CNOT uygula (Kontrol: 1. kübit, Hedef: 2. kübit)
    psi_bell = np.dot(CNOT, psi_mid)
    
    return psi_bell

def analyze_bell_state(state, name):
    print(f"\n--- {name} Analizi ---")
    probs = np.abs(state)**2
    states = ['|00>', '|01>', '|10>', '|11>']
    for s, p in zip(states, probs):
        if p > 0.01:
            print(f"{s}: %{p*100:.1f}")

if __name__ == "__main__":
    print("Dört Temel Bell Durumu (Dolanıklık) Simülasyonu")
    
    bell_names = {
        '00': 'Phi+ (|00> + |11>)',
        '10': 'Phi- (|00> - |11>)',
        '01': 'Psi+ (|01> + |10>)',
        '11': 'Psi- (|01> - |10>)'
    }
    
    for bits, name in bell_names.items():
        state = create_bell_state(bits)
        analyze_bell_state(state, name)
    
    print("\nSimülasyon başarıyla tamamlandı.")
