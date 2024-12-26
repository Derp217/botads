# bot_web_proxy.py
import requests
import random
import time

def visit_websites_with_proxies(websites, proxies):
    """
    Mengunjungi website menggunakan rotasi proxy.

    Parameters:
        websites (list): Daftar URL website untuk dikunjungi.
        proxies (list): Daftar proxy.
    """
    for idx, website in enumerate(websites):
        try:
            # Pilih proxy secara acak
            proxy = random.choice(proxies)
            proxy_dict = {"http": proxy, "https": proxy}
            print(f"[INFO] Menggunakan proxy: {proxy}")

            # Kirim permintaan HTTP
            response = requests.get(website, proxies=proxy_dict, timeout=10)

            # Tampilkan status kunjungan
            if response.status_code == 200:
                print(f"[INFO] Berhasil mengunjungi {website} | Status: {response.status_code}")
            else:
                print(f"[WARNING] Gagal mengunjungi {website} | Status: {response.status_code}")

            # Tunggu sebelum permintaan berikutnya
            time.sleep(random.randint(5, 10))

        except Exception as e:
            print(f"[ERROR] Error saat mengunjungi {website} | Error: {e}")

if __name__ == "__main__":
    # Daftar website
    website_list = [
        "https://www.profitablecpmrate.com/mmfky4hbp?key=97558b444c42b3ae67abc0cd2aa30622",
        "https://www.profitablecpmrate.com/fv0vzgmrsv?key=b52f4dc4a93de7a0c3dbaf45b42ed163",
    ]

    # Daftar proxy
    proxy_list = [
        "http://derp10-zone-custom-region-SG:derp10@107.150.117.141:6200",
        "http://proxy2:port",
        "http://proxy3:port",
    ]

    # Jalankan bot
    visit_websites_with_proxies(website_list, proxy_list)
