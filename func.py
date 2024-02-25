import bluetooth

class BluetoothScanner:
    def __init__(self):
        self.nearby_devices = []

    def perform_inquiry(self):
        print("Performing inquiry...")
        self.nearby_devices = bluetooth.discover_devices(lookup_names=True)
        print(f"Found {len(self.nearby_devices)} devices.")

    def print_devices(self):
        for addr, name in self.nearby_devices:
            print(f"Address: {addr}, Name: {name}")

"""
if __name__ == "__main__":
    scanner = BluetoothScanner()
    scanner.perform_inquiry()
    scanner.print_devices()
"""