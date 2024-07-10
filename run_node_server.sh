#!/bin/bash

# Function to run the Node.js script
# run_node_script() {
#     while true; do
#         node index.js
#         echo "Node.js script crashed with exit code $?.  Respawning.." >&2
#         sleep 5
#     done
# }

# # Run both scripts in parallel
# run_node_script &
# wait

# Jul 10 09:58:21 raspberrypi run_node_server.sh[800]: exec error: Error: Command failed: python3 display_image.py
# Jul 10 09:58:21 raspberrypi run_node_server.sh[800]: Traceback (most recent call last):
# Jul 10 09:58:21 raspberrypi run_node_server.sh[800]:   File "/home/pi/physql/display_image.py", line 3, in <module>
# Jul 10 09:58:21 raspberrypi run_node_server.sh[800]:     from waveshare_epd import epd7in5_V2
# Jul 10 09:58:21 raspberrypi run_node_server.sh[800]: ModuleNotFoundError: No module named 'waveshare_epd'