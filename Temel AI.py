# Doğrusal Regrasyon Yöntemiyle Basit ve Temel Yapay Zeka Örneği
#Bu kod, bir dizi veri kullanarak bir doğrusal regresyon modeli oluşturur ve tahminler yapar. Doğrusal regresyon, veriler arasındaki ilişkiyi ölçen bir regresyon yöntemidir ve yapay zeka algoritmaları arasında en temel olanlardan biridir.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Veri setini yükleyin
df = pd.read_csv('veri_seti.csv')

# Öznitelikleri ve hedef değişkeni ayırın
X = df.drop('hedef_degisken', axis=1)
y = df['hedef_degisken']

# Veri setini eğitim ve test kümelerine ayırın
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Doğrusal regresyon modelini oluşturun ve eğitin
model = LinearRegression()
model.fit(X_train, y_train)

# Test veri setini kullanarak tahminler yapın
predictions = model.predict(X_test)

# Tahminleri y_test ile karşılaştırın
for i, prediction in enumerate(predictions):
    print(f'Tahmin: {prediction}, Gerçek Değer: {y_test[i]}')

    
