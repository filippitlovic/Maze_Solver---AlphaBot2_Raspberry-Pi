import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2

Ab = AlphaBot2()

#ultrasonic sensors

TRIG = 22  
ECHO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN)

def Distance():
	GPIO.output(TRIG,GPIO.HIGH)
	time.sleep(0.000015)
	GPIO.output(TRIG,GPIO.LOW)
	while not GPIO.input(ECHO):
		pass
	t1 = time.time()
	while GPIO.input(ECHO):
		pass
	t2 = time.time()
	return (t2-t1)*34000/2

class Stack: 
    def __init__(self): 
        self.elements = [] 
    
    def push(self, data): 
        self.elements.append(data) 
        return data 
    
    def pop(self): 
        return self.elements.pop() 
        
    def peek(self): 
        return self.elements[-1] 
        
    def get_stack(self):
        return self.elements

    def is_empty(self):
        return self.size == 0

# 1 - forward
# 2 - right
# 3 - left
Stack = Stack()
Stack.push(1) #first element is forward (1)

#Maze Solver algorithm with the space mapping, space mapping is reffered to the parts which are using the stack

def MazeSolver():
        if zastavica = 1 #it means it's going back from the loop
                element_out_of_stack = stack.pop()
        time.sleep(1)
	print("20cm forward")
        Ab.forward()
        time.sleep(1.5) #1.5 second or 20cm forward
        Ab.stop()
        time.sleep(1) #1 second robot not moving
        Distance_Front = Distance() #calculating distance from the obstacle infront 
        print("Distance_Front = %0.2f cm" %Distance_Front)
        if Distance_Front > 200: #if the distance is higher than 200cm, it means it's the end of the labyrinth 
		Ab.stop() 
		print("Finish!! Getting out of the maze is successful")
		return 0
        Ab.right() #robot is turning 90 degrees to the right because of the ultrasonic sensors 
        time.sleep(0.4)
	Ab.stop()
	time.sleep(2)
        Distance_Right = Distance() ##calculating distance from the obstacle on the right
        print("Distance_Right = %0.2f cm" %Distance_Right)
        if Distance_Right >=20: #if there is no wall at the right side, go there, to the east 
                last_element = Stack.peek()
                if zastavica = 1 and element_out_of_stack = 2:#if the robot is going back and the last element poped out from stack is 'right' then push 'forward'
                        time.sleep(1)
                        Stack.push(1)
                        zastavica = 0 
                        print("No wall on the right, go right")
                        return MazeSolver()
                if zastavica = 1:#if the flag is equal to 1, push 'left' 
                        time.sleep(1)
                        Stack.push(3)
                        zastavica = 0 #not going the same way anymore
                        print("No wall on the right, go right")
                        return MazeSolver()
                elif zastavica = 0:
                        time.sleep(1)
                        Stack.push(2)
                        print("No wall on the right, go right")
                        return MazeSolver()
	if (20 <= Distance_Front <= 200):
                if zastavica = 0:
                        Ab.left() #robot is turning 90 degrees to the left, to the north
                        time.sleep(0.4)
                        print("Forward")
                        Stack.push(1)
                        return MazeSolver()
        Ab.left() # robot is turning to the west
        time.sleep(1.05) 
	Ab.stop()
	time.sleep(2)
        Distance_Left = Distance()##calculating distance from the obstacle on the left
        print("Distance_Left = %0.2f cm" %Distance_Left)
        elif Distance_Left >= 20: #if there is no wall at the left, turn left
                if zastavica = 0:
                        Stack.push(3)
                        time.sleep(1)
                        print("No wall on the left, go left")
                        return MazeSolver()
        elif ((Distance_Left <= 20 ) and (Distance_Front <= 20) and (Distance_Right <=20)): #if there are walls from all 3 sides, turn back
		zastavica = 1 
                print("Turn back")
		Ab.left() 
                time.sleep(0.5) 
		return MazeSolver()



#
#
#creating new stack, beacause we need the last element from the original stack to become the first element so we can run the maze again with those directions	

def New_stack():
        Stack_new = Stack()
	while Stack.notEmpty() != 0:
                direction = Stack.pop()
                Stack_new.push(direction)
        print("Correct directions for the maze are: ")
        print(Stack_new.get_stack())



#
#
#Function when putting the robot on the start again and running all the way to the goal of the labyrinth but only with the right directions
def MazeSolverSecondTurn():
        if Stack.notEmpty() != 0:
                direction = Stack_new.pop()
                print("The remaining directions until reaching the destination: ")
                print(Stack_new.get_stack())
                if smjer = 1:
                        Ab.forward()
                        time.sleep(1.5)
                elif direction = 2:
                        Ab.right()
                        time.sleep(0.4)
                        Ab.stop()
                        time.sleep(2)
                        Ab.forward()
                        time.sleep(1.5)
                elif direction = 3:
                        Ab.left()
                        time.sleep(0.4)
                        Ab.stop()
                        time.sleep(2)
                        Ab.forward()
                        time.sleep(1.5)
        elif:
                print("Finish!!")
                
        
                
function = MazeSolver()
time.sleep(10)
function2 = New_stack()
time.sleep(10)
function3= MazeSolverSecondTurn()

			
