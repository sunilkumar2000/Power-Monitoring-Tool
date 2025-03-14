# ✪ Power-Monitoring-Tool

Tracking the power usage of any Application i.e. executed within a Windows Operating System.
Taking the Power usage of the specific application into measurement using Intel Power Gadget and a Python library named psutil.
It keeps track of CPU power usage and application CPU usage continuously, writing the data to a CSV file for further processing and analysis.


## → Features

- Estimates the real-time power usage of any given specified application.
- Logs the entire power data into a CSV file for future analysis.
- Provides the total power consumed and total run time of the particular app when the monitoring session terminates with a Keyboard Interruption i.e. `Ctrl+C`.
- Integrates perfectly and continuously with Intel Power Gadget.


## → Prerequisites

Make sure :
- Python 3.(x) is installed on your system
- `psutil` library is installed.  If not, install it using the following command:
```bash
pip install psutil
```
- You CPU is powered by Intel and Intel Power Gadget is installed. If not install it from [Intel Power Gadget](https://www.techspot.com/downloads/downloadnow/7172/?evp=e89bb7915b334e8355e9bcfba67df4ba&file=9479#google_vignette).
- Your Operating System is Windows. (Because these operations and Integrations only work on Windows OS)


## → Installation and Setup

1. Install Required Dependencies
   - Before running the script make sure all the dependencies are installed. If not, Install using the command line
```bash
pip install psutil
```
2. Install Intel Power Gadget
   - This script integrates and relies on Intel Power Gadget for measuring the power consumption of the application.
   - Install it from here [Intel Power Gadget](https://www.techspot.com/downloads/downloadnow/7172/?evp=e89bb7915b334e8355e9bcfba67df4ba&file=9479#google_vignette).
3. Clone the Repository
   - If using Github clone the repository using:
```bash
git clone https://github.com/sunilkumar2000/Power-Monitoring-Tool
cd Power-Monitoring-Tool
```
4. Configure Intel Power Gadget Path
   - Make sure the Intel Power Gadget executable path in the script matches your system's installation location. If not, set it using through environment variables:
```bash
POWER_GADGET_PATH = r"C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe"
```

## → How to Use the Script

1. Run the Script
   - Navigate to the Project folder in your terminal or command prompt and execute.
```bash
python power_monitor.py
```
2. Specify the Application to the Monitor
   - By default, the script monitors Microsoft Edge:
```bash
app_name = "Edge"
```
  - To monitor another app, change "Edge" to any other process or app name (e.g., "Chrome", "Firefox", or "Notepad").
3. Stop Monitoring
  - Press `Ctrl+C` to stop the execution. Which is a keyboard interruption in technical terms
  - It displays:
      - Total power consumed during the session.
      - Total monitoring duration.


## → How the Script Works

The script monitors the power consumption of a specific application by utilizing Intel Power Gadget and psutil. It runs continuously, collecting power data at intervals and saving it into a CSV file.
1. Script Intialization
   - The script first imports required libraries:
       - `psutil` → To monitor CPU usage of a specific application.
       - `subprocess` → To run Intel Power Gadget and extract power data.
       - `csv` → To log the power data into a CSV file.
2. Intel Power Gadget Execution
   - The script executes Intel Power Gadget every second to record the CPU's total power usage (Watts).
   - The output is analyzed to extract TDP (Thermal Design Power).
3. Monitor CPU Usage of Specific Application
   - It looks for the target application (e.g., Edge, Chrome, Firefox, Notepad).
   - Grabs the CPU usage (%) of the application via psutil.
4. Power Usage Estimation
   - This script continuously checks:
       - Total Power Usage of the CPU(W)
       - CPU usage of the specified app(%)
   - Then it estimates the Power Consumption Using
```bash
estimated_power = total_power * (app_cpu_usage / 100)
```
  - This assumes that the power scales linearly with the CPU usage.
  - The data is displayed on the console and saved in a CSV file automatically.
5. Stop Monitoring
  - The user can stop monitoring by pressing `Ctrl + C`.
  - The script will display:
      - Total power consumed by the app
      - Total duration of the monitoring


## → Data Output and Saving (CSV File)

- This script saves all the data into a CSV file that is automatically generated inside the folder.
- Power_Monitor_Data.csv file provides the details of `Timestamp`, `App Name`, `CPU Usage(%)`, `Estimated Power(W)`.


## → Troubleshooting

- ModuleNotFoundError: No module named 'psutil'
Fix it by installing using the following command line:
```bash
pip install psutil
``` 
- Intel Power Gadget Not Found
Fix it by downloading and installing Intel Power Gadget for Windows system using [Intel Power Gadget](https://www.techspot.com/downloads/downloadnow/7172/?evp=e89bb7915b334e8355e9bcfba67df4ba&file=9479#google_vignette).


## Summary of the Entire Script Functionality
- ✅ Runs Intel Power Gadget to check total CPU power consumption.
- ✅ Determines the CPU usage (%) of the target app that have been in use.
- ✅ Estimates the power consumption(W) based on CPU usage .
- ✅ Saves real-time power data into a CSV file.
- ✅ Shows the total power drawn when monitoring is interrupted.


## → Note: The accuracy of the power consumption calculation may vary depending on the system's power management features and the precision of `psutil` data with the Intel Power Gadget and CPU processing.
## → Please ensure that the application you want to monitor is running during the execution of the script.
