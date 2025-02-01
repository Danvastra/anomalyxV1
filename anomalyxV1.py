import requests
import time
import nmap
from colorama import Fore, init

# Inisialisasi colorama
init(autoreset=True)

# ini Tools 1
def dapet_ip_info():
    try:
        # pake layanan API ipinfo.io untuk mendapatkan informasi IP nya
        response = requests.get('https://ipinfo.io/json')
        data = response.json()

        ip = data.get('ip')
        city = data.get('city')
        region = data.get('region')
        country = data.get('country')
        loc = data.get('loc')  # Lokasi GPS (latitude, longitude)
        
        #hasil nyee
        print(f"IP Address: {ip}")
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"Location (GPS): {loc}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

#ini tools 2
# Fungsi untuk memindai jaringan dengan nmap
def scan_network(ip_range):
    # Membuat objek scanner nmap
    nm = nmap.PortScanner()

    # Memindai rentang IP pada jaringan
    nm.scan(hosts=ip_range, arguments='-sn')  # -sn berarti hanya melakukan ping scan (tanpa port scan)

    # Menampilkan hasil pemindaian
    devices_list = []
    for host in nm.all_hosts():
        # Mendapatkan informasi host
        host_name = nm[host].hostname() if nm[host].hostname() else "Unknown"
        
        device_info = {
            "ip": host,
            "hostname": host_name,
            "status": nm[host].state()
        }
        devices_list.append(device_info)

    return devices_list

# Fungsi untuk menampilkan hasil pemindaian
def display_result(devices_list):
    print("Perangkat yang terhubung ke jaringan Wi-Fi:")
    print("IP Address\t\tHostname\t\tStatus")
    print("--------------------------------------------")
    for device in devices_list:
        print(f"{device['ip']}\t\t{device['hostname']}\t\t{device['status']}")





# ini tools 3
def dapet_ip(ip_address):
    # Menggunakan API ipinfo.io untuk mendapatkan informasi tentang IP address
    url = f"http://ipinfo.io/{ip_address}/json"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Menampilkan informasi dasar terkait IP
        if response.status_code == 200:
            print(f"Informasi IP Address {ip_address}:")
            print(f"IP: {data.get('ip')}")
            print(f"Hostname: {data.get('hostname')}")
            print(f"Location: {data.get('city')}, {data.get('region')}, {data.get('country')}")
            print(f"Org: {data.get('org')}")
        else:
            print(f"Gagal mendapatkan data untuk IP {ip_address}")
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan: {e}")




# ini menu utama
while True:
    time.sleep(3)
    print("\n")
    print(Fore.YELLOW + " + Anomalyx Tools v1 by Danvertt + ")
    print("\n")
    print("This Tools :")
    print("[1] Auto Check My IP Address")
    print("[2] Scanning IP Address")
    print("[3] Track IP Address")
    print("[4] Exit the Tools")
    print("\n")

    inputUser = (input("Please Select the Tools(Ex. 1/2) : "))
    time.sleep(3)
    print("\n")
    if inputUser == "1":
        dapet_ip_info()
    elif inputUser == "2":
        # Menentukan rentang IP yang ingin dipindai (misalnya 180.244.62.0/24 untuk jaringan lokal Anda)
        ip_range = "180.244.62.0/24"  # Rentang IP yang sesuai dengan jaringan Anda
        # Memanggil fungsi untuk melakukan pemindaian
        devices = scan_network(ip_range)
        # Menampilkan hasil pemindaian
        display_result(devices)
        
    elif inputUser == "3":
        # Program utama
        if __name__ == "__main__":
            ip_address = input("Masukkan IP address: ")
            dapet_ip(ip_address)
    elif inputUser == "4":
        print("Thanks For the Using This Program Tools!")
        break
    else:
        print("Error this Program, Please Try Again!")
        print("\n")

