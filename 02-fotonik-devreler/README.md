# Bölüm 02: Fotonik Entegre Devreler ve Silikon Fotoniği

Bu bölüm, optik bileşenlerin bir çip üzerinde entegre edilmesini sağlayan Fotonik Entegre Devre (Photonic Integrated Circuits) teknolojilerine odaklanmaktadır. Silikon fotoniği, günümüzde veri merkezlerinden yapay zeka işlemcilerine kadar geniş bir alanda devrim yaratmaktadır.

## 📂 Klasör İçeriği

### 1. Pasif Bileşenler (`/pasif-bilesenler`)
Dışarıdan bir enerji girişi gerektirmeden ışığı yönlendiren ve filtreleyen yapılar.
* **Dalga Kılavuzları (Waveguides):** Işığın çip üzerinde taşınması.
* **Yönlü Bağlaştırıcılar (Directional Couplers):** Işık gücünün bölünmesi ve birleştirilmesi.
* **Mach-Zehnder İnterferometreleri:** Faz farkı yaratarak girişim tabanlı kontrol sağlayan yapılar.
* **Halka Rezonatörler (Ring Resonators):** Spektral filtreleme ve optik geciktirme hatları.

### 2. Aktif Bileşenler (`/aktif-bilesenler`)
Elektriksel sinyallerle optik özellikleri değiştirilen bileşenler.
* **Elektro-Optik Modülatörler:** Verinin ışık üzerine bindirilmesi.
* **Termo-Optik Ayarlayıcılar:** Isıl yöntemle faz kontrolü.
* **Fotodedektörler:** Optik sinyalin tekrar elektriksel sinyale dönüştürülmesi.

### 3. Tasarım ve Yerleşim (Layout) (`/pic-tasarim-layout`)
Kod tabanlı donanım tasarımı süreçleri.
* **gdsfactory Kullanımı:** Python ile parametrik bileşen tasarımı.
* **GDSII Çıktıları:** Üretim (Dökümhane) için gerekli maske dosyalarının oluşturulması.

---

## 🛠️ Tasarım Araçları
Bu modülde aşağıdaki araçlarla çalışılmaktadır:
1. **gdsfactory:** Tasarım otomasyonu ve yerleşim.
2. **Meep:** Bileşen bazlı FDTD simülasyonları.
3. **Lumerical (Ticari):** Endüstriyel düzeyde simülasyon referansları.

---

## 📈 Öğrenim Hedefleri
* Nano ölçekte ışık hapsetme mekanizmalarını kavramak.
* Karmaşık fotonik devre şemalarını tasarlamak ve simüle etmek.
* Üretilebilir (DRC uyumlu) fotonik maske dosyaları üretmek.
