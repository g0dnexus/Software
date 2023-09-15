import platform
import netifaces
import subprocess

def get_os_details():
    os_name = platform.platform()
    return os_name

def get_processor_details():
    processor = platform.processor()
    return processor

def get_device_components():
    try:
        motherboard = platform.machine()
    except:
        motherboard = "Unknown"
    try:
        graphics_card = subprocess.check_output("wmic path win32_VideoController get Name", shell=True).decode("utf-8").strip()
    except subprocess.CalledProcessError:
        graphics_card = "Unknown"
    try:
        ram = subprocess.check_output("wmic ComputerSystem get TotalPhysicalMemory", shell=True).decode("utf-8").strip()
        ram = int(ram) // (1024**3) # Convert to GB
        ram = f"{ram} GB"
    except subprocess.CalledProcessError:
        ram = "Unknown"
    try:
        hostname = platform.node()
    except:
        hostname = "Unknown"
    try:
        network_interfaces = netifaces.interfaces()
    except:
        network_interfaces = []

    return motherboard, graphics_card, ram, hostname, network_interfaces

def get_device_info():
    os_details = get_os_details()
    processor = get_processor_details()
    motherboard, graphics_card, ram, hostname, network_interfaces = get_device_components()

    print("Device details: ", os_details)
    print("Processor: ", processor)
    print("Architecture: ", motherboard)
    print("Graphics card: ", graphics_card)
    print("RAM: ", ram)
    print("Hostname: ", hostname)
    print("Network Interfaces: ", network_interfaces)
    
    print("--------------------------")
    
    print("Детали устройства: ", os_details)
    print("Процессор: ", processor)
    print("Архитектура: ", motherboard)
    print("Видеокарта: ", graphics_card)
    print("Оперативная память: ", ram)
    print("Hostname: ", hostname)
    print("Сетевые интерфейсы: ", network_interfaces)

# Получение информации об устройстве
get_device_info()
