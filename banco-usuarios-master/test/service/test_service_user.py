from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_com_sucesso(self):
        #Setup
        service = ServiceUser()
        resposta_esperada = "Usuário adicionado"

        #Chamada
        resposta = service.add_user("Talita", "QA")

        #Avaliação
        assert resposta_esperada == resposta

    def test_add_user_com_falha_name_none(self):
        # Setup
        service = ServiceUser()
        resposta_esperada = "Usuário inválido"

        #Chamada
        resposta = service.add_user(None, "QA")

        #Avaliação
        assert resposta_esperada == resposta