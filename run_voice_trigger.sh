#!/bin/bash

# Function to run the voice trigger script
run_voice_trigger() {
    # Set up and activate the virtual environment
    python3 -m venv myenv
    source myenv/bin/activate

    # Ensure all necessary packages are installed
    pip install SpeechRecognition pyaudio requests waveshare-epd pillow

    while true; do
        python3 voice_trigger.py #>> /home/pi/path_to_your_script/logs/voice_trigger.log 2>&1
        echo "Voice trigger script crashed with exit code $?.  Respawning.." >&2
        sleep 5
    done
}

# Function to run the Node.js script
# run_node_script() {
#     while true; do
#         node index.js #>> /home/pi/path_to_your_script/logs/node_index.log 2>&1
#         echo "Node.js script crashed with exit code $?.  Respawning.." >&2
#         sleep 5
#     done
# }

# Run both scripts in parallel
# run_node_script &
run_voice_trigger &
wait
