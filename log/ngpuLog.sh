#!/bin/bash
pattern="updating. "
while :; do
    sleep 2
    wget -ca -O ./ngpu.log -o /dev/null http://log.ainngpu.io:9999/ngpu.log
    if [ "$pattern" == "updating. " ]; then
        pattern="updating.."
    else
        pattern="updating. "
    fi
    printf "%s\r" "$pattern"
done
