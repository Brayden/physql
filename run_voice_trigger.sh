#!/bin/bash

# Set up and activate the virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Ensure all necessary packages are installed
pip install SpeechRecognition pyaudio requests waveshare-epd pillow

show_loading_screen() {
    python3 display_image.py >> /home/pi/path_to_your_script/logs/display_image.log 2>&1
    echo "Startup screen displaying.." >> /home/pi/path_to_your_script/logs/display_image.log 2>&1
}

# Function to run the voice trigger script
run_voice_trigger() {
    while true; do
        python3 voice_trigger.py >> /home/pi/path_to_your_script/logs/voice_trigger.log 2>&1
        echo "Voice trigger script crashed with exit code $?.  Respawning.." >&2
        sleep 5
    done
}

# Function to run the Node.js script
run_node_script() {
    while true; do
        node index.js >> /home/pi/path_to_your_script/logs/node_index.log 2>&1
        echo "Node.js script crashed with exit code $?.  Respawning.." >&2
        sleep 5
    done
}

# Show the loading screen
show_loading_screen

# Run both scripts in parallel
run_voice_trigger &
run_node_script &
wait
