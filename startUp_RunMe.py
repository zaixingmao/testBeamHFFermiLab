#!/usr/bin/env python
import os as os
import subprocess as subprocess



# check control hub
# os.system('/opt/cactus/bin/controlhub_status > log.txt')
# grep_command = "grep 'Control Hub is up' log.txt "
# if os.system(grep_command) != 0:
#     print 'Starting control hub, type password:'
#     os.system('su -c \'/opt/cactus/bin/controlhub_start\'')
# 
# 
# #source stuff!
# os.system('source ~daqowner/daq.11.11.4/etc/env.csh')
# os.system('source /home/hcalpro/seema/TTTSoftware/environ.csh')
# os.system('source ~hcalpro/sckao/11_11_4/hcal/hcalUHTR/source.csh')



#configure TTT to take external clock
os.system('python ~hcalpro/seema/TTTSoftware/src/TTTtool.py')
# python ~hcalpro/seema/TTTSoftware/src/TTTtool.py
# ws 0x2 0x4
# q
# 
# #make AMC13 distribute the clock
# AMC13Tool.exe -n 11
# i 3 7
# #3 is uHTR, 7 is GLIB
# st #for log
# q
# 
# #configure ngCCM to take external clock
# cd ~/GLIBtool_UVA/
# ./GLIBtool
# [Enter]
# CLOCK
# CLKIN
# 0
# STATUS #for log
# QUIT
# EXIT
# [Enter]
# cd -
# 
# #make uHTR run correct clock
# bin/linux/x86_64_slc6/uHTRtool.exe 192.168.114.16
# [Enter]
# CLOCK
# SETUP
# 2
# RATES #for log (320 MHz on front!)
# QUIT
# 
# #init links--maybe better to put in another script...
# LINK
# INIT
# 1
# 5
# STATUS #for log
# 
# os.system(daq_check_command)
#             daq_check_command =  "%s -u %s -s %s/checkDAQ.uhtr > %s/daqcheck.txt" % (htr_tool,i, script_dir, tmpDir)
