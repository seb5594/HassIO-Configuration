#!/bin/bash

git add .
#git status

NOW=$(date +"%d/%m/%Y %H:%M")
git commit -m "Automated: HA Config as at $NOW"
git push origin main
exit
