# Power Settings Guardian

Power Settings Guardian is a simple Python automation tool that ensures your Windows display timeout always stays at your preferred value.

Windows updates and power plan changes can sometimes reset display timeout settings. This application automatically checks the current display timeout and restores it if it has changed.

Starting with **v1.1.0**, the application automatically installs itself into the Windows Startup folder on first launch, allowing it to run each time Windows starts without additional setup.

---

## Features

- Checks the current Windows display timeout.
- Automatically restores the display timeout if it has changed.
- Installs itself into the Windows Startup folder.
- Prevents duplicate startup launcher installation.
- Lightweight and built entirely with Python's standard library.

---

## Requirements

- Windows 10 or Windows 11
- Python 3.14+
- Administrator privileges may be required to modify power settings depending on your system configuration.

---

## Installation

1. Clone the repository.

```bash
git clone https://github.com/yourusername/Power-Settings-Guardian.git
```

2. Navigate to the project.

```bash
cd Power-Settings-Guardian
```

3. Run the application.

```bash
python main.py
```

On the first launch, the application will automatically create a launcher in your Windows Startup folder.

---

## How It Works

1. Checks whether a startup launcher already exists.
2. Creates one if it does not.
3. Reads the current Windows display timeout.
4. Compares it to the desired timeout.
5. Updates the timeout if necessary.
6. Verifies that the change was successful.

---

## Technologies Used

- Python 3
- pathlib
- subprocess
- sys

---

## Project Structure

```
Power-Settings-Guardian/
│
├── main.py
├── README.md
└── LICENSE
```

---

## Current Version

**v1.1.0**

### Features

- Automatic Windows Startup installation
- Display timeout verification
- Automatic timeout restoration
- Startup installation detection

---

## Future Plans

- Configuration file for custom timeout values
- Additional Windows power setting management
- Logging support
- Background monitoring mode
- System tray integration

---

## License

This project is licensed under the MIT License.