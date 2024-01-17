from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.textinput import TextInput


class CPFFormattingTextInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= 14:
            return

        if substring.isnumeric():
            if len(self.text) == 3 or len(self.text) == 7:
                self.text += '.'

            elif len(self.text) == 11:
                self.text += '-'
        else:
            return

        super(CPFFormattingTextInput, self).insert_text(substring, from_undo)


class DataNascimentoFormattingTextInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= 10:
            return

        if substring.isnumeric():
            if len(self.text) == 2 or len(self.text) == 5:
                self.text += '/'
        else:
            return

        super(DataNascimentoFormattingTextInput, self).insert_text(substring, from_undo)


GUI = Builder.load_file("screen.kv")


class ConnPsico(App):
    def build(self):
        Window.size = (350, 650)
        return GUI


if __name__ == '__main__':
    ConnPsico().run()
