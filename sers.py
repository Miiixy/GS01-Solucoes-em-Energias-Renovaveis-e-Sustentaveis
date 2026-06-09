import random
import time
import os

os.system("cls") 

modulos = [
    "modulo solar",
    "modulo de propulsao",
    "modulo de comunicacao",
    "modulo de suporte de vida"
]

limites = {
    "temperatura": {"normal": (15, 40), "atencao": (40.1, 60), "critico": (60.1, 100)},
    "energia": {"normal": (60, 100), "atencao": (30, 59), "critico": (0, 29)},
    "comunicacao": {"normal": (70, 100), "atencao": (40, 69), "critico": (0, 39)},
}


def simular_dados_modulo(modulo):
    return {
        "modulo": modulo,
        "temperatura": round(random.uniform(10, 95), 1),
        "energia": round(random.uniform(0, 100), 1),
        "comunicacao": round(random.uniform(0, 100), 1),
        "status": random.choice(["ativo", "ativo", "ativo", "standby", "falha"]),
    }


def simular_missao():
    return [simular_dados_modulo(m) for m in modulos]


def classificar_valor(tipo, valor):
    limite = limites[tipo]

    if limite["normal"][0] <= valor <= limite["normal"][1]:
        return "normal"
    elif limite["atencao"][0] <= valor <= limite["atencao"][1]:
        return "atencao"
    else:
        return "critico"


def monitorar_modulo(dados):
    resultado = {
        "modulo": dados["modulo"],
        "status": dados["status"],
        "leituras": {}
    }

    for campo in ["temperatura", "energia", "comunicacao"]:
        valor = dados[campo]
        classificacao = classificar_valor(campo, valor)

        resultado["leituras"][campo] = {
            "valor": valor,
            "classificacao": classificacao
        }

    return resultado


def gerar_alertas(resultado):
    alertas = []
    modulo = resultado["modulo"]

    if resultado["status"] == "falha":
        alertas.append(f"[alerta critico] {modulo}: modulo em falha!")
    elif resultado["status"] == "standby":
        alertas.append(f"[aviso] {modulo}: modulo em standby.")

    mensagens = {
        "temperatura": {
            "atencao": f"[aviso] {modulo}: temperatura elevada.",
            "critico": f"[alerta critico] {modulo}: temperatura em nivel perigoso",
        },
        "energia": {
            "atencao": f"[aviso] {modulo}: nivel de energia baixo.",
            "critico": f"[alerta critico] {modulo}: energia em nivel critico",
        },
        "comunicacao": {
            "atencao": f"[aviso] {modulo}: sinal de comunicacao fraco.",
            "critico": f"[alerta critico] {modulo}: falha de comunicacao detectada",
        },
    }

    for campo, leitura in resultado["leituras"].items():
        classificacao = leitura["classificacao"]

        if classificacao in mensagens[campo]:
            alertas.append(mensagens[campo][classificacao])

    return alertas


separador = "=" * 60
separador_fino = "-" * 60

unidades = {
    "temperatura": "°C",
    "energia": "%",
    "comunicacao": "%"
}


def exibir_cabecalho():
    print(separador)
    print("      sistema de monitoramento -- missao espacial")
    print(separador)
    print("         ciclo de monitoramento iniciado...\n")


def exibir_modulo(resultado, alertas):
    modulo = resultado["modulo"]
    status = resultado["status"]

    print(separador_fino)
    time.sleep(0.5)

    print(f"             {modulo} | status: {status}")
    time.sleep(0.5)

    print(separador_fino)
    time.sleep(0.5)

    for campo, leitura in resultado["leituras"].items():
        valor = leitura["valor"]
        classificacao = leitura["classificacao"]
        unidade = unidades[campo]

        print(f"  {campo:<15} {valor:>6}{unidade}   [{classificacao}]")
        time.sleep(0.5)

    if alertas:
        print("\nAnalisando situacao do modulo...")
        time.sleep(1)

        print()

        for alerta in alertas:
            print(f"  {alerta}")
            time.sleep(0.8)

    print()


def exibir_resumo(todos_alertas):
    total = sum(len(a) for a in todos_alertas)
    criticos = sum(
        1 for lista in todos_alertas for a in lista if "critico" in a
    )
    avisos = sum(
        1 for lista in todos_alertas for a in lista if "aviso" in a
    )

    print(separador)
    print("resumo do ciclo de monitoramento")
    print(separador)

    print(f"  total de alertas gerados : {total}")
    print(f"  alertas criticos         : {criticos}")
    print(f"  avisos                   : {avisos}")

    if criticos > 0:
        print("\n  acao recomendada: verificar modulos em estado critico!")
    elif avisos > 0:
        print("\n  acao recomendada: monitorar modulos em atencao.")
    else:
        print("\n  missao operando dentro dos parametros normais.")

    print(separador)


def tomar_decisao(resultado):
    acoes = []

    if resultado["status"] == "falha":
        acoes.append("isolar modulo")

    if resultado["leituras"]["energia"]["classificacao"] == "critico":
        acoes.append("ativar modo economia de energia")

    if resultado["leituras"]["temperatura"]["classificacao"] == "critico":
        acoes.append("acionar sistema de resfriamento")

    if resultado["leituras"]["comunicacao"]["classificacao"] == "critico":
        acoes.append("reiniciar sistema de comunicacao")

    return acoes


def prever_falha(risco):
    if risco >= 90:
        return "ALTA PROBABILIDADE DE FALHA"
    elif risco >= 70:
        return "RISCO CRITICO DE FALHA"
    elif risco >= 40:
        return "RISCO DE INSTABILIDADE"
    else:
        return "OPERACAO ESTAVEL"


def calcular_risco(resultado):
    risco = 0

    for leitura in resultado["leituras"].values():
        if leitura["classificacao"] == "atencao":
            risco += 20
        elif leitura["classificacao"] == "critico":
            risco += 40

    if resultado["status"] == "falha":
        risco += 30

    return min(risco, 100)


def executar_ciclo():
    exibir_cabecalho()

    dados_missao = simular_missao()
    todos_alertas = []

    for dados in dados_missao:
        resultado = monitorar_modulo(dados)

        alertas = gerar_alertas(resultado)
        acoes = tomar_decisao(resultado)

        risco = calcular_risco(resultado)
        previsao = prever_falha(risco)

        todos_alertas.append(alertas)

        exibir_modulo(resultado, alertas)

        print(f"indice de risco: {risco}%")
        print(f"previsao: {previsao}")

        if acoes:
            print("acoes automaticas:")

            for acao in acoes:
                print(f"  -> {acao}")

            print()

    exibir_resumo(todos_alertas)


if __name__ == "__main__":
    ciclos = 3
    intervalo = 2

    for i in range(1, ciclos + 1):
        print(f"\n{'*' * 60}")
        print(
            f"*                      ciclo {i} de {ciclos}                        *")
        print(f"{'*' * 60}")

        executar_ciclo()

        if i < ciclos:
            print(f"\n  proximo ciclo em {intervalo} segundos...\n")
            time.sleep(intervalo)

    print("\n  monitoramento encerrado.\n")
