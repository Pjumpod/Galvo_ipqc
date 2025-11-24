import pyvisa as visa
import time


def init(visa_port: str, baud: int):
    rm = visa.ResourceManager()
    try:
        myinst = rm.open_resource(visa_port)
        myinst.baud_rate = int(baud)
    except Exception as err:
        print('Exception : ' + str(err))
        return visa_port + ": " +  str(err)
    try:
        myinst.write("*IDN?")
        str_read = myinst.read()
        myinst.write(":OUTP:A 0")
        myinst.write(":OUTP:B 0")
        myinst.write("*IDN?")
        str_read = myinst.read()
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


def output_off(visa_port: str, baud: int):
    rm = visa.ResourceManager()
    try:
        myinst = rm.open_resource(visa_port)
        myinst.baud_rate = int(baud)
    except Exception as err:
        print('Exception : ' + str(err))
        return visa_port + ": " +  str(err)
    try:
        myinst.write(":OUTP:A 0")
        myinst.write(":OUTP:B 0")
        myinst.close()
        rm.close()
        return "SUCCESS"
    except Exception as err:
        try:
            myinst.close()
        except:
            print('error in close instrument')
        rm.close()
        print('Exception : ' + str(err))
        return visa_port + ": " + str(err)
    
def output_on(visa_port: str, baud: int):
    rm = visa.ResourceManager()
    try:
        myinst = rm.open_resource(visa_port)
        myinst.baud_rate = int(baud)
    except Exception as err:
        print('Exception : ' + str(err))
        return "0 " + visa_port + ": " +  str(err)
    try:
        myinst.write(":POW:A 2.5")
        myinst.write(":CURR:A 1")
        myinst.write(":VOLT:A 1")
        myinst.write(":VOLT:PROT:A 2.5")
        myinst.write(":OUTP:A 1")
        time.sleep(0.1)
        myinst.close()
        rm.close()
        return "SUCCESS"
    except Exception as err:
        try:
            myinst.close()
        except:
            print('error in close instrument')
        rm.close()
        print('Exception : ' + str(err))
        return "1 " + visa_port + ": " + str(err)
