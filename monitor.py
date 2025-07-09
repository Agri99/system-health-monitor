import psutil
import datetime

def log_system_status():
    now = datetime.datetime.now()
    log_file = "system-health.log"

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    with open(log_file, "a") as f:
        f.write(f"=== {now.strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        f.write(f"CPU Usage: {cpu}%\n")
        f.write(f"RAM Usage: {ram.percent}% ({ram.used // (1024**2)}MB used of{ram.total // (1024**2)}MB) \n")
        f.write(f"Disk Usage: {disk.percent}% ({disk.used // (1024**3)}GB used of {disk.total // (1024**3)}GB)\n\n")


if __name__ == "__main__":
    log_system_status()
    print("System status logged successfully.")

