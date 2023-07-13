# CSSR_Updated
An updated repository for Nicolas Brodu's implementation of CSSR. This repository fixes C++ compilation issues with the old repository.

# Requisites
Note: for these files to work, you need to have downloaded the Boost library for C++ and either added the library to your $PATH or use the -I option for your compiler (e.g. g++).

# Auto-compiling Time Series Analysis
Brodu's initial repo included a pre-built TimeSeries.cpp file for time-series analysis, however past and future sizes were hard coded into the .cpp file. To help with workflow, I created a AutoTimeSeries.py file that allows the user to run the TimeSeries.cpp file for different past and future sizes. The basic usage is:

python AutoTimeSeries.py N_Past N_Future Kernel_Size Flag DataFile.txt

Make sure to have an output directory setup at ../Output/DataFile, as all outputs will be put there. 

# Direct Time Series Analysis
If you want to work directly with this code, you will have to compile all necessary components yourself. Let us consider TimeSeries.cpp. If you haven't appeneded the Boost library to your $PATH, you will have to compile like so:

g++ -I /opt/local/libexec/boost/1.71/include -o Time TimeSeries.cpp ,

where the -I tells the compiler where to find the Boost library (this will be a different filepath depending on how and where you installed Boost). The -o option is required to correctly name the compiled executable. To then run the executable, usage is:

./Time Kernel_Size Flag Output_Directory DataFile.txt
