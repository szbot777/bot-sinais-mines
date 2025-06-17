import time
import random
import os
from telegram import Bot

# Pega o token e chat_id das variáveis de ambiente
TOKEN = os.environ.get('TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

bot = Bot(token=TOKEN)

def gerar_sinal():
    casas = list(range(1, 26))
    seguras = random.sample(casas, 5)
    return sorted(seguras)

def enviar_sinal():
    seguras = gerar_sinal()
    mensagem = f"""
🚨 NOVO SINAL MINES 🚨

✅ Casas seguras: {seguras}
💣 Bombas: 3
🎯 Estratégia: Jogar até 2 greens e parar
⚠️ Mantenha a gestão! Não aposte por impulso.
    """
    bot.send_message(chat_id=CHAT_ID, text=mensagem)
    print(f"Sinal enviado: {seguras}")

def main():
    while True:
        enviar_sinal()
        time.sleep(300)  # 5 minutos

if __name__ == '__main__':
    main()
