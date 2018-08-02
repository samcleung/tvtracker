#Samantha Leung
#tracker.py
#May 31, 2017
#This program will produce a textfile-based GUI program to track television shows.

#import abstract and tkinter
from abc import abstractmethod, ABCMeta
import Tkinter as tk
from tkFileDialog import askopenfilename
#import randomizing
import random

#initalizing Tkinter
win = tk.Tk()
win.title("TV Tracker")
win.configure(background = "#FFFFFF")

class Login():
    
    #constructor - creates Login layout
    #@param - self (object), master (window)
    #@return - none
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.configure(bg = "#FFFFFF")
        
        tk.Label(self.master, text = "Username", bg = "#FFFFFF").pack()
        #username entry
        self.uent = tk.Entry(self.master)
        self.uent.pack()
        
        tk.Label(self.master, text = "Password", bg = "#FFFFFF").pack()
        #password entry
        self.ent = tk.Entry(self.master)
        self.ent.pack()
        #login button
        go = tk.Button(self.master, text= "Login", command = self.check)
        go.pack()
    
    #check - checks text entry for correct password
    #@param - self
    #@return - none
    def check(self):
        self.name, self.pas, self.tod, self.mvs, self.yrs, self.day, self.tim, self.gen = self.rf()
        #correct password
        if self.ent.get() == self.pas and self.uent.get() == self.name:
            self.mainwin()
        #wrong password
        else:
            lbl = tk.Label(self.master, text = "Invalid username or password.", bg = "#FFFFFF")
            lbl.pack()
    
    #check - opens main window
    #@param - self
    #@return - none
    def mainwin(self):
        #withdraw login window
        self.master.withdraw()
        self.new = tk.Toplevel(self.master)
        self.win = Main(self.new, self.c, self.name, self.tod, self.mvs, self.yrs, self.day, self.tim, self.gen)
    
    #rf - reads text file
    #@param - self
    #@return - name(str), pas(str), tod(str), mvs(list), yrs(list), day(list), tim(list), gen(list)
    def rf(self):
        name = ''
        mvs, yrs, day, tim, gen = [], [], [], [], []
        self.c = askopenfilename(initialdir="D:\\tardisbreaker\\Google Drive\\ICS4U\\Unit 4")
        c = open(self.c).read().split('\n')
        #store name
        name = c[0]
        if "\n" in name:
            name = name[:len(name)-1]
        #store password
        pas = c[1]
        #store today
        tod = c[2]
        #store shows
        for i in range(3, len(c)):
            b = c[i].split(", ")
            mvs.append(b[0])
            yrs.append(b[1])
            day.append(b[2])
            tim.append(b[3])
            gen.append(b[4])
        return name, pas, tod, mvs, yrs, day, tim, gen

