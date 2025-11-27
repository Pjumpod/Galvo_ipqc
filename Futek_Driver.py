import clr
clr.AddReference("FUTEK.Devices")
import FUTEK.Devices
from FUTEK.Devices import DeviceRepository
import PSB2400L2_driver as power_supply

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


def measSensor(zerotorque:float, ps_visa: str, ps_baud: int, prefix_log:str, sernum: str):
    try:
        oFUTEKDeviceRepoDLL = FUTEK.Devices.DeviceRepository()
        print("FUTEK Devices DLL initialized.")
    except Exception as e:
        print(f"Error initializing FUTEK Devices DLL: {e}")
        return float(-99999998)
    devices = oFUTEKDeviceRepoDLL.DetectDevices()
    USB225 = devices[0] if devices else None
    prefix_log_ = prefix_log.replace("-","").replace(":","").replace(".","")
    logfile = r"C:\\Report\\" + sernum + "_" + prefix_log_ + ".csv"
    measSensor = []
    data_to_log = []
    if oFUTEKDeviceRepoDLL.DeviceCount > 0:
        print("Device connected.")
        if zerotorque == 0:
            measSensor.append(FUTEK.Devices.DeviceUSB225.GetChannelXReading(USB225, 0))
            ps_status = ""
        else:
            power_supply.output_turn_on(ps_visa, int(ps_baud))
            for num in range(1, 201):
                measSensor.append(FUTEK.Devices.DeviceUSB225.GetChannelXReading(USB225, 0))
            ps_status = power_supply.getstatus(ps_visa, int(ps_baud))
            power_supply.output_off(ps_visa, int(ps_baud))
        oFUTEKDeviceRepoDLL.DisconnectAllDevices()
        # measSensor = measSensor * 7.0616
        # avgdata = sum(measSensor) / len(measSensor)
        if ((abs(min(measSensor)) * 7.0616) - zerotorque) > ((abs(max(measSensor)) * 7.0616) - zerotorque):
            measData = min(measSensor)
            start_log = f"backward ({ps_status}),"
        else:
            measData = max(measSensor)
            start_log = f"forward ({ps_status}),"
        for num in measSensor:
            data_to_log.append((num * 7.0616) - zerotorque)
        line = start_log + ",".join(map(str, data_to_log)) + '\n'
        if zerotorque != 0:
            with open(logfile, 'a+') as file: #, newline=''
                file.write(line)
        measData = (measData * 7.0616) - zerotorque
        return float(measData)
    else:
        print("No device connected.")
        oFUTEKDeviceRepoDLL.DisconnectAllDevices()
        return float(-99999999)
    

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
