# -*- coding: utf-8 -*-
"""
CONFIGURAÇÃO DA LOJA
====================
Edite apenas os valores abaixo. Não é necessário mexer em HTML, CSS ou no app.py
para trocar nome, telefone, endereço ou produtos.
"""

STORE = {
    # Identidade
    "nome": "Distribuidora Fonte & Chama",
    "slogan": "Água mineral e gás de cozinha, entregues no mesmo dia",

    # Contato
    "telefone_exibicao": "(79) 99999-9999",   # como aparece escrito no site
    "whatsapp_numero": "5579999999999",       # DDI+DDD+número, só dígitos, para o link do WhatsApp
    "telefone_fixo": "(79) 3333-4444",        # opcional, aparece no rodapé. Deixe "" para ocultar.

    # Endereço
    "endereco_linha1": "Av. das Palmeiras, 452",
    "endereco_linha2": "Bairro Centro, Aracaju - SE",
    "endereco_cep": "49000-000",

    # Link do Google Maps para embutir (Compartilhar > Incorporar um mapa > copie só a URL do src="...")
    "maps_embed_url": "https://www.google.com/maps?q=Aracaju,SE&output=embed",
    # Link do Google Maps para o botão "Como chegar"
    "maps_link_url": "https://www.google.com/maps/search/?api=1&query=Aracaju,SE",

    # Horário de funcionamento
    "horario": [
        ("Segunda a sexta", "7h às 18h"),
        ("Sábado", "7h às 13h"),
        ("Domingo", "Fechado"),
    ],

    "area_entrega": "Entregamos em toda a região central e bairros vizinhos",
    "tempo_entrega": "Entrega em média em 30 a 60 minutos",
    "tempo_entrega_curto": "30 a 60 min",   # usado no painel rápido do topo
    "area_entrega_curta": "Centro e região",  # usado no painel rápido do topo

    # Formas de pagamento aceitas (aparece na seção de pedido)
    "pagamentos": ["Dinheiro", "Pix", "Cartão de débito", "Cartão de crédito"],
}

# Produtos exibidos no site. Preço pode ficar como "" se preferir combinar por telefone.
PRODUTOS_AGUA = [
    {"nome": "Galão de água mineral 20L", "detalhe": "Com troca de vasilhame", "preco": "R$ 12,00"},
    {"nome": "Galão de água mineral 20L", "detalhe": "Vasilhame novo (primeira compra)", "preco": "R$ 45,00"},
    {"nome": "Garrafão 10L", "detalhe": "Com troca de vasilhame", "preco": "R$ 8,00"},
    {"nome": "Fardo com 12 garrafas de 500ml", "detalhe": "Lacradas", "preco": "R$ 18,00"},
]

PRODUTOS_GAS = [
    {"nome": "Botijão de gás P13", "detalhe": "Uso residencial - com troca do vasilhame", "preco": "R$ 110,00"},
    {"nome": "Botijão de gás P45", "detalhe": "Uso comercial - com troca do vasilhame", "preco": "R$ 380,00"},
    {"nome": "Botijão de gás P90", "detalhe": "Uso comercial - com troca do vasilhame", "preco": "R$ 720,00"},
    {"nome": "Mangueira e registro", "detalhe": "Kit de instalação com certificação do Inmetro", "preco": "R$ 35,00"},
]

# Dicas de segurança
DICAS_GAS = [
    "Verifique se o botijão tem o selo do Inmetro e se a validade da mangueira e do registro não está vencida.",
    "Mantenha o botijão sempre na posição vertical e em ambiente ventilado, nunca dentro de armários fechados.",
    "Para checar vazamento, passe água com sabão nas conexões: se formar bolhas, feche o registro e chame o entregador.",
    "Nunca use fósforo ou isqueiro para testar vazamento de gás.",
    "Troque a mangueira a cada 5 anos, mesmo sem sinais de desgaste aparente.",
    "Mantenha o botijão longe de fontes de calor, tomadas elétricas e ao alcance de crianças.",
]

DICAS_AGUA = [
    "Confira se o lacre de segurança do galão está intacto antes de aceitar a entrega.",
    "Observe a data de validade impressa no rótulo ou na tampa do galão.",
    "Guarde os galões em local fresco, longe da luz solar direta, para preservar a qualidade da água.",
    "Higienize o bebedouro e o suporte do galão a cada 15 dias com água sanitária própria para esse fim.",
    "Não reutilize o galão vazio para armazenar outros líquidos ou produtos químicos.",
    "Ao trocar o vasilhame, verifique se o novo galão não está amassado, rachado ou estufado.",
]
