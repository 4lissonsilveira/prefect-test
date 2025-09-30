#!/bin/sh
#sleep 10
for module in /opt/flows/*; do
    if [ -f "$module/deployment.py" ]; then
        python "$module/deployment.py"
    fi
done