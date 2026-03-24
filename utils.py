"""
funções auxiliares de exibição compartilhadas entre as tarefas.
"""


def separador(titulo: str) -> None:
    """Imprime um separador visual com título."""
    largura = 62
    print(f"\n{'═' * largura}")
    print(f"  {titulo}")
    print(f"{'═' * largura}")


def exibir_resultado_duplicidade(
    encontrado: bool,
    cadastro: dict | None,
    campos: list,
    nome_lead: str,
) -> None:
    """Exibe o resultado de uma verificação de duplicidade."""
    if encontrado:
        print(f"      Lead '{nome_lead}' é DUPLICADO!⚠️")
        print(f"      Conflito com cadastro: {cadastro['nome']}")
        print(f"      Campos em conflito   : {', '.join(campos)}")
    else:
        print(f"      Lead '{nome_lead}' é NOVO — pode ser cadastrado.✅")