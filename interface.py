# -*- coding: utf-8 -*-
"""
Arquivo contendo a interface gráfica da calculadora usando Tkinter.
"""

import tkinter as tk
from tkinter import font
from funcoes import FuncoesCalculadora

class InterfaceCalculadora:
    """Classe que define a interface gráfica da calculadora."""

    def __init__(self, master, funcoes_calc):
        """Inicializa a interface gráfica."""
        self.master = master
        self.funcoes_calc = funcoes_calc
        self.expressao_atual = ""
        self.limpar_proximo_digito = False # Flag para limpar display após operador ou igual

        master.title("Calculadora Tkinter")
        master.geometry("400x600") # Tamanho inicial da janela
        master.resizable(False, False) # Impede redimensionamento
        master.configure(bg="#2E2E2E") # Cor de fundo da janela

        # Configuração de fontes
        self.fonte_display = font.Font(family="Segoe UI", size=28, weight="bold")
        self.fonte_botoes = font.Font(family="Segoe UI", size=14)
        self.fonte_botoes_especiais = font.Font(family="Segoe UI", size=12)

        # --- Display ---        
        self.frame_display = tk.Frame(master, bg="#2E2E2E")
        self.frame_display.pack(pady=20, padx=10, fill=tk.X)

        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.display_label = tk.Label(self.frame_display, 
                                      textvariable=self.display_var, 
                                      font=self.fonte_display, 
                                      anchor="e", 
                                      bg="#4A4A4A", 
                                      fg="#FFFFFF",
                                      padx=15,
                                      pady=10,
                                      borderwidth=2,
                                      relief="sunken")
        self.display_label.pack(fill=tk.X)

        # --- Botões ---        
        self.frame_botoes = tk.Frame(master, bg="#2E2E2E")
        self.frame_botoes.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Definição dos botões (texto, linha, coluna, [colspan], [sticky], [cor_fundo], [cor_texto], [fonte])
        botoes = [
            # Linha 0 (Funções científicas/memória)
            ("MC", 0, 0, 1, "nsew", "#555555", "#FFFFFF", self.fonte_botoes_especiais), 
            ("MR", 0, 1, 1, "nsew", "#555555", "#FFFFFF", self.fonte_botoes_especiais), 
            ("M+", 0, 2, 1, "nsew", "#555555", "#FFFFFF", self.fonte_botoes_especiais), 
            ("M-", 0, 3, 1, "nsew", "#555555", "#FFFFFF", self.fonte_botoes_especiais), 
            ("MS", 0, 4, 1, "nsew", "#555555", "#FFFFFF", self.fonte_botoes_especiais), # MS (Memory Store) - pode ser M+
            
            # Linha 1 (Funções científicas)
            ("sin", 1, 0, 1, "nsew", "#606060", "#FFFFFF", self.fonte_botoes_especiais), 
            ("cos", 1, 1, 1, "nsew", "#606060", "#FFFFFF", self.fonte_botoes_especiais), 
            ("tan", 1, 2, 1, "nsew", "#606060", "#FFFFFF", self.fonte_botoes_especiais), 
            ("log", 1, 3, 1, "nsew", "#606060", "#FFFFFF", self.fonte_botoes_especiais), 
            ("ln", 1, 4, 1, "nsew", "#606060", "#FFFFFF", self.fonte_botoes_especiais),
            
            # Linha 2 (Operações e limpeza)
            ("√", 2, 0, 1, "nsew", "#606060", "#FFFFFF"), 
            ("x²", 2, 1, 1, "nsew", "#606060", "#FFFFFF"), 
            ("1/x", 2, 2, 1, "nsew", "#606060", "#FFFFFF"), 
            ("CE", 2, 3, 1, "nsew", "#FF8C00", "#FFFFFF"), # Laranja para CE
            ("C", 2, 4, 1, "nsew", "#FF8C00", "#FFFFFF"), # Laranja para C
            
            # Linha 3 (Números e operações)
            ("7", 3, 0, 1, "nsew", "#3C3C3C", "#FFFFFF"), 
            ("8", 3, 1, 1, "nsew", "#3C3C3C", "#FFFFFF"), 
            ("9", 3, 2, 1, "nsew", "#3C3C3C", "#FFFFFF"), 
            ("/", 3, 3, 1, "nsew", "#606060", "#FFFFFF"), 
            ("±", 3, 4, 1, "nsew", "#606060", "#FFFFFF"),
            
            # Linha 4 (Números e operações)
            ("4", 4, 0, 1, "nsew", "#3C3C3C", "#FFFFFF"), 
            ("5", 4, 1, 1, "nsew", "#3C3C3C", "#FFFFFF"), 
            ("6", 4, 2, 1, "nsew", "#3C3C3C", "#FFFFFF"), 
            ("*", 4, 3, 1, "nsew", "#606060", "#FFFFFF"), 
            ("(", 4, 4, 1, "nsew", "#606060", "#FFFFFF"), # Parênteses
            
            # Linha 5 (Números e operações)
            ("1", 5, 0, 1, "nsew", "#3C3C3C", "#FFFFFF"), 
            ("2", 5, 1, 1, "nsew", "#3C3C3C", "#FFFFFF"), 
            ("3", 5, 2, 1, "nsew", "#3C3C3C", "#FFFFFF"), 
            ("-", 5, 3, 1, "nsew", "#606060", "#FFFFFF"), 
            (")", 5, 4, 1, "nsew", "#606060", "#FFFFFF"), # Parênteses
            
            # Linha 6 (Número, ponto, igual)
            ("0", 6, 0, 2, "nsew", "#3C3C3C", "#FFFFFF"), # Ocupa 2 colunas
            (".", 6, 2, 1, "nsew", "#3C3C3C", "#FFFFFF"), 
            ("+", 6, 3, 1, "nsew", "#606060", "#FFFFFF"), 
            ("=", 6, 4, 1, "nsew", "#007ACC", "#FFFFFF") # Azul para Igual
        ]

        # Configura o grid para expandir proporcionalmente
        for i in range(7): # 7 linhas de botões
            self.frame_botoes.grid_rowconfigure(i, weight=1)
        for i in range(5): # 5 colunas de botões
            self.frame_botoes.grid_columnconfigure(i, weight=1)

        # Cria e posiciona os botões
        for config in botoes:
            texto, linha, col, *params = config
            colspan = params[0] if len(params) > 0 else 1
            sticky = params[1] if len(params) > 1 else "nsew"
            cor_fundo = params[2] if len(params) > 2 else "#3C3C3C"
            cor_texto = params[3] if len(params) > 3 else "#FFFFFF"
            fonte = params[4] if len(params) > 4 else self.fonte_botoes
            
            # Cria o botão com estilo
            btn = tk.Button(self.frame_botoes, 
                            text=texto, 
                            font=fonte, 
                            bg=cor_fundo, 
                            fg=cor_texto, 
                            relief="raised", # Efeito de relevo
                            borderwidth=1,
                            activebackground="#777777", # Cor quando pressionado
                            activeforeground="#FFFFFF",
                            command=lambda t=texto: self.on_button_click(t))
            
            # Posiciona no grid
            btn.grid(row=linha, column=col, columnspan=colspan, sticky=sticky, padx=3, pady=3)

    def on_button_click(self, char):
        """Função chamada quando um botão é clicado."""
        current_display = self.display_var.get()

        if char.isdigit():
            if self.limpar_proximo_digito or current_display == "0" or "Erro" in current_display:
                self.display_var.set(char)
                self.limpar_proximo_digito = False
            else:
                self.display_var.set(current_display + char)
            self.expressao_atual += char
        
        elif char == ".":
            # Evita múltiplos pontos no mesmo número
            # Lógica simplificada: permite ponto se não houver um no último número
            partes = self.expressao_atual.split(" ") # Divide por operadores
            if "." not in partes[-1]:
                if self.limpar_proximo_digito or current_display == "0" or "Erro" in current_display:
                    self.display_var.set("0.")
                    self.expressao_atual += "0."
                    self.limpar_proximo_digito = False
                else:
                    self.display_var.set(current_display + ".")
                    self.expressao_atual += "."
        
        elif char in ["+", "-", "*", "/"]:
            if "Erro" in current_display:
                return # Não faz nada se houver erro
            # Adiciona espaço antes e depois do operador para clareza na expressão
            self.expressao_atual += f" {char} "
            self.display_var.set(char) # Mostra o operador no display temporariamente
            self.limpar_proximo_digito = True

        elif char == "=":
            if "Erro" in self.expressao_atual:
                 self.expressao_atual = ""
                 self.display_var.set("Erro")
                 return
            if not self.expressao_atual:
                 return
            
            # Tenta calcular a expressão completa
            # Nota: A função calcular atual avalia a expressão inteira. 
            # Para uma calculadora padrão, seria necessário processar a expressão passo a passo.
            # Esta implementação usa eval para simplicidade, o que pode ser um risco.
            # A função _avaliar_expressao em funcoes.py tenta mitigar isso.
            try:
                # Limpa espaços extras antes de calcular
                expressao_para_calcular = "".join(self.expressao_atual.split())
                resultado = self.funcoes_calc.calcular(expressao_para_calcular)
                self.display_var.set(resultado)
                self.expressao_atual = str(resultado) # Próxima operação começa com o resultado
                self.limpar_proximo_digito = True # Limpa display no próximo dígito
            except Exception as e:
                print(f"Erro no cálculo: {e}")
                self.display_var.set("Erro")
                self.expressao_atual = ""
                self.limpar_proximo_digito = True

        elif char == "C":
            self.expressao_atual = ""
            self.display_var.set("0")
            self.limpar_proximo_digito = False

        elif char == "CE":
            # Limpa a entrada atual (o que está no display)
            self.display_var.set("0")
            # Tenta remover o último número ou operador da expressão interna
            partes = self.expressao_atual.split(" ")
            if partes:
                partes.pop() # Remove o último elemento (número ou operador)
                # Se o último removido foi um operador, remove o espaço anterior também
                if len(partes) > 0 and partes[-1] == "": 
                    partes.pop()
                self.expressao_atual = " ".join(partes)
                if self.expressao_atual.endswith(" "): # Se terminou com operador
                     self.limpar_proximo_digito = True
                else:
                     self.limpar_proximo_digito = False
            else:
                self.expressao_atual = ""
                self.limpar_proximo_digito = False

        elif char == "±":
            if current_display != "0" and "Erro" not in current_display:
                if current_display.startswith("-"):
                    self.display_var.set(current_display[1:])
                else:
                    self.display_var.set("-" + current_display)
                # Atualiza a expressão atual também (simplificado)
                # Idealmente, deveria negar o último número na expressão
                if self.expressao_atual.endswith(current_display):
                     self.expressao_atual = self.expressao_atual[:-len(current_display)] + self.display_var.get()
                else: # Se o display foi limpo (após op ou =), aplica ao valor atual
                     self.expressao_atual = self.display_var.get()
                     self.limpar_proximo_digito = False # Permite continuar digitando

        elif char in ["sin", "cos", "tan", "log", "ln", "√", "x²", "1/x"]:
             if "Erro" in current_display:
                 return
             try:
                 valor_atual = self.display_var.get() # Usa o valor visível no display
                 resultado = self.funcoes_calc.calcular_funcao(char, valor_atual)
                 self.display_var.set(resultado)
                 self.expressao_atual = str(resultado) # Atualiza expressão com resultado
                 self.limpar_proximo_digito = True
             except Exception as e:
                 print(f"Erro ao aplicar função {char}: {e}")
                 self.display_var.set("Erro")
                 self.expressao_atual = ""
                 self.limpar_proximo_digito = True
                 
        elif char == "MC":
            self.funcoes_calc.memoria_limpar()
            # Pode adicionar um indicador visual de memória (ex: label)
            
        elif char == "MR":
            valor_memoria = self.funcoes_calc.memoria_recuperar()
            self.display_var.set(valor_memoria)
            # Decide se substitui ou anexa à expressão atual
            # Aqui, substitui o display e prepara para nova operação
            self.expressao_atual = valor_memoria 
            self.limpar_proximo_digito = True 
            
        elif char == "M+":
            if "Erro" not in current_display:
                self.funcoes_calc.memoria_adicionar(self.display_var.get())
                self.limpar_proximo_digito = True # Prepara para próxima entrada
                
        elif char == "M-":
            if "Erro" not in current_display:
                self.funcoes_calc.memoria_subtrair(self.display_var.get())
                self.limpar_proximo_digito = True
                
        elif char == "MS": # Memory Store (funciona como M+ aqui)
             if "Erro" not in current_display:
                self.funcoes_calc.memoria_adicionar(self.display_var.get())
                self.limpar_proximo_digito = True
                
        elif char == "(":
            if self.limpar_proximo_digito or current_display == "0" or "Erro" in current_display:
                self.display_var.set("(")
                self.expressao_atual += "("
                self.limpar_proximo_digito = False
            else:
                # Adiciona '*' implicitamente se o último caractere for um número ou ')'
                if self.expressao_atual and self.expressao_atual[-1].isdigit() or self.expressao_atual.endswith(")"): 
                    self.expressao_atual += " * " # Ou apenas "*" dependendo da lógica de eval
                self.display_var.set(current_display + "(")
                self.expressao_atual += "("
                
        elif char == ")":
            # Verifica se há um '(' correspondente (simplificado)
            if self.expressao_atual.count("(") > self.expressao_atual.count(")"):
                 self.display_var.set(current_display + ")")
                 self.expressao_atual += ")"
                 self.limpar_proximo_digito = False # Permite continuar após ')'

# Exemplo de como usar (será movido para main.py)
# if __name__ == "__main__":
#     root = tk.Tk()
#     funcoes = FuncoesCalculadora()
#     app = InterfaceCalculadora(root, funcoes)
#     root.mainloop()


