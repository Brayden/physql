#!/bin/bash

# Set up and activate the virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Ensure all necessary packages are installed
pip install SpeechRecognition pyaudio requests

# Function to run the voice trigger script
run_script() {
    while true; do
        python3 voice_trigger.py
        echo "Script crashed with exit code $?.  Respawning.." >&2
        sleep 5
    done
}

# Run the script
run_script
