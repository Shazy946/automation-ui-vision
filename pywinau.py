from pywinauto import application

def insert_text(text):
    app = application.Application()
    app.start("Notepad")
    dig = app.window(title='Untitled - Notepad')
    dig.edit.type_keys(text)
