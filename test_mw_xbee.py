from mw import MultiWii
import acsxbee

board = MultiWii("/dev/ttyO1")


xb=acsxbee.xbee()

altitude=[0,0,0,0]
PID=[0,0,0,0,0,0,0,0,0]
rc=[0,0,0,0]

try:
    while True:
        board.getData(MultiWii.ATTITUDE)
        altitude[0]=round(float(board.attitude['angx']),3)
        altitude[1]=round(float(board.attitude['angy']),3)
        altitude[2]=round(float(board.attitude['heading']),3)
        altitude[3]=round(float(board.attitude['elapsed']),3)
        xb.reportMW(altitude,PID,rc)
except Exception,error:
    print "Error on Main: "+str(error)
