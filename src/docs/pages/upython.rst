Running MicroPython on Nucleo-F446RE
==============

Currently I am using a STM Nucleo-F446RE dev board that as that is what I had on hand that is well supported.
Since the number of IO needed for Inmoov might be significant, I may need to upgrade to a different Nucleo board in the future but for now we can test with this.
If and when I do make the change then this page will be rewritten / updated accordingly.  

I have mentioned before, I unfortunately am not interested in trying to support a bunch of different configurations but I don't see any reason why other boards can't be used.





Workstation Setup
-----------
    We need a couple more packages installed for this to work.  First is ST-Link Tools.  This will give us the st-flash utility that micropython is going to need later.
    
    .. code-block:: console
        
        sudo apt install stlink-tools



The rest of these instructions are taken from:  https://github.com/micropython/micropython/tree/master/ports/stm32
I am going to summarize them here.


Downloading micropython
-------------
More information here: https://github.com/micropython/micropython/tree/master/ports/stm32

    Navigate to https://micropython.org/download/
    Download the latest tar version (currently 1.17 at the time of writting)
    https://micropython.org/resources/source/micropython-1.17.tar.xz

    and extract it somewhere on your computer.  I just used my downloads folder.  You can use the file manager in Gnome or from the command line
    .. code-block:: console
        
        tar -xvf micropython-1.17.tar.xz

    You will need xz-utils installed.  It was already on my system somehow.  Not sure if it is part of Ubunto 20.04.
    .. code-block:: console
        
        sudo apt install xz-utils

    change directory into micropython



    Publisher and subscriber nodes for topics.  Generic for now






Upload micropython to the controller
--------------
    This is where the msg services are stored

    Download rshell from git: 

    git clone https://github.com/dhylands/rshell.git
    cd rshell


    Create a test file named main.py (must be this name)

        led = pyb.LED(1)
        while True:
            led.toggle()
            pyb.delay(1000)
    




    python3 -m rshell.main -p /dev/ttyACM0
    cp main.py /flash


    cd /flash
    edit boot.py
     (remove comment from last line)

    
    
    python3 -m rshell.main -p /dev/ttyACM0 cp main.py /flash



repl

