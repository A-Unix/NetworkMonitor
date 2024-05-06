#!/usr/bin/python3

import time
import subprocess
import os
import sys
import platform
from plyer import notification

# Check if Colorama has been already installed or not
try:
    from colorama import init, Fore
    print(Fore.LIGHTMAGENTA_EX + "Colorama has been already installed, We have initialized it for you :)")
    time.sleep(5)
except ImportError:
    print(Fore.RED + "Colorama has not been installed. Installing it...")
    subprocess.run(["pip", "install", "colorama"], check=True)
    from colorama import init, Fore
    print(Fore.LIGHTMAGENTA_EX + "Done, Colorama has been installed.")
    time.sleep(3)

# Clear the terminal screen
    os.system("clear")
    time.sleep(1)

def create_3d_banner():
    # Banner text
    banner_text = "NetworkMonitor"

    try:
        # Use figlet to create ASCII art with mono9 font
        figlet_process = subprocess.Popen(
            ["figlet", "-w", "27", "-f", "mono9", "-c", banner_text],
            stdout=subprocess.PIPE
        )
        figlet_output, _ = figlet_process.communicate()

        # Use lolcat to add color to the ASCII art
        lolcat_process = subprocess.Popen(["lolcat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        banner_output, _ = lolcat_process.communicate(input=figlet_output)

        # Print the result
        print(banner_output.decode())

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + "Error: Make sure 'figlet' and 'lolcat' are installed on your system. (Hint: Run ./setup.sh)")
        time.sleep(2)

def check_internet_connection():
    if platform.system() == "Windows":
        try:
            # Check internet connectivity on Windows
            subprocess.run(["ping", "8.8.8.8"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except subprocess.CalledProcessError:
            return False
    elif platform.system() == "Linux":
        try:
            # Check internet connectivity on Linux (Kali)
            subprocess.run(["ping", "-c", "1", "8.8.8.8"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except subprocess.CalledProcessError:
            return False
    else:
        return False

def notify_user(message):
    notification.notify(
        title="Internet Connection Status",
        message=message,
        app_icon=None,
        timeout=10
    )

def main():
    while True:
        if check_internet_connection():
            print(Fore.GREEN + "Internet is connected.")
            time.sleep(10)  # Check every 10 seconds
        else:
            print(Fore.LIGHTRED_EX + "Internet is not connected.")
            notify_user(Fore.LIGHTRED_EX + "Internet is not connected.")
            time.sleep(3)  # Check every 1 minute

if __name__ == "__main__":
    main()
