class ParametroVazio(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ParametroInvalido(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class AtividadeInvalida(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
