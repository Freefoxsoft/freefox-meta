#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import webbrowser
import tkinter as tk
import exifread
import re
import PyPDF2
from tkinter import filedialog

import osint_graphique_support


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("1028x776+400+138")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(False, False)
        top.title("Freefox méta")
        top.iconbitmap("image/fox.ico")
        top.configure(background="#3F3A46")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        def load_file():
            self.top.filename = filedialog.askopenfilename(title="select a File",
                                                           filetypes=(("jpg files", "*jpg"), ("all files", "*.*")))

        def image():
            with open(self.top.filename, "rb") as file:
                exif = exifread.process_file(file)
                for tag in exif.keys():
                    print = (tag + " " + str(exif[tag]))
                    self.scanne.insert(0, print)

        def _convert_to_degress(value):
            """
            Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
            :param value:
            :type value: exifread.utils.Ratio
            :rtype: float
            """
            d = float(value.values[0].num) / float(value.values[0].den)
            m = float(value.values[1].num) / float(value.values[1].den)
            s = float(value.values[2].num) / float(value.values[2].den)
            return d + (m / 60.0) + (s / 3600.0)

        def gps():
            with open(self.top.filename, "rb") as file:
                exif = exifread.process_file(file)
            if not exif:
                print("Aucune métadonnée EXIF.")
            else:
                latitude = exif.get("GPS GPSLatitude")
                latitude_ref = exif.get("GPS GPSLatitudeRef")
                longitude = exif.get("GPS GPSLongitude")
                longitude_ref = exif.get("GPS GPSLongitudeRef")
                if latitude and longitude and latitude_ref and longitude_ref:
                    lat = _convert_to_degress(latitude)
                    long = _convert_to_degress(longitude)
                    if str(latitude_ref) != "N":
                        lat = 0 - lat
                    if str(longitude_ref) != "E":
                        long = 0 - long
                        rowze = ("LAT : " + str(lat))
                        rowze1 = ("LONG : " + str(long))
                        vrowze = ("http://maps.google.com/maps?q=loc:%s,%s" % (str(lat), str(long)))
                        self.coordonné_gps.insert(0, rowze, rowze1)
                        webbrowser.open_new(vrowze)

        def get_strings():
            with open(self.top.filename, "rb") as file:
                content = file.read()
            _re = re.compile("[\S\s]{4,}")
            for match in _re.finditer(content.decode("utf8", "backslashreplace")):
                print(match.group())

        def pdf_meta():
            pdf_file = PyPDF2.PdfFileReader(open(self.top.filename, "rb"))
            doc_info = pdf_file.getDocumentInfo()
            for info in doc_info:
                print = ("[+] " + info + " " + doc_info[info])
                self.Listbox2.insert(0, print)

        def discord():
            webbrowser.open_new("https://discord.gg/eFMGAnxUbE")

        def clear():
            self.scanne.delete(0, tk.END)
            self.coordonné_gps.delete(0, tk.END)

        self.top = top

        self.scanner = tk.Button(self.top)
        self.scanner.place(relx=0.0, rely=0.244, height=44, width=147)
        self.scanner.configure(activebackground="#3F3A46")
        self.scanner.configure(activeforeground="white")
        self.scanner.configure(activeforeground="#ffffff")
        self.scanner.configure(background="#3F3A46")
        self.scanner.configure(compound='left')
        self.scanner.configure(disabledforeground="#a3a3a3")
        self.scanner.configure(foreground="#ffffff")
        self.scanner.configure(highlightbackground="#d9d9d9")
        self.scanner.configure(highlightcolor="black")
        photo_location = "image/scan.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.scanner.configure(image=_img0)
        self.scanner.configure(pady="0")
        self.scanner.configure(text='''Scanner jpg''', command=image)
        self.tooltip_font = "TkDefaultFont"
        self.scanner_tooltip = \
            ToolTip(self.scanner, self.tooltip_font, '''si rien ne s'affiche s'est qu'il n'y a pas de méta''')

        self.scan = tk.Button(self.top)
        self.scan.place(relx=0.467, rely=0.308, height=44, width=157)

        self.scan.configure(activebackground="#3F3A46")
        self.scan.configure(activeforeground="white")
        self.scan.configure(activeforeground="#ffffff")
        self.scan.configure(background="#3F3A46")
        self.scan.configure(compound='left')
        self.scan.configure(disabledforeground="#a3a3a3")
        self.scan.configure(foreground="#ffffff")
        self.scan.configure(highlightbackground="#d9d9d9")
        self.scan.configure(highlightcolor="black")
        self.scan.configure(pady="0")
        self.scan.configure(text='''scan approfondie''', command=get_strings)
        self.tooltip_font = "TkDefaultFont"
        self.scan_tooltip = \
            ToolTip(self.scan, self.tooltip_font, '''affichage dans le cmd''')

        self.scan_approfondie = tk.Button(self.top)
        self.scan_approfondie.place(relx=0.146, rely=0.244, height=44, width=157)

        self.scan_approfondie.configure(activebackground="#3F3A46")
        self.scan_approfondie.configure(activeforeground="white")
        self.scan_approfondie.configure(activeforeground="#ffffff")
        self.scan_approfondie.configure(background="#3F3A46")
        self.scan_approfondie.configure(compound='left')
        self.scan_approfondie.configure(disabledforeground="#a3a3a3")
        self.scan_approfondie.configure(foreground="#ffffff")
        self.scan_approfondie.configure(highlightbackground="#d9d9d9")
        self.scan_approfondie.configure(highlightcolor="black")
        self.scan_approfondie.configure(pady="0")
        self.scan_approfondie.configure(text='''Scanner PDF''', command=pdf_meta)

        self.scanne = tk.Listbox(self.top)
        self.scanne.place(relx=0.0, rely=0.307, relheight=0.245, relwidth=0.466)
        self.scanne.configure(background="#584e57")
        self.scanne.configure(disabledforeground="#a3a3a3")
        self.scanne.configure(font="TkFixedFont")
        self.scanne.configure(foreground="#ffffff")
        self.scanne.configure(highlightbackground="#d9d9d9")
        self.scanne.configure(highlightcolor="black")
        self.scanne.configure(highlightthickness="0")
        self.scanne.configure(relief="flat")
        self.scanne.configure(selectbackground="blue")
        self.scanne.configure(selectforeground="white")

        self.Listbox2 = tk.Listbox(self.top)
        self.Listbox2.place(relx=0.0, rely=0.573, relheight=0.433
                            , relwidth=1.003)
        self.Listbox2.configure(background="#584e57")
        self.Listbox2.configure(disabledforeground="#a3a3a3")
        self.Listbox2.configure(font="TkFixedFont")
        self.Listbox2.configure(foreground="#ffffff")
        self.Listbox2.configure(highlightbackground="#d9d9d9")
        self.Listbox2.configure(highlightcolor="black")
        self.Listbox2.configure(highlightthickness="0")
        self.Listbox2.configure(relief="flat")
        self.Listbox2.configure(selectbackground="blue")
        self.Listbox2.configure(selectforeground="white")

        self.nettoyage = tk.Button(self.top)
        self.nettoyage.place(relx=0.301, rely=0.244, height=44, width=167)
        self.nettoyage.configure(activebackground="#3F3A46")
        self.nettoyage.configure(activeforeground="white")
        self.nettoyage.configure(activeforeground="#ffffff")
        self.nettoyage.configure(background="#3F3A46")
        self.nettoyage.configure(compound='left')
        self.nettoyage.configure(disabledforeground="#a3a3a3")
        self.nettoyage.configure(foreground="#ffffff")
        self.nettoyage.configure(highlightbackground="#d9d9d9")
        self.nettoyage.configure(highlightcolor="black")
        self.nettoyage.configure(pady="0")
        self.nettoyage.configure(text='''Clear''', command=clear)

        self.google_maps = tk.Button(self.top)
        self.google_maps.place(relx=0.73, rely=0.293, height=64, width=57)
        self.google_maps.configure(activebackground="#3F3A46")
        self.google_maps.configure(activeforeground="white")
        self.google_maps.configure(activeforeground="#000000")
        self.google_maps.configure(background="#3F3A46")
        self.google_maps.configure(borderwidth="0")
        self.google_maps.configure(compound='left')
        self.google_maps.configure(disabledforeground="#a3a3a3")
        self.google_maps.configure(foreground="#000000")
        self.google_maps.configure(highlightbackground="#d9d9d9")
        self.google_maps.configure(highlightcolor="black", command=gps)
        photo_location = "image/google.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.google_maps.configure(image=_img1)
        self.google_maps.configure(pady="0")
        self.google_maps.configure(relief="flat")
        self.tooltip_font = "TkDefaultFont"
        self.google_maps_tooltip = \
            ToolTip(self.google_maps, self.tooltip_font,
                    '''A utiliser apres avoir scannez votre image ou fichier pdf''')

        self.rapport_html = tk.Button(self.top)
        self.rapport_html.place(relx=0.058, rely=0.0, height=54, width=67)
        self.rapport_html.configure(activebackground="#3F3A46")
        self.rapport_html.configure(activeforeground="white")
        self.rapport_html.configure(activeforeground="#ffffff")
        self.rapport_html.configure(background="#3F3A46")
        self.rapport_html.configure(borderwidth="0")
        self.rapport_html.configure(compound='left')
        self.rapport_html.configure(disabledforeground="#a3a3a3")
        self.rapport_html.configure(foreground="#ffffff")
        self.rapport_html.configure(highlightbackground="#d9d9d9")
        self.rapport_html.configure(highlightcolor="black")
        photo_location = "image/load.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.rapport_html.configure(image=_img2)
        self.rapport_html.configure(pady="0")
        self.rapport_html.configure(relief="flat")
        self.tooltip_font = "TkDefaultFont"
        self.rapport_html_tooltip = \
            ToolTip(self.rapport_html, self.tooltip_font, '''Creer un rapport''')

        self.ouverture_du_fichier = tk.Button(self.top)
        self.ouverture_du_fichier.place(relx=0.0, rely=0.0, height=44, width=57)
        self.ouverture_du_fichier.configure(activebackground="#3F3A46")
        self.ouverture_du_fichier.configure(activeforeground="white")
        self.ouverture_du_fichier.configure(activeforeground="#000000")
        self.ouverture_du_fichier.configure(background="#3F3A46")
        self.ouverture_du_fichier.configure(borderwidth="0")
        self.ouverture_du_fichier.configure(compound='left')
        self.ouverture_du_fichier.configure(disabledforeground="#a3a3a3")
        self.ouverture_du_fichier.configure(foreground="#000000")
        self.ouverture_du_fichier.configure(highlightbackground="#d9d9d9")
        self.ouverture_du_fichier.configure(highlightcolor="black", command=load_file)
        photo_location = "image/save.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.ouverture_du_fichier.configure(image=_img3)
        self.ouverture_du_fichier.configure(pady="0")
        self.ouverture_du_fichier.configure(relief="flat")
        self.tooltip_font = "TkDefaultFont"
        self.ouverture_du_fichier_tooltip = \
            ToolTip(self.ouverture_du_fichier, self.tooltip_font, '''ouvre un fichier pdf ou jpg''')

        self.coordonné_gps = tk.Listbox(self.top)
        self.coordonné_gps.place(relx=0.788, rely=0.307, relheight=0.245
                                 , relwidth=0.205)
        self.coordonné_gps.configure(background="#584e57")
        self.coordonné_gps.configure(disabledforeground="#a3a3a3")
        self.coordonné_gps.configure(font="TkFixedFont")
        self.coordonné_gps.configure(foreground="#ffffff")
        self.coordonné_gps.configure(highlightbackground="#d9d9d9")
        self.coordonné_gps.configure(highlightcolor="black")
        self.coordonné_gps.configure(highlightthickness="0")
        self.coordonné_gps.configure(relief="flat")
        self.coordonné_gps.configure(selectbackground="blue")
        self.coordonné_gps.configure(selectforeground="white")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.788, rely=0.28, height=20, width=117)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#3F3A46")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''COORDONNEE GPS''')

        self.discord = tk.Button(self.top)
        self.discord.place(relx=0.924, rely=0.0, height=54, width=77)
        self.discord.configure(activebackground="#3F3A46")
        self.discord.configure(activeforeground="white")
        self.discord.configure(activeforeground="#000000")
        self.discord.configure(background="#3F3A46")
        self.discord.configure(borderwidth="0")
        self.discord.configure(compound='left')
        self.discord.configure(disabledforeground="#a3a3a3")
        self.discord.configure(foreground="#000000")
        self.discord.configure(highlightbackground="#d9d9d9")
        self.discord.configure(highlightcolor="black", command=discord)
        photo_location = "image/discord.png"
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.discord.configure(image=_img4)
        self.discord.configure(pady="0")
        self.discord.configure(relief="flat")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg='#3F3A46', fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.0, rely=0.209, height=22, width=404)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#3F3A46")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Creer par l'équipe de Freefox x) ^^''')


# Support code for Balloon Help (also called tooltips).
# derived from http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
from time import time


class ToolTip(tk.Toplevel):
    """ Provides a ToolTip widget for Tkinter. """

    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=0.5, follow=True):
        self.wdgt = wdgt
        self.parent = self.wdgt.master
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        self.withdraw()
        self.overrideredirect(True)
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                   font=tooltip_font,
                   aspect=1000).grid()
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        self.visible = 1
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        self.lastMotion = time()
        if self.follow is False:
            self.withdraw()
            self.visible = 1
        self.geometry('+%i+%i' % (event.x_root + 20, event.y_root - 10))
        try:
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        self.visible = 0
        self.withdraw()

    def update(self, msg):
        self.msgVar.set(msg)


#                   End of Class ToolTip

def start_up():
    osint_graphique_support.main()


if __name__ == '__main__':
    osint_graphique_support.main()
