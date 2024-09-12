from flet import *
def main(page:Page):
  t = Text("Hello")
  page.add(t)
  page.update()

app(target=main)
