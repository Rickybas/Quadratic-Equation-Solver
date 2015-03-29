__author__ = 'ricky'
from gi.repository import Gtk, Gdk
from math import sqrt

class Base:

    def about(self, widget):
        self.about_dia = Gtk.AboutDialog()
        self.about_dia.set_program_name("Quadratic Equation Solver")
        self.about_dia.set_version("0.1")
        self.about_dia.set_website("http://www.cosmicblocks.co.nr")
        self.about_dia.set_authors(["Ricky"])
        self.about_dia.set_comments("Small program written in Python to solve quadratic equations")
        self.about_dia.run()
        self.about_dia.destroy()

    def RepresentsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            try:
                float(s)
                return True
            except ValueError:
                return False

    def on_button_clicked(self, widget):
        if self.entry_a.get_text() != "" and self.entry_b.get_text() != "" and self.entry_c.get_text() != "":
            if self.RepresentsInt(self.entry_a.get_text()) and self.RepresentsInt(self.entry_b.get_text()) and self.RepresentsInt(self.entry_c.get_text()):
                self.text_a = float(self.entry_a.get_text())
                self.text_b = float(self.entry_b.get_text())
                self.text_c = float(self.entry_c.get_text())

                try:
                    self.ans_plus = ((-self.text_b) + sqrt(self.text_b**2 - (4 * self.text_a * self.text_c))) / (2 * self.text_a)
                    self.ans_min = ((-self.text_b) - sqrt(self.text_b**2 - (4 * self.text_a * self.text_c))) / (2 * self.text_a)

                    self.label_ans_plus.set_markup("""<span foreground="darkblue" size="15000">""" + "Plus: " + str(self.ans_plus) + """</span>""")
                    self.label_ans_min.set_markup("""<span foreground="darkblue" size="15000">""" + "Minus: " + str(self.ans_min) + """</span>""")
                except:
                    self.label_ans_plus.set_markup("""<span foreground="darkblue" size="15000">""" + "Syntax Error" + """</span>""")
                    self.label_ans_min.set_markup("""<span foreground="darkblue" size="15000">""" + "Syntax Error" + """</span>""")
            else:
                self.label_ans_plus.set_markup("""<span foreground="darkblue" size="15000">""" + "Enter numbers" + """</span>""")
                self.label_ans_min.set_markup("""<span foreground="darkblue" size="15000">""" + "Enter numbers" + """</span>""")
        else:
            self.label_ans_plus.set_markup("""<span foreground="darkblue" size="15000">""" + "Enter a value into all text boxes" + """</span>""")
            self.label_ans_min.set_markup("""<span foreground="darkblue" size="15000">""" + "Enter a value into all text boxes" + """</span>""")

    def __init__(self):
        self.win = Gtk.Window()
        self.win.set_name("QuadSolver")
        self.win.connect("delete-event", Gtk.main_quit)
        self.win.set_title("Quadratic Equation Solver")
        self.win.set_size_request(300, 200)
        self.win.set_border_width(10)
        self.win.set_resizable(False)

        self.style_provider = Gtk.CssProvider()

        self.text_a = ""
        self.text_b = ""
        self.text_c = ""
        self.ans_plus = None
        self.ans_min = None

        self.label = Gtk.Label()
        self.label.set_markup("""<span foreground="darkblue" size="18000">Quadratic Equation Solver</span>""")

        self.label_a = Gtk.Label()
        self.label_a.set_markup("<b>a = </b>")
        self.label_a.set_alignment(0, 0.5)

        self.entry_a = Gtk.Entry()
        self.entry_a.connect("activate", self.on_button_clicked)

        self.label_b = Gtk.Label()
        self.label_b.set_markup("<b>b = </b>")
        self.label_b.set_alignment(0, 0.5)

        self.entry_b = Gtk.Entry()
        self.entry_b.connect("activate", self.on_button_clicked)

        self.label_c = Gtk.Label()
        self.label_c.set_markup("<b>c = </b>")
        self.label_c.set_alignment(0, 0.5)

        self.entry_c = Gtk.Entry()
        self.entry_c.connect("activate", self.on_button_clicked)

        self.button = Gtk.Button("Click Here")
        self.button.set_name("Test")
        self.button.connect("clicked", self.on_button_clicked)

        self.label_ans_x = Gtk.Label()
        self.label_ans_x.set_markup("""<span foreground="darkblue" size="13000">""" + "x = " + """</span>""")

        self.label_ans_plus = Gtk.Label()
        self.label_ans_plus.set_markup("""<span foreground="darkblue" size="15000">""" + "Plus: " + """</span>""")
        self.label_ans_plus.set_alignment(0, 0.5)
        self.label_ans_plus.set_selectable(True)

        self.label_ans_or = Gtk.Label()
        self.label_ans_or.set_markup("""<span foreground="darkblue" size="13000">""" + "or" + """</span>""")
        self.label_ans_or.set_alignment(0, 0.5)

        self.label_ans_min = Gtk.Label()
        self.label_ans_min.set_markup("""<span foreground="darkblue" size="15000">""" + "Minus: " + """</span>""")
        self.label_ans_min.set_alignment(0, 0.5)
        self.label_ans_min.set_selectable(True)

        self.button_dio = Gtk.Button("About")
        self.button_dio.set_name("Test")
        self.button_dio.connect("clicked", self.about)

        self.dio = Gtk.AboutDialog(title="About", parent=None, flags=0, buttons=None, _buttons_property=None)

        self.box = Gtk.VBox(homogeneous=False, spacing=6)
        self.box.pack_start(self.label, False, True, 0)

        self.box.pack_start(self.label_a, False, True, 0)
        self.box.pack_start(self.entry_a, False, True, 0)

        self.box.pack_start(self.label_b, False, True, 0)
        self.box.pack_start(self.entry_b, False, True, 0)

        self.box.pack_start(self.label_c, False, True, 0)
        self.box.pack_start(self.entry_c, False, True, 0)

        self.box.pack_start(self.button, False, True, 0)

        self.box.pack_start(self.label_ans_x, False, True, 0)
        self.box.pack_start(self.label_ans_plus, False, True, 0)
        self.box.pack_start(self.label_ans_or, False, True, 0)
        self.box.pack_start(self.label_ans_min, False, True, 0)

        self.box.pack_start(self.button_dio, False, True, 0)


        css = """
        #Test:hover{
            background: lightblue;
            transition: 300ms linear;
        }
        """

        self.style_provider.load_from_data(css)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            self.style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.win.add(self.box)
        self.win.show_all()

    def main(self):
        Gtk.main()

if __name__ == "__main__":
    run = Base()
    run.main()