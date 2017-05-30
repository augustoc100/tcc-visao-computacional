
"""
Teste com a biblioteca de interface kivy, o primeiro tutorial da linguagem no site da biblioteca
"""

import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.lang import Builder

kvcode = """

PageLayout:
    Button:
        text: 'page1'
    Button:
        text: 'page2'
    
"""

from kivy.app import App
from kivy.uix.button import Button


class Tela(App):

	def build(self):
		return Builder.load_string(kvcode)

Tela().run()
