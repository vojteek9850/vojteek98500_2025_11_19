import sys
import os
import random
import json
import socket
from datetime import datetime
from urllib.request import urlopen, Request


def get_public_ip():
    """Získá veřejnou IP adresu pomocí api.ipify.org."""
    try:
        with urlopen("https://api.ipify.org?format=json", timeout=5) as r:
            data = json.loads(r.read().decode())
            return data.get("ip", "Unknown")
    except Exception:
        return "Unknown"


def get_local_ip():
    """Získá lokální IP adresu (např. 192.168.x.x)."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Neposílá se nic — jde jen o zjištění IP použité pro výstup ven
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "Unknown"


def download(url, target_path):
    """Stáhne obsah z URL do souboru."""
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=10) as response:
            data = response.read()

        with open(target_path, "wb") as f:
            f.write(data)
        return True

    except Exception as e:
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(f"Download failed: {e}\n")
        return False


def main():
    # Náhodný zdroj
    sources = [
        "https://www.bbc.com/news",
        "https://edition.cnn.com",
        "https://www.reuters.com/world",
        "https://apnews.com",
        "https://www.novinky.cz",
        "https://www.seznamzpravy.cz",
        "https://www.idnes.cz",
    ]

    chosen_url = random.choice(sources)

    script_dir = os.path.dirname(os.path.abspath(__file__))

    article_file = os.path.join(script_dir, "downloaded_article.html")
    log_file = os.path.join(script_dir, "run_info.txt")

    # Stažení článku
    download(chosen_url, article_file)

    # IP adresy
    public_ip = get_public_ip()
    local_ip = get_local_ip()

    # Log
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write(f"Random source: {chosen_url}\n")
        f.write(f"Script directory: {script_dir}\n")
        f.write(f"Python executable: {sys.executable}\n")
        f.write(f"Python version: {sys.version}\n")
        f.write(f"Public IP: {public_ip}\n")
        f.write(f"Local IP: {local_ip}\n")

    print("Hotovo! Soubor downloaded_article.html a run_info.txt byly vytvořeny.")


if __name__ == "__main__":
    main()