Please extract the files to a directory.

************************************************************************************************

Firstly, you should run following two lines in your terminal

sudo apt-get install python3-tk
python3 -m pip install --upgrade Pillow

************************************************************************************************

If you have Ubuntu system, when you run the main.py you should see the GUI directly. 

************************************************************************************************
However, If you run our code from Ubuntu terminal in Windows system, 
then you should run the following code in your terminal.

export DISPLAY=localhost:0.0

And then you should install Xming to your computer. (You can find the setup in the zip file)
And please make sure Xming is running on your computer! (XLaunch)

After that you can run main.py from your terminal.
************************************************************************************************