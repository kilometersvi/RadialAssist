import os
import time
import importlib
#dongleless = importlib.import_module("Dongleless-myo.dongleless")
from Dongleless_myo import dongleless

def unknown(myo):
    print("unknown")

def arm_synced(myo, x_dir, arm):
    print("arm_synced")

def arm_unsynced(myo):
    print("arm_unsynced")

def imu_data(myo, quat, accel, gyro):
    print("imu_data")

def emg_data(myo, emg):
    print("emg_data")

def main():
    print(f"### {time.asctime(time.localtime())} ###")
    print("Running RadialAssist service v0.1...")

    '''
    function_dict = {
        "unknown":unknown,
        "arm_synced":arm_synced,
        "arm_unsynced":arm_unsynced,
        "imu_data":imu_data,
        "emg_data":emg_data
    }
    '''

    dongleless.run(useMyoGrapher=False)#function_dict)

if __name__ == "__main__":
    main()
