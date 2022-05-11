# Open input file & output files, read input file by line, write formatted lines to output file.
#
# with open('input.txt') as input_f:
#     with open('output.txt', 'w') as output_f:
#         for line in input_f:
#             output_f.write('- [ ] ' + line)

import kivy.app
import kivy.uix.gridlayout
import kivy.uix.textinput
import kivy.uix.label


class Layout(kivy.uix.gridlayout.GridLayout):
    
    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)
        self.cols = 1

        self.input_box = kivy.uix.textinput.TextInput(multiline=True)
        self.input_box.bind(text=self.on_text)
        self.output_box = kivy.uix.textinput.TextInput(multiline=True)
        
        self.add_widget(self.input_box)
        self.add_widget(self.output_box)

    def on_text(self, *args):
        unformatted_text = self.input_box.text
        formatted_text = ''
        
        for line in unformatted_text.splitlines():
            formatted_text += '- [ ] ' + line + '\n'
        
        self.output_box.text = formatted_text


class MarkdownListGen(kivy.app.App):
    def build(self):
        return Layout()
    
    
if __name__ == '__main__':
    MarkdownListGen().run()