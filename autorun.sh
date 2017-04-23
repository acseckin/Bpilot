#!/bin/sh
cd /home/debian/autopilot_bbb/
./pins_config.sh
sleep 5
python Pauto.py
