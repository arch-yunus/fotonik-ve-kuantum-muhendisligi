# Faz 03: Optik İşlemciler ve Yapay Zeka (ONN)

Optik işlemciler, matris-vektör çarpımı gibi yoğun hesaplama gerektiren işlemleri ışık hızında ve ultra-düşük enerji tüketimiyle gerçekleştirmeyi hedefler. Bu bölüm, nöromorfik optik hesaplama ve Optik Sinir Ağları (ONN) üzerine odaklanır.

## 🧠 Optik Hesaplama Neden Gereklidir?

Geleneksel von Neumann mimarisi, veri taşıma (bellek darboğazı) ve ısı üretimi nedeniyle sınırlara dayanmıştır. Fotonik, şu avantajları sunar:
* **Paralellik:** Farklı dalga boyları (WDM) veya modlar kullanılarak aynı anda birden fazla işlem yapılabilir.
* **Hız:** Işığın yayılma süresi, işlem süresini belirler (latency < ns).
* **Enerji Verimliliği:** Pasif optik elemanlar (MZI ağları gibi) hesaplama sırasında neredeyse hiç enerji harcamaz.

## 🏗️ Optik Sinir Ağları (ONN) Mimarileri

### 1. Interferometrik Yapılar (Reck/Clements Mesh)
MZI birimlerinden oluşan bir matris ağı ile herhangi bir üniter matris (U) temsil edilebilir.
* **Uygulama:** Giriş vektörü ışık şiddeti veya fazı olarak kodlanır, MZI ağı içinden geçerken matris ile çarpılır.

### 2. Kırınım Tabanlı Ağlar (DONN - Diffractive ONN)
Işığın ardışık faz plakalarından (diffractive layers) geçmesiyle oluşan derin öğrenme modelidir.
* **Uygulama:** Her faz plakası bir nöron katmanı gibi davranır. Işık yayılımı fiziksel olarak çıkarım (inference) işlemini gerçekleştirir.

## 💻 Simülasyonlar

* `/optik-sinir-aglari/onn_simulation.py`: MZI tabanlı bir üniter matris çarpımı simülatörü.
* `/kirinim-islemcileri/`: Faz plakası optimizasyonu (hazırlanıyor).

## 📖 Literatür Takibi
1. Shen, Y., et al., "Deep learning with coherent optical neural networks," Nature Photonics (2017).
2. Lin, X., et al., "All-optical machine learning using diffractive deep neural networks," Science (2018).
3. Shainline, J. M., et al., "Optoelectronic exponential-integrate-and-fire neurons," Applied Physics Letters.
