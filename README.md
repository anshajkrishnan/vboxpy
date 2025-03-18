# Virtual Machine Automation with VirtualBox

This script automates the installation of VirtualBox (on Linux) and the creation of a virtual machine using `VBoxManage`. It allows users to specify VM configurations such as name, OS type, memory size, disk size, and ISO path for installation.

## Features
- Installs VirtualBox (Linux only; Windows users must install manually).
- Creates a virtual machine with specified configurations.
- Attaches an ISO file for OS installation.
- Starts the virtual machine.

## Prerequisites
- **Linux:** The script installs VirtualBox automatically.
- **Windows:** Download and install VirtualBox manually from [VirtualBox Downloads](https://www.virtualbox.org/wiki/Downloads).
- Ensure `VBoxManage` is accessible from the command line.
- Python 3 installed.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/anshajkrishnan/vboxpy.git
   cd vboxpy
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script and follow the prompts:

```bash
python vbox.py
```

### Input Parameters
- **VM Name:** Name of the virtual machine.
- **OS Type:** Choose between `Ubuntu_64` or `Windows_64`.
- **Memory Size:** Amount of RAM (in MB) allocated to the VM.
- **Disk Size:** Size of the virtual hard disk (in MB).
- **ISO Path:** Path to the OS installation ISO file.

## Example
```bash
Enter VM Name: MyUbuntuVM
Select OS Type:
1. Ubuntu_64
2. Windows_64
Enter your choice (1-2): 1
Enter Memory Size (MB): 2048
Enter Disk Size (MB): 20000
Enter path to iso image: /path/to/ubuntu.iso
```

## Logging
The script uses logging for status updates, warnings, and critical information. Logs are printed to the console.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit pull requests for enhancements or bug fixes.

