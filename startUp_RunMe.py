#!/usr/bin/env python
import os as os
import subprocess as subprocess
import json


# check control hub
# os.system('/opt/cactus/bin/controlhub_status > log.txt')
# grep_command = "grep 'Control Hub is up' log.txt "
# if os.system(grep_command) != 0:
#     print 'Starting control hub, type password:'
#     os.system('su -c \'/opt/cactus/bin/controlhub_start\'')
# 
# 
#configure TTT to take external clock
os.system('externalClockTTT.sh | python ~hcalpro/seema/TTTSoftware/src/TTTtool.py')
 
# #make AMC13 distribute the clock
am13_command = 'AMC13Tool.exe -u -n 11 -x AMC13Com.txt > log.txt'
os.system(am13_command)
# 
#  
# #configure ngCCM to take external clock
os.chdir('~/GLIBtool_UVA/')
# # ./GLIBtool
currentDir = os.getcwd()
os.system('%s/GLIB.sh | ./GLIBtool > log.txt' %currentDir)
# # cd -
# 
#make uHTR run correct clock
uHTR_command = 'bin/linux/x86_64_slc6/uHTRtool.exe 192.168.114.16 -s init.uhtr > log.txt'
os.system(uHTR_command)

# 

