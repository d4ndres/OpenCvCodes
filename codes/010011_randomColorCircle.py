import cv2
import numpy as np
import random 

def getDistance(x1,y1,x2,y2):
	x = x2-x1
	y = y2-y1
	return (x*x+y*y)**0.5


class Particle:
	def __init__(self, x, y, radius, canvas):
		
		COLORS = [(252,177,114), (163,114,252), (127,203,245)]
		self.x = x
		self.y = y
		self.radius = radius
		self.canvas = canvas
		self.color = COLORS[random.randint(0, len(COLORS) - 1)]

	def draw(self):
		cv2.circle(self.canvas, (self.x,self.y), self.radius, self.color , -1)


def run():
	w,h = 255,255
	image = 255*np.ones((w,h,3), dtype=np.uint8)

	particles = []


	r = 20
	i = 0
	while i < 15:
		x, y = random.randint(r,w-r), random.randint(r,h-r)
		particles.append( Particle(x,y,r,image) )

		j = 0
		while j < len(particles):
			
			d = getDistance( 	particles[i].x,
								particles[i].y,
								particles[j].x,
								particles[j].y)
			if particles[j] == particles[i]:
				pass
			elif d < r*2:
				
				particles[i].x = random.randint(r,w-r)
				particles[i].y = random.randint(r,h-r)
				j = 0
				continue
			j += 1
		i += 1

	for p in particles:
		p.draw()


	cv2.imshow('img', image)
	cv2.imwrite('src/randomColorCircle.png', image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	run()