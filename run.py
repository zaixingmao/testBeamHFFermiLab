#!/usr/bin/env python
import os as os




uHTR_initLink = 'bin/linux/x86_64_slc6/uHTRtool.exe 192.168.114.16 -s checkLink.uhtr > linkStatus.txt'
os.system(uHTR_command)


uHTR_command = 'bin/linux/x86_64_slc6/uHTRtool.exe 192.168.114.16 -s run.uhtr > eventsLog.txt'
os.system(uHTR_command)

