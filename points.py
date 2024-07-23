import math

# 2D uzaydaki noktaları temsil eden demetlerden oluşan liste
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Tüm nokta çiftleri arasındaki mesafeleri hesapla ve 'distances' listesine ekle
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 'distances' listesinden minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print("Minimum Mesafe:", min_distance)
