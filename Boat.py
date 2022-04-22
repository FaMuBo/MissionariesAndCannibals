
class boat:
    #boat sizes
    width = 40
    height = 100
    def __init__(self, x, y, position,image1,image2,gameDisplay):
        self.x = x
        self.y = y
        self.position = position
        self.image1 = image1
        self.image2 = image2
        self.gameDisplay = gameDisplay

    def highlight(self,a,b,c):
        if self.position==2 or self.position==3:
            if c=='M':
                self.gameDisplay.blit(self.image1,(a+20,b-50))
            elif c == 'C':
                self.gameDisplay.blit(self.image2,(a+20,b-50))

        elif self.position==4 or self.position==5:
            if c=='M':
                self.gameDisplay.blit(self.image1, (a+180,b-50))
            elif c == 'C':
                self.gameDisplay.blit(self.image2, (a + 180, b - 50))
