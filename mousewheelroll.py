import mouse
import time
import sys

# pos is to lef, neg to right
#

DELTA=-0.01
TIMER=2
SPEED=.01

# 3D
# DELTA=-0.1
# TIMER=2
# SPEED=0.1

# 2D
# DELTA=-0.01
# TIMER=2
# SPEED=.01

for i in range (0,TIMER):
	print("auto mousewheel %f in %d" % (DELTA,TIMER - i))
	sys.stdout.flush()
	time.sleep(1)
	
print("auto mousewheel scrolling...")
sys.stdout.flush()

while(1):
	mouse.wheel(delta=DELTA);
	time.sleep(SPEED)
	