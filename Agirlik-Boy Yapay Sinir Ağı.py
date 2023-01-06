
# İki giriş düğümü (ağırlık ve boy) ve bir çıktı düğümü (cinsiyet, 0 veya 1 olarak temsil edilir) içerir. "train" işlevi, giriş ve hedeflerle bir veri kümesini kullanarak sinir ağını eğitir ve tahmin edilen çıktı ile hedef değerler arasındaki hata kullanarak ağırlık ve bias değerlerini günceller."predict" işlevi daha sonra eğitilmiş ağırlıklar ve sapmalar kullanılarak yeni girdiler üzerinde tahminler yapmak için kullanılabilir.Giriş verilerinin, iki sütun (ağırlık ve boy(weight-height)) ve bir etiket sütunu (cinsiyet(gender)) içeren bir CSV dosyasında olduğu varsayılır. Veriler, modeli eğitmek için kullanılmadan önce normalleştirilir. Kod daha sonra modeli veriler üzerinde eğitir ve modelin performansını değerlendirmek için aynı veriler üzerinde tahminler yapar.


import numpy as np

def sigmoid(x):
  return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
  return x * (1 - x)

def train(inputs, targets, epochs, learning_rate):
  # Rastgele ağırlık ve bias değerleri oluştur
  weights = np.random.uniform(-1, 1, size=(inputs.shape[1], 1))
  biases = np.random.uniform(-1, 1, size=1)
  for epoch in range(epochs):
    # Öngörüleri hesapla
    output = sigmoid(np.dot(inputs, weights) + biases)
    # Hata hesapla
    error = targets - output
    # Ağırlık ve bias değerlerini güncelle
    update = error * sigmoid_derivative(output)
    weights += learning_rate * np.dot(inputs.T, update)
    biases += learning_rate * np.sum(update)
  # Güncellenmiş ağırlık ve bias değerlerini döndür
  return weights, biases

def predict(inputs, weights, biases):
  # Öngörüleri hesapla
  return sigmoid(np.dot(inputs, weights) + biases)

if __name__ == "__main__":
  # Veriyi yükle
  data = np.genfromtxt('weight-height.csv', delimiter=',')
  inputs = data[:, :-1]
  targets = data[:, -1:]
  # Girişleri normalize et
  inputs = (inputs - np.mean(inputs)) / np.std(inputs)
  # Modeli eğit
  weights, biases = train(inputs, targets, epochs=1000, learning_rate=0.5)
  # Modeli test et
  prediction = predict(inputs, weights, biases)
  for i in range(prediction.shape[0]):
    print(f'Prediction: {prediction[i, 0]:.4f}, Target: {targets[i, 0]:.4f}')
    
  #sehmusbulut
  
  
