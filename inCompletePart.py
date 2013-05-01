#'''
#Created on 2012-8-9
#
#@author: Thinkpad
#'''
#def goTotheTarget(self,timePassed):
#        tmp = self.theta
#        x1 = self.pos.x-player1.pos.x
#        y1 = self.pos.y-player1.pos.y
#        ttheta = atan2(y1,x1)
#        ttheta = 
#        if(tmp >0):
#            while(abs(tmp)>90):
#                tmp-=90
#        if(tmp <=0):
#            while(abs(tmp)>90):
#                tmp+=90
#        if(tmp>ttheta):
#            self.rotation_direction = -1
#            self.movement_direction = 1
#        if(tmp<ttheta):
#            self.rotation_direction = 1
#            if(y1>0):
#                self.movement_direction = 1
#       
#        heading_x = cos(ttheta)
#        heading_y = sin(ttheta)
#        heading = Vector2(heading_x, heading_y)
#        heading *= self.movement_direction
#        self.pos+= heading * self.ds*timePassed