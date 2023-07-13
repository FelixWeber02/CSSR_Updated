# CSSR_Updated
An updated repository for Nicolas Brodu's implementation of CSSR. This repository fixes C++ compilation issues with the old repository.

# Auto-compiling Time Series Analysis
Brodu's initial repo included a pre-built TimeSeries.cpp file for time-series analysis, however past and future sizes were hard coded into the .cpp file. To help with workflow, I created a AutoTimeSeries.py file that allows the user to run the TimeSeries.cpp file for different past and future sizes. The basic usage is:

python AutoTimeSeries.py N_Past N_Future Kernel_Size Flag DataFile.txt

Make sure to have an output directory setup at ../Output/DataFile, as all outputs will be put there. 
