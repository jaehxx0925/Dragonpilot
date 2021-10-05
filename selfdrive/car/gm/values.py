# flake8: noqa

from cereal import car
from selfdrive.car import dbc_dict
Ecu = car.CarParams.Ecu

class CarControllerParams():
  def __init__(self):
    self.STEER_MAX = 300
    self.STEER_STEP = 4              # how often we update the steer cmd
    self.STEER_DELTA_UP = 8           # ~0.75s time to peak torque (255/50hz/0.75s)
    self.STEER_DELTA_DOWN = 12        # ~0.3s from peak torque to zero
    self.MIN_STEER_SPEED = 3.
    self.STEER_DRIVER_ALLOWANCE = 50   # allowed driver torque before start limiting
    self.STEER_DRIVER_MULTIPLIER = 4   # weight driver torque heavily
    self.STEER_DRIVER_FACTOR = 100     # from dbc
    self.NEAR_STOP_BRAKE_PHASE = 0.5   # m/s, more aggressive braking near full stop

    # Takes case of "Service Adaptive Cruise" and "Service Front Camera"
    # dashboard messages.
    self.ADAS_KEEPALIVE_STEP = 100
    self.CAMERA_KEEPALIVE_STEP = 100

    # pedal lookups, only for Volt
    MAX_GAS = 3072              # Only a safety limit
    ZERO_GAS = 2048
    MAX_BRAKE = 350             # Should be around 3.5m/s^2, including regen
    self.MAX_ACC_REGEN = 1404  # ACC Regen braking is slightly less powerful than max regen paddle
    self.GAS_LOOKUP_BP = [-0.25, 0., 0.5]
    self.GAS_LOOKUP_V = [self.MAX_ACC_REGEN, ZERO_GAS, MAX_GAS]
    self.BRAKE_LOOKUP_BP = [-1., -0.25]
    self.BRAKE_LOOKUP_V = [MAX_BRAKE, 0]


class CAR:
  HOLDEN_ASTRA = "HOLDEN ASTRA RS-V BK 2017"
  EQUINOX = "CHEVROLET EQUINOX"

class CruiseButtons:
  INIT = 0
  UNPRESS = 1
  RES_ACCEL = 2
  DECEL_SET = 3
  MAIN = 5
  CANCEL = 6

class AccState:
  OFF = 0
  ACTIVE = 1
  FAULTED = 3
  STANDSTILL = 4

class CanBus:
  POWERTRAIN = 0
  OBSTACLE = 1
  CHASSIS = 2
  SW_GMLAN = 3

FINGERPRINTS = {
  # Astra BK MY17, ASCM unplugged
  CAR.HOLDEN_ASTRA: [{
    190: 8, 193: 8, 197: 8, 199: 4, 201: 8, 209: 7, 211: 8, 241: 6, 249: 8, 288: 5, 298: 8, 304: 1, 309: 8, 311: 8, 313: 8, 320: 3, 328: 1, 352: 5, 381: 6, 384: 4, 386: 8, 388: 8, 393: 8, 398: 8, 401: 8, 413: 8, 417: 8, 419: 8, 422: 1, 426: 7, 431: 8, 442: 8, 451: 8, 452: 8, 453: 8, 455: 7, 456: 8, 458: 5, 479: 8, 481: 7, 485: 8, 489: 8, 497: 8, 499: 3, 500: 8, 501: 8, 508: 8, 528: 5, 532: 6, 554: 3, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 567: 5, 647: 5, 707: 8, 715: 8, 723: 8, 753: 5, 761: 7, 806: 1, 810: 8, 840: 5, 842: 5, 844: 8, 866: 4, 961: 8, 969: 8, 977: 8, 979: 8, 985: 5, 1001: 8, 1009: 8, 1011: 6, 1017: 8, 1019: 3, 1020: 8, 1105: 6, 1217: 8, 1221: 5, 1225: 8, 1233: 8, 1249: 8, 1257: 6, 1259: 8, 1261: 7, 1263: 4, 1265: 8, 1267: 8, 1280: 4, 1300: 8, 1328: 4, 1417: 8, 1906: 7, 1907: 7, 1908: 7, 1912: 7, 1919: 7,
  }],
  CAR.EQUINOX: [
  # Chevrolet Equinox 2019 NO ACC
  {
    190: 8, 193: 8, 197: 8, 199: 4, 201: 8, 209: 7, 211: 8, 241: 6, 249:8, 257: 5, 288: 5, 289: 8, 298: 8, 304: 1, 309: 8, 311: 8, 313: 8, 320: 3, 322: 7, 328: 1, 352: 5, 381: 8, 384: 4, 386: 8, 388: 8, 393: 8, 398: 8, 401: 8, 413: 8, 417: 8, 419: 8, 422: 1, 426: 8, 431: 8, 442: 8, 451: 8, 452: 8, 453: 8, 455: 7, 456: 8, 479: 8, 481: 7, 485: 8, 489: 8, 497: 8, 499: 3, 500: 8, 501: 8, 508: 8, 510: 8, 528: 5, 532: 6, 554: 3, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 567: 5, 569: 3, 573: 1, 577: 4, 647: 8, 707: 8, 715: 8, 717: 5, 753: 5, 761: 7, 789: 5, 800: 6, 810: 8, 840: 5, 842: 5, 844: 8, 866: 4, 869: 4, 880: 6, 882: 8, 890: 1, 892: 2, 893: 2, 894: 1, 961: 8, 969: 8, 977: 8, 979: 8, 985: 8, 1001: 8, 1009: 8, 1011: 8, 1017: 8, 1020: 8, 1033: 7, 1034: 7, 1105: 6, 1217: 8, 1219: 8, 1221: 5, 1225: 8, 1231: 8, 1233: 8, 1249: 8, 1257: 6, 1259: 8, 1261: 8, 1263: 8, 1265: 8, 1267: 8, 1273: 3, 1280: 4, 1296: 4, 1300: 8, 1322: 6, 1328: 4, 1345: 8, 1346: 8, 1347: 5, 1353: 8, 1355: 8, 1362: 8, 1375: 8, 1417: 8, 1512: 8, 1514: 8, 1601: 8, 1906: 8, 1907: 7, 1912: 7, 1916: 7, 1919: 7, 1920: 7, 1930: 7 
  }],
}

STEER_THRESHOLD = 1.0

DBC = {
  CAR.HOLDEN_ASTRA: dbc_dict('gm_global_a_powertrain', 'gm_global_a_object', chassis_dbc='gm_global_a_chassis'),
  CAR.EQUINOX: dbc_dict('gm_global_a_powertrain', 'gm_global_a_object', chassis_dbc='gm_global_a_chassis'),
}
