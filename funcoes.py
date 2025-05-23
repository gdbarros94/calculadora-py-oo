# -*- coding: utf-8 -*-
"""
Arquivo contendo as funções lógicas da calculadora.
"""

import math

class FuncoesCalculadora:
    """Classe que encapsula as operações da calculadora."""

    def __init__(self):
        """Inicializa a classe."""
        self.memoria = 0.0

    def _avaliar_expressao(self, expressao):
        """Avalia uma expressão matemática de forma segura."""
        try:
            # Substitui símbolos para compatibilidade com eval
            expressao_segura = expressao.replace('^', '**').replace('√', 'math.sqrt')
            
            # Define um ambiente seguro para eval
            allowed_names = {"math": math, "sqrt": math.sqrt}
            
            # Avalia a expressão
            resultado = eval(expressao_segura, {"__builtins__": {}}, allowed_names)
            return resultado
        except ZeroDivisionError:
            return "Erro: Divisão por zero"
        except (SyntaxError, NameError, TypeError, ValueError) as e:
            print(f"Erro ao avaliar expressão: {e}") # Log do erro
            return "Erro"
        except Exception as e:
            print(f"Erro inesperado: {e}") # Log de erro inesperado
            return "Erro"

    def calcular(self, expressao):
        """Realiza o cálculo principal da expressão fornecida."""
        if not expressao:
            return ""
        
        resultado = self._avaliar_expressao(expressao)
        
        # Formata o resultado para exibição
        if isinstance(resultado, float):
            # Remove '.0' se for um inteiro
            if resultado.is_integer():
                return str(int(resultado))
            # Limita casas decimais para floats
            return f"{resultado:.10f}".rstrip('0').rstrip('.')
        return str(resultado) # Retorna como string em caso de erro ou outros tipos

    # Funções de memória (exemplo)
    def memoria_adicionar(self, valor_str):
        """Adiciona o valor atual à memória."""
        try:
            valor = float(valor_str)
            self.memoria += valor
        except ValueError:
            pass # Ignora se o valor não for numérico

    def memoria_subtrair(self, valor_str):
        """Subtrai o valor atual da memória."""
        try:
            valor = float(valor_str)
            self.memoria -= valor
        except ValueError:
            pass

    def memoria_recuperar(self):
        """Recupera o valor da memória."""
        if self.memoria.is_integer():
            return str(int(self.memoria))
        return f"{self.memoria:.10f}".rstrip('0').rstrip('.')

    def memoria_limpar(self):
        """Limpa a memória."""
        self.memoria = 0.0

    # Funções trigonométricas e outras (exemplo)
    def calcular_funcao(self, funcao, valor_str):
        """Calcula funções matemáticas como seno, cosseno, etc."""
        try:
            valor = float(valor_str)
            resultado = None
            if funcao == 'sin':
                resultado = math.sin(math.radians(valor)) # Assume graus
            elif funcao == 'cos':
                resultado = math.cos(math.radians(valor))
            elif funcao == 'tan':
                # Adiciona verificação para tangente de 90 graus (+ k*180)
                if (valor % 180) == 90:
                    return "Erro: Tangente indefinida"
                resultado = math.tan(math.radians(valor))
            elif funcao == 'log':
                if valor <= 0:
                    return "Erro: Log de não positivo"
                resultado = math.log10(valor)
            elif funcao == 'ln':
                if valor <= 0:
                    return "Erro: Ln de não positivo"
                resultado = math.log(valor)
            elif funcao == '√':
                 if valor < 0:
                    return "Erro: Raiz de negativo"
                 resultado = math.sqrt(valor)
            elif funcao == 'x²':
                 resultado = valor ** 2
            elif funcao == '1/x':
                 if valor == 0:
                    return "Erro: Divisão por zero"
                 resultado = 1 / valor
                 
            if resultado is not None:
                if isinstance(resultado, float) and resultado.is_integer():
                    return str(int(resultado))
                return f"{resultado:.10f}".rstrip('0').rstrip('.')
            else:
                return "Erro: Função inválida"
                
        except ValueError:
            return "Erro: Entrada inválida"
        except Exception as e:
            print(f"Erro ao calcular função {funcao}: {e}")
            return "Erro"

