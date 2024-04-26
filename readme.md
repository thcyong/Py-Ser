#use the below to install/update the service
python PyTestService.py install
#use the below to start the service.
python PyTestService.py start




To start the service successfully, it needs make sure the below things
1. Put the python PATH to system PATH, not the user PATH.
2. make sure to copy the two files pythoncomxx.dll and pywintypesxx.dll, from the folder \Lib\site-packages\pywin32_system32 to \Lib\site-packages\win32



//
mmc Services.msc
net stop PyTestService