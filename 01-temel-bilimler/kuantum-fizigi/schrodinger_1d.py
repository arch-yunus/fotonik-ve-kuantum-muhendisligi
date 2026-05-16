import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

def solve_schrodinger_1d(L, N, V_type='well', V_val=0):
    """
    1B Zaman Bağımsız Schrödinger Denklemini Çözer.
    Metot: Sonlu Farklar (Finite Difference Method)
    
    Parametreler:
        L: Sistemin toplam boyu (nm)
        N: Grid noktası sayısı
        V_type: Potansiyel tipi ('well', 'harmonic', 'barrier')
        V_val: Potansiyel değeri/yüksekliği
    """
    x = np.linspace(-L/2, L/2, N)
    dx = x[1] - x[0]
    
    # Potansiyel Enerji V(x) Tanımı
    if V_type == 'well':
        V = np.zeros(N)
        V[0] = V[-1] = 1e6 # Sonsuz potansiyel duvarları
    elif V_type == 'harmonic':
        V = 0.5 * V_val * x**2
    elif V_type == 'barrier':
        V = np.zeros(N)
        V[int(N/2)-10:int(N/2)+10] = V_val
    else:
        V = np.zeros(N)

    # Hamiltonian Matrisi Oluşturma (H = T + V)
    # T = -hbar^2 / (2m) * d^2/dx^2
    # m_e = 1 (Atomik birimler veya normalize edilmiş değerler kullanılıyor)
    
    hbar = 1
    m = 1
    
    # İkinci türev matrisi (Merkezi farklar)
    main_diag = -2 * np.ones(N)
    off_diag = np.ones(N-1)
    D2 = diags([off_diag, main_diag, off_diag], [-1, 0, 1]).toarray() / dx**2
    
    T = -(hbar**2 / (2 * m)) * D2
    V_mat = np.diag(V)
    H = T + V_mat
    
    # Özdeğer ve Özvektör Çözümü (En düşük k enerji seviyesi)
    k = 5
    energies, psi = eigsh(H, k=k, which='SM')
    
    return x, energies, psi, V

def plot_results(x, energies, psi, V):
    plt.figure(figsize=(10, 6))
    plt.plot(x, V, 'k--', label='Potansiyel V(x)', alpha=0.5)
    
    for i in range(len(energies)):
        # Dalga fonksiyonunu normalize et ve enerji seviyesine ötele
        y = psi[:, i] * 5 + energies[i]
        plt.plot(x, y, label=f'E{i} = {energies[i]:.2f}')
        plt.fill_between(x, energies[i], y, alpha=0.2)
        
    plt.title('1B Schrödinger Denklemi Çözümü')
    plt.xlabel('Konum (x)')
    plt.ylabel('Enerji / ψ(x)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()

if __name__ == "__main__":
    print("Simülasyon başlatılıyor: Sonsuz Potansiyel Kuyusu")
    L = 10.0
    N = 1000
    x, E, psi, V = solve_schrodinger_1d(L, N, V_type='well')
    
    print(f"Hesaplanan ilk {len(E)} enerji seviyesi:")
    for i, val in enumerate(E):
        print(f"Seviye {i}: {val:.4f}")
    
    # Not: Başsız ortamda plot_results görselleştirme yapmayabilir, 
    # ancak kodun doğruluğu terminal çıktısından görülebilir.
    # plot_results(x, E, psi, V)
