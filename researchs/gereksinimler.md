# Proje Gereksinimleri ve Analiz

## İşlevsel Gereksinimler
1. Kullanıcıdan bir paket ismi alınmalıdır.
2. Alınan isim `apt search`, `snap find` ve `flatpak search` komutlarına parametre olarak geçilmelidir.
3. Dönen ham metin verisi (stdout) Python string metodları ile parse edilmelidir.
4. Sonuçlar kullanıcıya renkli ve okunabilir bir tablo formatında sunulmalıdır.

## Sistem Gereksinimleri
- İşletim Sistemi: Ubuntu 22.04 LTS
- Dil: Python 3.10+
- Bağımlılıklar: Standart Python kütüphaneleri (subprocess, json, sys).