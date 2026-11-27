import pickle

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

# 1. Baca dataset
df = pd.read_csv("wine.csv")

# 2. Preprocessing: cek data kosong
print("Jumlah data kosong:", df.isna().sum().sum())

# 3. Pisahkan fitur (X) dan target (y)
X = df.drop(columns="kelas")
y = df["kelas"]

# 4. Bagi data: 80% latih, 20% uji
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Latih model Decision Tree
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluasi pada data uji
y_pred = model.predict(X_test)
akurasi = accuracy_score(y_test, y_pred)
matriks = confusion_matrix(y_test, y_pred)
print("Data latih:", len(X_train), "| Data uji:", len(X_test))
print("Akurasi latih:", accuracy_score(y_train, model.predict(X_train)))
print("Akurasi uji:", akurasi)
print("Confusion matrix:")
print(matriks)
print(classification_report(y_test, y_pred))
print(export_text(model, feature_names=list(X.columns)))

# 7. Simpan model beserta hasil evaluasinya
with open("model.pkl", "wb") as f:
    pickle.dump({"model": model, "akurasi": akurasi, "matriks": matriks}, f)
print("Model tersimpan di model.pkl")
