#from src.models import user
from src.models.store import Store
from src.models.user import User


class ServiceUser:

    def __init__(self):
        self.store = Store()

    def verify_user(self, user):
        for db_user in self.store.bd:
            if db_user == user:
                return True
        return False

    def get_id_by_name(self, name):
        for index, user in enumerate(self.store.bd):
            if user.name == name:
                return index
        return False

    def add_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                user = User(name=name, job=job)
                if not self.verify_user(user):
                    self.store.bd.append(user)
                    return "Usuário adicionado"
                else:
                    return "Usuário já existe!"
            else:
                return "Usuário ou Job inválido(s)"
        else:
            return "Usuário ou Job Vazio!"

    def remove_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                user = User(name=name, job=job)
                if self.verify_user(user):
                    self.store.bd.remove(user)
                    return "Usuário removido"
                else:
                    return "Usuário não existe!"
            else:
                return "Usuário ou Job inválido(s)"
        else:
            return "Usuário ou Job Vazio!"

    def update_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                user = User(name=name, job=job)
                for index, db_user in enumerate(self.store.bd):
                    if db_user.name == user.name:
                        self.store.bd[index] = user
                        return "Usuário Atualizado"
                return "Usuário não existe!"
            else:
                return "Usuário ou Job inválido(s)"
        else:
            return "Usuário ou Job Vazio!"
        
    def get_user_by_name(self, name):
        if name is not None:
            if isinstance(name, str):
                for user in self.store.bd:
                    if user.name == name:
                        return user
                return "Usuário com nome " + name + " não existe!"
            else:
                return "Nome inválido"
        else:
            return "Nome vazio!"
