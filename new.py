# bot_web_proxy.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import time

def visit_websites_with_proxies(websites, proxies, visits_per_website=1):
    """
    Mengunjungi website menggunakan Selenium dengan rotasi proxy dan User-Agent.

    Parameters:
        websites (list): Daftar URL website untuk dikunjungi.
        proxies (list): Daftar proxy.
        visits_per_website (int): Jumlah kunjungan per website.
    """
    for idx, website in enumerate(websites):
        for visit in range(visits_per_website):
            try:
                # Pilih proxy secara acak
                proxy = random.choice(proxies)

                # Konfigurasi Selenium
                chrome_options = Options()
                chrome_options.add_argument("--headless")  # Mode tanpa tampilan browser
                chrome_options.add_argument(f"--proxy-server={proxy}")

                # Tambahkan User-Agent acak
                user_agent = random.choice([
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                ])
                chrome_options.add_argument(f"--user-agent={user_agent}")

                # Path ke ChromeDriver
                driver_path = "path/to/chromedriver"  # Ganti dengan path ChromeDriver Anda
                driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

                # Membuka link
                print(f"[INFO] Menggunakan proxy: {proxy} dan User-Agent: {user_agent}")
                print(f"[INFO] Membuka link ({visit + 1}/{visits_per_website}) {idx + 1}/{len(websites)}: {website}")
                driver.get(website)

                # Tunggu beberapa saat untuk mensimulasikan kunjungan
                time.sleep(random.randint(5, 10))

                # Cetak judul halaman
                print("[INFO] Judul halaman:", driver.title)

            except Exception as e:
                print(f"[ERROR] Gagal mengunjungi {website} | Error: {e}")

            finally:
                driver.quit()

if __name__ == "__main__":
    # Daftar website
    website_list = [
        "http://tiny.cc/m5z2001",
        
    ]

    # Daftar proxy
    proxy_list = [
        "http://derp10-zone-custom-region-SG:derp10@107.150.117.141:6200",
    ]

    # Jumlah kunjungan per website
    visits_per_site = 3

    # Jalankan bot
    visit_websites_with_proxies(website_list, proxy_list, visits_per_website=visits_per_site)
