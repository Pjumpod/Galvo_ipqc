import pyvisa as visa
import time

def init(visa_port: str, baud: int):
    rm = visa.ResourceManager()
    try:
        myinst = rm.open_resource(visa_port)
        myinst.baud_rate = int(baud)
    except Exception as err:
        print('Exception : ' + str(err))
        return visa_port + " (1): " +  str(err)
    try:
        # myinst.write("SYST:RES FETCH")
        # myinst.write("SYST:SHAK OFF")
        # myinst.write("SYST:CODE OFF")
        str_read = myinst.query("*IDN?")
        # time.sleep(2)
        # str_read = myinst.read()
        myinst.close()
        rm.close()
        return str_read
    except Exception as err:
        try:
            myinst.close()
        except:
            print('error in close instrument')
        rm.close()
        print('Exception : ' + str(err))
        return visa_port + ": " + str(err)
    

def measInductance(visa_port: str, baud:int, freq: str):
    rm = visa.ResourceManager()
    try:
        myinst = rm.open_resource(visa_port)
        myinst.baud_rate = int(baud)
    except Exception as err:
        print('Exception : ' + str(err))
        return float(-99999998)
    try:
        # clear buffer.
        # myinst.write("*IDN?")
        # str_read = myinst.read()
        myinst.write("DISP:PAGE MEAS")
        time.sleep(0.22)
        myinst.write("FUNC Ls-Rs")
        time.sleep(0.22)
        myinst.write("FUNC:RANGe:AUTO on")
        time.sleep(0.22)
        myinst.write("APER MED")
        time.sleep(0.22)
        myinst.write("FREQ " + str(freq))
        time.sleep(0.22)
        str_read = myinst.query("FETC?")
        # time.sleep(0.22)
        print(str_read)
        inductance = str_read.split(',')[0]
        myinst.close()
        rm.close()
        return float(inductance)
    except Exception as err:
        print("err1")
        try:
            myinst.close()
        except:
            print('error in close instrument')
        print("err2")
        rm.close()
        print('Exception : ' + str(err))
        return float(-99999999)
    

def measResistance(visa_port: str, baud:int):
    rm = visa.ResourceManager()
    try:
        myinst = rm.open_resource(visa_port)
        myinst.baud_rate = int(baud)
    except Exception as err:
        print('Exception : ' + str(err))
        return float(-99999998)
    try:
        # clear buffer.
        # myinst.write("*IDN?")
        # str_read = myinst.read()
        myinst.write("DISP:PAGE MEAS")
        time.sleep(0.22)
        myinst.write("FUNC R-X")
        time.sleep(0.22)
        myinst.write("APER FAST")
        time.sleep(0.22)
        myinst.write("FUNC:RANGe:AUTO on")
        time.sleep(0.22)
        str_read = myinst.query("FETCH?")
        # str_read = str(myinst.read())
        inductance = str_read.split(',')[0]
        myinst.close()
        rm.close()
        return float(inductance)
    except Exception as err:
        try:
            myinst.close()
        except:
            print('error in close instrument')
        rm.close()
        print('Exception : ' + str(err))
        return float(-99999999)
