import math
import matplotlib.pylab as plt
from termcolor import colored
g=9.8

angle = int(input(colored("Enter the angle of launch in degrees: ","red")))
vel = int(input(colored("Enter the initial velocity (m/s): ","red")))
h1= int(input(colored("Enter initial height in meters: ","red")))
h2= int(input(colored("Enter final height in meters: ","red"))) 

print("\n----------------------------------------OUTPUT----------------------------------------\n\n")

def cosine(x):
    c = math.cos(math.radians(x))
    return(c)


def sine(x):
    s = math.sin(math.radians(x))
    return(s)

def langle(angle):
    langle= -angle
    print(colored("Landing angle: -"+str(angle)+" degrees\n","green")) 

def calcVelocities(s,c,v):
    v0x = v*c
    v0y = v*s
    print(colored("Initial horizontal velocity: " + str(v0x) + " m/s\n","cyan"))
    print(colored("Initial vertical velocity: " + str(v0y) + " m/s\n","cyan"))
    vFx = v0x
    vFy = -v0y
    print(colored("Final horizontal velocity: " + str(vFx) + " m/s\n","cyan"))
    print(colored("Final vertical velocity: " + str(vFy) + " m/s\n","cyan"))

def inheight():
    ih=h1
    print(colored("Initial height: "+str(h1)+" meters\n","blue"))             

def maxHeight(v,s,h1):
    h = h1+((v*v)s*2)/(2*g)
    print(colored("Max height: " + str(h) + " meters\n","blue"))
    return h

def fheight():
    fh=h2
    print(colored("Final height: "+str(h2)+" meters\n","blue"))        
    

def horizontalRange(v,s,c):
    r = ((v**2)*2*s*c)/(g)
    print(colored("Horizontal range: " + str(r) + " meters\n","blue"))
    return r
    
    
def timeOfFlight(v,s):
    t = 2*((v)*s)/(g)
    print(colored("Time in flight: " + str(t) + " seconds\n","magenta"))
    t1=t/2
    print(colored("Time to reach maximum height: "+str(t1)+" seconds","magenta"))
    return t
    return t1
def t(v,s,g):
    return 2*((v)*s)/(g) 

def h_t():
    T=0.0
    H=[]
    t_s=[]
    while T<=t(vFy,v0y,g):
      h=v0y*T-0.5*g*T*T+h1
      H.append(h)
      t_s.append(T)
      T=T+0.01
    plt.plot(t_s,H)
    plt.xlabel('Time(s)')
    plt.ylabel('Height(m)')
    plt.title('Height vs Time')
    
    plt.show()

def vx_t():
  T=0.0
  t_s=[]
  vx=[]
  while T <= t(vFy,v0y,g):
    vx.append(v0x)
    t_s.append(T)
    T=T+0.01
  plt.plot(t_s,vx,("--b"))
  plt.xlabel("Time(s)")
  plt.ylabel("Vx(m/s)")
  plt.title("Horizontal velocity vs Time")

  plt.show()

def vy_t():
  T=0.0
  vy=[]
  t_s=[]
  while T<=t(vFy,v0y,g):
    v=v0y-g*T
    vy.append(v)
    t_s.append(T)
    T=T+0.01
    
  plt.plot(t_s,vy,("--b"))
  plt.xlabel("Time(s)")
  plt.ylabel("Vy(m/s)")
  plt.title("Vertical velocity vs Time")
  plt.show()

def calcProjMot(x,v):
    c = cosine(x)
    s = sine(x)
    langle(angle)
    calcVelocities(s,c,v)
    inheight()
    maxHeight(v,s,h1)
    fheight()
    horizontalRange(v,s,c)
    timeOfFlight(v,s)
calcProjMot(angle, vel)