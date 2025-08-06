#!/bin/bash

#1.Log Running Process
logfile="process_log_$(date +F).log"
ps -e > "logfile"

#2. Check for high memory usage
echo "Checking for high memory usage.."
ps aux | awk '$4+0 > 30' >>high_mem_processes.log

#3. check disk space
disk_usage=$(df -h /c |awk 'NR==2 {gsub("%", "",$5); print $5}')
if [ "$disk_usage" -gt 80 ]; then
echo "Warning Disk usage on / is above 80% ($disk_usage%)"
fi

#4. Display Summary
total_processes=$(ps aux | wc -l)
high_mem_count=$(ps aux | awk '$4 > 30' | wc -l)

echo ""
echo "===== System Health Summary ====="
echo "Total Running Processes: $total_processes"
echo "Processes >30% Memory : $high_mem_count"
echo "Disk Usage on /: $disk_usage%"


