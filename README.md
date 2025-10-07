# Fila-de-espera-medica-Projeto.py
Um sistema em Python que simula e gerencia uma fila de atendimento médico usando uma lista duplamente encadeada, com regras de prioridade e monitoramento de memória em tempo real.

# Projeto 01 - Simulação de Fila de Espera em um Atendimento Médico

Este projeto implementa uma simulação de fila de atendimento médico utilizando uma estrutura de dados de **lista duplamente encadeada** em Python. O sistema permite gerenciar pacientes de forma interativa via terminal, respeitando regras de prioridade, e monitora o consumo de memória a cada operação.

## 👨‍💻 Integrantes do Grupo

* Luiggi Benso Cavalhieri Tavolucci - RA: 22408691
* Pedro Perçu Nazari Ribeiro reis - RA: 22401219
* Tiego de Costa Ferreira - RA: 22403192 

## ✨ Funcionalidades

-   **Estrutura de Dados**: Utilização de uma lista duplamente encadeada para máxima eficiência na manipulação dos nós (pacientes).
-   **Gerenciamento de Pacientes**:
    -   `Adicionar`: Insere pacientes na fila, posicionando prioritários (P) à frente dos normais (N).
    -   `Atender (Remover)`: Remove o próximo paciente da fila, seguindo a ordem de chegada e prioridade.
    -   `Alterar`: Permite a modificação dos dados de um paciente (nome, idade, prioridade), reposicionando-o na fila se necessário.
-   **Regra de Negócio Avançada**: Implementa a regra de alternância de chamada: quando a proporção de pacientes prioritários para normais atinge `1/7` ou mais, o sistema alterna a chamada entre eles para evitar longas esperas para os pacientes normais.
-   **Monitoramento de Memória**: Exibe o consumo de memória em bytes antes e depois de cada operação de adição, remoção ou alteração, destacando a diferença.
-   **Exibição Gráfica**: A fila é exibida de forma visual e clara no terminal, usando caracteres ASCII, com opções para visualização normal e invertida.
-   **Modo Interativo Amigável**: O usuário pode interagir com o sistema através de comandos simples no terminal, com o menu de opções sendo exibido após cada ação para facilitar o uso contínuo.

## 🚀 Como Executar

1.  **Pré-requisitos**: Ter o Python 3 instalado em sua máquina.
2.  **Clone o repositório**:
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    ```
3.  **Navegue até a pasta do projeto**:
    ```bash
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```
4.  **Execute o script**:
    ```bash
    python nome_do_arquivo.py
    ```
    O programa iniciará, carregará uma lista de 10 pacientes para teste e exibirá o menu de comandos.

## ⌨️ Comandos do Modo Interativo

Após a execução, utilize os seguintes comandos para interagir com a fila:

| Comando                          | Descrição                                                                         | Exemplo                                   |
| -------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------- |
| `add <nome> <idade> <P/N>`       | Adiciona um novo paciente na fila.                                                  | `add Ana 28 P`                            |
| `assist`                         | Atende (remove) o próximo paciente da fila.                                         | `assist`                                  |
| `edit <nome> <novo> <idade> <P/N>` | Altera os dados de um paciente existente.                                           | `edit Ana Paula 29 N`                     |
| `show`                           | Exibe a fila de atendimento na ordem correta.                                       | `show`                                    |
| `show_inverted`                  | Exibe a fila na ordem inversa.                                                      | `show_inverted`                           |
| `help`                           | Mostra esta lista de todos os comandos disponíveis.                                 | `help`                                    |
| `exit`                           | Encerra a execução do programa.                                                     | `exit`                                    |

---
