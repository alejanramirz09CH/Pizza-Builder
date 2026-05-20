import flet as ft

def main(page: ft.Page):
    page.title = "Chef de Pizza"
    page.window.width = 600
    page.window.height = 700

    def toggle_pepperoni(e):
        pepperoni.visible = switchpepperoni.value
        page.update()

    def toggle_hongos(e):
        hongos.visible = switchhongos.value
        page.update()

    def toggle_jamon(e):
        jamon.visible = switchjamon.value
        page.update()

    pizza = ft.Image(src="pizza.png", width=400, height=400)
    pepperoni = ft.Image(src="pepperoni.png", width=400, height=400, visible=False)
    hongos = ft.Image(src="hongos.png", width=400, height=400, visible=False)
    jamon = ft.Image(src="jamon.png", width=400, height=400, visible=False)

    stackpizza = ft.Stack(
        width=400,
        height=400,
        controls=[pizza, pepperoni, hongos, jamon]
    )

    switchpepperoni = ft.Switch(label="Pepperoni", on_change=toggle_pepperoni)
    switchhongos = ft.Switch(label="Hongos", on_change=toggle_hongos)
    switchjamon = ft.Switch(label="Jamon", on_change=toggle_jamon)

    page.add(
        ft.Column(
            [
                ft.Text("Chef, Construya Su Pizza", size=30, weight="bold"),
                stackpizza,
                switchpepperoni,
                switchhongos,
                switchjamon
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )   

ft.run(main=main, assets_dir="assets")