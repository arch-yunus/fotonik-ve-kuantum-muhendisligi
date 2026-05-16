import numpy as np

# --- Tek Kübitlik Kuantum Kapıları ---
I = np.array([[1, 0], [0, 1]])
X = np.array([[0, 1], [1, 0]])     # NOT (Bit-flip) Kapısı
Y = np.array([[0, -1j], [1j, 0]])  # Pauli-Y
Z = np.array([[1, 0], [0, -1]])    # Phase-flip Kapısı
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])  # Hadamard (Süperpozisyon)

# --- İki Kübitlik Kuantum Kapıları ---
# CNOT: Kontrol kübiti 1 ise hedef kübiti tersle (flip)
CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

def tensor_product(gate1, gate2):
    """İki kapının Kronecker çarpımını (tensor product) hesaplar."""
    return np.kron(gate1, gate2)

def get_state_probabilities(state):
    """Bir kuantum durumunun ölçüm olasılıklarını döndürür."""
    return np.abs(state)**2

def describe_state(state, label="Durum"):
    """Kuantum durumunu ve olasılıklarını yazdırır."""
    print(f"\n--- {label} Analizi ---")
    print(f"Vektör: {state}")
    probs = get_state_probabilities(state)
    for i, p in enumerate(probs):
        binary = format(i, f'0{int(np.log2(len(state)))}b')
        print(f"|{binary}> olma olasılığı: %{p*100:.2f}")

if __name__ == "__main__":
    print("Kuantum Kapı ve Durum Simülasyonu")
    
    # 1. Başlangıç Durumu |0>
    psi_0 = np.array([1, 0])
    
    # 2. Hadamard Uygulama: |+> = H|0>
    psi_plus = np.dot(H, psi_0)
    describe_state(psi_plus, "Hadamard Sonrası (|+>)")
    
    # 3. İki Kübitlik Sistem: |00>
    psi_00 = np.kron(psi_0, psi_0)
    
    # 4. Bell Durumu Oluşturma (Dolanıklık):
    # H kapısını ilk kübite uygula, sonra CNOT uygula
    H_full = tensor_product(H, I) # Sadece ilk kübite H uygula
    psi_step1 = np.dot(H_full, psi_00)
    psi_bell = np.dot(CNOT, psi_step1)
    
    describe_state(psi_bell, "Bell Durumu (Phi+)")
    
    print("\nSimülasyon Başarıyla Tamamlandı.")
