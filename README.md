# New-Spotlight-Manager

A Python script to **enable or disable** the redesigned Spotlight and Launchpad UI introduced in **macOS Tahoe beta**.

---

## Overview
This utility toggles Apple’s hidden **feature flags** for Spotlight and Launchpad. It’s ideal for developers or users who want to switch between the **new redesign** and the **classic interface**.

---

## ⚠️ Important
- This script **modifies system feature flags**.  
- **Administrator privileges required** (you’ll be prompted for your password).  
- **macOS only** — tested on Tahoe beta (macOS 26).

---

## Requirements
- macOS (Tahoe beta or later)  
- Python 3.x  
- Administrator privileges

---

## Usage

### 1. Download the script
Save the file as `spotlight.py`.

### 2. Run the script
Open Terminal and run:
```bash
python3 spotlight.py
```

3. Follow prompts
	•	Press E to enable the new UI
	•	Press D to disable and revert to classic UI
	•	Restart your Mac for changes to take effect

⸻

Disclaimer

Use at your own risk. This script edits feature flags in /Library/Preferences/FeatureFlags/Domain. While safe in testing, it’s intended for developers familiar with macOS internals.
