import subprocess, time, sys
from threading import Thread

vmon = None
vmon_log = []
vmon_nice_kill = False

def exec_vmon_monitor():
    global vmon
    global vmon_log
    global vmon_nice_kill
    vmon = subprocess.Popen(['python','sinai2_sim.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    while True:
        nextline = vmon.stdout.readline()
        if nextline == '' and vmon.poll() is not None:
            break
        vmon_log.append(nextline)
        sys.stdout.flush()
        if (vmon_nice_kill == True):
            vmon.stdin.write("\n")
    output = vmon.communicate()[0]
    exitCode = vmon.returncode
    if (exitCode == 0):
        return output
    else:
        raise ProcessException(command, exitCode, output)

def vmon_running():
    time.sleep(.1)
    global vmon
    vmon_started = False
    loc_time = None
    while vmon.poll() is None:
        vmon_started = True
        print ('Thread is Running')
        time.sleep(5)
    if(vmon_started == False):
        print ('Thread Failed to Start')

def vmon_stub_nice_kill(time_s = 7):
    global vmon_nice_kill
    time.sleep(time_s)
    vmon_nice_kill = True

vmon_exe = Thread(None, exec_vmon_monitor, None,())
vmon_pulse = Thread(None, vmon_running, None,())
vmon_timed_kill = Thread(None, vmon_stub_nice_kill, None,())

vmon_exe.start()
vmon_pulse.start()
vmon_timed_kill.start()

vmon_exe.join()
vmon_pulse.join()
vmon_timed_kill.join()

print ('Log Results')
for element in vmon_log:
    sys.stdout.write(element)
