Maze solver with the ability of mapping the space. Maze solving is based on the right wall rule. Robot has only front ultrasonic sensors, unlike most others robots on the Internet,
so it is necessary to turn robot to the right side to check if there is a wall. The robot is stopping every 20 cm and checking the right side. ( On the video, it's checking also 
the left side but it's just wasting a time, so it's fixed in the code).
Space mapping is based on using the stack. Every 20cm robot is pushing the direction to stack. Also in the situations when it's going back the same way 
its poping the element from the stack. At the end, you get the stack with the correct paths to the goal. It's explained in the code with the comments. If you have any questions
or need more detailed explanation feel free to ask. I will send you my final work, it was a faculty task, where everything is explained. Also keep in mind that robot, especially 
AlphaBot2 which I'm using, is not the perfect one. It has a lot of bugs like turning to the right side by itself, when the batteries are not full charged it's not working well 
and so on.
