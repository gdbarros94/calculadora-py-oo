# -*- coding: utf-8 -*-
"""
Arquivo principal para iniciar a aplicação da calculadora Tkinter.
"""

import tkinter as tk
from interface import InterfaceCalculadora
from funcoes import FuncoesCalculadora

def main():
    """Função principal que configura e inicia a aplicação."""
    # Cria a janela principal da aplicação
    root = tk.Tk()
    
    # Instancia a classe com as funções lógicas da calculadora
    funcoes_calculadora = FuncoesCalculadora()
    
    # Instancia a classe da interface gráfica, passando a janela principal
    # e a instância das funções
    app = InterfaceCalculadora(root, funcoes_calculadora)
    
    # Inicia o loop principal do Tkinter, que mantém a janela aberta
    # e responsiva aos eventos do usuário
    root.mainloop()

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Chama a função principal para iniciar a aplicação
    main()

