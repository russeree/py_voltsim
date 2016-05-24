import threading
import time
threads = []

class VMinHandler:
    # Initializtion
    def __init__(self):
        self.v_data = []
        self.dbg_lvl = 0
        self.testing = False
        self.success = False
    # Sleep for a number of micro secconds
    def usleep(self, u_secconds = 1000):
        time.sleep(u_secconds/1000000)

    # Sets the class debug level that determines output verboseness
    def set_dbg_lvl(self, level = 0):
        # 0 = None
        # 1 = Print Important Execution Detals
        # 2 = Print Important Vaible Details
        # 3 = Print Verbose Details
        if ((level <= 3) & (level >= 0)):
            self.dbg_lvl = level
            print ('Debug Level Set: %s') % (level)

    # Simulates a Typical KBL votlage reading as would be imported VIA Sinai2
    def voltage_sim (self, v_offset = 1.1, v_range = 0.2, sample_rate_us = 1000000):
        import random
        self.v_data.append([(len(self.v_data)), (v_offset + (random.uniform(0,v_range)))])
        if(self.dbg_lvl == 3):
            print self.v_data
        self.usleep(sample_rate_us)

    # Simulates a test in progress
    def test_sim(self, run_time_seconds = 6, sim_start_delay = 10):
        if(self.dbg_lvl == 3):
            print ('Test Sim Begining')
        time.sleep(sim_start_delay)
        self.testing = True
        if(self.dbg_lvl == 3):
            print ('Testing Has Began')
        time.sleep(run_time_seconds)
        self.testing = False
        self.success = True
        if(self.dbg_lvl == 3):
            print ('Testing has concluded')
            print ('Test Sim Exit')

    # Logs a voltage while a test is in progress
    def voltage_accumulator(self):
        if(self.dbg_lvl == 3):
            print ('Voltage Acumulation Begining')
        while(1):
            if(self.testing == True):
                self.voltage_sim()
            elif (self.success == True):
                break
        if(self.dbg_lvl == 3):
            print ('Voltage Acumulation Exit')

thread_test = VMinHandler()
thread_test.set_dbg_lvl(3)
t_tsim = threading.Thread(target=thread_test.test_sim)
v_tsim = threading.Thread(target=thread_test.voltage_accumulator)
threads.append(t_tsim)
threads.append(v_tsim)
t_tsim.start()
v_tsim.start()

