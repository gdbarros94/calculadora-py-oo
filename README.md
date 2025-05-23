# Calculadora Tkinter em Python

Este repositório contém o código-fonte de uma calculadora de desktop desenvolvida em Python utilizando a biblioteca Tkinter para a interface gráfica. O projeto foi estruturado de forma modular, separando a lógica de cálculo, a interface do usuário e o ponto de entrada da aplicação, visando facilitar o entendimento e a manutenção.

## Visão Geral

A calculadora oferece funcionalidades básicas e algumas operações científicas, além de recursos de memória. A interface foi projetada para ser intuitiva e visualmente agradável.

## Funcionalidades

*   **Operações Básicas:** Adição (+), Subtração (-), Multiplicação (*), Divisão (/).
*   **Operações Científicas:** Raiz Quadrada (√), Potência ao Quadrado (x²), Inverso (1/x), Seno (sin), Cosseno (cos), Tangente (tan), Logaritmo base 10 (log), Logaritmo Natural (ln).
*   **Funções de Memória:** Limpar Memória (MC), Recuperar Memória (MR), Adicionar à Memória (M+), Subtrair da Memória (M-), Salvar na Memória (MS - funciona como M+ neste exemplo).
*   **Controle:** Limpar Entrada Atual (CE), Limpar Tudo (C), Inverter Sinal (±).
*   **Parênteses:** Suporte básico para agrupar operações.
*   **Display:** Exibe a entrada atual e os resultados.

## Estrutura do Projeto

O código está organizado nos seguintes arquivos:

*   `main.py`: Ponto de entrada da aplicação. Responsável por instanciar as classes necessárias e iniciar a interface gráfica.
*   `interface.py`: Contém a classe `InterfaceCalculadora`, que define todos os elementos visuais da calculadora (janela, display, botões) usando Tkinter e gerencia a interação do usuário.
*   `funcoes.py`: Contém a classe `FuncoesCalculadora`, que encapsula toda a lógica de cálculo, incluindo a avaliação de expressões, funções matemáticas e operações de memória.

```
calculadora_tkinter/
├── funcoes.py
├── interface.py
└── main.py
```

## Como Executar

1.  **Pré-requisitos:** Certifique-se de ter o Python 3 instalado em seu sistema. Tkinter geralmente já vem incluído na instalação padrão do Python.
2.  **Clone o Repositório (Opcional):** Se estiver usando Git, clone este repositório:
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd calculadora_tkinter
    ```
3.  **Descompacte (se baixou o ZIP):** Se você baixou o arquivo `.zip`, descompacte-o.
4.  **Navegue até a Pasta:** Abra um terminal ou prompt de comando e navegue até o diretório onde os arquivos `.py` estão localizados (a pasta `calculadora_tkinter`).
5.  **Execute o Script Principal:**
    ```bash
    python main.py
    ```
    ou, dependendo da sua configuração:
    ```bash
    python3 main.py
    ```

A janela da calculadora deverá aparecer.

## Observações

*   A avaliação da expressão matemática (`eval`) em `funcoes.py` foi implementada com algumas medidas de segurança, mas o uso de `eval` com entrada do usuário pode ser arriscado em aplicações reais. Para fins didáticos, ele simplifica o processo de cálculo.
*   A lógica de tratamento de entrada e cálculo pode ser aprimorada para lidar com casos de uso mais complexos e fornecer feedback de erro mais detalhado.
*   O estilo visual pode ser customizado alterando as cores, fontes e layout no arquivo `interface.py`.

## Contribuição

Este projeto foi criado como um exemplo didático. Sinta-se à vontade para fazer fork, modificar e experimentar!

