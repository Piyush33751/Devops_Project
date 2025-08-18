from hal import hal_input_switch as input_switch
import AlertSystem as AlertSys
import TempSmoke as tempsmoke
from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_ir_sensor as ir_sensor
import RemoteAccess as RemoteAccess
#UNDER FIRE CONDITONS 

def test_temp_humidity_sensor():
  temperature =True#test conditions under a fire 
  x=tempsmoke.get_temp_state()
  assert(temperature==x)

def test_ir_sensor():
  ir_detected = True
  x = ir_sensor.get_ir_sensor_state()
  assert(ir_detected == x)

def test_remote_access():
  alert = AlertSys.alert()
  y = RemoteAccess.sendMsg()
  assert(alert==y)