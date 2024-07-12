#!/bin/bash

# Function to set up and activate the virtual environment
setup_and_activate_venv() {
    if [ ! -d "myenv" ]; then
        python3 -m venv myenv
    fi
    source myenv/bin/activate
}

# Function to install necessary packages if they are not already installed
install_packages() {
    setup_and_activate_venv

    # List of required packages
    packages=("SpeechRecognition" "pyaudio" "requests" "waveshare-epd" "pillow" "pybluez")

    for package in "${packages[@]}"; do
        pip list | grep -q "$package" || pip install "$package"
    done
}

# Function to run the voice trigger script and bluetooth server concurrently
run_scripts() {
    setup_and_activate_venv
    python3 voice_trigger.py &
    python3 bluetooth_server.py &
    wait
}

# Ensure the script does not run multiple times
if pidof -o %PPID -x "$(basename "$0")" > /dev/null; then
   echo "Script is already running"
   exit 1
fi

install_packages
run_scripts


# Function to set up and activate the virtual environment
# setup_and_activate_venv() {
#     if [ ! -d "myenv" ]; then
#         python3 -m venv myenv
#     fi
#     source myenv/bin/activate
# }

# # Function to install necessary packages if they are not already installed
# install_packages() {
#     setup_and_activate_venv

#     # Check if the packages are installed, if not, install them
#     pip freeze | grep -q SpeechRecognition || pip install SpeechRecognition
#     pip freeze | grep -q pyaudio || pip install pyaudio
#     pip freeze | grep -q requests || pip install requests
#     pip freeze | grep -q waveshare-epd || pip install waveshare-epd
#     pip freeze | grep -q pillow || pip install pillow
#     pip freeze | grep -q pybluez || pip install pybluez
# }

# # Function to run the voice trigger script
# run_voice_trigger() {
#     setup_and_activate_venv
#     python3 voice_trigger.py
#     python3 bluetooth_server.py
# }

# # Ensure the script does not run multiple times
# if pidof -o %PPID -x "$(basename "$0")" > /dev/null; then
#    echo "Script is already running"
#    exit 1
# fi

# install_packages
# run_voice_trigger
