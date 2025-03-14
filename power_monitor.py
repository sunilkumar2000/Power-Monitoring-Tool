try:
    import psutil as p
    import time as t
    import subprocess as sp
    import csv

except ModuleNotFoundError: # If module not found, install it and exit (Exception 1)
    print("Ooops!! Seems like you are missiong a picece here I mean the module. Run this 'pip install psutil' to own and fix it. Try again.")
    raise SystemExit

POWER_GADGET_PATH = r"C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe"
CSV_FILE = "Power_Monitor_Data.csv"

#Creating a CSV file to store the data
with open(CSV_FILE, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "App Name", "App CPU Usage (%)", "Estimated Power (W)"])

def get_total_power():
    """Runing the Intel Power Gadget, Understanding and extracting CPU power consumption from the Gadget."""
    try:
        # Running PowerLog3.0.exe for a duration of 1 second
        output = sp.check_output([POWER_GADGET_PATH, "-duration", "1"], stderr=sp.STDOUT, shell=True)
        output_text = output.decode() # Decoding the output to text
        
        # To Find and obtain the line containing power usage
        for line in output_text.split("\n"):
            if "TDP(mWh)_0" in line:
                power_value = float(line.split("=")[1].strip())  # Extracting the power value
                return power_value / 1000  # Converting mWh to Watts
        
    except sp.CalledProcessError as e: # If error occurs while running the command (Exception 2)
        print("Error in getting the total power:", e.output.decode())
    return None  # If failed to exexute the command

def get_process_cpu_usage(process_name):
    """Finding out the CPU usage percentage of a particular application i.e. running currently."""
    for proc in p.process_iter(['pid', 'name', 'cpu_percent']):
        if process_name.lower() in proc.info['name'].lower():
            return proc.info['cpu_percent']
    return 0  # If process not found

def estimate_power_usage(app_name):
    print(f"Monitoring power usage for {app_name}...\n")
    total_power_consumed = 0
    duration = 0
    
    try:
        while True:
            total_power = get_total_power()
            app_cpu_usage = get_process_cpu_usage(app_name)

            if total_power is not None:
                estimated_power = total_power * (app_cpu_usage / 100)  # Estimated or Approximate power usage
                timestamp = t.strftime("%Y-%m-%d %H:%M:%S")
                total_power_consumed += estimated_power
                duration += 2
                print(f"{app_name} - {timestamp} - CPU: {app_cpu_usage}% - Power: {estimated_power:.2f} W")

#Appending the Data to the CSV file
                with open(CSV_FILE, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([t.strftime("%Y-%m-%d %H:%M:%S"), app_name, app_cpu_usage, estimated_power])

            t.sleep(2)  # Checking the application for every 2 seconds of their running time.
    except KeyboardInterrupt: # If user interrupts the monitoring i.e. Ctrl+C (Exception 3)
        print("\nMonitoring stopped.")
        print(f"Total power consumed by {app_name} during the session: {total_power_consumed:.2f} W.")
        print(f"Monitoring duration: {duration} seconds.")

if __name__ == "__main__":
    app_name = "Edge"  # You can change it's name to any sort of target app that you are willing to moniter (e.g Chrome, Firefox, Edge, etc.)
    estimate_power_usage(app_name)
