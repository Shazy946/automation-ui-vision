# import sys
import os
import datetime
import subprocess
import time

log_calc = "none"
info_run = "note"

def PlayAndWait(macro, timeout_seconds=10, var1='-', var2='-', var3='-', path_downloaddir=None, path_autorun_html=None,
                browser_path=None):
    assert os.path.exists(path_downloaddir)
    assert os.path.exists(path_autorun_html)
    assert os.path.exists(browser_path)

    log = 'log_' + datetime.datetime.now().strftime('%m-%d-%Y_%H_%M_%S') + '.txt'
    log_1 = 'Log Date: ' + datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    path_downloaddir_1 = 'E:\Download'
    path_log = os.path.join(path_downloaddir, log)

    path_log_1 = os.path.join(path_downloaddir_1, log)

    args = r'file:///' + path_autorun_html + '?macro=' + macro + '&cmd_var1=' + var1 + '&cmd_var2=' + var2 + '&cmd_var3=' + var3 + '&closeKantu=0&direct=1&savelog=' + log

    proc = subprocess.Popen([browser_path, args])

    status_runtime = 0

    # print("Log File with show up at " + path_log)

    while (not os.path.exists(path_log) and status_runtime < timeout_seconds):
        #print("Waiting for macro to finish, seconds=%d" % status_runtime)
        time.sleep(1)
        status_runtime = status_runtime + 1

    if status_runtime < timeout_seconds:
        with open(path_log) as f:
            status_text = f.readline()

        status_init = 1 if status_text.find('Status=OK') != -1 else -1
    else:
        status_text = "Macro did not complete withing the time given: %d" % timeout_seconds
        status_init = -2
        proc.kill()

    global log_calc
    global info_run

    f = open(path_log_1, 'r')

    info_run = f.read()
    log_calc = log_1

def start():
    PlayAndWait('desktop', timeout_seconds=35, path_downloaddir=r'E:\Download\\',
                    path_autorun_html=r'E:\Download\calculate.html',
                    browser_path=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

def screenshot():
    PlayAndWait('screen', timeout_seconds=35, path_downloaddir=r'E:\Download\\',
                path_autorun_html=r'E:\Download\screen.html',
                browser_path=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')