class Screen():
    
    __metaclass__ = ABCMeta
    
    #constructor - stores parameters and creates Main, AllShows, ManageToday, WeeklySchedule menu bar
    #@param - self (object), master (window), c (file), name (str), tod (str), mvs (list), yrs (list), day (list), tim (list), gen (list)
    #@return - none
    def __init__(self, master, c, name, tod, mvs, yrs, day, tim, gen):
        self.master = master
        self.c, self.name, self.tod, self.mvs, self.yrs, self.day, self.tim, self.gen = c, name, tod, mvs, yrs, day, tim, gen
        self.master.configure(bg = "#FFFFFF")
        
        #menu bar
        bar = tk.Menu(self.master)
        filemenu = tk.Menu(bar, tearoff = 0)
        editmenu = tk.Menu(bar, tearoff = 0)
        helpmenu = tk.Menu(bar, tearoff = 0)
        
        #file menu
        filemenu.add_command(label = "New", command = self.new)
        filemenu.add_separator()
        filemenu.add_command(label = "Close All Windows", command = self.close)
        #editmenu
        editmenu.add_command(label = "Change Username", command = self.change_user)
        editmenu.add_command(label = "Change Password", command = self.change_pas)
        editmenu.add_separator()
        editmenu.add_command(label = "Add Show", command = self.add_show)
        editmenu.add_command(label = "Remove Show", command = self.remove_show)
        editmenu.add_separator()
        editmenu.add_command(label = "Change Today", command = self.change_day)
        #helpmenu
        helpmenu.add_command(label = "Instructions", command = self.hover)
        
        #pack them to the menu bar
        bar.add_cascade(label = "File", menu = filemenu)
        bar.add_cascade(label = "Edit", menu = editmenu)
        bar.add_cascade(label = "Help", menu = helpmenu)
        
        #set menu on screen
        self.master.config(menu = bar)
        
        #lists for repeated use in some menu functions
        self.days = ['Monday', "Tuesday", 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.newlbl = ["Show (\"Riverdale\")", "Year (\"2017\")", "Day (\"Monday\")", "Time (\"8:00 pm\")", "Genre (\"Drama\")"]
        
    #new - opens new instance of program
    #@param - self
    #@return - none
    def new(self):
        self.nnew = tk.Toplevel(self.master)
        self.win = Login(self.nnew)
    
    #close - closes all windows
    #@param - self
    #@return - none
    def close(self):
        self.master.quit()
    
    #change_user - opens new window for user to change username
    #@param - self
    #@return - none  
    def change_user(self):
        self.unew = tk.Toplevel(self.master)
        self.unew.configure(bg = "#FFFFFF")
        self.unew.title("Change Username")
        tk.Label(self.unew, text = "New Username:", bg = "#FFFFFF").pack()
        self.tex = tk.Entry(self.unew)
        chbut = tk.Button(self.unew, text = "Change Username", command = self.set_user)
        self.tex.pack()
        chbut.pack()
    
    #set_user - sets new username once button is clicked and opens new window with new username
    #@param - self
    #@return - none  
    def set_user(self):
        self.user = self.tex.get()
        c = open(self.c).read().split('\n')
        #change line with username
        c[0] = self.user
        #and write everything back
        ce = open(self.c, 'w')
        #rewrite whole file first with first line
        ce.write(c[0]+'\n')
        for i in range(1, len(c)-1):
            #then add the rest
            ce = open(self.c, 'a')
            ce.write(c[i]+'\n')
        ce.write(c[len(c)-1])
        #close the other windows
        self.unew.withdraw()
        self.master.withdraw()
        #open new Home window
        self.hnew = tk.Toplevel(self.master)
        self.win = Main(self.hnew, self.c, c[0], self.tod, self.mvs, self.yrs, self.day, self.tim, self.gen)
    
    #change_pas - opens new window to change password
    #@param - self
    #@return - none
    def change_pas(self):
        self.pnew = tk.Toplevel(self.master)
        self.pnew.configure(bg = "#FFFFFF")
        self.pnew.title("Change Password")
        tk.Label(self.pnew, text = "New Password:", bg = "#FFFFFF").pack()
        self.tex = tk.Entry(self.pnew)
        chbut = tk.Button(self.pnew, text = "Change Password", command = self.set_pas)
        restart = tk.Label(self.pnew, bg = "#FFFFFF", text = "You must login again once the change has been made.")
        self.tex.pack()
        chbut.pack()
        restart.pack()
    
    #set_pas - sets new password once button is clicked and opens new login page
    #@param - self
    #@return - none     
    def set_pas(self):
        self.pas = self.tex.get()
        c = open(self.c).read().split('\n')
        #change line with password
        c[1] = self.pas
        #and write everything back
        ce = open(self.c, 'w')
        #rewrite whole file starting with first line
        ce.write(c[0]+'\n')
        for i in range(1, len(c)-1):
            #then add the rest
            ce = open(self.c, 'a')
            ce.write(c[i]+'\n')
        ce.write(c[len(c)-1])
        #close other windows
        self.pnew.withdraw()
        self.master.withdraw()
        #open new login window for new password
        self.lnew = tk.Toplevel(self.master)
        self.win = Login(self.lnew)
    
    #add_show - opens new window for user to add new show
    #@param - self
    #@return - none  
    def add_show(self):
        self.anew = tk.Toplevel(self.master)
        self.anew.configure(bg = "#FFFFFF")
        self.anew.title("Add Show")
        self.new_show = []
        for i in range(5):
            tk.Label(self.anew, bg = "#FFFFFF", text = self.newlbl[i]).pack()
            self.new_show.append(tk.Entry(self.anew))
            self.new_show[i].pack()
        chbut = tk.Button(self.anew, text = "Add Show", command = self.set_show)
        chbut.pack()
    
    #set_show - adds new show to lists and file and opens new window with changes
    #@param - self
    #@return - none  
    def set_show(self):
        
        #test show

        #test for empty string
        if self.new_show[0].get().strip() == '':
            tk.Label(self.anew, bg = "#FFFFFF", text = "Invalid Show Name.").pack()
            return
        
        #test year
        
        #test for integer value
        try:
            int(self.new_show[1].get())
        except ValueError:
            tk.Label(self.anew, bg = "#FFFFFF", text = "Invalid Year.").pack()
            return
        #test for natural value
        if int(self.new_show[1].get()) < 0:
            tk.Label(self.anew, bg = "#FFFFFF", text = "Invalid Year.").pack()
            return
        
        #test day
        for i in range(len(self.days)):
            if self.new_show[2].get().capitalize() == self.days[i]:
                break
            elif i == len(self.days)-1:
                tk.Label(self.anew, bg = "#FFFFFF", text = "Invalid Day.").pack()
                return
        
        #test timeslot
        
        #test am or pm
        if self.new_show[3].get()[len(self.new_show[3].get())-2:] != 'am' and self.new_show[3].get()[len(self.new_show[3].get())-2:] != 'pm':
            tk.Label(self.anew, bg = "#FFFFFF", text = "Invalid Timeslot.").pack()
            return
        #check for space in timeslot
        if self.new_show[3].get()[len(self.new_show[3].get())-3] != ' ':
            tk.Label(self.anew, bg = "#FFFFFF", text = "Add a space before am/pm in your timeslot.").pack()
            return
        #check for legitimate time according to 12-hour clock
        timenum = self.new_show[3].get()[:len(self.new_show[3].get())-3].split(':')
        if int(timenum[0]) < 1 or int(timenum[0]) > 12 or int(timenum[1]) < 0 or int(timenum[1]) > 59:
            tk.Label(self.anew, bg = "#FFFFFF", text = "Invalid Timeslot.").pack()
            return
        
        c = open(self.c).read().split('\n')
        # now add the show
        c.append(self.new_show[0].get() + ', ' + self.new_show[1].get() + ', ' + self.new_show[2].get().capitalize() + ', ' + self.new_show[3].get() + ', ' + self.new_show[4].get().capitalize())
        #add the new show to all the lists
        self.mvs.append(self.new_show[0].get())
        self.yrs.append(self.new_show[1].get())
        self.day.append(self.new_show[2].get().capitalize())
        self.tim.append(self.new_show[3].get())
        self.gen.append(self.new_show[4].get().capitalize())
        ce = open(self.c, 'w')
        #rewrite whole file with first line
        ce.write(c[0]+'\n')
        for i in range(1, len(c)-1):
            #then add the rest
            ce = open(self.c, 'a')
            ce.write(c[i]+'\n')
        ce.write(c[len(c)-1])
        #close other windows
        self.anew.withdraw()
        self.master.withdraw()
        #open new Home window
        self.hnew = tk.Toplevel(self.master)
        self.win = Main(self.hnew, self.c, self.name, self.tod, self.mvs, self.yrs, self.day, self.tim, self.gen)
    
    #remove_show - opens new window to remove a show
    #@param - self
    #@return - none  
    def remove_show(self):
        self.rnew = tk.Toplevel(self.master)
        self.rnew.configure(bg = "#FFFFFF")
        self.rnew.title("Remove Show")
        self.new_show = []
        #loop to pack diifferent text entries
        for i in range(5):
            tk.Label(self.rnew, bg = "#FFFFFF", text = self.newlbl[i]).pack()
            self.new_show.append(tk.Entry(self.rnew))
            self.new_show[i].pack()
        chbut = tk.Button(self.rnew, text = "Remove Show", command = self.forget_show)
        chbut.pack()
        tk.Label(self.rnew, text = "Remember to add space before am/pm in your timeslot.").pack()
     
    #forget_show -removes show if it exists
    #@param - self
    #@return - none  
    def forget_show(self):
        c = open(self.c).read().split('\n')
        # now remove the show
        for i in range(3, len(c)):
            b = c[i].split(", ")
            #check if all show components exist
            for j in range(5):
                if self.new_show[j].get().capitalize() != b[j].capitalize():
                    break
            else:
                c.pop(i)
                #remove show from all lists
                self.mvs.pop(i-3)
                self.yrs.pop(i-3)
                self.day.pop(i-3)
                self.tim.pop(i-3)
                self.gen.pop(i-3)
                break
            if i == len(c)-1:
                #the show is not in the file!
                tk.Label(self.rnew, bg = "#FFFFFF", text = "No such show exists.").pack()
                return
            continue
        ce = open(self.c, 'w')
        #rewrite whole file with first line
        ce.write(c[0]+'\n')
        for i in range(1, len(c)-1):
            #then add the rest
            ce = open(self.c, 'a')
            ce.write(c[i]+'\n')
        ce.write(c[len(c)-1])
        #close other windows
        self.rnew.withdraw()
        self.master.withdraw()
        #open new Home window
        self.hnew = tk.Toplevel(self.master)
        self.win = Main(self.hnew, self.c, self.name, self.tod, self.mvs, self.yrs, self.day, self.tim, self.gen)
    
    #change_day - opens new window for user to change today's day
    #@param - self
    #@return - none  
    def change_day(self):
        #create new window
        self.dnew = tk.Toplevel(self.master)
        self.dnew.configure(bg = "#FFFFFF")
        self.dnew.title("Change Today")
        tk.Label(self.dnew, text = "Day (\"Tuesday\")", bg = "#FFFFFF").pack()
        self.tex = tk.Entry(self.dnew)
        chbut = tk.Button(self.dnew, text = "Change Today", command = self.set_day)
        self.tex.pack()
        chbut.pack()
        
    #set_day - sets new day and opens new window with the new day
    #@param - self
    #@return - none  
    def set_day(self):
        self.week = self.tex.get().capitalize()
        #check for valid day
        if self.week not in self.days:
            tk.Label(self.dnew, bg = "#FFFFFF", text = "Please enter in a day of the week.").pack()
            return
        c = open(self.c).read().split('\n')
        #change line with day
        c[2] = self.week
        ce = open(self.c, 'w')
        #rewrite whole file with first line
        ce.write(c[0]+'\n')
        for i in range(1, len(c)-1):
            #add the rest
            ce = open(self.c, 'a')
            ce.write(c[i]+'\n')
        ce.write(c[len(c)-1])
        #close other windows
        self.dnew.withdraw()
        self.master.withdraw()
        #open new Home window
        self.hnew = tk.Toplevel(self.master)
        self.win = Main(self.hnew, self.c, self.name, c[2], self.mvs, self.yrs, self.day, self.tim, self.gen)
    
    def hover(self):
        #user guide instructions on terminal
        print "HOW TO USE"
        print
        print "Your Data"
        print "There is no easy way to initiate the program except to write out all of your data in the following format:"
        print "Username"
        print "Password"
        print "Today (Thursday)"
        print "Name of Show (Riverdale), Year (2017), Day of Week (Thursday), Time (8:00 pm), Genre (SciFi)"
        print
        print "Home"
        print "The Main Home window acts as a navigation for all the features in the program. When using any option from the menu bar, it is best to use it solely from the Home window with nothing else open if you want to close all the old windows before your changes. You have three main options in the Home: All Shows, Manage Today, and Weekly Schedule. Click any of these buttons to access their unique features personalized to your data."
        print
        print "All Shows" 
        print "The All Shows button lists your shows the way you did them in your text file, by default. The filter sidebar on the left allows the option of filtering by the five built-in genres: Action, Drama, Fantasy, Comedy, and SciFi. The program allows additional genres into the list but you cannot use their genres as filters. The sort sidebar on the right has five options as well: Show, Year, Day, Time, and Genre. Click any one of these and then click Sort underneath the listbox. All filters will erase when you sort, but you can filter after sorting."
        print
        print "Manage Today"
        print "This window will automatically take into today's day of the week from your text file (which you can change in Edit > Change Today) and allow you to make your own custom schedule for the day based on the shows you watch. Additionally, if you're completely free and don't want to go to the trouble of picking, let chance decide with the I'm Feeling Lucky button, placed right below the Create Today's Schedule button."
        print
        print "Weekly Schedule"
        print "The Weekly Schedule window is quite self explanatory in that it gives you an overview of the week's schedule regarding your TV show watching. To allow for multiple shows in the same day and timeslot, there could be multiple lines of the same timeslot, depending on your shows. There's nothing special to press here."
        print
        print "Menu"
        print "The full list of options:"
        print "File - Open, Close All Windows"
        print "The Open option opens up a new login page, allowing another user to access their data while keeping yours open. The Close All Windows option closes all the windows of the program."
        print "Edit - Change Username, Change Password, Add Show, Remove Show, Change Today"
        print "The Change Username option opens a new window where you can enter in a new username and the program automatically opens a new Home window with your new username. The Change Password option opens a new window where you can enter in a new password and the program automatically opens a new login window to confirm your new password. The Add Show Option opens a window where you can enter in a new show with a name, year, day, time, and genre. The year must be a positive number and the timeslot must have the 12-hour clock format (ie. 9:00 pm). All existing genres are supported by this program but only Action, Drama, SciFi, Fantasy, and Comedy are in the filter section for the All Shows window. The Remove Show option has the same format as Add Show, and remember to enter in the show information exactly as it is entered into the system. The Change Today option lets you manually change the day of the week so Manage Today works properly."
        #direct user to terminal label
        self.inew = tk.Toplevel(self.master)
        self.inew.configure(bg = "#FFFFFF")
        self.inew.title("Instructions")
        tk.Label(self.inew, text = "Go to terminal to access help instructions.").pack()
        
    @abstractmethod
    def display(self):
        pass
    
class Main(Screen):
    
    #constructor - create Main/Home full layout
    #@param - self (Screen), master (window), c (file), name (str), tod (str), mvs (list), yrs (list), day (list), tim (list), gen (list)
    #@return - none
    def __init__(self, master, c, name, tod, mvs, yrs, day, tim, gen):
        Screen.__init__(self, master, c, name, tod, mvs, yrs, day, tim, gen)
        self.master.title("Home")
        
        label = tk.Label(self.master, text = "TV TRACKER", bg = "#FFFFFF", font = ("A Box For", 45))
        label.pack()
        
        nlabel = tk.Label(self.master, text = "Welcome, " + self.name + ".", bg = "#FFFFFF", font = ("Signika", 12))
        nlabel.pack()
        
        dlabel = tk.Label(self.master, text = "Today is " + self.tod + ".", bg = "#FFFFFF", font = ("Signika", 12))
        dlabel.pack()
        
        #all shows window
        allbut = tk.Button(self.master, bg = "#327AFF", fg = "white", text = "All Shows", font = ("Mayton", 20), command = self.allwin)
        allbut.pack(fill = tk.X)
        #manage today window
        managebut = tk.Button(self.master, bg = "#00FF55", fg = "white", text = "Manage Today", font = ("Mayton", 20), command = self.managewin)
        managebut.pack(fill = tk.X)
        #weekly schedule window
        weekbut = tk.Button(self.master, bg = "#FF1988", fg = "white", text = "Weekly Schedule", font = ("Mayton", 20), command = self.weekwin)
        weekbut.pack(fill = tk.X)
    
    #display - nothing to display for home window
    #@param - self
    #@return - none
    def display(self):
        pass
    
    #allwin - opens all shows window
    #@param - self
    #@return - none
    def allwin(self):
        self.new = tk.Toplevel(self.master)
        self.win = AllShows(self.new, self.c, self.name, self.tod, self.mvs, self.yrs, self.day, self.tim, self.gen)
    
    #managewin - opens manage today window
    #@param - self
    #@return - none
    def managewin(self):
        self.new = tk.Toplevel(self.master)
        self.win = ManageToday(self.new, self.c, self.name, self.tod, self.mvs, self.yrs, self.day, self.tim, self.gen)
     
    #weekwin - opens weekly shedule window
    #@param - self
    #@return - none   
    def weekwin(self):
        self.new = tk.Toplevel(self.master)
        self.win = WeeklySched(self.new, self.c, self.name, self.tod, self.mvs, self.yrs, self.day, self.tim, self.gen)

class AllShows(Screen):
    
    #constructor - create AllShows basic layout
    #@param - self, master (window), c (file), name (str), tod (str), mvs (list), yrs (list), day (list), tim (list), gen (list)
    #@return - none
    def __init__(self, master, c, name, tod, mvs, yrs, day, tim, gen):
        Screen.__init__(self, master, c, name, tod, mvs, yrs, day, tim, gen)
        self.master.title("All Shows")
        label = tk.Label(self.master, text = "ALL SHOWS", bg = "#FFFFFF", font = ("A Box For", 45))
        label.pack()
        
        #sort listbox
        sor = tk.Frame(self.master, width=150, bg='white', height=500, relief='sunken', borderwidth=2)
        sor.pack(expand=False, fill='both', side='right', anchor='nw')
        stitle = tk.Label(sor, bg = "#FFFFFF", text = "  Sort  ", font = ("Signika", 18))
        stitle.pack()
        self.types = ["Show", "Year", "Day", "Time", "Genre"]
        self.sbox = tk.Listbox(sor, font = ("Signika", 10), width = 8, height = 5)
        self.sbox.pack()
        #insert listbox elements
        for i in range(len(self.types)):
            self.sbox.insert(i, self.types[i])
        sbut = tk.Button(sor, bg = "white", text = "Sort", font = ("Signika", 12), command = self.sort)
        sbut.pack()
        
        #filter checkbuttons
        fil = tk.Frame(self.master, width=150, bg='white', height=500, relief='sunken', borderwidth=2)
        fil.pack(expand=False, fill='both', side='left', anchor='nw')
        ftitle = tk.Label(fil, bg = "#FFFFFF", text = "Filter", font = ("Signika", 18))
        ftitle.pack()
        genre = tk.Label(fil, bg = "white", text = "GENRE", font = ("Signika", 12))
        genre.pack()
        
        #checkbutton integer variables
        self.avar = tk.IntVar()
        self.dvar = tk.IntVar()
        self.svar = tk.IntVar()
        self.fvar = tk.IntVar()
        self.cvar = tk.IntVar()
        
        #checkbuttons
        act = tk.Checkbutton(fil, bg = 'white', text = "Action", variable = self.avar, font = ("Signika", 10), command = self.action)
        dra = tk.Checkbutton(fil, bg = 'white', text = "Drama", variable = self.dvar, font = ("Signika", 10), command = self.drama)
        sci = tk.Checkbutton(fil, bg = 'white', text = "Sci-Fi", variable = self.svar, font = ("Signika", 10), command = self.scifi)
        fan = tk.Checkbutton(fil, bg = 'white', text = "Fantasy", variable = self.fvar, font = ("Signika", 10), command = self.fantasy)
        com = tk.Checkbutton(fil, bg = 'white', text = "Comedy", variable = self.cvar, font = ("Signika", 10), command = self.comedy)
        act.pack()
        dra.pack()
        sci.pack()
        fan.pack()
        com.pack()
        
        #main content area
        self.mainarea = tk.Frame(self.master, bg = "#5998FF", width = 500, height = 500)
        self.mainarea.pack(expand = True, fill = 'both', side = 'right')
        self.display()
    
    #action - filters action shows
    #@param - self
    #@return - none    
    def action(self):
        #uncheck all other filters
        self.dvar.set(0)
        self.svar.set(0)
        self.fvar.set(0)
        self.cvar.set(0)
        self.display()
        if self.avar.get() == 1:
            for i in range(len(self.l[0])):
                #filter the genre
                if self.l[4][i] != 'Action':
                    for j in range(len(self.l)):
                        self.l2[j][i].config(text = " "*32)
    
    #drama - filters drama shows
    #@param - self
    #@return - none     
    def drama(self):
        #uncheck all other filters
        self.avar.set(0)
        self.svar.set(0)
        self.fvar.set(0)
        self.cvar.set(0)
        self.display()
        if self.dvar.get() == 1:
            for i in range(len(self.l[0])):
                #filter the genre
                if self.l[4][i] != 'Drama':
                    for j in range(len(self.l)):
                        self.l2[j][i].config(text = " "*32)
    
    #scifi - filters scifi shows
    #@param - self
    #@return - none         
    def scifi(self):
        #uncheck all other filters
        self.dvar.set(0)
        self.avar.set(0)
        self.fvar.set(0)
        self.cvar.set(0)
        self.display()
        if self.svar.get() == 1:
            for i in range(len(self.l[0])):
                #filter the genre
                if self.l[4][i] != 'SciFi':
                    for j in range(len(self.l)):
                        self.l2[j][i].config(text = " "*32)
    
    #fantasy - filters fantasy shows
    #@param - self
    #@return - none  
    def fantasy(self):
        #uncheck all other filters
        self.dvar.set(0)
        self.svar.set(0)
        self.avar.set(0)
        self.cvar.set(0)
        self.display()
        if self.fvar.get() == 1:
            for i in range(len(self.l[0])):
                #filter the genre
                if self.l[4][i] != 'Fantasy':
                    for j in range(len(self.l)):
                        self.l2[j][i].config(text = " "*32)
    
    #comedy - filters comedy shows
    #@param - self
    #@return - none 
    def comedy(self):
        #uncheck all other filters
        self.dvar.set(0)
        self.svar.set(0)
        self.fvar.set(0)
        self.avar.set(0)
        self.display()
        if self.cvar.get() == 1:
            for i in range(len(self.l[0])):
                #filter the genre
                if self.l[4][i] != 'Comedy':
                    for j in range(len(self.l)):
                        self.l2[j][i].config(text = " "*32)
    
    #sort - sorts tvv shows by chosen listbox selection
    #@param - self
    #@return - none 
    def sort(self):
        #uncheck all filters
        self.dvar.set(0)
        self.svar.set(0)
        self.fvar.set(0)
        self.cvar.set(0)
        self.avar.set(0)
        #clear old labels
        for i in range(len(self.l[0])):
            for j in range(len(self.l)):
                self.l2[j][i].config(text = " "*32)
        by = self.sbox.curselection()
        #show alphabetical sort
        if 0 in by:
            self.mvs, self.yrs, self.day, self.tim, self.gen = zip(*sorted(zip(self.mvs, self.yrs, self.day, self.tim, self.gen)))
        #year ascending order sort
        elif 1 in by:
            self.yrs, self.mvs, self.day, self.tim, self.gen = zip(*sorted(zip(self.yrs, self.mvs, self.day, self.tim, self.gen)))
        #days of week sort
        elif 2 in by:
            d = []
            for i in range(len(self.day)):
                if self.day[i] == "Monday":
                    d.append(0)
                elif self.day[i] == "Tuesday":
                    d.append(1)
                elif self.day[i] == "Wednesday":
                    d.append(2)
                elif self.day[i] == "Thursday":
                    d.append(3)
                elif self.day[i] == "Friday":
                    d.append(4)
                elif self.day[i] == "Saturday":
                    d.append(5)
                elif self.day[i] == "Sunday":
                    d.append(6)
            d, self.day, self.yrs, self.mvs, self.tim, self.gen = zip(*sorted(zip(d, self.day, self.yrs, self.mvs, self.tim, self.gen)))
        #timeslot sort
        elif 3 in by:
            d = []
            for i in range(len(self.tim)):
                j = self.tim[i].index(":")
                de = self.tim[i][:j] + self.tim[i][j+1:]
                apm = de[len(de)-2:]
                de = int(de[:len(de)-3])
                if apm == 'pm':
                    if de < 1200:
                        de += 1200
                elif apm == 'am':
                    if de >= 1200:
                        de -= 1200
                d.append(de)
            d, self.tim, self.yrs, self.day, self.mvs, self.gen = zip(*sorted(zip(d, self.tim, self.yrs, self.day, self.mvs, self.gen)))
        #genre alphabetical sort
        elif 4 in by:
            self.gen, self.yrs, self.day, self.tim, self.mvs = zip(*sorted(zip(self.gen, self.yrs, self.day, self.tim, self.mvs)))
        self.display()
    
    #display - displays the tv shows and their corresponding details
    #@param - self
    #@return - none   
    def display(self):
        self.l = [self.mvs, self.yrs, self.day, self.tim, self.gen]
        self.l2 = [[], [], [], [], []]
        for i in range(len(self.l)):
            #header names
            header = tk.Label(self.mainarea, bg = "#5998FF", fg = "white", font = ("Signika", 14, 'bold'), text = self.types[i])
            header.grid(row = 0, column = i)
            for j in range(len(self.mvs)):
                #add elements
                m = tk.Label(self.mainarea, bg = "#5998FF", fg = "white", font = ("Signika", 12),text = self.l[i][j])
                self.l2[i].append(m)
                self.l2[i][j].grid(row = j+1, column = i)
    
class ManageToday(Screen):
    
    #constructor - creates ManageToday basic layout
    #@param - self, master (window), c (file), name (str), tod (str), mvs (list), yrs (list), day (list), tim (list), gen (list)
    #@return - none
    def __init__(self, master, c, name, tod, mvs, yrs, day, tim, gen):
        Screen.__init__(self, master, c, name, tod, mvs, yrs, day, tim, gen)
        self.master.title("Manage Today")
        label = tk.Label(self.master, text = "MANAGE TODAY", bg = "#FFFFFF", font = ("A Box For", 45))
        label.pack()
        instr = tk.Label(self.master, fg = "black", bg = "white", text = "Click a show to cancel/approve.", font = ("Signika", 18))
        instr.pack()
        bla = tk.Label(self.master, fg = "black", bg = "white", text = "Red = Cancelled\t\tGreen = Approved", font = ("Signika", 10))
        bla.pack()
        
        #main content area
        self.mainarea = tk.Frame(self.master, bg = "#9BF28C", width = 500, height = 500)
        self.mainarea.pack(expand = True, fill = 'both', side = 'right')
        self.display()
    
    #display - displays the tv shows and their corresponding details
    #@param - self
    #@return - none     
    def display(self):
        self.l = [self.tim, self.mvs, self.gen]
        #reference list for values of time, shows, and genre
        self.l2 = [[], [], []]
        #list of actual tkinter objects
        self.l3 = [[], [], []]
        d = []
        #filter only for today's shows
        for i in range(len(self.day)):
            if self.day[i] == self.tod or self.day[i] == self.tod.lower():
                self.l2[0].append(self.l[0][i])
                self.l2[1].append(self.l[1][i])
                self.l2[2].append(self.l[2][i])
        #sort by timeslot
        for i in range(len(self.l2[0])):
            j = self.l2[0][i].index(":")
            de = self.l2[0][i][:j] + self.l2[0][i][j+1:]
            apm = de[len(de)-2:]
            de = int(de[:len(de)-3])
            if apm == 'pm':
                    if de < 1200:
                        de += 1200
            elif apm == 'am':
                if de >= 1200:
                    de -= 1200
            d.append(de)
        d, self.l2[0], self.l2[1], self.l2[2] = zip(*sorted(zip(d, self.l2[0], self.l2[1], self.l2[2])))
        #display grid format
        for i in range(len(self.l2)):
            for j in range(len(self.l2[0])):
                if i == 1:
                    #show button
                    m = tk.Button(self.mainarea, bg = "#00ED72", fg = "#FFFFFF", font = ("Signika", 12), relief = "sunken", width = 20, text = self.l2[i][j], command = lambda j=j: self.check(j))
                else:
                    #corresponding timeslot and genre
                    m = tk.Label(self.mainarea, bg = "#9BF28C", fg = "#FFFFFF", font = ("Signika", 12), relief = "sunken", width = 20, text = self.l2[i][j])
                #add objects to list
                self.l3[i].append(m)
                #grid objects
                self.l3[i][j].grid(row = j, column = i)
        #button to go to function to create file output
        tk.Button(self.mainarea, bg = "#FFFFFF", fg = "black", text = "Create Today's Schedule", relief = "ridge", font = ("Signika", 14), command = lambda j=j: self.appcan(j)).grid(row = j+2, column = 1)
        tk.Button(self.mainarea, bg = "black", fg = "#FFFFFF", text = "I'm Feeling Lucky", relief = "ridge", font = ("Signika", 12), command = lambda j=j: self.rando(j)).grid(row = j+3, column = 1)
    
    #check - checks approved and cancelled shows
    #@param - self
    #@return - none 
    def check(self, j):
        #if green, make red
        if self.l3[1][j].cget('bg') == "#00ED72":
            self.l3[1][j].configure(bg = "#D80000")
        #otherwise, make red
        else:
            self.l3[1][j].configure(bg = "#00ED72")
    
    #appcan - writes new schedule for today into text file
    #@param - self
    #@return - none 
    def appcan(self, j):
        #create text file
        tsched = open(self.name + '_' + self.tod + '_Schedule.txt', 'w')
        #header of text file
        tsched.write(self.name + " - TV Schedule (" + self.tod + ") \n\n")
        for i in range(len(self.l3[0])):
            #check for green = approved shows
            if self.l3[1][i].cget('bg') == "#00ED72":
                #write time and show
                tsched.write(self.l2[0][i] + ' - ' + self.l2[1][i] + '\n')
        tk.Label(self.mainarea, text = "Find text file named \"{}_{}_Schedule\" in the folder with your data file.".format(self.name, self.tod), bg = "#00ED72").grid(row = j+4, column = 1)
    
    #rando - writes new rnadom schedule for today into tet file
    #@param - self
    #@return - none
    def rando(self, j):
        #create text file
        rsched = open(self.name + '_' + self.tod + '_Random.txt', 'w')
        #header of text file
        rsched.write(self.name + " - TV Schedule (" + self.tod + ") \n\n")
        for i in range(len(self.l2[0])):
            #randomize each show
            v = random.randint(0, 1)
            if v == 0:
                rsched.write(self.l2[0][i] + ' - ' + self.l2[1][i] + '\n')
        tk.Label(self.mainarea, text = "Find text file named \"{}_{}_Random\" in the folder with your data file.".format(self.name, self.tod), bg = "#00ED72").grid(row = j+4, column = 1)

class WeeklySched(Screen):
    
    #constructor - create WeeklySchedule basic layout
    #@param - self, master (window), c (file), name (str), tod (str), mvs (list), yrs (list), day (list), tim (list), gen (list)
    #@return - none
    def __init__(self, master, c, name, tod, mvs, yrs, day, tim, gen):
        Screen.__init__(self, master, c, name, tod, mvs, yrs, day, tim, gen)
        self.master.title("Weekly Schedule")
        label = tk.Label(self.master, text = "Weekly Schedule", bg = "#FFFFFF", font = ("A Box For", 45))
        label.pack()
        #main area layout
        self.mainarea = tk.Frame(self.master, bg = "#FFA0D2", width = 500, height = 500)
        self.mainarea.pack(expand = True, fill = 'both', side = 'right')
        self.display()
    
    #display - displays the tv shows and their corresponding details
    #@param - self
    #@return - none    
    def display(self):
        self.l = [self.mvs, self.day, self.tim]
        self.l2 = [[], [], [], [], []]
        self.days = ['Monday', "Tuesday", 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        d = []
        #sort by timeslot
        for i in range(len(self.tim)):
            j = self.tim[i].index(":")
            de = self.tim[i][:j] + self.tim[i][j+1:]
            apm = de[len(de)-2:]
            de = int(de[:len(de)-3])
            #convert to military time
            if apm == 'pm':
                if de < 1200:
                    de += 1200
            elif apm == 'am':
                if de >= 1200:
                    de -= 1200
            d.append(de)
        #sort all lists corresponding to time
        d, self.tim, self.mvs, self.day = zip(*sorted(zip(d, self.tim, self.mvs, self.day)))
        #display in grid
        for i in range(1, len(self.days)+1):
            #every day header
            header = tk.Label(self.mainarea, bg = "#FFA0D2", fg = "white", width = 16, relief = "groove", font = ("Signika", 14, 'bold'), text = self.days[i-1])
            header.grid(row = 0, column = i)
            for j in range(1, len(self.tim)+1):
                #timeslot
                time = tk.Label(self.mainarea, bg = "#FFA0D2", fg = "white", width = 7, relief = "groove", font = ("Signika", 14, 'bold'), text = self.tim[j-1])
                time.grid(row = j, column = 0)
                #set space for show
                show = tk.Label(self.mainarea, bg = "#FFA0D2", fg = "white", width = 16, relief = "groove", font = ("Signika", 14, 'bold'))
                show.grid(row = j, column = i)
                #check for corresponding day and show and configure the label
                if self.day[j-1] == self.days[i-1]:
                    show.configure(text = self.mvs[j-1])

#start program
start = Login(win)
win.mainloop()
