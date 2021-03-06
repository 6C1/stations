from os import system
from sys import maxint
system('clear')
import time
try:
    import pygtk
except:
    x = raw_input("Stations requires PyGTK to run. Press [ENTER] to cancel, or type \"yes\" to attempt automated installation.")
    if x=="yes" or x=="Yes" or x=="YES":
        print("Installation may require input of your 'sudo' password")
        try:
            system('sudo apt-get install python-gtk2')
            print('...\n...\n...\nInstallation complete!')
            time.sleep(1)
            import pygtk
            print('...')
        except: 
            print("Installation failed.")
            exit()
    else: exit()
pygtk.require('2.0')
import gtk
import random
import math

def main():
    print "\n\n\n\n\nInitialization -", time.strftime("%y%m%d %H%M%S %Z") 
    print "World generation ...",
    world = World(84)
    print "success\nGraphics launch ...",
    base = Base(world)
    print "success\n\n\n"
    gtk.main()
    print "Shutting down...\n\n\n"

class World:
    def __init__(self, num = 5):
        self.nodes = []
        for i in xrange(num):
            self.nodes.append(Node())

class Node:
    def __init__(self, coords=(-1,-1)):
        self.coords = coords
        if ( min(coords) < 0):
            self.coords = (random.randint(0,800),random.randint(0,480))

    def __str__(self):
        return "Node-["+str(self.coords[0])+","+str(self.coords[1])+"]"

    def nearest(self, nodes):
        mind = [self,maxint]
        for node in nodes:
            if node != self and self.dist(node) < mind[1]:
                mind = [node,self.dist(node)]
        return mind[0]

    def dist(self, other): 
        return math.sqrt( (self.coords[0] - other.coords[0])**2 + (self.coords[1] - other.coords[1])**2)


class Base:
    def __init__(self, world):
        self.world = world

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("STATIONS")
        self.window.set_position(gtk.WIN_POS_CENTER)

        #behaviors
        self.window.connect("destroy", self.destroy)
        self.window.show()

        #looks
        self.window.set_border_width(10)
        self.window.set_resizable(False)

        # make vbox
        self.vbox = gtk.VBox(False,0)
        self.window.add(self.vbox)

        # make menu
        self.menu_bar = gtk.MenuBar()
        self.file_menu = gtk.Menu()

        self.quit_item = gtk.MenuItem("Quit\t (ctrl + Q)")
        self.file_menu.append(self.quit_item)
        self.quit_item.connect_object("activate", self.destroy, "file.quit")
        self.quit_item.show()

        self.vbox.add(self.menu_bar)
        self.menu_bar.show()

        self.file_item = gtk.MenuItem("File")
        self.file_item.show()
        self.file_item.set_submenu(self.file_menu)
        self.menu_bar.append(self.file_item)

        # make canvas
        self.area = gtk.DrawingArea()
        self.area.size(800,480)
        self.vbox.add(self.area)
        self.area.show()
        self.area.set_events(gtk.gdk.POINTER_MOTION_MASK | gtk.gdk.POINTER_MOTION_HINT_MASK )
        self.area.connect("expose-event", self.area_expose_cb)
        self.drawable = self.area.window

        # show ALL the things
        self.vbox.show()
        self.window.show()



    def destroy(self, widget, data=None):
        gtk.main_quit()
    def area_expose_cb(self, area, event):
        self.set_colors()
        self.style = self.area.get_style()
        self.gc = self.drawable.new_gc(background=self.bluecolor,foreground=self.retrocolor)
        for i in xrange(len(self.world.nodes)):
            print "--", self.world.nodes[i], self.world.nodes[i].nearest(self.world.nodes)
            self.drawable.draw_line(self.gc, 
                                    self.world.nodes[i].coords[0], 
                                    self.world.nodes[i].coords[1], 
                                    self.world.nodes[i].nearest(self.world.nodes).coords[0],
                                    self.world.nodes[i].nearest(self.world.nodes).coords[1],
                                    )
            self.drawable.draw_arc(self.gc,
                                   False,
                                   self.world.nodes[i].coords[0] - 7,
                                   self.world.nodes[i].coords[1] - 7,
                                   14,14,
                                   0, 360*64
                                   )
        return True

    def set_colors(self):
        self.bluecolor = gtk.gdk.color_parse("#0A1E39")
        self.greencolor = gtk.gdk.color_parse("#306E6B")
        self.watercolor = gtk.gdk.color_parse("#8CAA92")
        self.retrocolor = gtk.gdk.color_parse("#F1D653")
        self.mondocolor = gtk.gdk.color_parse("#F84160")

if __name__=="__main__": main()
