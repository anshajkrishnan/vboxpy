import os
import subprocess
import platform
from log import *
import sys


def install_virtualbox():
    system = platform.system()
    logger.info(f"platform is {str(system)}")
    if system == 'Windows':
        logger.warning("Please download and install VirtualBox manually from https://www.virtualbox.org/wiki/Downloads \n")
    elif system == 'Linux':
        logger.info("Installing Virtual Box On Linux\n")
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'virtualbox'], check=True)
        logger.info(f"Virtual Box Installed Succesfully \n")
    else:
        print(f"Unsupported Os")


def create_vm(vm_name, os_type, memory, disk_size, iso_path):
    logger.info(f"Creating Virtual Machine {vm_name}")
    subprocess.run(['VBoxManage', 'createvm', '--name', vm_name, '--ostype', os_type, '--register'], check=True)
    subprocess.run(
        ['VBoxManage', 'modifyvm', vm_name, '--memory', str(memory), '--vram', '16', '--nic1', 'nat', '--natpf1',
         'ssh,tcp,,2222,,22'])
    subprocess.run(['VBoxManage', 'createhd', '--filename', f"{vm_name}.vdi", '--size', str(disk_size)], check=True)
    subprocess.run(['VBoxManage', 'storagectl', vm_name, '--name', 'SATA Controller', '--add', 'sata', '--controller',
                    "IntelAhci"], check=True)

    subprocess.run(
        ['VBoxManage', 'storageattach', vm_name, '--storagectl', 'SATA Controller', '--port', '1', '--device', '0',
         '--type', 'hdd', '--medium', f'{vm_name}.vdi'], check=True)

    # Attach Manually Downloaded ISO File

    subprocess.run(['VBoxManage', 'storagectl', vm_name, '--name', 'IDE Controller', '--add', 'ide'], check=True)

    subprocess.run(
        ['VBoxManage', 'storageattach', vm_name, '--storagectl', 'IDE Controller', '--port', '1', '--device', '0',
         '--type', 'dvddrive', '--medium', iso_path], check=True)
    logger.info(f"VM {vm_name} created and iso image attached succesfully")

    # start vm

    subprocess.run(['VBoxManage', 'startvm', vm_name, '--type', 'gui'], check=True)
    logger.critical(f"VM {vm_name} Started ...")


if __name__ == '__main__':
    vm_name = input(f"Enter VM Name: ")
    install_virtualbox()
    sys.stdout.flush()
    choices = ['Ubuntu_64', 'Windows_64']
    print("Select Os Type")
    for i, choice in enumerate(choices, 1):
        print(f"{i}.{choice}")
    selection = int(input("Enter your choice(1-2): "))
    os_type = choices[selection - 1]
    memory = int(input(f"Enter Memory Size(MB): "))
    disk_size = int(input(f"Enter Disk Size (MB): "))
    iso_path = input(f"Enter path to iso image")
    create_vm(vm_name, os_type, memory, disk_size, iso_path)
