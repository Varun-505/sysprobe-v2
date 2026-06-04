import psutil
import time

def bytes_to_gb(bytes_value):
    return round(bytes_value / (1024 ** 3), 2)

def cpu_info():
    return psutil.cpu_percent(interval=1)

def memory_info():
    mem = psutil.virtual_memory()
    return {
        "total_gb": bytes_to_gb(mem.total),
        "used_gb": bytes_to_gb(mem.used),
        "percent": mem.percent
    }

def disk_info():
    disk = psutil.disk_usage('/')
    return {
        "total_gb": bytes_to_gb(disk.total),
        "used_gb": bytes_to_gb(disk.used),
        "percent": disk.percent
    }

def top_processes(n=5):
    processes = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(p.info)
        except:
            pass

    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)
    return processes[:n]

def main():
    print("\n==============================")
    print("   SYS PROBE - SYSTEM INFO   ")
    print("==============================\n")

    print(f"CPU Usage: {cpu_info()}%")

    mem = memory_info()
    print(f"Memory: {mem['used_gb']}GB / {mem['total_gb']}GB ({mem['percent']}%)")

    disk = disk_info()
    print(f"Disk: {disk['used_gb']}GB / {disk['total_gb']}GB ({disk['percent']}%)")

    print("\nTop Processes:")
    for p in top_processes():
        print(f"PID {p['pid']} - {p['name']} - CPU {p['cpu_percent']}%")

    print("\n==============================\n")

if __name__ == "__main__":
    main()