import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

def solve_schrodinger_1d(L=1.0, N=1000, V_type='infinite', V0=1000, a=0.2):
    """
    1-Boyutlu Zamandan Bağımsız Schrödinger Denklemi Çözücü.
    
    Parametreler:
    - L: Sistemin toplam uzunluğu (metre cinsinden temsil).
    - N: Izgara (grid) noktası sayısı.
    - V_type: 'infinite' (sonsuz kuyu) veya 'finite' (sonlu kuyu).
    - V0: Sonlu kuyu için potansiyel bariyer yüksekliği.
    - a: Sonlu kuyu genişliği.
    """
    x = np.linspace(-L/2, L/2, N)
    dx = x[1] - x[0]
    
    # Kinetik Enerji Matrisi (Hamiltonian'ın Laplacian kısmı)
    # H = - (hbar^2 / 2m) * d^2/dx^2 + V
    # Normalizasyon: hbar = 1, m = 1 (Atomik birimler veya normalize edilmiş form)
    
    main_diag = 2.0 * np.ones(N) / dx**2
    off_diag = -1.0 * np.ones(N-1) / dx**2
    H = np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
    
    # Potansiyel Enerji Tanımı
    V = np.zeros(N)
    if V_type == 'finite':
        # Merkezde -a/2 ile a/2 arasında 0 potansiyel, dışında V0
        V = np.where(np.abs(x) > a/2, V0, 0)
    
    # Potansiyeli Hamiltonian'a ekle
    H += np.diag(V)
    
    # Özdeğer Probleminin Çözümü (Enerjiler ve Dalga Fonksiyonları)
    energies, wavefunctions = eigh(H)
    
    return energies, wavefunctions, x, V

def plot_results(energies, wavefunctions, x, V, num_states=3):
    """Sonuçları görselleştirir."""
    plt.figure(figsize=(10, 6))
    
    # Potansiyeli çiz
    plt.plot(x, V, 'k-', lw=2, label='Potansiyel V(x)')
    
    # İlk 'num_states' kadar dalga fonksiyonunu çiz
    for i in range(num_states):
        # Dalga fonksiyonunu enerji seviyesine göre kaydır (Görselleştirme kolaylığı için)
        psi = wavefunctions[:, i]
        # Normalizasyon ve ölçeklendirme
        psi_scaled = psi * (np.max(V)*0.1 if np.max(V) > 0 else 1.0) + energies[i]
        plt.plot(x, psi_scaled, label=f'n={i+1}, E={energies[i]:.2f}')
        plt.axhline(y=energies[i], color='gray', linestyle='--', alpha=0.5)
    
    plt.title("1-Boyutlu Schrödinger Denklemi Sayısal Çözümü")
    plt.xlabel("Konum (x)")
    plt.ylabel("Enerji / Psi(x)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    print("--- 1D Schrödinger Denklemi Çözücü Başlatılıyor ---")
    
    # Sonsuz Kuyu Çözümü
    E_inf, psi_inf, x, V_inf = solve_schrodinger_1d(V_type='infinite')
    print(f"Sonsuz Kuyu - İlk 3 Enerji Seviyesi: {E_inf[:3]}")
    
    # Görselleştirmek için (Not: Terminalde çalışırken grafik penceresi açılmayabilir,
    # ancak kod yapısı tamdır.)
    # plot_results(E_inf, psi_inf, x, V_inf)
    
    print("\nSimülasyon başarıyla tamamlandı.")
