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
subprocess.check_call(['/bin/csh', '-c', 'source ~daqowner/daq.11.11.4/etc/env.csh'])
subprocess.check_call(['/bin/csh', '-c', 'source /home/hcalpro/seema/TTTSoftware/environ.csh'])
subprocess.check_call(['/bin/csh', '-c', 'source ~hcalpro/sckao/11_11_4/hcal/hcalUHTR/source.csh'])

#configure TTT to take external clock
os.system('externalClockTTT.sh | python ~hcalpro/seema/TTTSoftware/src/TTTtool.py')
 
# #make AMC13 distribute the clock
am13_command = "AMC13Tool.exe -u -n 11 -x AMC13Com.txt > log.txt" 
os.system(am13_command)

 
#configure ngCCM to take external clock
#os.system('cd ~/GLIBtool_UVA/')
# ./GLIBtool
os.system('GLIB.sh | ./../GLIBtool_UVA/GLIBtool > log.txt')
# cd -

#make uHTR run correct clock
uHTR_command =  "bin/linux/x86_64_slc6/uHTRtool.exe -u 192.168.114.16 -s init.uhtr > log.txt"(htr_tool,i)
os.system(daq_check_command)

# 
# #init links--maybe better to put in another script...
# LINK
# INIT
# 1
# 5
# STATUS #for log
# 

