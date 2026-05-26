# Termux-battery-Tool
Test your charger, spot broken cables, and monitor phone temperature.

• **🛠️ Installation & Usage**

First install Python and Termux API support:
```
pkg update -y
pkg install python termux-api -y
```
Install git if you havent:
```
pkg install git
```
1: Make sure you also install the Termux:API app on your phone
You can find the apk here:
https://github.com/termux/termux-api

~ Then clone the repo and run the tool:
```
git clone https://github.com/webcodepirat-netizen/Termux-battery-Tool
cd Termux-battery-Tool
python check.py
```
This tool tells you the absolute truth about your charger and your cable on the spot.

<img src="https://github.com/user-attachments/assets/db8fb9ec-7bbb-429d-9798-952b7ce7afca">


---

## 🎯 Test Your Cable and Charger Block

This script is built to do one main thing: show you if your charging gear is broken or working.

• **Spot Bad Cables & Weak Bricks:**
If your cable is ripped inside or your wall plug is cheap, your phone will say "Charging" but the battery will stay stuck or drop. This tool catches that immediately.

• **The 3 Simple Rules:**

🟢 **YES. It WILL go up.**
Your charger is good. Your battery is actually filling up right now.

🟡 **It wont move.**
Your charger is way too weak. The battery percentage is going to stay stuck.

🔴 **NO. It will not go up.**
Your phone is using power faster than the plug can give it. Your phone is going to drain and die while plugged in.

Simple, accurate, and straight to the point.

---

## 🔥 Other Cool Stuff It Does

• **Phone Too Hot?:** It monitors your exact phone temperature. If your phone gets dangerously hot, it warns you immediately so you don't damage your hardware.

• **No Lag:** It is super lightweight. It doesn't slow down your device and closes cleanly the exact second you hit Enter or Ctrl+C.

• Tracks how long your phone has been running since the last restart

• Shows last phone reboot uptime
---
