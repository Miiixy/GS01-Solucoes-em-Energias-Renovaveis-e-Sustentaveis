## Global Solution 2026 – Soluções em Energias Renováveis e Sustentáveis
Global Solution FIAP

# Sistema Inteligente de Monitoramento Espacial

### Integrantes

* Mikaella Mirela Dos Santos Lucindo - RM: 573775
* Lara Dos Santos Cândido Alves - RM: 573827
* Giulliana Maistro Brasolin - RM: 569381


## Sobre o Projeto

A exploração espacial depende de sistemas capazes de monitorar continuamente as condições operacionais dos módulos da missão. Falhas relacionadas à energia, temperatura ou comunicação podem comprometer equipamentos, interromper operações e colocar toda a missão em risco.

Pensando nesse cenário, desenvolvemos um sistema inteligente de monitoramento espacial capaz de simular e analisar dados operacionais em tempo real. A solução recebe informações dos módulos da missão, identifica situações de risco, gera alertas automáticos e executa ações corretivas quando necessário.

Além dos requisitos básicos propostos no desafio, o projeto também incorpora mecanismos de análise de risco e previsão de falhas, tornando o monitoramento mais inteligente e preventivo.

## Objetivo

Desenvolver uma plataforma computacional capaz de:

* Simular dados operacionais de uma missão espacial;
* Monitorar continuamente os módulos da operação;
* Analisar condições de temperatura, energia e comunicação;
* Gerar alertas automáticos;
* Executar respostas automatizadas diante de situações críticas;
* Exibir as informações de forma organizada;
* Auxiliar na identificação preventiva de possíveis falhas.


## Funcionamento do Sistema

O sistema opera em ciclos de monitoramento.

Durante cada ciclo, dados simulados são gerados para todos os módulos da missão espacial. Essas informações são analisadas e classificadas de acordo com níveis de criticidade previamente definidos.

Após a análise, o sistema:

1. Monitora os dados recebidos;
2. Classifica as condições operacionais;
3. Gera alertas automáticos;
4. Calcula o índice de risco;
5. Realiza previsão de falhas;
6. Executa ações automáticas quando necessário;
7. Apresenta um resumo geral da missão.


## Módulos Monitorados

O sistema realiza o monitoramento dos seguintes módulos:

* Módulo Solar
* Módulo de Propulsão
* Módulo de Comunicação
* Módulo de Suporte de Vida

Cada módulo possui os seguintes parâmetros monitorados:

| Parâmetro   | Descrição                         |
| ----------- | --------------------------------- |
| Temperatura | Condição térmica do módulo        |
| Energia     | Nível de energia disponível       |
| Comunicação | Qualidade do sinal de comunicação |
| Status      | Estado operacional do módulo      |


## Classificação dos Dados

Os valores monitorados são classificados em três níveis:

### Normal

Indica que o módulo está operando dentro dos parâmetros esperados.

### Atenção

Indica uma situação que exige monitoramento mais próximo.

### Crítico

Indica uma condição de risco que pode comprometer a operação da missão.


## Sistema de Alertas

Quando uma condição anormal é detectada, o sistema gera alertas automáticos para informar o operador sobre o problema identificado.

Exemplos:

* Temperatura elevada;
* Energia em nível crítico;
* Comunicação instável;
* Módulo em falha.


## Tomada de Decisão Automática

Além de emitir alertas, o sistema também executa respostas automatizadas para reduzir os impactos dos problemas detectados.

Entre as ações implementadas estão:

* Isolamento de módulos em falha;
* Ativação do modo de economia de energia;
* Acionamento do sistema de resfriamento;
* Reinicialização do sistema de comunicação.


## Inovações Implementadas

### Índice de Risco

Como diferencial do projeto, foi desenvolvido um índice de risco para cada módulo monitorado.

Esse índice é calculado com base nos parâmetros operacionais e permite identificar rapidamente quais módulos apresentam maior criticidade.

Exemplo:

```text
Índice de Risco: 80%
```


### Previsão de Falhas

O sistema também realiza uma análise preditiva simples baseada no índice de risco calculado.

As previsões possíveis são:

* Operação Estável
* Risco de Instabilidade
* Risco Crítico de Falha
* Alta Probabilidade de Falha

Dessa forma, a solução não apenas reage aos problemas existentes, mas também auxilia na identificação antecipada de possíveis falhas futuras.


## Tecnologias Utilizadas

* Python 3
* Biblioteca Random
* Biblioteca Time


## Estrutura do Projeto

```text
projeto/
│
├── main.py    
└── README.md
```


## Como Executar

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
```

### 2. Acessar a pasta do projeto

```bash
cd projeto
```

### 3. Executar o sistema

```bash
python main.py
```

---

## Exemplo de Saída

```text
Modulo Solar | Status: ativo

Temperatura: 82.5°C [critico]
Energia: 18.0% [critico]
Comunicacao: 90.0% [normal]

[alerta critico] energia em nivel critico

Indice de Risco: 80%

Previsao: RISCO CRITICO DE FALHA

Acoes Automaticas:
-> ativar modo economia de energia
-> acionar sistema de resfriamento
```

