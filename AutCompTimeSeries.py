import subprocess
import os
import sys

#Settings

N_Past = sys.argv[1]
N_Fut = sys.argv[2]

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

res = subprocess.run("g++ -I /opt/local/libexec/boost/1.71/include -o TimeVar_"+str(N_Past)+"_"+str(N_Fut) + " TimeSeries.cpp", shell=True, capture_output=True) 
#print(res)

if len(res.stderr)==0:
    print('Success! - TimeVar_'+str(N_Past)+"_"+str(N_Fut))
else:
    print('Error: Check TimeSeries.cpp')