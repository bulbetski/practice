from io import BytesIO
from PIL import Image
import parser
import requests
from random import randint
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def show_random_picture(all_posts, min, max):
    arr = []
    for post in all_posts:
        try:
            if post['attachments'][0]['type']:
                img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
            else:
                img_url = 'pass'
        except:
            pass
        if int(min) <= post['likes']['count'] <= int(max):
            arr.append(img_url)
    if len(arr) != 0:
        r = randint(0, len(arr) - 1)
        response = requests.get(arr[r])
        img = Image.open(BytesIO(response.content))
        img.show()
    else:
        print('Нет постов, удовлетворяющих условию')


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 1

        self.inside.add_widget(
            Label(text="Введите кол-во лайков (в первое поле нижнюю границу диапозона, во второе верхнюю)"))

        self.inside.add_widget(Label(text="Минимальное кол-во лайков:"))
        self.min = TextInput(multiline=False)
        self.inside.add_widget(self.min)

        self.inside.add_widget(Label(text="Максимальное кол-во лайков:"))
        self.max = TextInput(multiline=False)
        self.inside.add_widget(self.max)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=60)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        show_random_picture(parser.p, self.min.text, self.max.text)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()