import pyvisa as visa
import time

def init(visa_port: str, baud: int):
    rm = visa.ResourceManager()
    try:
        DAQ970A = rm.open_resource(visa_port)
        DAQ970A.baud_rate = baud
    except Exception as err:
        print('Exception : ' + str(err))
        return visa_port + ": " +  str(err)
    try:
        idn = DAQ970A.query('*IDN?')
        ctype = DAQ970A.query(':SYSTem:CTYPe? %d' % (1))
        DAQ970A.close()
        rm.close()
        return f"{idn} {ctype}"
    except Exception as err:
        try:
            DAQ970A.close()
        except:
            print('error in close instrument')
        rm.close()
        print('Exception : ' + str(err))
        return visa_port + ": " + str(err)

def measResistance(visa_port: str, baud: int, channel: str):
    rm = visa.ResourceManager()
    try:
        DAQ970A = rm.open_resource(visa_port)
        DAQ970A.baud_rate = baud
    except Exception as err:
        print('Exception : ' + str(err))
        return float(-99999998)
    try:
        resistance = DAQ970A.query('*IDN?') # clear buffer
        DAQ970A.write(':INSTrument:DMM 1') # turn on the DMM
        resistance = DAQ970A.query(f'MEAS:RES? 1000,1,(@{channel})')
        DAQ970A.close()
        rm.close()
        return float(resistance)
    except Exception as err:
        try:
            DAQ970A.close()
        except:
            print('error in close instrument')
        rm.close()
        print('Exception : ' + str(err))
        return float(-99999999)


def route(visa_port: str, baud: int, channel: str):
    rm = visa.ResourceManager()
    try:
        DAQ970A = rm.open_resource(visa_port)
        DAQ970A.baud_rate = baud
    except Exception as err:
        print('Exception : ' + str(err))
        return visa_port + ": " + str(err)
    try:
        temp_str = DAQ970A.query('*IDN?') # clear buffer
        DAQ970A.write(':INSTrument:DMM 0') # turn on the DMM
        DAQ970A.write(':ROUTe:CHANnel:ADVance:SOURce EXTernal')
        DAQ970A.write(f':ROUTe:CHANnel:FWIRe 0,(@{channel})')
        DAQ970A.close()
        rm.close()
        return "Success"
    except Exception as err:
        try:
            DAQ970A.close()
        except:
            print('error in close instrument')
        rm.close()
        print('Exception : ' + str(err))
        return visa_port + ": " + str(err)
    
# rm = visa.ResourceManager()
# DAQ970A = rm.open_resource('USB0::0x2A8D::0x5101::MY58000845::0::INSTR')
# idn = DAQ970A.query('*IDN?')
# ctype = DAQ970A.query(':SYSTem:CTYPe? %d' % (1))
# DAQ970A.write(':INSTrument:DMM %d' % (0))
# DAQ970A.write(':ROUTe:CHANnel:ADVance:SOURce %s' % ('EXTernal'))
# DAQ970A.write(':ROUTe:CHANnel:FWIRe %d,(%s)' % (1, '@103'))
# DAQ970A.write(':ROUTe:CHANnel:FWIRe %d,(%s)' % (0, '@104'))
# DAQ970A.close()
# rm.close()