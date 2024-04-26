import os,sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".")) + os.path.sep + "."))
import logging
import time
from SMWinservice import SMWinservice

class PythonCornerExample(SMWinservice):
    _svc_name_ = "91SF Python"
    _svc_display_name_ = "91SF Python"
    _svc_description_ = "DY: That's a great service!"
     
    def start(self):
        self.isrunning = True
    
    def stop(self):
        self.isrunning = False

    def main(self):
        i = 0
        self.isrunning=True
        while self.isrunning:  
            try: 
                # will to do
                time.sleep(5)
            except Exception as e:
                raise e
if __name__ == '__main__':
    PythonCornerExample.parse_command_line()
    #p = PythonCornerExample("start")
    #p.main()
