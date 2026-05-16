import numpy as np
import matplotlib.pyplot as plt

def simulate_mzi(phase_diff_range):
    """
    Mach-Zehnder İnterferometresi (MZI) Güç Transmisyon Simülasyonu.
    
    P_out = P_in * cos^2(delta_phi / 2)
    """
    p_in = 1.0  # Giriş gücü (Normalize edilmiş)
    
    # Çıkış güçlerini hesapla
    p_out = p_in * np.cos(phase_diff_range / 2)**2
    
    return p_out

if __name__ == "__main__":
    print("Mach-Zehnder İnterferometresi (MZI) Analizi Başlatılıyor...")
    
    # Faz farkı aralığı (0 ile 2*pi arası)
    phi = np.linspace(0, 2 * np.pi, 500)
    transmission = simulate_mzi(phi)
    
    # Görselleştirme
    plt.figure(figsize=(8, 5))
    plt.plot(phi / np.pi, transmission, 'b-', lw=2)
    plt.title("MZI Güç Transmisyonu vs Faz Farkı")
    plt.xlabel("Faz Farkı (Δφ / π)")
    plt.ylabel("Normalize Çıkış Gücü (P_out / P_in)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axvline(x=1, color='r', linestyle=':', label='Yıkıcı Girişim (Destructive)')
    plt.axvline(x=0, color='g', linestyle=':', label='Yapıcı Girişim (Constructive)')
    plt.axvline(x=2, color='g', linestyle=':')
    plt.legend()
    
    print("Grafik verileri hazırlandı. MZI karakterizasyonu tamamlandı.")
    # plt.show() # Terminal ortamında kapalıdır.
