import subprocess
import json
import time
import os
import sys
import select
import signal
CYAN="\033[96m"
GREEN="\033[92m"
YELLOW="\033[93m"
RED="\033[91m"
MAGENTA="\033[95m"
WHITE="\033[97m"
DARK_GRAY="\033[90m"
BOLD="\033[1m"
BLINK="\033[5m"
RESET="\033[0m"
CYBER_PINK="\033[38;2;255;0;127m"
DRACULA_PURPLE="\033[38;2;189;147;249m"
SYNTH_TANGERINE="\033[38;2;255;133;51m"
NORD_BLUE="\033[38;2;136;192;208m"
def get_data():
    try:
        res = subprocess.run(['termux-battery-status'], capture_output=True, text=True)
        return json.loads(res.stdout)
    except:
        return None
def get_uptime_str():
    try:
        res = subprocess.run(['uptime', '-p'], capture_output=True, text=True)
        if res.returncode == 0:
            return res.stdout.strip().replace("up ", "")
        return "N/A"
    except:
        return "N/A"
def clear():
    os.system('clear')
def make_bar(pct, length=25):
    filled = int(pct * length / 100)
    bar = "█" * filled + "░" * (length - filled)
    return bar
def flush_input():
    try:
        import termios
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
    except:
        pass
def silent_exit(signum, frame):
    try:
        flush_input()
        os.system('tput cnorm')
        os.system('clear')
    except:
        pass
    sys.exit(0)
signal.signal(signal.SIGINT, silent_exit)
signal.signal(signal.SIGTERM, silent_exit)
try:
    os.system('tput civis')

    while True:
        data = get_data()
        if not data:
            print("Failed to get battery data.")
            break
        raw_curr = data['current']
        temp = data['temperature']
        pct = data['percentage']
        status = data['status']
        plugged = data['plugged']
        health = data['health']
        voltage = data['voltage']
        uptime_str = get_uptime_str()
        power_mw = (raw_curr * voltage) / 1000000
        curr_str = f"+{raw_curr:,}" if raw_curr >= 0 else f"{raw_curr:,}"
        if temp >= 44.0:
            temp_color = f"{BOLD}{RED}{BLINK}"
        elif temp >= 41.0:
            temp_color = RED
        elif temp >= 39.0:
            temp_color = YELLOW
        else:
            temp_color = GREEN
        if pct <= 20:
            bar_color = RED
        elif pct <= 50:
            bar_color = YELLOW
        else:
            bar_color = GREEN
        clear()
        print(f"════════════════════════════════════════════")
        print(f"{CYAN}TERMUX {GREEN}BATTERY{CYAN} MONITOR{RESET}")
        print(f"{DARK_GRAY}Last phone reset was in{RED}: \n{GREEN}{uptime_str} {RESET}ago{RED}.{RESET}")
        print(f"════════════════════════════════════════════\n")
        print(f"[{bar_color}{make_bar(pct)}{RESET}] {YELLOW if pct <= 50 and pct > 20 else bar_color}{pct}%{RESET}\n")
        if raw_curr == 0:
            print(f"⚡ Current    {SYNTH_TANGERINE}{curr_str} uA{RESET}")
        elif raw_curr > 0:
            print(f"⚡ Current    {GREEN}{curr_str} uA{RESET}")
        else:
            print(f"⚡ Current    {RED}{curr_str} uA{RESET}")
        print(f"🌡  Temp       {temp_color}{temp}°C{RESET}")
        print(f"🔌 Status     {NORD_BLUE}{status}{RESET}")
        print(f"🔌 Plugged    {DRACULA_PURPLE}{plugged}{RESET}")
        print(f"   Health     {GREEN}{health}{RESET}")
        print(f"   Voltage    {WHITE}{voltage} mV{RESET}")
        print(f"   Power      {NORD_BLUE}{power_mw:.1f} mW{RESET}")
        print(f"\n────────────────────────────────────────────")
        if raw_curr == 0:
            print(f"{CYBER_PINK}-{YELLOW}It wont move.{RESET}")
        elif raw_curr > 0:
            print(f"{CYBER_PINK}-{GREEN}YES.{RESET} It {GREEN}WILL {RESET}go up.{RESET}")
        else:
            print(f"{CYBER_PINK}-{RED}NO. It will not go up.{RESET}")
        if temp >= 44.0:
            print(f"{CYBER_PINK}-{BOLD}{RED}DISCONNECT NOW AND PUT PHONE SOMEWHERE COLD{RESET}")
        elif temp >= 41.0:
            print(f"{CYBER_PINK}-{RESET}Running{RED}HOT.{RESET}")
        elif temp >= 39.0:
            print(f"{CYBER_PINK}-{RESET}Running {DRACULA_PURPLE}Warm.{RESET}")
        else:
            print(f"{CYBER_PINK}-{RESET}Running{GREEN} Normal.{RESET}")
        print(f"{DARK_GRAY}⏱️ Est{GREEN}.{DARK_GRAY} full{GREEN}: {CYBER_PINK}~572 min{RESET}")
        print(f"════════════════════════════════════════════")
        print(f"{DARK_GRAY}Press {DRACULA_PURPLE}Enter{DARK_GRAY} to close {RED}|{DARK_GRAY} {DRACULA_PURPLE}Ctrl+C{DARK_GRAY} to force exit{GREEN}.{RESET}")
        if sys.stdin in select.select([sys.stdin], [], [], 0.05)[0]:
            break
        time.sleep(0.45)
except Exception:
    pass
finally:
    silent_exit(None, None)
