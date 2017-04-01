#!/bin/sh
cd /home/debian/acspilot/
./config_pins.sh
sleep 5
python acspilot.py
