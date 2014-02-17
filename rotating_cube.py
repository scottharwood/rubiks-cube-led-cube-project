"""
 Simulation of a rotating 3D Cube
 Developed by Leonel Machava <leonelmachava@gmail.com>

 http://codeNtronix.com
"""
import sys, math, pygame
from operator import itemgetter

class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)
 
    def rotateX(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)
 
    def rotateY(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)
 
    def rotateZ(self, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)
 
    def project(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, self.z)

class Simulation:
    def __init__(self, win_width = 640, win_height = 480):
        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Simulation of a rotating 3D Cube (http://codeNtronix.com)")
        
        self.clock = pygame.time.Clock()

        self.vertices = [
            Point3D(-1,-1,-1),#0
            Point3D(0,-1,-1),#1
            Point3D(1,-1,-1),#2
            Point3D(2,-1,-1),#3
            Point3D(-1,0,-1),#4
            Point3D(0,0,-1),#5
            Point3D(1,0,-1),#6
            Point3D(2,0,-1),#7
            Point3D(-1,1,-1),#8
            Point3D(0,1,-1),#9
            Point3D(1,1,-1),#10
            Point3D(2,1,-1),#11
            Point3D(-1,2,-1),#12
            Point3D(0,2,-1),#13
            Point3D(1,2,-1),#14
            Point3D(2,2,-1),#15
            #
            Point3D(-1,-1,0),#16
            Point3D(0,-1,0),#17
            Point3D(1,-1,0),#18
            Point3D(2,-1,0),#19
            Point3D(-1,0,0),#20
            Point3D(2,0,0),#21
            Point3D(-1,1,0),#22
            Point3D(2,1,0),#23
            Point3D(-1,2,0),#24
            Point3D(0,2,0),#25
            Point3D(1,2,0),#26
            Point3D(2,2,0),#27
            #
            Point3D(-1,-1,1),#28
            Point3D(0,-1,1),#29
            Point3D(1,-1,1),#30
            Point3D(2,-1,1),#31
            Point3D(-1,0,1),#32
            Point3D(2,0,1),#33
            Point3D(-1,1,1),#34
            Point3D(2,1,1),#35
            Point3D(-1,2,1),#36
            Point3D(0,2,1),#37
            Point3D(1,2,1),#38
            Point3D(2,2,1),#39
            #
            Point3D(-1,-1,2),#40
            Point3D(0,-1,2),#41
            Point3D(1,-1,2),#42
            Point3D(2,-1,2),#43
            Point3D(-1,0,2),#44
            Point3D(0,0,2),#45
            Point3D(1,0,2),#46
            Point3D(2,0,2),#47
            Point3D(-1,1,2),#48
            Point3D(0,1,2),#49
            Point3D(1,1,2),#50
            Point3D(2,1,2),#51
            Point3D(-1,2,2),#52
            Point3D(0,2,2),#53
            Point3D(1,2,2),#54
            Point3D(2,2,2),#55
        ]

        # Define the vertices that compose each of the 6 faces. These numbers are
        # indices to the vertices list defined above.
        self.faces  = [(0,1,2,3),(1,5,6,2),(5,4,7,6),(4,0,3,7),(0,4,5,1),(3,2,6,7)]

        # Define colors for each face
        self.colors = [(255,0,255),(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,255,0)]

        self.angle = 0
        
    def run(self):
        """ Main Loop """
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(50)
            self.screen.fill((0,32,0))

            # It will hold transformed vertices.
            t = []
            
            for v in self.vertices:
                # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                r = v.rotateX(self.angle).rotateY(self.angle).rotateZ(self.angle)
                # Transform the point from 3D to 2D
                p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                # Put the point in the list of transformed vertices
                t.append(p)

            # Calculate the average Z values of each face.
            avg_z = []
            i = 0
            for f in self.faces:

                z = (t[f[0]].z + t[f[1]].z + t[f[2]].z + t[f[3]].z) / 4.0
                avg_z.append([i,z])
                i = i + 1

            # Draw the faces using the Painter's algorithm:
            # Distant faces are drawn before the closer ones.
            for tmp in sorted(avg_z,key=itemgetter(1),reverse=True):
                face_index = tmp[0]
                f = self.faces[face_index]
                pointlist = [
                             (t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y),
                             (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y),
                             (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y),
                             (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y)
                             ]
                pygame.draw.polygon(self.screen,self.colors[face_index],pointlist)

                
            self.angle += 1
            
            pygame.display.flip()

if __name__ == "__main__":
    Simulation().run()
