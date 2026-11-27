import pickle

import pandas as pd
from django.conf import settings
from django.shortcuts import render

from .forms import WineForm, fitur

# Muat model yang sudah dilatih oleh train.py
with open(settings.BASE_DIR / "model.pkl", "rb") as f:
    data = pickle.load(f)
model = data["model"]


def beranda(request):
    form = WineForm(request.POST or None)
    hasil = None
    proporsi = []

    # Prediksi hanya jika form dikirim dan isinya valid
    if request.method == "POST" and form.is_valid():
        baris = pd.DataFrame([form.cleaned_data])[list(fitur.columns)]
        hasil = model.predict(baris)[0]
        peluang = model.predict_proba(baris)[0]
        proporsi = [(k, f"{p:.1%}") for k, p in zip(model.classes_, peluang)]

    konteks = {
        "form": form,
        "hasil": hasil,
        "proporsi": proporsi,
        "akurasi": f"{data['akurasi']:.2%}",
        "matriks": list(zip(model.classes_, data["matriks"].tolist())),
    }
    return render(request, "klasifikasi/index.html", konteks)
