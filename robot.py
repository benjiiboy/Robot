import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BOARD)
 
global GlobAlarmTid
global antalx
antalx = 1
 
GlobAlarmTid = []
 
 
def CheckAlarmTime():
    if len(GlobAlarmTid) == 5:
        if GlobAlarmTid[0] < 3:
            if GlobAlarmTid[1] < 4:
                if GlobAlarmTid[2] < 6:
                    if GlobAlarmTid[3] < 10:
                        if GlobAlarmTid[4] == "A":
                            AlarmArmed(GlobAlarmTid)
    else:
        FejlIAlarm()
 
 
def AlarmArmed(Alarmtid):
    print("alarm sat")
 
 
def FejlIAlarm():
    print("Error fejl i alarm tid")
 
 
MATRIX = [[1, 2, 3, 'A'],
          [4, 5, 6, 'B'],
          [7, 8, 9, 'C'],
          ['*', 0, '#', 'D']]
 
ROW = [7, 11, 13, 15]
COL = [12, 16, 18, 22]
 
for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)
 
for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
try:
    while (antalx == 1):
        for j in range(4):
            GPIO.output(COL[j], 0)
            for i in range(4):
                if GPIO.input(ROW[i]) == 0:
                    if len(GlobAlarmTid) == 0:
                        print("min matrix 1: ", MATRIX[i][j])
 
                        _minv = MATRIX[i][j]
                        GlobAlarmTid.append(_minv)
                        if len(GlobAlarmTid) == 1:
                            print("min matrix 2: ", MATRIX[i][j])
 
                            _minv = MATRIX[i][j]
                            GlobAlarmTid.append(_minv)
                            if len(GlobAlarmTid) == 2:
                                print("min matrix 3: ", MATRIX[i][j])
 
                                _minv = MATRIX[i][j]
                                GlobAlarmTid.append(_minv)
                                if len(GlobAlarmTid) == 3:
                                    print("min matrix 4: ", MATRIX[i][j])
 
                                    _minv = MATRIX[i][j]
                                    GlobAlarmTid.append(_minv)
                                    print(GlobAlarmTid)
 
            GPIO.output(COL[j], 1)
        if (len(GlobAlarmTid) == 5):
            global GlobAlarmTid
            global antalx
            print("printer array",GlobAlarmTid)
            CheckAlarmTime()
            print("if statement")
            GlobAlarmTid = []
            print("printer efter array er slettet", GlobAlarmTid)
            antalx + 9999
            break
 
 
except KeyboardInterrupt:
    GPIO.cleanup()
