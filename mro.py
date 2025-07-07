class Device:

    all_devices: list = []

    def __init__(self, brand: str, model: str, **kwargs):
        self.brand = brand
        self.model = model
        super().__init__(**kwargs)

    def register(self):
        Device.all_devices.append(self)
        return f"Объект добавлен в список"

    def __str__(self):
        return f"{self.brand} {self.model}"

    @classmethod
    def print_registry(cls):
        return "\n".join(str(device) for device in cls.all_devices)


class NetworkEnabled:
    def __init__(self, mac_address: str, **kwargs):
        self.mac_address = mac_address
        super().__init__(**kwargs)

    def connect(self):
        return f"Устройство с mac-адресом {self.mac_address} успешно подключено"

    def __str__(self):
        return f"{self.mac_address}"


class BatteryPowered:
    def __init__(self, battery_level: int, **kwargs):
        self.battery_level = battery_level
        super().__init__(**kwargs)

    def status(self):
        return f"Заряд батареи составляет - {self.battery_level}%"

    def __str__(self):
        return f"{self.battery_level}%"


class SmartSensor(Device, NetworkEnabled, BatteryPowered):
    def __init__(self, brand, model, mac_address, battery_level, sensor_type):
        Device.__init__(self, brand, model)
        NetworkEnabled.__init__(self, mac_address)
        BatteryPowered.__init__(self, battery_level)
        self.sensor_type = sensor_type
        super().__init__(
            brand=brand,
            model=model,
            mac_address=mac_address,
            battery_level=battery_level,
        )
        self.sensor_type = sensor_type


# print(SmartSensor.__mro__)
d = Device("Apple", "HT-802")
d.register()
print(Device.print_registry())
smart = SmartSensor("Xiaomi", "HT404", "aa:bb:cc:dd:55:22:32:44", 15, "сенсорный")
smart2 = SmartSensor("Xiaomi", "HT405", "aa:bb:cc:dd:55:22:32:44", 15, "сенсорный")
print(smart.status())
print(smart.connect())
smart.register()
smart2.register()
print(Device.print_registry())
