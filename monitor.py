import psutil
import datetime
import socket
from colorama import init, Fore, Style
init(autoreset=True)

#Internet Connectivity Check
def check_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False

#Service Status Check
def check_service_running(service_name):
    for proc in psutil.process_iter(['name']):
        try:
            if service_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NosuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
                return False

#Logging System Status
def log_system_status():
    now = datetime.datetime.now()
    log_file = "system-health.log"

    cpu = psutil.cpu_percent(interval=1)
    cpu_color = Fore.RED if cpu > 85 else (Fore.YELLOW if cpu > 65 else Fore.GREEN)
    ram = psutil.virtual_memory()
    ram_color = Fore.RED if ram.percent > 90 else (Fore.Yellow if cpu > 70 else Fore.GREEN)
    disk = psutil.disk_usage('/')
    disk_color = Fore.RED if disk.percent > 90 else (Fore.Yellow if cpu > 70 else Fore.GREEN)
    internet = check_internet()
    internet_color = Fore.GREEN if internet else Fore.RED
    service_name = "sshd" #Change to what you want to monitor
    service_status = check_service_running(service_name)
    service_color = Fore.GREEN if service_status else Fore.RED
    
    with open(log_file, "a") as f:
        f.write(f"=== {now.strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        f.write(cpu_color + f"CPU Usage: {cpu}%\n")
        f.write(ram_color + f"RAM Usage: {ram.percent}% ({ram.used // (1024**2)}MB used of{ram.total // (1024**2)}MB) \n")
        f.write(disk_color + f"Disk Usage: {disk.percent}% ({disk.used // (1024**3)}GB used of {disk.total // (1024**3)}GB)\n\n")
        f.write(internet_color + f"Internet Connectivity: {'Online' if internet else 'Offline'}\n\n")
        f.write(service_color + f"Service '{service_name}':, {'Running' if service_status else 'NOT Running'}\n\n")


if __name__ == "__main__":
    log_system_status()
    print("System status logged successfully.")


