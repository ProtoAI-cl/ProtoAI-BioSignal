#ifndef MOVEHAND_H
#define MOVEHAND_H

// Function declarations

// Move the hand based on pin and angle arrays
int move(int pin[], int angle[]);

// Stop and release GPIO resources
void stopBoard();

// Initialize the servos based on the pin array
int initialiseServos(int pin[]);

// Move the hand with custom angles
int customMoveHand(int pin[], int angle[]);

// Open the hand (moves all servos to 180 degrees)
void openHand(int pin[]);

// Close the hand (moves all servos to 0 degrees)
void closeHand(int pin[]);

// Convert angle to percentage in ms for servo movement
float percentage(int angle);

#endif // MOVEHAND_H