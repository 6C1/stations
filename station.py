import pygtk
pygtk.require('2.0')
import gtk

def main():
    base = Base()
    base.main()

class World:
    def __init__(self, num = 5):
        pass

class Base:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("STATIONS")
        self.window.set_position(gtk.WIN_POS_CENTER)

        #behaviors
        self.window.connect("destroy", self.destroy)
        self.window.show()

        #looks
        self.window.set_border_width(42)
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
        self.drawable = self.area.window

        self.set_colors()
        self.gc = self.drawable.new_gc(background=self.bluecolor)
        self.drawable.draw_point(self.gc,42,42)
        self.area.show()

        # show ALL the things
        self.vbox.show()
        self.window.show()

    def destroy(self, widget, data=None):
        gtk.main_quit()
        
    def main(self):
        gtk.main()

    def set_colors(self):
        self.bluecolor = gtk.gdk.color_parse("#0A1E39")
        self.greencolor = gtk.gdk.color_parse("#306E6B")
        self.watercolor = gtk.gdk.color_parse("#8CAA92")
        self.retrocolor = gtk.gdk.color_parse("#F1D653")
        self.mondocolor = gtk.gdk.color_parse("#F84160")

print __name__
if __name__=="__main__": main()
