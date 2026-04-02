# Sprint 3 Hospital São Rafael
## DYNAMIC PROGRAMMING - Recursão e Memoização
## Para acessar a documentação técnica, clique aqui no [link da documentação do projeto.](https://docs.google.com/document/d/12iFjDxmj4o4cLB6VeEuLOk47B1eSCFefqIFj37hK0GY/edit?usp=sharing)

**Turma:** 2ESPS  

**Alunos:**
- Ana Luiza Santana RM: 561194  
- Erick Cardoso RM: 560440  
- Gabrielly Candido RM: 560916  
- João Victor Ferreira RM: 560439  
- Luiza Ribeiro RM: 560200
---
##  Sobre o projeto
Este repositório contém a **Sprint 3** do Challenge do desenvolvido para o **Hospital São Rafael**


O foco desta sprint é aplicar técnicas de **programação dinâmica** para resolver dois problemas centrais:

1. **Verificação de duplicidade** ao cadastrar novos leads/pacientes
2. **Otimização de agenda médica** para maximizar o aproveitamento do tempo disponível


---

##  Estrutura do repositório

```
SPRINT3-HSR-PY/
│
├── main.py          # Ponto de entrada - executa as 3 tarefas em sequência
├── dados.py         # Médicos, leads e agendas simulados
├── recursao.py      # 1 — Verificação recursiva de duplicidade
├── memoizacao.py    # 2 — Memoização nas comparações de leads
├── agenda.py        # 3 — Otimização de agenda com subproblemas
├── utils.py         # Funções auxiliares de exibição compartilhadas
└── README.md        # Documentação do projeto
```

Cada arquivo de tarefa também pode ser executado individualmente para melhor visualização.

---

## Como executar

**Pré-requisito:** Python 3.10 ou superior

```bash
# clonar o repositório
git clone https://github.com/anarand/sprint3-hsr-dynamicprogramming
cd sprint3-hsr-dynamicprogramming

# executar o projeto completo
python main.py

# executar uma tarefa individualmente
python recursao.py
python memoizacao.py
python agenda.py
```


