import pyvisa as visa


def init(visa_port: str, baud: int):
    rm = visa.ResourceManager()
    try:
        myinst = rm.open_resource(visa_port)
        myinst.baud_rate = baud
    except Exception as err:
        print('Exception : ' + str(err))
        return visa_port + ": " +  str(err)
    try:
        myinst.write("*IDN?")
        str_read = myinst.read()
        myinst.write("SYST:RES FETCH")
        myinst.write("SYST:SHAK OFF")
        myinst.write("SYST:CODE OFF")
        myinst.write("*IDN?")
        str_read = myinst.read()
        myinst.close()
        return str_read
    except Exception as err:
        myinst.close()
        print('Exception : ' + str(err))
        return visa_port + ": " + str(err)
    

def measInductance(visa_port: str, baud:int, freq: str):
    rm = visa.ResourceManager()
    try:
        myinst = rm.open_resource(visa_port)
        myinst.baud_rate = baud
    except Exception as err:
        print('Exception : ' + str(err))
        return float(-99999998)
    try:
        # clear buffer.
        myinst.write("*IDN?")
        str_read = myinst.read()
        myinst.write("DISP:PAGE MEAS")
        myinst.write("APER SLOW")
        myinst.write("FUNC Ls-Q")
        myinst.write("FUNC:RANGe:AUTO on")
        myinst.write(f"FREQ {freq}")
        myinst.write("FETCH?")
        str_read = str(myinst.read())
        inductance = str_read.split(',')[0]
        return float(inductance)
    except Exception as err:
        myinst.close()
        print('Exception : ' + str(err))
        return float(-99999999)