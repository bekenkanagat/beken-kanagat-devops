#!/usr/bin/env bash

echo "=============================="
echo "Student Information"
echo "=============================="
echo "Name: Kanagat"
echo "Surname: Beken"
echo "Group: IT2-2307"
echo "Student ID: 38052"

echo "=============================="
echo "System Information"
echo "=============================="
echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -srm)"

echo "Disk Usage:"
df -h /

echo "Memory Usage:"
free -h

if [ -f "$HOME/devops/beken_kanagat/Beken_Kanagat_info.txt" ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi
