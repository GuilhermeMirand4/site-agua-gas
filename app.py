# -*- coding: utf-8 -*-
from urllib.parse import quote
from flask import Flask, render_template

from config import STORE, PRODUTOS_AGUA, PRODUTOS_GAS, DICAS_GAS, DICAS_AGUA

app = Flask(__name__)


def montar_link_whatsapp():
    """Monta o link do WhatsApp com uma mensagem pré-pronta.
    O cliente só precisa preencher endereço, forma de pagamento, troco e pedido."""
    mensagem = (
        "Olá! Gostaria de fazer um pedido 🙂\n\n"
        "📍 Endereço para entrega: \n"
        "💳 Forma de pagamento: \n"
        "💵 Precisa de troco? Para quanto? \n"
        "🛒 Pedido (produto e quantidade): "
    )
    numero = STORE["whatsapp_numero"]
    return f"https://wa.me/{numero}?text={quote(mensagem)}"


@app.route("/")
def home():
    return render_template(
        "index.html",
        store=STORE,
        produtos_agua=PRODUTOS_AGUA,
        produtos_gas=PRODUTOS_GAS,
        dicas_gas=DICAS_GAS,
        dicas_agua=DICAS_AGUA,
        whatsapp_link=montar_link_whatsapp(),
        ano_atual=2026,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
