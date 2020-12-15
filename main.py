import math
import matplotlib.pylab as plt
g=9.8


print("\n----------INPUT----------\n")

angle = int(input("Enter the angle of launch in degrees: "))
vel = int(input("Enter the initial velocity (m/s): "))
h1= int(input("Enter initial height in meters: "))
h2= int(input("Enter final height in meters: ")) 

print("\n----------OUTPUT----------\n")

def cosine(x):
    c = math.cos(math.radians(x))
    return(c)

def sine(x):
    s = math.sin(math.radians(x))
    return(s)

def langle(angle):
    langle= -angle
    print("Landing angle: -"+str(angle)+" degrees\n")

def calcVelocities(s,c,v):
    v0x = v*c
    v0y = v*s
    print("Initial horizontal velocity: " + str(v0x) + " m/s\n")
    print("Initial vertical velocity: " + str(v0y) + " m/s\n")
    vFx = v0x
    vFy = -v0y
    print("Final horizontal velocity: " + str(vFx) + " m/s\n")
    print("Final vertical velocity: " + str(vFy) + " m/s\n")

def inheight():
    ih=h1
    print("Initial height: "+str(h1)+" meters\n")            

def maxHeight(v,s,h1):
    h = h1+((v*v)*s**2)/(2*g)
    print("Max height: " + str(h) + " meters\n")
    return h

def fheight():
    fh=h2
    print("Final height: "+str(h2)+" meters\n")        
   
def horizontalRange(v,s,c):
    r = ((v**2)*2*s*c)/(g)
    print("Horizontal range: " + str(r) + " meters\n")
    return r
   
def timeOfFlight(v,s):
    t = 2*((v)*s)/(g)
    print("Time in flight: " + str(t) + " seconds\n","magenta")
    t1=t/2
    print("Time to reach maximum height: "+str(t1)+" seconds","magenta")
    return t
    return t1

def t(v,s,g):
    return 2*(v*s)/(g)

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
# ===============================================================

def vx_t(vFy,v0y,g):
  T=0.0
  t_s=[]
  vx=[]
  while T <= t(vFy,sine(angle),g):
    vx.append(vFy*sine(angle))
    t_s.append(T)
    T=T+0.01
  plt.plot(t_s,vx,("--b"))
  plt.xlabel("Time(s)")
  plt.ylabel("Vx(m/s)")
  plt.title("Horizontal velocity vs Time")

  plt.show()

def vy_t(vFy,v0y,g):
  T=0.0
  vy=[]
  t_s=[]
  while T<=t(vFy,sine(angle),g):
    v=v0y-g*T
    vy.append(v)
    t_s.append(T)
    T=T+0.01
  plt.plot(t_s,vy,("--b"))
  plt.xlabel("Time(s)")
  plt.ylabel("Vy(m/s)")
  plt.title("Vertical velocity vs Time")
  plt.show()



def h_t():
    T=0.0
    H=[]
    t_s=[]
    while T<=2*vel*sine(angle)/g:
      h = sine(angle)*vel*T - 0.5*g*T**2 + h1
      H.append(h)
      t_s.append(T)
      T += 0.01
    plt.plot(t_s,H)
    plt.xlabel('Time(s)')
    plt.ylabel('Height(m)')
    plt.title('Height vs Time')
    plt.show()

calcProjMot(angle, vel)

choice = -1
while choice!=4:
    print("Enter you choice:")
    choice = int(input("\n1. Height vs Time Graph (H vs T)\n2. Vertical Velocity vs Time (Vy vs T)\n3. Horizontal Velocity vs Time (Vx vs T)\n4.Exit\n"))
    if choice==1:
        h_t()
    elif choice == 2:
        vy_t(vel, sine(angle)*vel ,g)
    elif choice == 3:
        vx_t(vel, sine(angle)*vel ,g)
    else:
        break