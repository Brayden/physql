#!/bin/bash

# Set up and activate the virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Ensure all necessary packages are installed
pip install SpeechRecognition pyaudio requests

show_loading_screen() {
    python3 startup_script.py
    echo "Startup screen displaying.."
}

# Function to run the voice trigger script
run_voice_trigger() {
    while true; do
        python3 voice_trigger.py
        echo "Voice trigger script crashed with exit code $?.  Respawning.." >&2
        sleep 5
    done
}

# Function to run the Node.js script
run_node_script() {
    while true; do
        node index.js
        echo "Node.js script crashed with exit code $?.  Respawning.." >&2
        sleep 5
    done
}

# Run both scripts in parallel
show_loading_screen &
run_voice_trigger &
run_node_script &
wait
