

import subprocess
import os
import time

import uiautomation as automation





def exec_cmd(cmd, cwd=None, is_wait=True, timeout=15):
    rst = subprocess.Popen(cmd, cwd=cwd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           shell=True)
    # if is_wait:
    #     result = rst.communicate(timeout=timeout)
    #     result = dispose_result(result)
    #     return result
    # else:
    #     return rst.pid

# TQ_PATH = r"C:\Program Files (x86)\qianxin\tianqing"
# SAFEUI_PATH = os.path.join(TQ_PATH, r"TQSafeUI.exe")
# exec_cmd(SAFEUI_PATH)
# # tq_obj = TQClientUI()
# time.sleep(3)
#
# tq_obj.find_windows_control(ClassName="Qt5QWindowIcon")
#
# tq_obj.click(73, 530)

automation.WindowControl(ClassName="#32770").Click(10,10)




