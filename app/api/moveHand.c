#include <pigpio.h>
#include "moveHand.h"

int move(int pin[], int angle[]){
    /*
     * This function is used to execute a hand motion.
     * It recieves 12 inputs in 2 int arrays:
     * pin[] contains the pin number for each servo
     * angle[] contains the angle of movement desired
     */
    
    if(initialiseServos(pin)!=0){return 1;}
    if(openHand(pin)!=0){return 1;}
    if(customMoveHand(pin, angle)!=0){return 1;}

    return 0;
}

void stopComunication(){
    /*
     * Stops the comunication, releases memory and stop
     * any running thread.
    */
    gpioTerminate();
}

int initialiseServos(int pin[]){
    if(gpioInitialise()<0){return 1;}
    for(int indexPinFinger=0;indexPinFinger<=5;i++){
        if(gpioSetMode(pin[indexPinFinger],PI_OUTPUT)!=0){return 1;}
    }
}

int customMoveHand(int pin[], int angle[])
{
    for(int indexFinger=0;indexFinger<=5;indexFinger++){
        if(gpioSetPWMrange(pin[indexFinger], angle[indexFinger])!=0){return 1;}
    }
    return 0;
}

void openHand(int pin[])
{
    int angle[5] = {180, 180, 180, 180, 180};
    return customMoveHand(pin,angle)
}

void closeHand(int pin[])
{
    int angle[5] = {0, 0, 0, 0, 0};
    return customMoveHand(pin,angle)
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


