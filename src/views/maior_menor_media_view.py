import flet as ft


class MaiorMenorMedia(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/mmm"
        self.appbar = ft.AppBar(
            title=ft.Text(value="Maior, menor e média", color="white"),
            bgcolor="green",
        )
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.txt_resultado = ft.Text(size=20)
        self.ttf_um = ft.TextField(
            label="Número 01",
            hint_text="Digite um número",
            keyboard_type=ft.KeyboardType.NUMBER,
        )
        self.ttf_dois = ft.TextField(
            label="Número 02",
            hint_text="Digite um número",
            keyboard_type=ft.KeyboardType.NUMBER,
        )
        self.ttf_tres = ft.TextField(
            label="Número 03",
            hint_text="Digite um número",
            keyboard_type=ft.KeyboardType.NUMBER,
        )
        self.btn_calcular = ft.ElevatedButton(text="Calcular", on_click=self.calcular)

        self.controls = [
            self.ttf_um,
            self.ttf_dois,
            self.ttf_tres,
            self.btn_calcular,
            self.txt_resultado,
        ]

    def calcular(self, e):
        numero_1 = float(self.ttf_um.value)
        numero_2 = float(self.ttf_dois.value)
        numero_3 = float(self.ttf_tres.value)

        media = (numero_1 + numero_2 + numero_3) / 3

        if numero_1 < numero_2 < numero_3:
            maior = numero_3
            menor = numero_1
        elif numero_1 < numero_3 < numero_2:
            maior = numero_2
            menor = numero_1
        elif numero_1 > numero_2 > numero_3:
            maior = numero_1
            menor = numero_3
        elif numero_1 > numero_3 > numero_2:
            maior = numero_1
            menor = numero_2
        elif numero_3 > numero_1 > numero_2:
            maior = numero_3
            menor = numero_2
        elif numero_3 < numero_1 < numero_2:
            maior = numero_2
            menor = numero_3

        self.txt_resultado.value = f"Maior: {maior} \nMenor: {menor} \nMédia: { media }"
        self.txt_resultado.update()
