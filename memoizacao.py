"""
Memoização na Comparação de Leads 

Descrição:
    Em um CRM ativo, o mesmo lead pode ser verificado várias vezes
    (diferentes operadores, reentradas por outro canal etc.).
    Esta tarefa adiciona um cache manual sobre a recursão da Tarefa 1:
    cada par (lead, cadastro) é comparado no máximo UMA vez.
    Nas chamadas seguintes, o resultado é retornado diretamente do cache.
"""

from recursao import _campos_em_comum

# Cache manual: (chave_lead, chave_cadastro) → lista de campos duplicados
_cache_comparacoes: dict = {}


def _chave(registro: dict) -> str:
    """
    Gera uma chave única para um registro.
    Prioriza e-mail; usa CPF como fallback.
    """
    return registro.get("email") or registro.get("cpf", "desconhecido")


def _comparar_com_memo(lead: dict, cadastro: dict) -> list:
    """
    Compara lead e cadastro com memoização.

    Na primeira chamada para um par: calcula e armazena no cache.
    Nas chamadas seguintes para o mesmo par: retorna do cache.

    Args:
        lead    : dicionário do novo lead
        cadastro: dicionário de um cadastro existente

    Returns:
        list[str]: campos duplicados (pode ser vazia)
    """
    cache_key = (_chave(lead), _chave(cadastro))

    if cache_key in _cache_comparacoes:
        print(
            f"    [CACHE HIT]  {cache_key[0][:28]:<28}"
            f" × {cache_key[1][:28]} → recuperado do cache"
        )
        return _cache_comparacoes[cache_key]

    resultado = _campos_em_comum(lead, cadastro)
    _cache_comparacoes[cache_key] = resultado
    print(
        f"    [CALCULADO]  {cache_key[0][:28]:<28}"
        f" × {cache_key[1][:28]} → armazenado no cache"
    )
    return resultado


def verificar_duplicidade_memoizado(
    novo_lead: dict,
    cadastros: list,
    indice: int = 0,
) -> tuple:
    """
    Versão memoizada da verificação de duplicidade (Tarefa 1 + cache).

    Combina recursão com cache manual: cada par (lead, cadastro)
    é processado no máximo uma vez, mesmo em verificações repetidas.

    Args:
        novo_lead : dicionário com os dados do novo lead
        cadastros : lista de cadastros existentes
        indice    : posição atual (não informar na chamada inicial)

    Returns:
        tuple(bool, dict | None, list[str]): igual à Tarefa 1
    """
    if indice >= len(cadastros):
        return False, None, []

    cadastro_atual = cadastros[indice]
    campos_dup = _comparar_com_memo(novo_lead, cadastro_atual)

    if campos_dup:
        return True, cadastro_atual, campos_dup

    return verificar_duplicidade_memoizado(novo_lead, cadastros, indice + 1)


def info_cache() -> dict:
    """Retorna estatísticas do cache atual."""
    return {
        "entradas_no_cache": len(_cache_comparacoes),
        "pares_analisados": list(_cache_comparacoes.keys()),
    }



# DEMONSTRAÇÃO ISOLADA

if __name__ == "__main__":
    from dados import cadastros_existentes, lead_duplicado, lead_novo
    from utils import separador, exibir_resultado_duplicidade

    separador("Verificação com Memoização")

    print("\n▶ 1ª verificação do lead DUPLICADO (cache ainda vazio):")
    enc, cad, cam = verificar_duplicidade_memoizado(lead_duplicado, cadastros_existentes)
    exibir_resultado_duplicidade(enc, cad, cam, lead_duplicado["nome"])

    print("\n▶ 2ª verificação do MESMO lead (deve usar cache em todos os pares):")
    enc2, _, _ = verificar_duplicidade_memoizado(lead_duplicado, cadastros_existentes)
    print(f" Resultado consistente: {'DUPLICADO' if enc2 else 'NOVO'}")

    print("\n▶ Verificando lead NOVO (Gabriela Teixeira):")
    enc3, cad3, cam3 = verificar_duplicidade_memoizado(lead_novo, cadastros_existentes)
    exibir_resultado_duplicidade(enc3, cad3, cam3, lead_novo["nome"])

    stats = info_cache()
    print(f"\n  Total de entradas no cache: {stats['entradas_no_cache']}")