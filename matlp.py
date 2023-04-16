import numpy as np
import matplotlib.pyplot as plt

# Veri oluşturma
x = np.linspace(-10, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Çizgi grafiği
plt.figure(figsize=(8, 6))  # Grafik boyutunu ayarlama
plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)  # Çizgi grafiği oluşturma
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)  # Çizgi grafiği oluşturma
plt.plot(x, y3, label='tan(x)', color='green', linestyle=':', linewidth=2)  # Çizgi grafiği oluşturma
plt.title('Trigonometrik Fonksiyonlar')  # Grafik başlığını ayarlama
plt.xlabel('X Ekseni')  # X ekseni etiketi
plt.ylabel('Y Ekseni')  # Y ekseni etiketi
plt.legend()  # Grafikteki etiketleri gösterme
plt.grid(True)  # Kılavuz çizgilerini gösterme
plt.show()  # Grafiği görüntüleme

# Histogram
plt.figure(figsize=(8, 6))  # Grafik boyutunu ayarlama
plt.hist(y1, bins=20, alpha=0.5, label='sin(x)', color='blue')  # Histogram oluşturma
plt.hist(y2, bins=20, alpha=0.5, label='cos(x)', color='red')  # Histogram oluşturma
plt.hist(y3, bins=20, alpha=0.5, label='tan(x)', color='green')  # Histogram oluşturma
plt.title('Trigonometrik Fonksiyonların Histogramı')  # Grafik başlığını ayarlama
plt.xlabel('Değerler')  # X ekseni etiketi
plt.ylabel('Frekans')  # Y ekseni etiketi
plt.legend()  # Grafikteki etiketleri gösterme
plt.grid(True)  # Kılavuz çizgilerini gösterme
plt.show()  # Grafiği görüntüleme

# Dağılım grafiği
plt.figure(figsize=(8, 6))  # Grafik boyutunu ayarlama
plt.scatter(x, y1, label='sin(x)', color='blue', s=30, marker='o')  # Dağılım grafiği oluşturma
plt.scatter(x, y2, label='cos(x)', color='red', s=50, marker='s')  # Dağılım grafiği oluşturma
plt.scatter(x, y3, label='tan(x)', color='green', s=40, marker='^')  # Dağılım grafiği oluşturma

#Trigonometrik Fonksiyonların Dağılım Grafiği') # Grafik başlığını ayarlama
plt.xlabel('X Ekseni') # X ekseni etiketi
plt.ylabel('Y Ekseni') # Y ekseni etiketi
plt.legend() # Grafikteki etiketleri gösterme
plt.grid(True) # Kılavuz çizgilerini gösterme
plt.show() # Grafiği görüntüleme

#Bar grafiği
categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 30, 22, 18, 35]

plt.figure(figsize=(8, 6)) # Grafik boyutunu ayarlama
plt.bar(categories, values, color='purple', alpha=0.8) # Bar grafiği oluşturma
plt.title('Kategorilere Göre Değerlerin Bar Grafiği') # Grafik başlığını ayarlama
plt.xlabel('Kategoriler') # X ekseni etiketi
plt.ylabel('Değerler') # Y ekseni etiketi
plt.grid(True) # Kılavuz çizgilerini gösterme
plt.show() # Grafiği görüntüleme

#Pasta grafiği
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 25, 10, 20]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'purple']

plt.figure(figsize=(8, 6)) # Grafik boyutunu ayarlama
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140) # Pasta grafiği oluşturma
plt.title('Değerlerin Pasta Grafiği') # Grafik başlığını ayarlama
plt.show() # Grafiği görüntüleme
