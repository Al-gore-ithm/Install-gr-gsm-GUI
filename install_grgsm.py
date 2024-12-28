import subprocess
import sys

# Function to ensure tkinter is installed
def ensure_tkinter_installed():
    try:
        # Check if tkinter is available
        import tkinter
    except ImportError:
        print("The 'tkinter' module is not installed. Attempting to install it...")
        try:
            subprocess.check_call(["sudo", "apt", "install", "-y", "python3-tk"])
            print("tkinter installed successfully. Restarting the script...")
            # Restart the script after tkinter is installed
            subprocess.check_call([sys.executable] + sys.argv)
            sys.exit(0)
        except subprocess.CalledProcessError as e:
            print(f"Failed to install 'tkinter': {e}. Please install it manually using:")
            print("sudo apt install python3-tk")
            sys.exit(1)

# Ensure tkinter is installed
ensure_tkinter_installed()

# Import tkinter after ensuring it's installed
import tkinter as tk
from tkinter import messagebox

# Function to install dependencies for gr-gsm
def install_dependencies():
    dependencies = (
        "cmake git autoconf libtool pkg-config build-essential "
        "python3-docutils libcppunit-dev swig doxygen liblog4cpp5-dev gr-osmosdr libosmogsm18 "
        "libosmocodec0 libosmogsm-doc libosmosdr0 libosmocodec-doc libosmosdr-dev libosmocoding0 "
        "libosmocoding-doc libosmocore libosmocore19 libosmocore-dev libosmocore-doc "
        "libosmocore-utils libosmoctrl0 libosmoctrl-doc liborc-0.4-dev libpthread-workqueue-dev "
        "libpthread-stubs0-dev libvolk-dev libvolk3.1"
    )
    try:
        subprocess.check_call(["sudo", "apt", "update"])
        subprocess.check_call(["sudo", "apt", "install", "-y"] + dependencies.split())
        messagebox.showinfo("Success", "Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to install dependencies:\n\n{e}")

# Function to install gr-gsm
def install_gr_gsm():
    commands = (
        "git clone https://github.com/bkerler/gr-gsm.git && "
        "cd gr-gsm && mkdir build && cd build && cmake .. && "
        "make -j$(nproc) && sudo make install && sudo ldconfig"
    )
    try:
        subprocess.check_call(commands, shell=True)
        messagebox.showinfo("Success", "gr-gsm installed successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to install gr-gsm:\n\n{e}")

# GUI for installation
def create_gui():
    root = tk.Tk()
    root.title("Install gr-gsm")

    tk.Label(root, text="Install gr-gsm and Dependencies", padx=10, pady=10).pack()

    # Install dependencies button
    tk.Button(
        root,
        text="Install Dependencies",
        command=install_dependencies,
        padx=20,
        pady=10,
    ).pack(pady=5)

    # Install gr-gsm button
    tk.Button(
        root,
        text="Install gr-gsm",
        command=install_gr_gsm,
        padx=20,
        pady=10,
    ).pack(pady=5)

    # Exit button
    tk.Button(root, text="Exit", command=root.quit, padx=20, pady=10).pack(pady=5)

    root.mainloop()

# Main function
if __name__ == "__main__":
    create_gui()
