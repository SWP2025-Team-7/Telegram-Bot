from enum import Enum

class ButtonsText(Enum):
    confirm = "Подтвердить"
    decline = "Отклонить"

class MessagesText(Enum):
    send_instructions = """
    Отправьте вашу справку в формате pdf
    """