import subprocess
import os
import sys

# Usage: python AutoTimeSeries.py N_past N_Fut Kernel_Size Flag Data_file

#Settings 

if len(sys.argv)<6:
    raise ValueError("Not Enough Arguement: Usage: python AutoTimeSeries.py N_past N_Fut Kernel_Size Flag Data_file")

N_Past = sys.argv[1]
N_Fut = sys.argv[2]
k = sys.argv[3]
flag = sys.argv[4]
data_file = sys.argv[5]


print('Compiling for ', N_Past, ' Past Samples, and ', N_Fut, ' Future Samples')

#Change file of TimeSeries.cpp

file = open('TimeSeries.cpp')
#print(file.read())

script = file.read()

parse = script.split(sep='#define N_PAST_SAMPLES ')
subparse = parse[1].split(sep='\n')
subparse[0] = str(N_Past)
parse1 = ''
for line in subparse:
    parse1 += line + '\n'
script = parse[0] + '#define N_PAST_SAMPLES '+ parse1

parse = script.split(sep='#define N_FUTURE_SAMPLES ')
subparse = parse[1].split(sep='\n')
subparse[0] = str(N_Fut)
parse1 = ''
for line in subparse:
    parse1 += line + '\n'
script = parse[0] + '#define N_FUTURE_SAMPLES '+ parse1

file = open('TimeSeries.cpp', 'w')
file.write(script)

# Compile File

res = subprocess.run("g++ -I /opt/local/libexec/boost/1.71/include -o Time TimeSeries.cpp", shell=True, capture_output=True) 
#print(res)

if len(res.stderr)==0:
    print('Success! - Time is compiled')
else:
    print('Error: Check TimeSeries.cpp')
    
os.chdir("..")

#print(os.getcwd())

Out_Folder = data_file.split(sep='.')[0].split(sep='/')[1]

print(Out_Folder)
    
res = subprocess.run("./Compiled/Time " + str(k) + ' ' + str(flag) + ' Output/'+ Out_Folder + ' ' + str(data_file), shell=True, capture_output=True)

print(res.stdout.decode())
