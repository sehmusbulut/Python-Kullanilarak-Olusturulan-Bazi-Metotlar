  # Trapezoid verisi kullanılarak integral hesaplama
def integrate(f, a, b, n):
  # f: hesaplanacak integralin fonksiyonu
  # a: integralin alt sınırı
  # b: integralin üst sınırı
  # n: trapezoidların sayısı (daha fazla sayı, daha hassas bir sonuç verir)

  # Trapezoidlar arasındaki adım boyutunu hesapla
  h = (b-a) / n

  # Trapezoidların toplamını hesapla
  result = 0.0
  for i in range(n):
    result += f(a + i*h) + f(a + (i+1)*h)
  result *= h / 2
  return result
