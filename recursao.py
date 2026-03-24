"""
1 — Verificação Recursiva de Duplicidade 

Descrição:
    Quando um novo lead chega ao CRM (via Instagram, Tiktok etc.),
    o sistema precisa garantir que ele ainda não está cadastrado.
    Esta tarefa implementa essa verificação de forma RECURSIVA,
    comparando o lead com cada cadastro existente pelos campos:
    nome, telefone, e-mail e CPF.
"""

# Campos considerados para identificar duplicidade
CAMPOS_VERIFICACAO = ["nome", "telefone", "email", "cpf"]


def _campos_em_comum(lead: dict, cadastro: dict) -> list:
    """
    Retorna os campos com valor idêntico entre lead e cadastro.

    Args:
        lead    : dicionário do novo lead
        cadastro: dicionário de um cadastro existente

    Returns:
        list[str]: nomes dos campos com valores iguais
    """
    return [
        campo
        for campo in CAMPOS_VERIFICACAO
        if lead.get(campo) and lead.get(campo) == cadastro.get(campo)
    ]


def verificar_duplicidade_recursiva(
    novo_lead: dict,
    cadastros: list,
    indice: int = 0,
) -> tuple:
    """
    Verifica recursivamente se um novo lead já existe na base.

    Estratégia:
        Caso base : indice >= len(cadastros) → nenhuma duplicata encontrada
        Passo     : compara o lead com cadastros[indice]
                    › Se houver campo em comum → duplicata, para a recursão
                    › Caso contrário           → avança para indice + 1

    Complexidade:
        Tempo : O(n · k)  — n cadastros, k campos verificados
        Espaço: O(n)      — profundidade máxima da pilha de recursão

    Args:
        novo_lead : dicionário com os dados do novo lead
        cadastros : lista de cadastros já existentes no sistema
        indice    : posição atual na lista (não informar na chamada inicial)

    Returns:
        tuple(bool, dict | None, list[str]):
            [0] True se duplicata encontrada, False caso contrário
            [1] Cadastro conflitante (ou None)
            [2] Lista de campos duplicados (ou lista vazia)
    """
    #  Caso base: percorreu toda a lista sem encontrar duplicata 
    if indice >= len(cadastros):
        return False, None, []

    cadastro_atual = cadastros[indice]
    campos_dup = _campos_em_comum(novo_lead, cadastro_atual)

    #  Duplicata encontrada: interrompe a recursão 
    if campos_dup:
        return True, cadastro_atual, campos_dup

    # Chamada recursiva para o próximo cadastro 
    return verificar_duplicidade_recursiva(novo_lead, cadastros, indice + 1)



# DEMONSTRAÇÃO ISOLADA

if __name__ == "__main__":
    from dados import cadastros_existentes, lead_duplicado, lead_novo
    from utils import separador, exibir_resultado_duplicidade

    separador("Verificação Recursiva de Duplicidade")

    print("\n Verificando lead DUPLICADO (Bruno Ferreira):")
    enc, cad, cam = verificar_duplicidade_recursiva(lead_duplicado, cadastros_existentes)
    exibir_resultado_duplicidade(enc, cad, cam, lead_duplicado["nome"])

    print("\n Verificando lead NOVO (Gabriela Teixeira):")
    enc2, cad2, cam2 = verificar_duplicidade_recursiva(lead_novo, cadastros_existentes)
    exibir_resultado_duplicidade(enc2, cad2, cam2, lead_novo["nome"])