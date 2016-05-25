import time, sys
from threading import Thread

v_data = None
dbg_lvl = 3
kill_proc = False

def usleep(u_secconds = 1000000):
    time.sleep(u_secconds/1000000)

def voltage_sim (v_offset = 1.1, v_range = 0.2, sample_rate_us = 1000000):
    import random
    global v_data
    global dbg_lvl
    while(kill_proc == False):
        v_data = (v_offset + (random.uniform(0,v_range)))
        if(dbg_lvl == 3):
            sys.stdout.flush()
            print ("['" + str(v_data) + "`]")
        usleep(sample_rate_us)

def exit_pipe():
    global kill_proc
    while (1):
        inpt = None
        inpt   = raw_input()
        if (inpt == ''):
            kill_proc = True
            break

sinai_2_sim = Thread(None, voltage_sim, None,())
exit_sinai_2_sim = Thread(None, exit_pipe, None,())

exit_sinai_2_sim.start()
sinai_2_sim.start()

sinai_2_sim.join()
exit_sinai_2_sim.join()
