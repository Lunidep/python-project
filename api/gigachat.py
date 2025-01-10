from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import SystemMessage, HumanMessage

auth = 'Njc4N2RhM2EtNDg4ZS00ZmExLWIxYTQtMjhmNDEwYWNhYjI3Ojk3MTEwMDk2LTg1NzktNDcxYS1iY2ZjLWQwOTE0MWZiMzJlYg=='
giga = GigaChat(credentials=auth,
                model='GigaChat:latest',
                verify_ssl_certs=False
                )

system_prompt = ("Ты выступаешь в роли советчика мест для проведения досуга. "
                 "Твоя задача - предлагать пользователю по его запросу 5 мест, "
                 "которые соответствуют его предпочтениям. Ответ должен содержать "
                 "список мест и их описание, желательно адрес. Ответ должен быть "
                 "вежливым и позитивным. Запрос пользователя должен напрямую относиться "
                 "к проведению досуга, если это не так пиши сообщение \"Извините, не "
                 "могу подобрать места, попробуйте переформулируйте свой запрос.\". "
                 "Если не указан город, предлагай варианты из Москвы. Если запрос напрямую "
                 "относится к проведению досуга, то ты обязан написать варианты")


def giga_chat_request(msg: str):
    msgs = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=msg)
    ]
    answer = giga(msgs)
    return answer.content
