import subprocess

class SimpleAdb():
  def __init__(self, serial=''):
    self.serial = serial
    self.serialStr = '' if serial=='' else '-s '+serial

  def RunShellCommand(self, cmd):
    """Returns: dict of output lines"""
    self.currentCmd = 'adb '+self.serialStr+' shell '+cmd
    self.curOutput = subprocess.check_output(self.currentCmd, shell=True)
    if(len(self.curOutput) > 0 and self.curOutput[-1] == '\n'):
      self.curOutput = self.curOutput[0:-1]
    if(len(self.curOutput) == 0):
      return []
    return self.curOutput.split('\n')