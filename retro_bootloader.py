import time
import sys
import random

# Function to simulate typing with errors
def type_with_errors(text, error_rate=0.1, typing_speed=0.05):
    for char in text:
        # Random chance of an error happening
        if random.random() < error_rate and char.isalpha():
            # Insert a random wrong character
            sys.stdout.write(random.choice("abcdefghijklmnopqrstuvwxyz"))
            sys.stdout.flush()
            time.sleep(typing_speed)
            # Backspace (simulate correcting the mistake)
            sys.stdout.write('\b \b')
            sys.stdout.flush()
            time.sleep(typing_speed)

        # Type the correct character
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(typing_speed)
    print()  # For newline at the end

message = '''
C:\\> _ATTENTION_

Initiating connection to Serial No. 0867-5309...  
  
Error: "Jenny" not found. Please check the wall.  

Reverting to backup protocol...  

Rock ON, Command Line Maverick.

From one oldtimer to another: You might be born in '63, but you've still got those Hot 100 vibes from '82.

C:\\> _END TRANSMISSION_
'''

# Simulating the typing of the message with some errors
type_with_errors(message, error_rate=0.1, typing_speed=0.05)
