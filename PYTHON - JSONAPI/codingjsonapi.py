import json

data = {"nama": "Zahra", "umur": 18}
json_str = json.dumps(data)
print(json_str)

python_obj = json.loads(json.str)
print(python_obj["nama"])

# kalau angka gak usah pake tanda petik, tanda petik dipake buat huruf aja
# kalau mau import json, nama file pythonnya jangan json juga karena nanti bingung mau import json yang mana
# json alat bantu dari python, tapi harus nulis codingannya sendiri, tetep harus nulis codingannya sendiri karena biar tau buat apa datanya ini
# ibarat kotak peralatan