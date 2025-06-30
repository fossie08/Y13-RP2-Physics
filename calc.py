import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

df = pd.read_excel('data.xlsx', sheet_name=0)

df.columns = ['Time', 'Angle']
time = df['Time']
angle = df['Angle']
peaks, _ = find_peaks(angle)
troughs, _ = find_peaks(-angle)
peak_times = time.iloc[peaks]
peak_angles = angle.iloc[peaks]
trough_times = time.iloc[troughs]
trough_angles = angle.iloc[troughs]

plt.figure(figsize=(10, 6))
plt.plot(time, angle, label='Angle (deg)', color='blue')
plt.plot(peak_times, peak_angles, 'ro', label='Oscillation Peaks')
plt.plot(trough_times, trough_angles, 'ro', label='Oscillation Troughs')
plt.title('Oscillations Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.legend()
plt.grid(True)
plt.show()

print("Oscillation peak times (s):")
print(peak_times.to_list())
print("Oscillation peak angles (deg):")
print(peak_angles.to_list())
print("Oscillation trough times (s):")
print(trough_times.to_list())
print("Oscillation trough angles (deg):")
print(trough_angles.to_list())
