import time
#the class that is a cube, that massive list of attributes represents the faces of a solved cube
class cube:
    def __init__(self, b1, b2, b3, b4, g1, g2, g3, g4, y1, y2, y3, y4, s1, s2, s3, s4, o1, o2, o3, o4, r1, r2, r3, r4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.g1 = g1
        self.g2 = g2
        self.g3 = g3
        self.g4 = g4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.o1 = o1
        self.o2 = o2
        self.o3 = o3
        self.o4 = o4
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
#this function here does all the possible 'moves' u can do on a 2x2 (or 3x3 but thats not relevant) cube
    def move(self, z, n):
         n = n%4
         fronk = 0
         for fronk in n:
            if z == 'u':
                frank = self.b1
                self.b1 = self.b2
                self.b2 = self.b3
                self.b3 = self.b4
                self.b4 = frank
                jimbo = self.g1
                self.g1 = self.r1
                self.r1 = self.s1
                self.s1 = self.o1
                self.o1 = jimbo
                jiminycricket = self.g2
                self.g2 = self.r2
                self.r2 = self.s2
                self.s2 = self.o2
                self.o2 = jiminy cricket
            elif z == 'd':
                babycowboy = self.y1
                self.y1 = self.y4
                self.y4 = self.y3
                self.y3 = self.y2
                self.y2 = babycowboy
                michaeljacksonsredhothair = self.g4
                self.g4 = self.r4
                self.r4 = self.s4
                self.s4 = self.o4
                self.o4 = michaeljacksonsredhothair
                elvispresleyskillerpoo = self.g3
                self.g3 = self.r3
                self.r3 = self.s3
                self.s3 = self.o3
                self.o3 = elvispresleyskillerpoo
            elif z == 'l':
                pleaseletmegoijustwannaseemywifeandkids = self.o1
                self.o1 = self.o2
                self.o2 = self.o3
                self.o3 = self.o4
                self.o4 = pleaseletmegoijustwannaseemywifeandkids
                thephantomoftheoperaishereinsidemymind = self.b1
                self.b1 = self.s4
                self.s4 = self.y4
                self.y4 = self.g2
                self.g2 = thephantomoftheoperaishereinsidemymind
                stopmakingfunofmycode = self.b4
                self.b4 = self.s1
                self.s1 = self.y1
                self.y1 = self.g3
                self.g3 = stopmakingfunofmycode
            elif z == 'r':
                pleasedontkillmeforwritingbadcode = self.r1
                self.r1 = self.r2
                self.r2 = self.r3
                self.r3 = self.r4
                self.r4 = pleasedontkillmeforwritingbadcode
                usbubedaufbawyifbwayfubyhvubd = self.b3
                self.b3 = self.g4
                self.g4 = self.y2
                self.y2 = self.s2
                self.s2 = usbubedaufbawyifbwayfubyhvubd
                its0250iwanttosleepihatemyselfforleavingthistothelastminute = self.b2
                self.b2 = self.g1
                self.g1 = self.y3
                self.y3 = self.s3
                self.s3 = its0250iwanttosleepihatemyselfforleavingthistothelastminute
            elif z =='f':
                selfywelfy = self.g1
                self.g1 = self.g2
                self.g2 = self.g3
                self.g3 = self.g4
                self.g4 = selfywelfy
                fricklefrackle = self.y3
                self.y3 = self.r2
                self.r2 = self.b4
                self.b4 = self.o4
                self.o4 = fricklefrackle
                ernorubikhimself = self.y4
                self.y4 = self.r3
                self.r3 = self.b3
                self.b3 = self.o1
                self.o1 = ernorubikhimself
            elif z =='b':
                backlewackle = self.s1
                self.s1 = self.s2
                self.s2 = self.s3
                self.s3 = self.s4
                self.s4 = backlewackle
                roundabout = self.b2
                self.b2 = self.r4
                self.r4 = self.y1
                self.y1 = self.o2
                self.o2 = roundabout
                yes = self.b1
                self.b1 = self.r1
                self.r1 = self.y2
                self.y2 = self.o3
                self.o3 = yes
            else:
                print("u've mucked up")
                #this is the closest i've got to an error message
                
#makes a cube that is to all intents and purposes 'solved' and can be compared to the usercube to see if the usercube is 'solved'
def cubesolved():
    solvedcube = cube("b1", "b2", "b3", "b4", "g1", "g2", "g3", "g4", "y1", "y2", "y3", "y4", "s1", "s2", "s3", "s4", "o1", "o2", "o3", "o4", "r1", "r2", "r3", "r4")
    return solvedcube

#makes a cube, fills it with arbitrary values        
def blankcube():
    cubeblank = cube(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
    return cubeblank

#makes the user describe how their cube looks
def entercube():
    print("As i said earlier, the finished code should look like this:")
    printsolvedcube()
    print("I need you to describe the cube to me, so with the cube still in the orientation from earlier, you need to enter which pieces are where")
    print("okay you're gonna tell me all about your cube now")
    print("Make sure you're still holding it the way I described earlier, if you've moved it, close the program and start again.")
    wait(5)
    usercube.b4 = 'b'
    usercube.g2 = 'g'
    usercube.o1 = 'o'
    print("First let's do the 'up' face, the face that is facing up, the one with the black square in the bottom left corner")
    usercube.b3 = input("What colour is the square directly to the right of that black piece? Please choose from: B O R G S Y : ")
    usercube.b1 = input("Now what colour is the square on the top left corner of the 'up' face? ")
    usercube.b2 = input("Now what colour is the square on the top right corner of the 'up' face? ")
    print("This concludes the 'up' face")
    wait(5)
    print("Now lets do the 'left' face, this is the face that has an orange piece in the top right corner.")
    usercube.o4 = input("What colour is the square directly below that orange piece? Please choose from: B O R G S Y : ")
    usercube.o2 = input("What colour is the square next to that orange piece? ")
    usercube.o3 = input("What colour is the last square on that face? ")
    wait(5)
    print("Cool, now lets do the 'front' face, this is the face with the green square in the top left corner.")
    usercube.g1 = input("What colour is the square next to that green square? Remember borgsy! ")
    usercube.g3 = input("What colour is the square below that green square? ")
    usercube.g4 = input("What colour is the last square on that face? ")
    print("Now this gets difficult!")
    wait(5)
    print("Let's start with the 'right' face, this is the face opposite the 'left' face, which is the face with the orange square in the top right corner.")
    usercube.r2 = input("Lets say that the square opposite the orange one is the top left corner, what colour is it? ")
    usercube.r1 = input("What about the piece next to it? ")
    usercube.r3 = input("What about the piece below it? ")
    usercube.r4 = input("And the last cube on the face? ")
    wait(5)
    print("Okay, now the 'back' face, this is the face opposite the 'front' face, which is the face with the green square in the top left corner.")
    print("Again, let's say that the face opposite that green square is the top right corner.")
    usercube.s1 = input("What colour is that piece? ")
    usercube.s2 = input("What colour is the piece next to it? ")
    usercube.s4 = input("What colour is the piece below it? ")
    usercube.s3 = input("What colour is the last piece? ")
    wait(5)
    print("Okay and lastly lets do the 'down' face, this is the face opposite that one black piece in the bottom left corner of the 'up' face.")
    usercube.y4 = input("Once more, let's say that the piece opposite it is the bottom right corner, what colour is this piece? " )
    usercube.y3 = input("And the piece next to it? ")
    usercube.y1 = input("The piece above it? ")
    usercube.y2 = input("Lastly, the final piece? ")
    print("okay dokay")
    print("Please return your cube to the original position.")
    print("Okay lets figure out how to solve this bad boy." )

#this function is more for my convenience than the function of the code    
def wait(amount):
    time.sleep(amount)
    print()
    print()
    '''print("OOH yes wait a minute mr postman")'''

#does what it says on the tin    
def printsolvedcube():
    print("             ")
    wait(1)
    print("     Y Y     ")
    wait(1)
    print("     Y Y     ")
    wait(1)
    print("     O O     ")
    wait(1)
    print("     O O     ")
    wait(1)
    print(" G G B B S S ")
    wait(1)
    print(" G G B B S S ")
    wait(1)
    print("     R R     ")
    wait(1)
    print("     R R     ")
    wait(1)
    print("             ")

def solverwolver():
    #i have not written this function, this function will brute force every possible combination of the 6 moves, starting at a combination of length 1, increasing incrementally, once solved
    #it will advise the user of which moves to undertake to solve their cube. Brute forcing is not an efficient method of solving a cube, however it will work well enough for a 2x2.

#the main body of code    
print("Hello and welcome to Louie and Mikolaj's epic code! This code will allow you to enter information describing what the faces of a 2x2 rubiks cube look like, and then it will help you solve it!")
print("Please note; I am not good at code, do not try to break my code, do not try anything fancy becuase you are curious about what will happen. What will happen is that the code will break and i will be sad. :(")
wait(5)
print("In our interface this is what a solved rubiks cube looks like:")
printsolvedcube()
print("This is a flat map of the 2x2 cube, the letters represent the different colours, with 4 squares of colour on each face.")
wait(5)
print("Y stands for yellow. O stands for orange. B stands for black. R stands for red. G stands for green. S stands for blue. Why does S stand for blue? Well why shouldn't it? Think before you speak.")
wait(5)
print("Now I'd like you to take your cube and look at it. Notice that each piece has 3 colours each. Find the piece that has 1 black square, 1 green and 1 orange.")
wait(5)
print("Got it? Good, press enter when you do.")
input()
print("Great, this is gonna be our central piece, this piece won't move, if you understand what I mean, if you don't, please file a complaint, I don't care who with.")
wait(1)
print("Orient the cube so that the black face of the central piece is in the bottom left corner of a face facing you, this should mean the red face of that piece is facing down, and the green face is facing left.")
wait(1)
print("If this isn't the case, your cube may be different to mine - in version 2 I'll allow users to tell this program what colours their cube is, for now, I'm sorry but this program may be hard to follow.")
wait(1)
print("When you're ready to continue, please press enter.")
input()
usercube = blankcube()
solvedcube = cubesolved()
entercube()
solverwolver()
