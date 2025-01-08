from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import SystemMessage, HumanMessage

auth = 'Njc4N2RhM2EtNDg4ZS00ZmExLWIxYTQtMjhmNDEwYWNhYjI3Ojk3MTEwMDk2LTg1NzktNDcxYS1iY2ZjLWQwOTE0MWZiMzJlYg=='
giga = GigaChat(credentials=auth,
                model='GigaChat:latest',
                verify_ssl_certs=False
                )

system_promt = "Порекомендуй наилучшее место для проведения досуга по запросу пользователя"


def giga_chat_request(msg: str):
    msgs = [
        SystemMessage(content=system_promt),
        HumanMessage(content=msg)
    ]
    answer = giga(msgs)
    return answer.content