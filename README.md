# Site — Distribuidora de Água e Gás

Site institucional responsivo em Flask (Python), com botão de WhatsApp que já
abre com uma mensagem pré-pronta (o cliente só preenche endereço, forma de
pagamento, troco e o pedido).

## Como rodar localmente

```bash
pip install -r requirements.txt
python app.py
```

Depois abra **http://localhost:5000** no navegador.

## Como personalizar

Você **não precisa mexer em HTML ou CSS**. Edite só o arquivo `config.py`:

- `STORE["nome"]`, `STORE["slogan"]` — nome e frase de efeito da loja
- `STORE["whatsapp_numero"]` — número no formato DDI+DDD+número, só dígitos
  (ex.: `55` + `79` + `999999999`)
- `STORE["telefone_exibicao"]` — como o telefone aparece escrito no site
- `STORE["endereco_linha1"/"endereco_linha2"/"endereco_cep"]` — endereço da loja
- `STORE["maps_embed_url"]` — link do mapa incorporado (veja abaixo como pegar)
- `STORE["horario"]` — dias e horários de funcionamento
- `STORE["pagamentos"]` — formas de pagamento aceitas
- `PRODUTOS_AGUA` / `PRODUTOS_GAS` — lista de produtos, detalhes e preços
- `DICAS_GAS` / `DICAS_AGUA` — dicas de segurança exibidas no site

### Como pegar o link do mapa (`maps_embed_url`)

1. Abra o [Google Maps](https://maps.google.com) e busque o endereço da loja.
2. Clique em **Compartilhar** → **Incorporar um mapa**.
3. Copie apenas o valor que está dentro de `src="..."` e cole em
   `maps_embed_url` no `config.py`.

### Como funciona a mensagem pré-pronta do WhatsApp

O texto é montado em `app.py`, na função `montar_link_whatsapp()`. Se quiser
mudar os campos ou emojis da mensagem, edite o texto dentro dessa função.

## Estrutura do projeto

```
site-agua-gas/
├── app.py                 # aplicação Flask
├── config.py               # ← edite aqui: nome, telefone, endereço, produtos
├── requirements.txt
├── templates/
│   └── index.html          # estrutura da página
└── static/
    └── css/
        └── style.css        # visual do site
```

## Colocando no ar (hospedagem)

Este projeto roda em qualquer serviço que suporte Flask, por exemplo:
[Render](https://render.com), [Railway](https://railway.app) ou um VPS com
Gunicorn + Nginx. Para produção, não use `app.run(debug=True)` — troque por
um servidor WSGI como Gunicorn:

```bash
pip install gunicorn
gunicorn app:app
```
