



import kivy
kivy.require('1.0.6') # 

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox

from ctrlFirst import CtrlFirst



class FirstPage(GridLayout):

	def __init__(self,**kwargs):
		print "ctrl"
		super(FirstPage,self).__init__(**kwargs)
		self.ctrl = CtrlFirst()
		

	def activate(self):

		ids = self.ids

		novos = {}

		if ids.circulo.active :
			novos['forma'] = 'circulo'
		else :
			novos['forma'] = 'retangulo'



		if ids.vermelho.active:
			novos['cor'] = 'vermelho'

		else:
			novos['cor'] = 'verde'

		return novos
			

	def iniciar(self):
		self.ids.lb_certo.text,self.ids.lb_errado.text = "0","0"
		escolhas=self.activate()
		lbs = (self.ids.lb_certo,self.ids.lb_errado)
		self.ctrl.iniciar(escolhas,lbs)

	def parar(self):
		for i in range(1000):
			ct=self.ids.lb_certo.text
			lc = int(ct)
			self.ids.lb_certo.text = str(lc +1 )

		print self.ids.lb_certo

class MyApp(App):

    def build(self):
    	pass


MyApp().run()