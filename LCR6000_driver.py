import pyvisa as visa


def init(visa_port: str):
    rm = visa.ResourceManager()
    try:
        myinst = rm.open_resource(visa_port)
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