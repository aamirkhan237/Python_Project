# pip install speedtest-cli
import speedtest
from speedtest import Speedtest
from speedtest import Speedtest

s = Speedtest()
# Bytes for conversion
bytes_num = 1000000
# Get download speed
dws = round(s.download() / bytes_num, 3)
# Get upload speed
ups = round(s.upload() / bytes_num, 2)
# Print internet speed
print(f'My download speed is: {dws} Mbps')
print(f'My upload speed is: {ups} Mbps')
