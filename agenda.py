"""
3 — Otimização de Agenda com Subproblemas

Descrição:
    Dado o tempo disponível de um médico em um dia e os tipos de
    consulta possíveis (em minutos), calcular o encaixe que maximiza
    o tempo aproveitado — sem recalcular os mesmos subproblemas.

Modelagem — Unbounded Knapsack Problem:
    ┌─────────────────────────────┬──────────────────────────────┐
    │ Problema clássico           │ Nossa adaptação              │
    ├─────────────────────────────┼──────────────────────────────┤
    │ Capacidade da mochila       │ Tempo disponível (minutos)   │
    │ Itens                       │ Tipos de consulta            │
    │ Valor do item               │ Própria duração em minutos   │
    │ Repetição de itens          │ Sim (mesma duração pode      │
    │                             │  repetir várias vezes)       │
    │ Objetivo                    │ Maximizar minutos usados     │
    └─────────────────────────────┴──────────────────────────────┘

Recorrência:
    f(t, duracoes) = max(
        f(t, duracoes[1:]),               # não usa o tipo atual
        dur[0] + f(t - dur[0], duracoes)  # usa o tipo atual (repetível)
    )
    Caso base: t <= 0 ou duracoes vazia → 0
"""

import time
from functools import lru_cache


@lru_cache(maxsize=None)
def _melhor_encaixe(tempo_restante: int, duracoes: tuple) -> int:
    """
    Calcula recursivamente o máximo de minutos aproveitáveis.

    O decorador @lru_cache armazena automaticamente cada combinação
    (tempo_restante, duracoes) já calculada. Como `duracoes` é uma
    tupla (imutável e hashável), é compatível com o cache.

    Complexidade com memoização:
        Tempo : O(T · D)  — T = tempo total, D = tipos de consulta
        Espaço: O(T · D)  — tamanho do cache

    Args:
        tempo_restante: minutos ainda disponíveis na agenda
        duracoes      : tupla com as durações de consulta possíveis

    Returns:
        int: máximo de minutos que podem ser preenchidos
    """
    # Caso base
    if tempo_restante <= 0 or not duracoes:
        return 0

    duracao_atual = duracoes[0]
    resto_tipos   = duracoes[1:]

    # Opção A: não usar este tipo de consulta
    sem_este_tipo = _melhor_encaixe(tempo_restante, resto_tipos)

    # Opção B: usar este tipo (se couber no tempo restante)
    com_este_tipo = 0
    if duracao_atual <= tempo_restante:
        com_este_tipo = duracao_atual + _melhor_encaixe(
            tempo_restante - duracao_atual,
            duracoes,      # mesmo conjunto — tipo pode repetir
        )

    return max(sem_este_tipo, com_este_tipo)


def otimizar_agenda_medico(
    medico: str,
    tempo_disponivel_min: int,
    tipos_consulta_min: list,
) -> dict:
    """
    Calcula o melhor aproveitamento de agenda para um médico em um dia.

    Args:
        medico              : nome/especialidade do médico
        tempo_disponivel_min: total de minutos disponíveis no dia
        tipos_consulta_min  : lista com as durações possíveis de consulta

    Returns:
        dict com métricas de aproveitamento:
            - medico
            - tempo_disponivel_min
            - tipos_consulta_min
            - tempo_aproveitado_min
            - tempo_ocioso_min
            - eficiencia_pct
    """
    duracoes = tuple(sorted(set(tipos_consulta_min)))
    tempo_aproveitado = _melhor_encaixe(tempo_disponivel_min, duracoes)
    tempo_ocioso      = tempo_disponivel_min - tempo_aproveitado
    eficiencia        = (
        round((tempo_aproveitado / tempo_disponivel_min) * 100, 2)
        if tempo_disponivel_min > 0 else 0.0
    )

    return {
        "medico"               : medico,
        "tempo_disponivel_min" : tempo_disponivel_min,
        "tipos_consulta_min"   : list(duracoes),
        "tempo_aproveitado_min": tempo_aproveitado,
        "tempo_ocioso_min"     : tempo_ocioso,
        "eficiencia_pct"       : eficiencia,
    }



# DEMONSTRAÇÃO ISOLADA

if __name__ == "__main__":
    from dados import agendas_medicos
    from utils import separador

    separador("TAREFA 3 — Otimização de Agenda com Subproblemas")

    for agenda in agendas_medicos:
        resultado = otimizar_agenda_medico(
            agenda["medico"],
            agenda["tempo_disponivel_min"],
            agenda["tipos_consulta_min"],
        )
        print(f"\n   {resultado['medico']}")
        print(f"     Tempo disponível : {resultado['tempo_disponivel_min']} min")
        print(f"     Tipos de consulta: {resultado['tipos_consulta_min']} min")
        print(f"     Tempo aproveitado: {resultado['tempo_aproveitado_min']} min")
        print(f"     Tempo ocioso     : {resultado['tempo_ocioso_min']} min")
        print(f"     Eficiência       : {resultado['eficiencia_pct']}%")

    # ── Benchmark: impacto do lru_cache ──
    print("\n   Benchmark — impacto do @lru_cache:")
    _melhor_encaixe.cache_clear()

    t0 = time.perf_counter()
    _melhor_encaixe(480, (30, 45, 60))
    t1 = time.perf_counter()
    print(f"     1ª chamada (sem cache): {(t1 - t0) * 1000:.4f} ms")

    t2 = time.perf_counter()
    _melhor_encaixe(480, (30, 45, 60))
    t3 = time.perf_counter()
    print(f"     2ª chamada (com cache): {(t3 - t2) * 1000:.4f} ms")
    print(f"     Info cache: {_melhor_encaixe.cache_info()}")