# Music Maker!!!!

Sam and Matt are making an app that generates music. Weew!

First steps - https://github.com/samhann/FractalMusicGen


# Boostrap working environment

Open PowerShell as Administrator

###1. Enable PowerShell script execution

Run this in PowerShell:
```
Set-ExecutionPolicy RemoteSigned
```

###2. Install Chocolatey package manager for Windows

Run this in PowerShell:
```
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

###3. Install git and python

Run this in PowerShell:
```
choco install git -y
choco install choco install python2 -y
powershell              # reload powershell 
```

To check that this worked run
```
Get-Command python      # should show path to python.exe
Get-Command git         # should show path to git.exe

python -V               # should print Python 2.7.11
git                     # should show git help prompt
```


###4. Clone repository

Navigate to the folder where you want to put your working folder and run the following in PowerShell
(eg you want your code in C:\code\music_maker)
```
cd C:\code\
git clone git@github.com:MattSegal/MusicMaker.git music_maker
```
Hopefully this works

###5. Install python packages

Navigate to C:\code\music_maker and install the required python packages

Test that your python package manager (pip) works
```
Get-Command pip         # should show path to pip.exe
pip -V                  # should show version of pip
```

then use it to install all of the packages in requirements.txt

```
pip install -r requirements.txt
```

now you should be ready to work!
