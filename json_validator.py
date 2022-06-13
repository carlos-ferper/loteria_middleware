
LOGIN_SCHEMA = ['email', 'senha']
AUMENTAR_SALDO_SCHEMA = ['token', 'valor']
CRIAR_SORTEIO_SCHEMA = ['token', "tipo_sorteio", "data_sorteio", "inicio_vendas", "fim_vendas",
                        "quantidade_ingressos", "ingressos_por_usuario", "preco_ingresso", "premio"]
COMPRAR_INGRESSO_SCHEMA = ['token', 'sorteio']
SORTEAR_SCHEMA = ['token', 'sorteio']
LISTAR_INGRESSOS_SCHEMA = ['token', 'status']
LISTAR_SORTEIOS_SCHEMA = ['token', 'status']
CRIAR_USUARIO_SCHEMA = ['token', 'status']
