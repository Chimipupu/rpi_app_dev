import os

def get_cpu_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return temp.replace("temp=", "").replace("'C\n", "")

print(f"CPU温度: {get_cpu_temp()}°C")