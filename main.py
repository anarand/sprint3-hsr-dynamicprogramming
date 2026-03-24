
import time

from dados import cadastros_existentes, lead_duplicado, lead_novo, agendas_medicos
from recursao import verificar_duplicidade_recursiva
from memoizacao import verificar_duplicidade_memoizado, info_cache
from agenda import otimizar_agenda_medico, _melhor_encaixe
from utils import separador, exibir_resultado_duplicidade


def main():

    # ──────────────────────────────────────────────────────────────
    # Recursão simples
    # ──────────────────────────────────────────────────────────────
    separador("Verificação Recursiva de Duplicidade")

    print("\n▶ Verificando lead DUPLICADO (Bruno Ferreira):")
    enc, cad, cam = verificar_duplicidade_recursiva(lead_duplicado, cadastros_existentes)
    exibir_resultado_duplicidade(enc, cad, cam, lead_duplicado["nome"])

    print("\n▶ Verificando lead NOVO (Gabriela Teixeira):")
    enc2, cad2, cam2 = verificar_duplicidade_recursiva(lead_novo, cadastros_existentes)
    exibir_resultado_duplicidade(enc2, cad2, cam2, lead_novo["nome"])

    # ──────────────────────────────────────────────────────────────
    # Memoização
    # ──────────────────────────────────────────────────────────────
    separador("Verificação com Memoização")

    print("\n▶ 1ª verificação do lead DUPLICADO (cache ainda vazio):")
    enc3, cad3, cam3 = verificar_duplicidade_memoizado(lead_duplicado, cadastros_existentes)
    exibir_resultado_duplicidade(enc3, cad3, cam3, lead_duplicado["nome"])

    print("\n▶ 2ª verificação do MESMO lead (todos os pares devem vir do cache):")
    enc4, _, _ = verificar_duplicidade_memoizado(lead_duplicado, cadastros_existentes)
    print(f"   Resultado consistente: {'DUPLICADO' if enc4 else 'NOVO'}")

    print("\n▶ Verificando lead NOVO com memoização:")
    enc5, cad5, cam5 = verificar_duplicidade_memoizado(lead_novo, cadastros_existentes)
    exibir_resultado_duplicidade(enc5, cad5, cam5, lead_novo["nome"])

    stats = info_cache()
    print(f"\n  Total de entradas no cache: {stats['entradas_no_cache']}")

    # Otimização de agenda
    separador("Otimização de Agenda com Subproblemas")

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

    # Benchmark
    print("\n Benchmark — impacto do @lru_cache:")
    _melhor_encaixe.cache_clear()

    t0 = time.perf_counter()
    _melhor_encaixe(480, (30, 45, 60))
    t1 = time.perf_counter()
    print(f"     1ª chamada (sem cache): {(t1 - t0) * 1000:.4f} ms")

    t2 = time.perf_counter()
    _melhor_encaixe(480, (30, 45, 60))
    t3 = time.perf_counter()
    print(f"     2ª chamada (com cache): {(t3 - t2) * 1000:.4f} ms")
    print(f"     Info cache            : {_melhor_encaixe.cache_info()}")


if __name__ == "__main__":
    main()