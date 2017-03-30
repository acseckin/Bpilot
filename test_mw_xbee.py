from mw import MultiWii
import acsxbee

board = MultiWii("/dev/ttyO1")
xb=acsxbee.xbee()
altitude=[0,0,0,0]
PID=[0,0,0,0,0,0,0,0,0]
rc=[0,0,0,0]
print "Basliyor"
while True:
    board.getData(MultiWii.ATTITUDE)
    board.getData(MultiWii.RC)
    
    altitude[0]=float(board.attitude['angx'])
    altitude[1]=float(board.attitude['angy'])
    altitude[2]=float(board.attitude['heading'])
    altitude[3]=round(float(board.attitude['elapsed']),3)
    rc[0]=int(board.rcChannels['roll'])
    rc[1]=int(board.rcChannels['pitch'])
    rc[2]=int(board.rcChannels['yaw'])
    rc[3]=int(board.rcChannels['throttle'])
    xb.reportMW(altitude,PID,rc)
    print altitude

