import subprocess
import plistlib


def get_ioreg_output():
    # Run ioreg and capture the output
    ioreg_process = subprocess.Popen(['ioreg', '-r', '-d', '1', '-k', 'BatteryPercent', '-a'],
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ioreg_output, _ = ioreg_process.communicate()
    return ioreg_output


def parse_ioreg_output(output):
    # Parse the output into a dictionary
    try:
        plist_data = plistlib.loads(output)
        return plist_data
    except plistlib.InvalidFileException:
        print("Invalid plist file")


def get_ioreg_battery_percent():
    ioreg_output = get_ioreg_output()
    items = parse_ioreg_output(ioreg_output)
    if items:
        for item in items:
            if "Mouse" in item.get("Product"):
                return int(item.get("BatteryPercent"))


if __name__ == "__main__":
    print(get_ioreg_battery_percent())
