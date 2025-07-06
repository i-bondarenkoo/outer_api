class Device:

    all_devices = []

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def register(self, value):
        if not isinstance(value, Device):
            raise ValueError("Передан неправильный объект")
        Device.all_devices.append(value)
        return f"Объект добавлен в список"


class NetworkEnabled:
    def __init__(self, mac_address: str):
        self.mac_address = mac_address

    def connect(self):
        return f"Устройство успешно подключилось к сети"


class BatteryPowered:
    def __init__(self, battery_level: int):
        self.battery_level = battery_level

    def battery_status(self):
        return f"Заряд батареи - {self.battery_level}"


class SmartLight(Device, NetworkEnabled):
    def __init__(self, brand, model, mac_address, is_on=True):
        Device.__init__(self, brand=brand, model=model)
        NetworkEnabled.__init__(self, mac_address=mac_address)
        self.is_on = True

    def toggle(self):
        if self.is_on == True:
            self.is_on = False
            return f"Лампа выключена"
        else:
            self.is_on == True
            return f"Лампочка включена"


class SmartVacuum(Device, NetworkEnabled, BatteryPowered):
    def __init__(self, brand, model, mac_address, battery_level):
        Device.__init__(self, brand=brand, model=model)
        NetworkEnabled.__init__(self, mac_address=mac_address)
        BatteryPowered.__init__(self, battery_level=battery_level)

    def clean(self):
        if self.battery_level > 10:
            self.battery_level -= 10
            return f"Запущена уборка, состояние батареи {self.battery_level}"
        else:
            return f"Слишком мало заряда, невозможно начать уборку"


print(SmartLight.__mro__)
print(SmartVacuum.__mro__)
smart_l = SmartLight("Xiaomi", "g-123", "aa:bb:cc:dd:11:23:43:44")
device1 = Device("Apple", "f-15")
Device.register(device1)
print(Device.all_devices)
