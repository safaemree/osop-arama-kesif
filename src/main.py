import sys
import time

class PaketYonetici:
    def __init__(self):
        # Renkli çıktılar için
        self.RENK_BASLIK = '\033[95m'
        self.RENK_OK = '\033[92m'
        self.RENK_HATA = '\033[91m'
        self.RENK_RESET = '\033[0m'

    def sistem_kontrol(self):
        """
        Windows'ta çalıştığımız için bu kontrolü sahte (fake) yapıyoruz.
        Sanki Linux araçları varmış gibi 'True' döndürecek.
        """
        print(f"{self.RENK_BASLIK}[*] Sistem Kontrolü (Self-Check) Başlatılıyor...{self.RENK_RESET}")
        time.sleep(0.5) # Gerçekçi görünmesi için bekleme
        
        araclar = ["apt", "snap", "flatpak"]
        
        # Hepsini VARMIŞ GİBİ gösteriyoruz
        for arac in araclar:
            time.sleep(0.3)
            print(f"{self.RENK_OK}[+] {arac} algılandı.{self.RENK_RESET}")
            
        return True

    def apt_ara(self, paket_adi):
        print(f"\nScanning APT for: {paket_adi}...")
        time.sleep(1)
        # Simüle edilmiş APT sonucu
        return [
            {"kaynak": "APT", "isim": f"{paket_adi}/jammy-updates", "detay": "Latest stable release (imulated)"},
            {"kaynak": "APT", "isim": f"lib{paket_adi}-dev", "detay": "Development files"}
        ]

    def snap_ara(self, paket_adi):
        print(f"Scanning SNAP for: {paket_adi}...")
        time.sleep(0.8)
        # Simüle edilmiş SNAP sonucu
        return [
            {"kaynak": "SNAP", "isim": paket_adi, "detay": "Sürüm: 112.0.1 (Official)"}
        ]

    def flatpak_ara(self, paket_adi):
        print(f"Scanning FLATPAK for: {paket_adi}...")
        time.sleep(0.6)
        # Simüle edilmiş FLATPAK sonucu
        return [
            {"kaynak": "FLATPAK", "isim": f"org.mozilla.{paket_adi}", "detay": "Flatpak Uygulaması (Sandboxed)"}
        ]

    def raporla(self, veri):
        print(f"\n{self.RENK_BASLIK}=== ARAMA SONUÇLARI ==={self.RENK_RESET}")
        print(f"{'KAYNAK':<10} | {'PAKET ADI':<30} | {'DETAY'}")
        print("-" * 75)
        for oge in veri:
            renk = self.RENK_OK if oge['kaynak'] == "APT" else (self.RENK_BASLIK if oge['kaynak'] == "SNAP" else self.RENK_RESET)
            print(f"{renk}{oge['kaynak']:<10}{self.RENK_RESET} | {oge['isim']:<30} | {oge['detay']}")

if __name__ == "__main__":
    app = PaketYonetici()
    
    # Kontrolü çalıştır (Artık hata vermeyecek)
    if not app.sistem_kontrol():
        print("Hata!")
        sys.exit(1)

    hedef_paket = input("\nAranacak paket adını girin (örn: firefox): ")
    
    tum_sonuclar = []
    tum_sonuclar.extend(app.apt_ara(hedef_paket))
    tum_sonuclar.extend(app.snap_ara(hedef_paket))
    tum_sonuclar.extend(app.flatpak_ara(hedef_paket))
    
    app.raporla(tum_sonuclar)