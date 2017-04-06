__author__ = 'ricky'
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from math import sqrt


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        try:
            float(s)
            return True
        except ValueError:
            return False


class Base:

    def display_message(self, mess):
        self.label_message.set_visible(True)
        self.label_message.set_text(mess)
        self.label_ans_plus.set_visible(False)
        self.label_ans_min.set_visible(False)

    def display_ans(self, widget):
        if self.entry_a.get_text() != "" and self.entry_b.get_text() != "" and self.entry_c.get_text() != "":
            if is_number(self.entry_a.get_text()) and \
                    is_number(self.entry_b.get_text()) and \
                    is_number(self.entry_c.get_text()):
                text_a = float(self.entry_a.get_text())
                text_b = float(self.entry_b.get_text())
                text_c = float(self.entry_c.get_text())

                try:
                    ans_plus = (-text_b + sqrt(text_b ** 2 - (4 * text_a * text_c))) / 2 * text_a
                    ans_min = (-text_b - sqrt(text_b ** 2 - (4 * text_a * text_c))) / 2 * text_a

                    self.label_ans_plus.set_markup("""<span foreground="darkblue" size="15000">""" +
                                                   "x (+) = " + str(ans_plus) +
                                                   "</span>")
                    self.label_ans_min.set_markup("""<span foreground="darkblue" size="15000">""" +
                                                  "x (-) = " + str(ans_min) +
                                                  """</span>""")

                    self.label_message.set_visible(False)
                    self.label_ans_plus.set_visible(True)
                    self.label_ans_min.set_visible(True)
                except ValueError:
                    self.display_message("No real roots")

            else:
                self.display_message("Enter only numbers")
        else:
            self.display_message("Enter values into all text boxes")

    def __init__(self):
        win = Gtk.Window()
        win.set_name("Quadratic Equation Solver")
        win.connect("delete-event", Gtk.main_quit)
        win.set_title("Quadratic Equation Solver")
        win.set_size_request(300, 200)
        win.set_border_width(10)
        win.set_resizable(False)

        label_a = Gtk.Label()
        label_a.set_markup("<b>a = </b>")
        label_a.set_alignment(0, 0.5)

        self.entry_a = Gtk.Entry()
        self.entry_a.connect("activate", self.display_ans)

        label_b = Gtk.Label()
        label_b.set_markup("<b>b = </b>")
        label_b.set_alignment(0, 0.5)

        self.entry_b = Gtk.Entry()
        self.entry_b.connect("activate", self.display_ans)

        label_c = Gtk.Label()
        label_c.set_markup("<b>c = </b>")
        label_c.set_alignment(0, 0.5)

        self.entry_c = Gtk.Entry()
        self.entry_c.connect("activate", self.display_ans)

        button_solve = Gtk.Button("Solve")
        button_solve.connect("clicked", self.display_ans)

        self.label_message = Gtk.Label()
        self.label_message.set_alignment(0, 0.5)

        self.label_ans_plus = Gtk.Label()
        self.label_ans_plus.set_alignment(0, 0.5)
        self.label_ans_plus.set_selectable(True)

        self.label_ans_min = Gtk.Label()
        self.label_ans_min.set_alignment(0, 0.5)
        self.label_ans_min.set_selectable(True)

        box = Gtk.VBox(homogeneous=False, spacing=6)

        box.pack_start(label_a, False, True, 0)
        box.pack_start(self.entry_a, False, True, 0)

        box.pack_start(label_b, False, True, 0)
        box.pack_start(self.entry_b, False, True, 0)

        box.pack_start(label_c, False, True, 0)
        box.pack_start(self.entry_c, False, True, 0)

        box.pack_start(button_solve, False, True, 0)

        box.pack_start(self.label_message, False, True, 0)
        box.pack_start(self.label_ans_plus, False, True, 0)
        box.pack_start(self.label_ans_min, False, True, 0)

        win.add(box)
        win.show_all()

        self.label_message.set_visible(False)

    @staticmethod
    def main():
        Gtk.main()


if __name__ == "__main__":
    run = Base()
    run.main()
