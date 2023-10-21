import psutil as pst
import platform as plt
import GPUtil as GPU

uname = plt.uname()

def getInfoSystem():
    print(f"System name: {uname.system}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}\n")

def getNamePC():
    print(f"Computer name: {uname.node}\n")

def getInfoCPU():
    print(f"Processor name: {uname.processor}")
    print(f"Physical CPUs: {pst.cpu_count(logical=False)}")
    print(f"Logical CPUs: {pst.cpu_count()}")

    freqCPU = pst.cpu_freq()
    print(f"CPU frequence max: {freqCPU.max / 1000} GHz")
    print(f"CPU frequence min: {freqCPU.min / 1000} GHz\n")

def getInfoMemory():
    print(f"Total memory: {round(pst.virtual_memory().total / 1000000000, 3)} GB")
    print(f"Used memory: {round(pst.virtual_memory().used / 1000000000, 3)} GB")
    print(f"Free memory: {round(pst.virtual_memory().free / 1000000000, 3)} GB")
    print(f"Total swap memory: {round(pst.swap_memory().total / 1000000000, 3)} GB")
    print(f"Used swap memory: {round(pst.swap_memory().used / 1000000000, 3)} GB")
    print(f"Free swap memory: {round(pst.swap_memory().free / 1000000000, 3)} GB\n")

def getInfoDisks():
    disks = pst.disk_partitions(all = False)
    for disk in disks:
        print(f"Disk name: {disk.device}")
        print(f"Mountpoint: {disk.mountpoint}")
        print(f"File system type: {disk.fstype}")
        print(f"Disk total space: {round(pst.disk_usage(disk.mountpoint).total / 1000000000, 3)} GB")
        print(f"Disk used space: {round(pst.disk_usage(disk.mountpoint).used / 1000000000, 3)} GB")
        print(f"Disk free space: {round(pst.disk_usage(disk.mountpoint).free / 1000000000, 3)} GB\n")

def getInfoGPU():
    gpus = GPU.getGPUs()
    for gpu in gpus:
        print(f"GPU name: {gpu.name}")
        print(f"GPU load: {gpu.load*100}%")
        print(f"GPU total memory: {gpu.memoryTotal} MB")
        print(f"GPU used memory: {gpu.memoryUsed} MB")
        print(f"GPU free memory: {gpu.memoryFree} MB")
        print(f"GPU temperature: {gpu.temperature} °C\n")

def main():
    print("="*3, "System information", "="*3)
    getInfoSystem()
    print("="*3, "PC Name", "="*3)
    getNamePC()
    print("="*3, "CPU information", "="*3)
    getInfoCPU()
    print("="*3, "Memory information", "="*3)
    getInfoMemory()
    print("="*3, "Disks information", "="*3)
    getInfoDisks()
    print("="*3, "GPU information", "="*3)
    getInfoGPU()

main()