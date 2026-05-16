# Faz 04: Kuantum Teknolojileri (Donanım ve Yazılım)

Kuantum teknolojileri; süperpozisyon, dolanıklık ve tünelleme gibi kuantum mekaniksel fenomenleri kullanarak hesaplama, haberleşme ve algılama süreçlerinde devrim yaratır. Bu bölüm, kuantum kapılarından algoritmalara kadar olan süreci kapsar.

## ⚛️ Kuantum Hesaplama Temelleri

### 1. Kübit (Quantum Bit)
Klasik bitin aksine, aynı anda hem 0 hem de 1 durumunda bulunabilen (süperpozisyon) temel bilgi birimi.
* **Bloch Küresi:** Kübitin durumunu görselleştirmek için kullanılan geometrik temsil.

### 2. Kuantum Kapıları (Quantum Gates)
Kübitler üzerinde işlem yapan üniter matrisler.
* **Tek Kübit Kapıları:** X (NOT), Y, Z, H (Hadamard - süperpozisyon oluşturur), S, T.
* **Çoklu Kübit Kapıları:** CNOT (kontrollü-NOT), SWAP, Toffoli.

### 3. Dolanıklık (Entanglement)
İki veya daha fazla kübitin, aralarındaki mesafe ne olursa olsun birbirlerinin durumuna bağlı olması. Bell durumları bu fenomenin temelini oluşturur.

## 🛠️ Kuantum Programlama Ekosistemi

* **Qiskit (IBM):** Python tabanlı, açık kaynaklı kuantum programlama çerçevesi.
* **PennyLane:** Diferansiyellenebilir kuantum programlama (Kuantum Makine Öğrenmesi).
* **Strawberry Fields:** Fotonik tabanlı kuantum hesaplama simülatörü (CV - Continuous Variable).

## 📡 Kuantum Haberleşme

* **QKD (Quantum Key Distribution):** BB84 gibi protokollerle güvenli anahtar değişimi.
* **Kuantum Teleportasyon:** Bir kuantum durumunun dolanık çiftler kullanılarak bir yerden başka bir yere aktarılması.

## 💻 Mevcut Kodlar

* `/kuantum-kapilari/quantum_gates.py`: Temel kuantum kapılarının matris operasyonları ile simülasyonu.
* `/kuantum-algoritmalari/bell_states.py`: Bell durumlarının (dolanıklık) oluşturulması.

## 📖 Kaynakça
1. Nielsen, M. A., & Chuang, I. L., "Quantum Computation and Quantum Information".
2. Hidary, J. D., "Quantum Computing: An Applied Approach".
