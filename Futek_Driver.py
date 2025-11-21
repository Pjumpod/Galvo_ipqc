import clr
clr.AddReference("FUTEK.Devices")
import FUTEK.Devices
from FUTEK.Devices import DeviceRepository

def init():
    try:
        oFUTEKDeviceRepoDLL = FUTEK.Devices.DeviceRepository()
        print("FUTEK Devices DLL initialized.")
    except Exception as e:
        print(f"Error initializing FUTEK Devices DLL: {e}")
        return f"Error initializing FUTEK Devices DLL: {e}"

    if oFUTEKDeviceRepoDLL.DeviceCount > 0:
        print("Device connected.")
        oFUTEKDeviceRepoDLL.DisconnectAllDevices()
        return "Success"
    else:
        print("No device connected.")
        oFUTEKDeviceRepoDLL.DisconnectAllDevices()
        return "Error No device connected."


def measSensor():
    try:
        oFUTEKDeviceRepoDLL = FUTEK.Devices.DeviceRepository()
        print("FUTEK Devices DLL initialized.")
    except Exception as e:
        print(f"Error initializing FUTEK Devices DLL: {e}")
        return f"Error initializing FUTEK Devices DLL: {e}"
    devices = oFUTEKDeviceRepoDLL.DetectDevices()
    USB225 = devices[0] if devices else None

    measSensor = []
    if oFUTEKDeviceRepoDLL.DeviceCount > 0:
        print("Device connected.")
        for num in range(1, 11):
            measSensor[num] = FUTEK.Devices.DeviceUSB225.GetChannelXReading(USB225, 0)
        oFUTEKDeviceRepoDLL.DisconnectAllDevices()
        measData = sum(measSensor) / len(measSensor)
        return str(measData)
    else:
        print("No device connected.")
        oFUTEKDeviceRepoDLL.DisconnectAllDevices()
        return "Error No device connected."
    

def getModelNumber():
    try:
        oFUTEKDeviceRepoDLL = FUTEK.Devices.DeviceRepository()
        print("FUTEK Devices DLL initialized.")
    except Exception as e:
        print(f"Error initializing FUTEK Devices DLL: {e}")
        return f"Error initializing FUTEK Devices DLL: {e}"
    devices = oFUTEKDeviceRepoDLL.DetectDevices()
    USB225 = devices[0] if devices else None

    if oFUTEKDeviceRepoDLL.DeviceCount > 0:
        print("Device connected.")
        ModelNumber = FUTEK.Devices.Device.GetModelNumber(USB225)
        oFUTEKDeviceRepoDLL.DisconnectAllDevices()
        return str(ModelNumber)
    else:
        print("No device connected.")
        oFUTEKDeviceRepoDLL.DisconnectAllDevices()
        return "Error No device connected."


def getSerialNumber():
    try:
        oFUTEKDeviceRepoDLL = FUTEK.Devices.DeviceRepository()
        print("FUTEK Devices DLL initialized.")
    except Exception as e:
        print(f"Error initializing FUTEK Devices DLL: {e}")
        return f"Error initializing FUTEK Devices DLL: {e}"
    devices = oFUTEKDeviceRepoDLL.DetectDevices()
    USB225 = devices[0] if devices else None

    if oFUTEKDeviceRepoDLL.DeviceCount > 0:
        print("Device connected.")
        SerialNumber = FUTEK.Devices.Device.GetInstrumentSerialNumber(USB225)
        oFUTEKDeviceRepoDLL.DisconnectAllDevices()
        return str(SerialNumber)
    else:
        print("No device connected.")
        oFUTEKDeviceRepoDLL.DisconnectAllDevices()
        return "Error No device connected."


def getDataUnit():
    try:
        oFUTEKDeviceRepoDLL = FUTEK.Devices.DeviceRepository()
        print("FUTEK Devices DLL initialized.")
    except Exception as e:
        print(f"Error initializing FUTEK Devices DLL: {e}")
        return f"Error initializing FUTEK Devices DLL: {e}"
    devices = oFUTEKDeviceRepoDLL.DetectDevices()
    USB225 = devices[0] if devices else None

    if oFUTEKDeviceRepoDLL.DeviceCount > 0:
        print("Device connected.")
        DataUnit = FUTEK.Devices.DeviceUSB225.GetChannelXUnitOfMeasure(USB225, 0)
        oFUTEKDeviceRepoDLL.DisconnectAllDevices()
        return str(DataUnit)
    else:
        print("No device connected.")
        oFUTEKDeviceRepoDLL.DisconnectAllDevices()
        return "Error No device connected."