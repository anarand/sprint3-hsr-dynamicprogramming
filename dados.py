"""
Dados de exemplo que simulam o banco de dados do CRM.
"""

# médicos

medicos = [
    {
        "nome": "Dr. Fernando Alves",
        "crm": "BA-12345",
        "especialidade": "Aparelho Digestivo",
        "email": "fernando.alves@hsrafael.com.br",
        "telefone": "71991110001",
    },
    {
        "nome": "Dra. Camila Duarte",
        "crm": "BA-23456",
        "especialidade": "Cirurgia Plástica",
        "email": "camila.duarte@hsrafael.com.br",
        "telefone": "71991110002",
    },
    {
        "nome": "Dr. Henrique Bastos",
        "crm": "BA-34567",
        "especialidade": "Dermatologia",
        "email": "henrique.bastos@hsrafael.com.br",
        "telefone": "71991110003",
    },
    {
        "nome": "Dra. Patrícia Nunes",
        "crm": "BA-45678",
        "especialidade": "Ginecologia",
        "email": "patricia.nunes@hsrafael.com.br",
        "telefone": "71991110004",
    },
    {
        "nome": "Dra. Renata Leal",
        "crm": "BA-56789",
        "especialidade": "Nutrição",
        "email": "renata.leal@hsrafael.com.br",
        "telefone": "71991110005",
    },
    {
        "nome": "Dr. Gustavo Meira",
        "crm": "BA-67890",
        "especialidade": "Ortopedia",
        "email": "gustavo.meira@hsrafael.com.br",
        "telefone": "71991110006",
    },
]

# cadastros existentes

cadastros_existentes = [
    {
        "nome": "Ana Clara Souza",
        "cpf": "111.111.111-11",
        "email": "anaclarasouza@gmail.com",
        "telefone": "71988880001",
        "canal": "Instagram",
        "procedimento": "Consulta Dermatologia",
    },
    {
        "nome": "Bruno Ferreira",
        "cpf": "222.222.222-22",
        "email": "brunoferreira@outlook.com",
        "telefone": "71988880002",
        "canal": "Google",
        "procedimento": "Consulta Ortopedia",
    },
    {
        "nome": "Carla Mendonça",
        "cpf": "333.333.333-33",
        "email": "carlamendonca@gmail.com",
        "telefone": "71988880003",
        "canal": "Facebook",
        "procedimento": "Consulta Ginecologia",
    },
    {
        "nome": "Diego Santana",
        "cpf": "444.444.444-44",
        "email": "diegosantana@hotmail.com",
        "telefone": "71988880004",
        "canal": "TikTok",
        "procedimento": "Consulta Aparelho Digestivo",
    },
    {
        "nome": "Eduarda Lima",
        "cpf": "555.555.555-55",
        "email": "eduardalima@gmail.com",
        "telefone": "71988880005",
        "canal": "Google",
        "procedimento": "Consulta Nutrição",
    },
    {
        "nome": "Felipe Rocha",
        "cpf": "666.666.666-66",
        "email": "feliperocha@gmail.com",
        "telefone": "71988880006",
        "canal": "Instagram",
        "procedimento": "Consulta Cirurgia Plástica",
    },
]

# novos leads chegando

# lead duplicado - já existe (mesmo e-mail, CPF e telefone)
lead_duplicado = {
    "nome": "Bruno Ferreira",
    "cpf": "222.222.222-22",
    "email": "brunoferreira@outlook.com",
    "telefone": "71988880002",
    "canal": "TikTok",               # veio por canal diferente desta vez
    "procedimento": "Consulta Ortopedia",
}

# lead novo
lead_novo = {
    "nome": "Gabriela Teixeira",
    "cpf": "777.777.777-77",
    "email": "gabrielateixeira@gmail.com",
    "telefone": "71988880099",
    "canal": "Instagram",
    "procedimento": "Consulta Cirurgia Plástica",
}


# AGENDAS MÉDICAS - tempo disponível e tipos de consulta (minutos)

agendas_medicos = [
    {
        "medico": "Dr. Fernando Alves — Aparelho Digestivo",
        "tempo_disponivel_min": 480,   # 8 h
        "tipos_consulta_min": [30, 60],
    },
    {
        "medico": "Dra. Camila Duarte — Cirurgia Plástica",
        "tempo_disponivel_min": 360,   # 6 h (consultas pré-op mais longas)
        "tipos_consulta_min": [45, 90],
    },
    {
        "medico": "Dr. Henrique Bastos — Dermatologia",
        "tempo_disponivel_min": 300,   # 5 h
        "tipos_consulta_min": [20, 30],
    },
    {
        "medico": "Dra. Patrícia Nunes — Ginecologia",
        "tempo_disponivel_min": 420,   # 7 h
        "tipos_consulta_min": [30, 45],
    },
    {
        "medico": "Dra. Renata Leal — Nutrição",
        "tempo_disponivel_min": 240,   # 4 h
        "tipos_consulta_min": [40, 60],
    },
    {
        "medico": "Dr. Gustavo Meira — Ortopedia",
        "tempo_disponivel_min": 360,   # 6 h
        "tipos_consulta_min": [30, 45, 60],
    },
]