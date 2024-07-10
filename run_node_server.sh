#!/bin/bash

# Function to run the Node.js script
run_node_script() {
    while true; do
        node index.js
        echo "Node.js script crashed with exit code $?.  Respawning.." >&2
        sleep 5
    done
}

# Run both scripts in parallel
run_node_script &
wait
