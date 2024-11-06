import os
import winreg as reg

def add_to_startup(file_path):
    # Modify the path to the .bat file
    bat_file = os.path.join(file_path, "omid_fantastic_debuger.bat")
    
    try:
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_WRITE)
        reg.SetValueEx(reg_key, "MyServerStartup", 0, reg.REG_SZ, bat_file)
        reg.CloseKey(reg_key)
        print("Startup entry added successfully!")
    except Exception as e:
        print(f"Failed to add startup entry: {e}")

if __name__ == "__main__":
    add_to_startup(os.path.dirname(os.path.realpath(__file__)))
