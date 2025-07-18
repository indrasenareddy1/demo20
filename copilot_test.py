import os
import sys

def get_uptime():
    # Try Linux /proc/uptime
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            hours = int(uptime_seconds // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            seconds = int(uptime_seconds % 60)
            return f"System uptime: {hours}h {minutes}m {seconds}s"
    except Exception:
        pass

    # Try using 'uptime' command for other OS
    try:
        import subprocess
        output = subprocess.check_output(['uptime'], universal_newlines=True)
        return f"System uptime: {output.strip()}"
    except Exception as e:
        return f"Could not determine system uptime: {e}"

if __name__ == "__main__":
    print(get_uptime())
