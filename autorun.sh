#!/bin/sh
cd /home/debian/autopilot_bbb/
./config_pins.sh
sleep 5
python Pauto.py
