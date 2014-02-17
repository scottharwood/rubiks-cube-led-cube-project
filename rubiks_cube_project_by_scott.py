import sys, math, pygame
from operator import itemgetter
class Point3D:
    def __init__(self, x = 0, y = 0,z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def rotateX(self, angle):
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)

    def rotateY(self, angle):
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)
    def rotateZ(self, angle):
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * cosa + self.y * sina
        return Point3D(x, y, self.z)
    def project(self, win_width, win_height, fov, viewer_distance):
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, 1)
class Simulation:
    def __init__(self, win_width = 640, win_height = 480):
        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("rubiks cube by Scott Harwood")

        self.clock = pygame.time.Clock()

        self.vertices = [
            Point3D(-1,-1,-1),
            Point3D(-1,-1,2),
            Point3D(-1,2,-1),
            Point3D(-1,2,2),
            Point3D(2,-1,-1),
            Point3D(2,2,-1),
            Point3D(2,-1,2),
            Point3D(2,2,2)

        ]
        self.faces = [(0,1,2,3),(1,5,6,2),(5,4,7,6),(4,0,3,7),(0,4,5,1),(3,2,6,7)]
        self.colors = [(255,0,255),(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,255,0)]
        
        self.angle = 0
    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(50)
            self.screen.fill((0,32,0))

            t = []

            for v in self.vertices:
                r = v.rotateX(self.angle).rotateY(self.angle).rotateZ(self.angle)
                p = r.project(self.screen.get_width(), self.screen.get_height(), 265, 4)
                t.append(p)

            avg_z = []
            i = 0
            for f in self.faces:
                z = (t[f[0]].z + t[f[1]].z + t[f[2]].z + t[f[3]].z) / 4.0
                avg_z.append([i,z])
                i = i + 1

            for tmp in sorted(avg_z, key=itemgetter(1),reverse=True):
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
        

    
                
            
    
