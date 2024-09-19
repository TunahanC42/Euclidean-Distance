import math

print("Bu programda koordinatlarını vereceğiniz iki noktanın arasındaki mesafe Euclides yöntemi ile hesaplanacaktır.")
distances = []

def euclideanDistance(first,second):
    first=tuple(map(int,first))     # int(input...) şeklinde yazmadığımız için burada standart olarak str olan tuple larımızı "map" aracılığıyla int değer haline getiriyoruz.
    second=tuple(map(int,second))
    horDistance=abs(first[0]-second[0])
    verDistance=abs(first[1]-second[1])
    distance=math.sqrt(horDistance**2 + verDistance**2)
    distances.append(distance)


while True:
    print("Şimdi istenen koordianat değerlerini giriniz. (Çıkış için sayı dışında rastgele bir karakter giriniz.)")
    try:
        x1 = int(input("İlk noktanın x-ekseni üzerindeki koordinatını giriniz: "))
        y1 = int(input("İlk noktanın y-ekseni üzerindeki koordinatını giriniz: "))
        x2 = int(input("İkinci noktanın x-ekseni üzerindeki koordinatını giriniz: "))
        y2 = int(input("İkinci noktanın y-ekseni üzerindeki koordinatını giriniz: "))
    except ValueError:
        print("Çıkış yapılıyor...")
        break


    points = [(x1, y1), (x2, y2)]
    euclideanDistance(points[0], points[1])

print(f"Tüm mesafeler aşağıda verilmiştir:\n{distances}")
print(f"Bu mesafelerden en kısa olanı: {sorted(distances)[0]}")