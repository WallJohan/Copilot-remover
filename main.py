import subprocess
import winreg
import ctypes
import sys
# Check if the script is running as administrator
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # If not running as administrator, relaunch the script with admin privileges
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)

print("1 Disabling")
selection = input("Enter an option")
while selection != "4":
        print("1 Disable Chat")
        print("2 Disable Copilot")
        print("3 Disable Bing Chat")
        print("4 Exit")
        selection = input("Enter an option: ")


        if selection == "1":
            # The CMD command you want to execute
            cmd_command = 'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /f /v TaskbarMn /t REG_DWORD /d 0 && REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Chat" /f /v ChatIcon /t REG_DWORD /d 3'

            # Execute the CMD command
            try:
                result = subprocess.check_output(cmd_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                print("Command output:")
                print(result)
            except subprocess.CalledProcessError as e:
                print(f"Command execution failed with error code {e.returncode}")
                print(f"Error output:\n{e.output}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
            cmd_command1 = 'REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Chat" /f /v ChatIcon /t REG_DWORD /d 3'
        elif selection == "2":
            print("Option 2 selected")
            cmd_command = 'REG ADD HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\WindowsCopilot1 /f /v TurnOffWindowsCopilot1 /t REG_DWORD /d 1'
            try:
                result = subprocess.check_output(cmd_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                print("Command output:")
                print(result)
            except subprocess.CalledProcessError as e:
                print(f"Command execution failed with error code {e.returncode}")
                print(f"Error output:\n{e.output}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
        elif selection == "3":
            cmd_command = 'REG ADD HKEY_CURRENT_USER\Software\Policies\Microsoft\Edge /f /v HubSidebarEnabled /t REG_DWORD /d 0'
            try:
                result = subprocess.check_output(cmd_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                print("Command output:")
                print(result)
            except subprocess.CalledProcessError as e:
                print(f"Command execution failed with error code {e.returncode}")
                print(f"Error output:\n{e.output}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
        input("press enter to continue")
else:
    print("Press enter to exit")