# bot_adsterra.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

def open_adsterra_links(links, proxies=None):
    """
    Membuka link Adsterra dengan opsi proxy rotasi.

    Parameters:
        links (list): Daftar URL Adsterra untuk dikunjungi.
        proxies (list): Daftar proxy (opsional).
    """
    for idx, link in enumerate(links):
        try:
            # Konfigurasi Selenium
            chrome_options = Options()
            chrome_options.add_argument("--headless")  # Mode tanpa tampilan browser (opsional)

            # Atur proxy jika diberikan
            if proxies:
                proxy = random.choice(proxies)
                chrome_options.add_argument(f'--proxy-server={proxy}')
                print(f"[INFO] Menggunakan proxy: {proxy}")

            # Path ke ChromeDriver
            driver_path = "path/to/chromedriver"  # Ganti dengan path ChromeDriver Anda
            driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

            # Membuka link
            print(f"[INFO] Membuka link {idx + 1}/{len(links)}: {link}")
            driver.get(link)

            # Tunggu beberapa saat
            time.sleep(random.randint(5, 10))

            # Cetak judul halaman
            print("[INFO] Judul halaman:", driver.title)

        except Exception as e:
            print(f"[ERROR] Gagal membuka link: {link} | Error: {e}")

        finally:
            driver.quit()

if __name__ == "__main__":
    # Daftar link Adsterra
    ad_links = [
        "https://your-adsterra-link1.com",
        "https://your-adsterra-link2.com",
    ]

    # Daftar proxy (opsional)
    proxy_list = [
        "http://proxy1:port",
        "http://proxy2:port",
    ]

    # Jalankan bot
    open_adsterra_links(ad_links, proxies=proxy_list)
