class DbClass:
    def set_valores_dict(self, dicionario):
        for key in dicionario.keys():
            self.__dict__[key] = dicionario.get(key)

    def json(self):
        return self.__dict__

    def get_attrs(self):
        return list(self.__dict__.keys())
