import socket
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    """Menampilkan banner aplikasi dengan warna."""
    banner = f"""
    {Fore.CYAN}================================
        {Fore.GREEN}FSoftLoc - IP Locator
    {Fore.CYAN}================================
    """
    print(banner)

def get_ip_from_domain(domain):
    """Mengambil alamat IP dari nama domain."""
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def get_location_from_ip(ip):
    """Mengambil lokasi berdasarkan alamat IP menggunakan ip-api.com."""
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                return {
                    "IP": ip,
                    "Country": data.get("country"),
                    "Region": data.get("regionName"),
                    "City": data.get("city"),
                    "ISP": data.get("isp"),
                    "Lat": data.get("lat"),
                    "Lon": data.get("lon")
                }
            else:
                return {"Error": data.get("message")}
        else:
            return {"Error": "Failed to connect to the API."}
    except requests.RequestException as e:
        return {"Error": str(e)}

def main():
    print_banner()

    while True:
        user_input = input(f"{Fore.YELLOW}Ketik 'fadelkeren' untuk melanjutkan: ")
        if user_input.strip().lower() == "fadelkeren":
            print(f"{Fore.GREEN}Akses diterima! Selamat menggunakan FSoftLoc!")
            break
        else:
            print(f"{Fore.RED}Akses ditolak! Coba lagi.")

    domain = input(f"{Fore.MAGENTA}Masukkan nama domain (contoh: google.com): ")
    ip_address = get_ip_from_domain(domain)
    if ip_address:
        print(f"{Fore.GREEN}Alamat IP untuk {domain}: {Fore.CYAN}{ip_address}")
        location_info = get_location_from_ip(ip_address)
        if "Error" in location_info:
            print(f"{Fore.RED}Error: {location_info['Error']}")
        else:
            print(f"{Fore.BLUE}Informasi Lokasi:")
            for key, value in location_info.items():
                print(f"{Fore.YELLOW}{key}: {Fore.CYAN}{value}")
    else:
        print(f"{Fore.RED}Gagal mendapatkan alamat IP. Pastikan domain valid.")

if __name__ == "__main__":
    main()
