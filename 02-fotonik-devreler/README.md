# Faz 02: Fotonik Entegre Devreler (PIC)

Fotonik Entegre Devreler, geleneksel elektronik devrelerin yaptığı işi (sinyal işleme, iletim, hesaplama) elektronlar yerine fotonlar (ışık) ile gerçekleştiren yapılardır. Bu bölüm, PIC bileşenlerinin tasarımı ve simülasyonuna odaklanır.

## 🏗️ PIC Bileşen Mimarisi

### 1. Pasif Bileşenler
Enerji tüketmeden ışığı yönlendiren veya filtreleyen elemanlar.
* **Dalga Kılavuzları (Waveguides):** Işığın hapsedildiği yollar (genellikle silikon veya silikon nitrür).
* **MZI (Mach-Zehnder Interferometer):** Işığı iki kola ayırıp tekrar birleştirerek faz farkına dayalı anahtarlama yapar.
* **Halka Rezonatörler (Ring Resonators):** Belirli dalga boylarını süzmek için kullanılan yüksek Q-faktörlü halkalar.
* **Yönlü Bağlaştırıcılar (Directional Couplers):** Evanescent dalga teorisi ile ışığı kanallar arasında paylaştırır.

### 2. Aktif Bileşenler
Dışarıdan bir sinyal (elektrik, ısı vb.) ile ışığın özelliklerini değiştiren elemanlar.
* **Elektro-Optik Modülatörler:** Elektrik sinyalini optik sinyale çevirir (Ghz hızlarında veri iletimi).
* **Faz Kaydırıcılar:** Termo-optik veya plazma dispersiyon etkisi ile ışığın fazını değiştirir.
* **Fotodedektörler:** Işığı tekrar elektriğe dönüştüren p-n veya p-i-n eklemleri.

## 📐 Tasarım ve Layout Süreci

PIC tasarımı genellikle bir simülasyon-layout döngüsünden oluşur:
1. **Mod Analizi:** Dalga kılavuzu geometrisinin belirlenmesi (Lumerical, Meep).
2. **Devre Simülasyonu:** Bileşenlerin birbirleriyle olan etkileşimi (Interconnect, Caphe).
3. **Layout (Maske Tasarımı):** Çip fabrikasyonu için GDSII formatında çizim (gdsfactory, Nazca).

## 💻 Mevcut Kodlar

* `/pasif-bilesenler/ring_resonator.py`: Halka rezonatör spektrum analizi.
* `/pasif-bilesenler/mach_zehnder_interferometer.py`: MZI geçirim spektrumu ve faz duyarlılığı.
* `/pic-tasarim-layout/`: gdsfactory tabanlı otomatik layout üretim örnekleri (hazırlanıyor).

## 📖 Temel Kitaplar
1. Chrostowski, L., & Hochberg, M., "Silicon Photonics Design".
2. Coldren, L. A., "Diode Lasers and Photonic Integrated Circuits".
