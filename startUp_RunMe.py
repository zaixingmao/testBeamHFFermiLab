import os as os

os.system(daq_check_command)
            daq_check_command =  "%s -u %s -s %s/checkDAQ.uhtr > %s/daqcheck.txt" % (htr_tool,i, script_dir, tmpDir)
