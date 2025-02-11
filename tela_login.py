from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class LoginApp(App):
    def build(self):
        layout = BoxLayout(orientation = "vertical", spacing = 10, padding = 20)

        # CAMPO DO NOME (TEXTO NORMAL)
        self.username = TextInput(hint_text = "Digite seu nome",
        multiline = False,
        font_size = 20,
        padding=[10, 10, 10, 10]
        )
        layout.add_widget(Label(text = "Nome:"))
        layout.add_widget(self.username)

        # CAMPO DO SENHA (TEXTO OCULTO)
        self.password = TextInput(hint_text = "Digite sua senha", password =  True, multiline = False)
        layout.add_widget(Label(text = "Senha:"))
        layout.add_widget(self.password)

        # BOTÃO DE LOGIN
        btn = Button(text = "Entrar")
        btn.bind(on_press = self.login)
        layout.add_widget(btn)

        return layout
    
    def login(self, instance):
        print(f"Usuário: {self.username.text}")
        print(f"Senha: {self.password.text}")

LoginApp().run()