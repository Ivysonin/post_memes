from datetime import datetime
import pytz


def horario_local():
    return datetime.now(pytz.timezone('America/Sao_Paulo'))