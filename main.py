from src.service.service_user import ServiceUser

service = ServiceUser()
resposta = service.add_user("Talita", "QA")
print(resposta)

resposta = service.add_user(None, "QA")
print(resposta)

resposta = service.add_user("Talita", "QA")
print(resposta)

resposta = service.add_user("Talita", "QA")
print(resposta)

resposta = service.remove_user("Talita", "QA")
print(resposta)
service