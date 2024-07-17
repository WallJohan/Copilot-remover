import subprocess
import winreg
import ctypes
import sys
import tkinter as tk
from tkinter import messagebox

# Check if the script is running as administrator
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def execute_command(cmd_command):
    try:
        result = subprocess.check_output(cmd_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        messagebox.showinfo("Command output", result)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Command execution failed", f"Error code: {e.returncode}\nError output:\n{e.output}")
    except Exception as e:
        messagebox.showerror("An error occurred", str(e))

def disable_chat():
    cmd_command = 'REG ADD "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /f /v TaskbarMn /t REG_DWORD /d 0 && REG ADD "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Chat" /f /v ChatIcon /t REG_DWORD /d 3'
    execute_command(cmd_command)

def disable_copilot():
    cmd_command = 'REG ADD HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\WindowsCopilot1 /f /v TurnOffWindowsCopilot1 /t REG_DWORD /d 1'
    execute_command(cmd_command)

def disable_bing_chat():
    cmd_command = 'REG ADD HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Edge /f /v HubSidebarEnabled /t REG_DWORD /d 0'
    execute_command(cmd_command)

if not is_admin():
    # If not running as administrator, relaunch the script with admin privileges
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)

# GUI setup
root = tk.Tk()
root.title("Registry Modification Tool")

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

tk.Label(frame, text="Choose an option:").pack(pady=10)

btn_disable_chat = tk.Button(frame, text="Disable Chat", command=disable_chat)
btn_disable_chat.pack(fill=tk.X, pady=5)

btn_disable_copilot = tk.Button(frame, text="Disable Copilot", command=disable_copilot)
btn_disable_copilot.pack(fill=tk.X, pady=5)

btn_disable_bing_chat = tk.Button(frame, text="Disable Bing Chat", command=disable_bing_chat)
btn_disable_bing_chat.pack(fill=tk.X, pady=5)

btn_exit = tk.Button(frame, text="Exit", command=root.quit)
btn_exit.pack(fill=tk.X, pady=20)

root.mainloop()
