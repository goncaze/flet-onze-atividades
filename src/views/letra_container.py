import flet as ft


class LetraContainer(ft.Container):
    def __init__(self, txt_valor: ft.Text):
        super().__init__()
        # conteúdo
        self.content = txt_valor
        self.alignment = ft.alignment.center

        # Dimensão, formato, aparência
        self.width = 40
        self.height = 40
        self.margin = 0
        self.bgcolor = ft.colors.AMBER

        # Animação
        self.offset = ft.transform.Offset(x=0, y=0)
        self.animate_offset = True
        self.animate = ft.animation.Animation(
            duration=10000, curve=ft.AnimationCurve.EASE
        )

    def animacao_offtset(self, x: int = 0, y: int = -10):
        self.offset = ft.transform.Offset(x, y)
        self.update()
