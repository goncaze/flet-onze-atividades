import flet as ft


class TabuadaView(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/tabuada"
        self.appbar = ft.AppBar(title=ft.Text("Tabuada"), bgcolor="green")
        self.page = page
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.ttf_numero = ft.TextField(
            label="Número",
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        self.dd_operacoes = ft.Dropdown(
            label="Operação básica",
            hint_text="Selecione uma operação",
            options=[
                ft.dropdown.Option("Adição"),
                ft.dropdown.Option("Subtração"),
                ft.dropdown.Option("Multiplicação"),
                ft.dropdown.Option("Divisão"),
            ],
        )
        self.clm_tabuada = ft.Column()

        self.controls = [
            self.ttf_numero,
            self.dd_operacoes,
            ft.ElevatedButton(
                text="Gerar tabuada",
                on_click=self.gerar_tabuada,
            ),
            self.clm_tabuada,
        ]

    def gerar_tabuada(self, e):
        numero = int(self.ttf_numero.value)
        match self.dd_operacoes.value:
            case "Adição":
                self.calcular("+", numero)
            case "Subtração":
                self.calcular("-", numero)
            case "Multiplicação":
                self.calcular("*", numero)
            case "Divisão":
                self.calcular("/", numero)

    def calcular(self, operacao: str, numero: int):
        tabuada: list[ft.Text] = []

        match operacao:
            case "+":
                for n in range(1, 11):
                    tabuada.append(
                        ft.Text(
                            value=f"{n} {operacao} {numero} = {n + numero}", size=20
                        )
                    )
            case "-":
                for n in range(1, 11):
                    tabuada.append(
                        ft.Text(
                            value=f"{n} {operacao} {numero} = {n - numero}", size=20
                        )
                    )
            case "*":
                for n in range(1, 11):
                    tabuada.append(
                        ft.Text(
                            value=f"{n} {operacao} {numero} = {n * numero}", size=20
                        )
                    )
            case "/":
                for n in range(1, 11):
                    tabuada.append(
                        ft.Text(
                            value=f"{n} {operacao} {numero} = {n / numero}", size=20
                        )
                    )

        self.clm_tabuada.controls = tabuada
        self.clm_tabuada.update()
