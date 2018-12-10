# Reflex Tester

A reflex tester game written in python to run on the Raspberry Pi with GrovePi peripherals connected.  

## Getting Started

Connect the GrovePi peripherals as instructed below and then power on the Pi. Copy the reflex_tester.py file to your Raspberry Pi. 

### Prerequisites

You will need the following hardware to run the program:

```
1.	Raspberry Pi
2.	GrovePi Board
3.	GroveBuzzer
4.	GroveLCD
5.	GroveLED
6.	Grove Connect Wires
```

### Installing
To run the program properly, the peripherals must be connected to the GrovePi board in the following way:
* LCD screen into LCD port (middle port on USB/network input side)
* LED light into D3
* Button into D4
* Buzzer into D2

## Running the program

* Run the program from the command line on the Raspberry Pi by navigating to the containing folder and typing "python reflext_tester.py" 
* Follow the on-screen prompts. 
* Make sure to hit “enter” after inputting 'y' after each guess.

## Built With

* [GrovePi](https://www.dexterindustries.com/grovepi/)
* [RaspberryPi](https://www.raspberrypi.org/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
