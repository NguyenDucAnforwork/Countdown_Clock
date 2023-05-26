# Countdown_Clock
This is a small Python program that I wrote myself where I create a countdown clock. You can adjust the hours and minutes as you like,
and when it counts down to zero, it will automatically ring to signal the end of time. 

This program is quite simple, very suitable for beginners to code 
and get acquainted with the Pygame library as well as the Python programming language.

# Explanation: 

1. Display the screen, set up fps, sound, font, and variables, 
2. Initialize total to store the initial time, total_secs as temporary time, start to start countdown, 
3. Declare 3 variables total_secs, total, start to mark when to countdown, 
4. Check for mouse clicks in each case: quit button, start button,..., 
5. After pressing start, the seconds decrease by 1, need to calculate the coordinates of the hour hand, minute hand and check the stop case. To update the clockwise at their correct coordinates after each second, we need to use some trigonometric tranformation. NOTE: we will work with Radian instead of degrees in Pygame.




