# physql

TODO:
1. Create `systemd` scripts to automatically run `node index` and `./run_voice_trigger.sh` on startup
2. Create `systemd` script to clear the screen on shutdown

How to Run:
1. `node index` in one terminal for server
2. `./run_voice_trigger.sh` in another terminal for the microphone

Troubleshoot:

- If the screen doesn't load anything try running the python script directly: `python3 display_image.py`. This should be auto-executed by the `node index` script though.

- Install Chromium dependencies:  
```sudo apt-get install gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget
```

Setup New Raspberry Pi:
- Updates: `sudo apt-get update`
- Install npm & nodejs: `sudo apt-get install -y nodejs npm`
- Install Chromium on Raspberry Pi: `sudo apt-get install chromium-browser`

Microphone Support
- Install Python package manager: `sudo apt-get install -y python3-pip`
- Install requests: `pip install requests`
- Install Python virtual environment: `sudo apt-get install -y python3-venv`
- Create virtual environment: `python3 -m venv myenv`
- Activate environment: `source myenv/bin/activate`

- Install dependencies: `sudo apt-get install -y portaudio19-dev python3-pyaudio`
- Install speechrecognition: `pip install pyaudio speechrecognition`
- Instal FLAC conversion utility: `sudo apt-get install flac`
- Clone Github repository: `git@github.com:Brayden/physql.git`

Auto-Start on Launch:
- crontab -e
- Add `@reboot cd /physql && /usr/bin/node index` at bottom of file

------

Auto-Stop on Shutdown (NOT WORKING):
- crontab -e
- Add `@reboot /physql/shutdown_script.sh` at bottom of file

Auto-Stop on Shutdown (NOT WORKING):
- `sudo nano /etc/systemd/system/shutdown_script.service`
- Paste the following into the file:
```
[Unit]
Description=Run Python script on shutdown
DefaultDependencies=no
Before=shutdown.target

[Service]
Type=oneshot
ExecStart=/home/pi/physql/shutdown_script.py
RemainAfterExit=true

[Install]
WantedBy=halt.target poweroff.target reboot.target
```
- `sudo systemctl daemon-reload`
- `sudo systemctl enable shutdown_script.service`