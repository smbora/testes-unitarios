from src.service.service_user import ServiceUser
from src.models.user import User


class TestServiceUser:

    def test_add_user_com_sucesso(self):
        #Setup
        service = ServiceUser()
        resposta_esperada = "Usuário adicionado"

        #Chamada
        resposta = service.add_user("Sarita", "QA")

        #Avaliação
        assert resposta_esperada == resposta

    def test_add_user_com_falha_name_vazio(self):
        # Setup
        service = ServiceUser()
        resposta_esperada = "Usuário ou Job Vazio!"

        # Chamada
        resposta = service.add_user(None, "QA")

        #Avaliação
        assert resposta_esperada == resposta

    def test_add_user_com_falha_job_vazio(self):
        # Setup
        service = ServiceUser()
        resposta_esperada = "Usuário ou Job Vazio!"

        # Chamada
        resposta = service.add_user("Sarita", None)

        # Avaliação
        assert resposta_esperada == resposta

    def test_add_user_com_falha_name_invalido(self):
        # Setup
        service = ServiceUser()
        resposta_esperada = "Usuário ou Job inválido(s)"

        # Chamada
        resposta = service.add_user(500, "QA")

        #Avaliação
        assert resposta_esperada == resposta

    def test_add_user_com_falha_job_invalido(self):
        # Setup
        service = ServiceUser()
        resposta_esperada = "Usuário ou Job inválido(s)"

        # Chamada
        resposta = service.add_user("Sarita", 500)

        # Avaliação
        assert resposta_esperada == resposta
    def test_remove_user_com_sucesso(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Usuário removido"

        # Chamada
        resposta = service.remove_user("Sarita", "QA")

        # Avaliação
        assert resposta_esperada == resposta
    def test_remove_user_com_falha_nome(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Usuário não existe!"

        # Chamada
        resposta = service.remove_user("Hana", "QA")

        # Avaliação
        assert resposta_esperada == resposta

    def test_remove_user_com_falha_job(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Usuário não existe!"

        # Chamada
        resposta = service.remove_user("Sarita", "Developer")

        # Avaliação
        assert resposta_esperada == resposta

    def test_remove_user_com_falha_nome_vazio(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Usuário ou Job Vazio!"

        # Chamada
        resposta = service.remove_user(None, "QA")

        # Avaliação
        assert resposta_esperada == resposta

    def test_remove_user_com_falha_job_vazio(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Usuário ou Job Vazio!"

        # Chamada
        resposta = service.remove_user("Sarita", None)

        # Avaliação
        assert resposta_esperada == resposta

    def test_remove_user_com_falha_nome_invalido(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Usuário ou Job inválido(s)"

        # Chamada
        resposta = service.remove_user(500, "QA")

        # Avaliação
        assert resposta_esperada == resposta

    def test_remove_user_com_falha_job_invalido(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Usuário ou Job inválido(s)"

        # Chamada
        resposta = service.remove_user("Sarita", 500)

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_user_by_name_com_sucesso(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")

        # Chamada
        resposta = service.get_user_by_name("Sarita")

        # Avaliação
        assert isinstance(resposta, User)
        assert resposta.name == "Sarita"
        assert resposta.job == "QA"

    def test_get_user_by_name_com_falha_nome_invalido(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Nome inválido"

        # Chamada
        resposta = service.get_user_by_name(500)

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_user_by_name_com_sucesso_usuario_inexistente(self):
        # Setup
        service = ServiceUser()
        resposta_esperada = "Usuário com nome Sarita não existe!"

        # Chamada
        resposta = service.get_user_by_name("Sarita")

        # Avaliação
        assert resposta_esperada == resposta

    def test_update_user_com_sucesso(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Usuário Atualizado"

        # Chamada
        resposta = service.update_user("Sarita", "Developer")

        # Avaliação
        assert resposta == resposta_esperada
        confirmacao = service.get_user_by_name("Sarita")
        assert confirmacao.name == "Sarita"
        assert confirmacao.job == "Developer"

    def test_update_user_com_falha_nome_vazio(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Usuário ou Job Vazio!"

        # Chamada
        resposta = service.update_user(None, "Developer")

        # Avaliação
        assert resposta == resposta_esperada

    def test_update_user_com_falha_job_vazio(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Usuário ou Job Vazio!"

        # Chamada
        resposta = service.update_user("Sarita", None)

        # Avaliação
        assert resposta == resposta_esperada

    def test_update_user_com_falha_nome_invalido(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Usuário ou Job inválido(s)"

        # Chamada
        resposta = service.update_user(500, "Developer")

        # Avaliação
        assert resposta == resposta_esperada

    def test_update_user_com_falha_job_invalido(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Usuário ou Job inválido(s)"

        # Chamada
        resposta = service.update_user("Sarita", 500)

        # Avaliação
        assert resposta == resposta_esperada

    def test_update_user_com_falha_usario_inexistente(self):
        # Setup
        service = ServiceUser()
        service.add_user("Sarita", "QA")
        resposta_esperada = "Usuário não existe!"

        # Chamada
        resposta = service.update_user("Hana", "Developer")

        # Avaliação
        assert resposta == resposta_esperada