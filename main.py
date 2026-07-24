import subprocess
import sys
from pathlib import Path


startup_folder = (
    Path.home() / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
)

startup_file = startup_folder / "Power Settings Guardian.bat"

def get_power_settings():
    result = subprocess.run(
        ["powercfg", "/query"],
        capture_output=True,
        text=True
    )

    found_display = False

    for line in result.stdout.splitlines():
        if "Turn off display after" in line:
            found_display = True
        if found_display and "Current AC Power Setting Index" in line:
            value = line.split()
            hex_value = value[-1]
            timeout = int(hex_value, 16)
            return timeout

def set_power_settings(desired_timeout_minutes):
    subprocess.run(
        ["powercfg", "/change", "monitor-timeout-ac", str(desired_timeout_minutes)]
    )


def install_startup():
    script_path = Path(__file__).resolve()
    python_executable = sys.executable
    batch_contents = (
        f'@echo off\n'
        f'"{python_executable}" "{script_path}"'
    )

    if startup_file.exists():
        return False
    startup_file.write_text(batch_contents)
    return True

installed = install_startup()
if installed:
    print("Startup Launcher installed.")
else:
    print("Startup launcher already installed.")

current_timeout_seconds = get_power_settings()
desired_timeout_minutes = 5
desired_timeout_seconds = desired_timeout_minutes * 60

if current_timeout_seconds != desired_timeout_seconds:
    set_power_settings(desired_timeout_minutes)
    new_timeout = get_power_settings()
    if new_timeout == desired_timeout_seconds:
        print(f"Display timeout was changed - New display is {desired_timeout_minutes} minutes")
    else:
        print("Failed to update timeout time.")
else:
    print("Display timeout is correct.")