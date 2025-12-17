import flet as ft

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    greeting_history = []
    history_text = ft.Text('История приветствий')

    def on_button_click(_):
        print(name_input.value)
        name = name_input.value.strip()

        if name:
            greeting_text.value = f"Hello, {name}!"
            greeting_text.color = None
            name_input.value = None
            

            
            greeting_history.append(name)
            print(greeting_history)
            history_text.value = f"История приветствий: \n" + f""

        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED

        page.update()

    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)

    elevated_button = ft.ElevatedButton(text="send", on_click=on_button_click, icon=ft.Icons.SEND, color=ft.Colors.GREEN, icon_color=ft.Colors.RED)

    text_button = ft.TextButton(text='send', on_click=on_button_click, icon=ft.Icons.SEND)

    icon_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=toggle_theme)

    # page.add(greeting_text, name_input, text_button, elevated_button, icon_button)

    page.add(greeting_text, ft.Row([name_input, elevated_button]), history_text)
ft.app(target=main)