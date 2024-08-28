# BioSignal Bridge


## What is this?

This is a Linux interface that receives and analyzes data from a USB device and sends it via WebSocket.

**Please read this README before running your program**


## How to run?

First, initialize your virtual environment:

```
python -m venv venv
```
Then activate it. On linux,use:
```
. venv/bin/activate
```
Now, Install the dependencies:
```
pip install -r dependencies.txt
```
You can now start editing or execute the program.

## Environment

This project is developed using a Raspberry Pi model 3B+. I encountered some problems running the dependencies. To solve these issues, you must install some additional packages.

**(assuming you have your virtual environment active)**
```
sudo apt-get update
```
```
sudo apt-get install build-essential
```
```
pip install --upgrade pip
```
