import re
class Seguridad:

    def __init__(self):
        self.dict = {}
        self.regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        
    def _verEmail(self, email):
        match = re.search(self.regex, email)

        if(match):
            return True
        else:
            return False

    def _verPass(self):
        pass

    def registrarUsuario(self, email, password, password2):        
        return self._verEmail(email)

    def ingresarUsuario(self, email, password):
        pass





if __name__ == '__main__':
    pass