# light-utils-py
Kumpulan utilitas Python kecil yang ringan, praktis, dan mudah dikembangkan. Cocok sebagai starter repo untuk belajar kontribusi open-source.


## Fitur
- Konversi waktu (detik → HH:MM:SS)
- Fungsi aman untuk membaca/menulis JSON
- Slugify & pembersihan teks
- Hashing (SHA256, MD5)
- Generator password & random string


## Instalasi
pip install -e
## Contoh Penggunaan
```python
from light_utils.time_utils import to_hms
from light_utils.string_utils import slugify


print(to_hms(3601))
print(slugify("Hello World!!"))
---


## light_utils/__init__.py
```python
from .time_utils import to_hms, ms_to_seconds
from .file_utils import read_json_safe, write_json
from .string_utils import slugify, clean_text
from .crypto_utils import sha256_hash, md5_hash
from .random_utils import generate_password, random_string
