# Sprint 3 Hospital São Rafael: Recursão e Memoização no CRM
> ## DYNAMIC PROGRAMMING
> TURMA: 2ESPS
> ALUNOS:

Ana Luiza Santana RM: 561194

Erick Cardoso RM: 560440

Gabrielly Candido RM: 560916

João Victor Ferreira RM: 560439

Luiza Ribeiro RM: 560200
---

##  Sobre o projeto

Este repositório contém a **Sprint 3** do Challenge do desenvolvimento de um CRM para o **Hospital São Rafael**


O foco desta sprint é aplicar técnicas de **programação dinâmica** para resolver dois problemas centrais do sistema:

1. **Verificação de duplicidade** ao cadastrar novos leads/pacientes
2. **Otimização de agenda médica** para maximizar o aproveitamento do tempo disponível


---

##  Conceitos de Dynamic Programming aplicados

| Conceito | Onde é usado |
|---|---|
| **Recursão** - Percorre a lista de cadastros comparando lead a lead
| **Memoização manual** (`dict`) | Cache de comparações entre pares (lead × cadastro) 
| **`@lru_cache`** - Cache automático do Python na otimização de agenda
| **Unbounded Knapsack** - Modelo para encaixar consultas no tempo disponível 

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
└── README.md
```

> Cada arquivo de tarefa também pode ser executado individualmente para melhor visualização.

---

## Como executar

**Pré-requisito:** Python 3.10 ou superior

```bash
# clonar o repositório
git clone https://github.com/seu-usuario/SPRINT3-HSR-PY.git
cd SPRINT3-HSR-PY

# executar o projeto completo
python main.py

# executar uma tarefa individualmente
python recursao.py
python memoizacao.py
python agenda.py
```

---

## Tarefas Implementadas

---

### Tarefa 1 — Verificação Recursiva de Duplicidade
**Arquivo:** `recursao.py`

Quando um novo lead chega ao CRM, o sistema precisa verificar se ele já existe na base. A comparação considera quatro campos: `nome`, `telefone`, `email` e `cpf`.

**Fluxo da recursão:**

```
verificar_duplicidade_recursiva(lead, cadastros, indice=0)
 │
 ├─ Caso base: indice >= len(cadastros)
 │   └─ Retorna (False, None, [])  ← nenhuma duplicata encontrada
 │
 ├─ Compara lead com cadastros[indice] campo a campo
 │   └─ Se houver campo em comum → retorna (True, cadastro, campos)
 │
 └─ Chamada recursiva com indice + 1
```

**Exemplo de uso:**

```python
enc, cadastro, campos = verificar_duplicidade_recursiva(novo_lead, cadastros_existentes)

# Lead duplicado
# → (True, {...}, ["nome", "telefone", "email", "cpf"])

# Lead novo
# → (False, None, [])
```

**Complexidade:**
- Tempo: `O(n · k)` — n cadastros, k campos verificados por par
- Espaço: `O(n)` — profundidade máxima da pilha de recursão

---

### Tarefa 2 — Memoização na Comparação de Leads
**Arquivo:** `memoizacao.py`

Em um CRM ativo, o mesmo lead pode ser consultado várias vezes — por operadores diferentes, em reentradas por outro canal ou em reprocessamentos. Esta tarefa adiciona um cache manual (`dict`) sobre a recursão da Tarefa 1: cada par *(lead × cadastro)* é comparado no máximo uma vez.

**Funcionamento do cache:**

```python
_cache_comparacoes: dict = {}

# Chave: (email_lead, email_cadastro)
cache_key = (_chave(lead), _chave(cadastro))

if cache_key in _cache_comparacoes:
    return _cache_comparacoes[cache_key]   # ← CACHE HIT

resultado = _campos_em_comum(lead, cadastro)
_cache_comparacoes[cache_key] = resultado  # ← armazena para próximas chamadas
return resultado
```

**Saída ao executar:**

```
▶ 1ª verificação (cache vazio):
    [CALCULADO]  brunoferreira@outlook.com × anaclarasouza@gmail.com    → armazenado
    [CALCULADO]  brunoferreira@outlook.com × brunoferreira@outlook.com  → armazenado

▶ 2ª verificação do mesmo lead:
    [CACHE HIT]  brunoferreira@outlook.com × anaclarasouza@gmail.com    → recuperado
    [CACHE HIT]  brunoferreira@outlook.com × brunoferreira@outlook.com  → recuperado
```

**Vantagem prática:** Em um sistema com centenas de leads e acessos repetidos, o cache elimina comparações redundantes e reduz o tempo de resposta progressivamente conforme o volume cresce.

---

### Tarefa 3 — Otimização de Agenda com Subproblemas
**Arquivo:** `agenda.py`

Dado o tempo disponível de um médico em um dia e os tipos de consulta possíveis, o sistema calcula o encaixe que **maximiza o tempo aproveitado** — sem recalcular os mesmos subproblemas.

**Modelagem — Unbounded Knapsack Problem:**

| Problema clássico | Nossa adaptação |
|---|---|
| Capacidade da mochila | Tempo disponível (minutos) |
| Itens disponíveis | Tipos de consulta |
| Valor de cada item | Própria duração em minutos |
| Repetição de itens | ✅ Sim — o mesmo tipo pode repetir |
| Objetivo | Maximizar minutos aproveitados |

**Recorrência:**

```
f(t, duracoes) = max(
    f(t, duracoes[1:]),                      # não usa o tipo atual
    dur[0] + f(t - dur[0], duracoes)         # usa o tipo atual (pode repetir)
)

Caso base: t ≤ 0 ou duracoes vazia → 0
```

**Memoização com `@lru_cache`:**

O decorador armazena automaticamente cada combinação `(tempo_restante, duracoes)` já calculada. Como `duracoes` é uma `tuple` (imutável e hashável), é compatível com o cache nativo do Python.

```python
@lru_cache(maxsize=None)
def _melhor_encaixe(tempo_restante: int, duracoes: tuple) -> int:
    ...
```

Sem memoização, a recursão recalcularia os mesmos subproblemas exponencialmente. Com ela, a complexidade cai para `O(T × D)`.

**Exemplo de saída:**

```
    Dr. Gustavo Meira — Ortopedia
   Tempo disponível : 360 min
   Tipos de consulta: [30, 45, 60] min
   Tempo aproveitado: 360 min
   Tempo ocioso     : 0 min
   Eficiência       : 100.0%

    Benchmark:
   1ª chamada (sem cache): 0.0455 ms
   2ª chamada (com cache): 0.0004 ms  ← ~100x mais rápido
```

**Complexidade com memoização:**
- Tempo: `O(T · D)` — T = tempo total em minutos, D = tipos de consulta
- Espaço: `O(T · D)` — tamanho do cache

---

## Conexão com o CRM Completo

| Funcionalidade do CRM | Sprint relacionada |
|---|---|
| Restrição de Duplicidade (leads, pacientes, médicos) | Tarefas 1 e 2 |
| Agendamento e controle de ociosidade médica | Tarefa 3 |
| Performance de Atendimento (tempo de resposta) | Benefício indireto da memoização |

---

