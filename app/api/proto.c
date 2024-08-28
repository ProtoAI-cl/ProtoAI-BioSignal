#include <stdio.h>
#include <pigpio.h>

int move(int pin[], int angle[]){
    /*
     * This function is used to execute a hand motion.
     * It recieves 12 inputs in 2 int arrays:
     * pin[] contains the pin number for each servo
     * angle[] contains the angle of movement desired
     */
    if(gpioInitialise()<0){return 1;}

    gpioSetMode(pin[0],PI_OUTPUT);
    gpioSetMode(pin[1],PI_OUTPUT);
    gpioSetMode(pin[2],PI_OUTPUT);
    gpioSetMode(pin[3],PI_OUTPUT);
    gpioSetMode(pin[4],PI_OUTPUT);
    gpioSetMode(pin[5],PI_OUTPUT);

    gpioSetPWMrange(pin[0],180);
    gpioSetPWMrange(pin[1],180);
    gpioSetPWMrange(pin[2],180);
    gpioSetPWMrange(pin[3],180);
    gpioSetPWMrange(pin[4],180);
    gpioSetPWMrange(pin[5],180);

    if(gpioPWM(pin[0],angle[0])!=0){return 1;}
    if(gpioPWM(pin[1],angle[1])!=0){return 1;}
    if(gpioPWM(pin[2],angle[2])!=0){return 1;}
    if(gpioPWM(pin[3],angle[3])!=0){return 1;}
    if(gpioPWM(pin[4],angle[4])!=0){return 1;}
    if(gpioPWM(pin[5],angle[5])!=0){return 1;}

    return 0;
}

float percentage(int angle){
    // Given the allowed servo input, wich should be
    // and ammount between 1 and 2 ms, calculate
    // this number having the desired movement angle.
    //
    // For this, divides 1 ms in 180 parts, multiplies
    // it by the desired angle, and adds 1 ms wich is the
    // base ms.
    return (angle/180.0) + 1;
}
