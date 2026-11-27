import pandas as pd
from django import forms
from django.conf import settings

df = pd.read_csv(settings.BASE_DIR / "wine.csv")
fitur = df.drop(columns="kelas")


class WineForm(forms.Form):
    # Membuat 13 isian: batas = min dan max data, nilai awal = median
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for nama in fitur.columns:
            self.fields[nama] = forms.FloatField(
                label=nama,
                min_value=float(fitur[nama].min()),
                max_value=float(fitur[nama].max()),
                initial=float(fitur[nama].median()),
            )
