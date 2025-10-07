import sys

class Paciente:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = int(idade)
        self.prioridade = int(prioridade)
        self.proximo = None
        self.anterior = None

class FilaDeAtendimento:
    def __init__(self):
        self.head = None
        self.tail = None
        self.chamadas_p_seguidas = 0

    def _monitorar_memoria(self, operacao, antes_depois):
        memoria_total = sys.getsizeof(self)
        atual = self.head
        while atual:
            memoria_total += sys.getsizeof(atual)
            atual = atual.proximo
        print(f"Memória {antes_depois} da '{operacao}': {memoria_total} bytes")
        return memoria_total

    def adicionar_paciente(self, nome, idade, prioridade):
        """
        Adiciona um novo paciente à fila de acordo com sua prioridade.
        Prioritários entram antes dos normais.
        """
        mem_antes = self._monitorar_memoria("Adicionar", "antes")
        novo_paciente = Paciente(nome, idade, prioridade)

        if not self.head:
            self.head = self.tail = novo_paciente
        elif novo_paciente.prioridade == 2: # Prioritário
            cursor = self.head
            ultimo_prioritario = None
            while cursor and cursor.prioridade == 2:
                ultimo_prioritario = cursor
                cursor = cursor.proximo
            
            if ultimo_prioritario: # Insere no final do grupo prioritário
                novo_paciente.proximo = ultimo_prioritario.proximo
                if ultimo_prioritario.proximo:
                    ultimo_prioritario.proximo.anterior = novo_paciente
                else:
                    self.tail = novo_paciente
                ultimo_prioritario.proximo = novo_paciente
                novo_paciente.anterior = ultimo_prioritario
            else: # Insere no início da fila
                novo_paciente.proximo = self.head
                self.head.anterior = novo_paciente
                self.head = novo_paciente
        else: # Normal
            self.tail.proximo = novo_paciente
            novo_paciente.anterior = self.tail
            self.tail = novo_paciente

        mem_depois = self._monitorar_memoria("Adicionar", "depois")
        print(f"Diferença de memória: {mem_depois - mem_antes} bytes\n")

    def remover_paciente(self):
        """
        Remove o paciente atendido (o primeiro da fila).
        Implementa a regra de alternância 1P/7N.
        """
        if not self.head:
            print("A fila está vazia.\n")
            return

        mem_antes = self._monitorar_memoria("Remover", "antes")

        total_p = 0
        total_n = 0
        cursor = self.head
        while cursor:
            if cursor.prioridade == 2:
                total_p += 1
            else:
                total_n += 1
            cursor = cursor.proximo
        
        paciente_a_remover = self.head
        
        proporcao_atingida = (total_n > 0 and total_p > 0 and (total_p / total_n) >= (1/7))

        if proporcao_atingida and self.chamadas_p_seguidas >= 1:
            cursor_normal = self.head
            while cursor_normal and cursor_normal.prioridade != 1:
                cursor_normal = cursor_normal.proximo
            if cursor_normal:
                paciente_a_remover = cursor_normal

        if paciente_a_remover.prioridade == 2:
            self.chamadas_p_seguidas += 1
        else:
            self.chamadas_p_seguidas = 0

        print(f"Paciente atendido: {paciente_a_remover.nome}")

        if paciente_a_remover.anterior:
            paciente_a_remover.anterior.proximo = paciente_a_remover.proximo
        else:
            self.head = paciente_a_remover.proximo

        if paciente_a_remover.proximo:
            paciente_a_remover.proximo.anterior = paciente_a_remover.anterior
        else:
            self.tail = paciente_a_remover.anterior

        if self.head:
            print(f"Próximo paciente: {self.head.nome}")
        else:
            print("A fila ficou vazia.")
        
        mem_depois = self._monitorar_memoria("Remover", "depois")
        print(f"Diferença de memória: {mem_depois - mem_antes} bytes\n")

    def alterar_dados(self, nome_antigo, novo_nome, nova_idade, nova_prioridade):
        cursor = self.head
        paciente_encontrado = None
        while cursor:
            if cursor.nome.lower() == nome_antigo.lower():
                paciente_encontrado = cursor
                break
            cursor = cursor.proximo
    
        if not paciente_encontrado:
            print(f"Paciente '{nome_antigo}' não encontrado.\n")
            return
    
        mem_antes = self._monitorar_memoria("Alterar", "antes")
        if paciente_encontrado.anterior:
            paciente_encontrado.anterior.proximo = paciente_encontrado.proximo
        else:
            self.head = paciente_encontrado.proximo
        if paciente_encontrado.proximo:
            paciente_encontrado.proximo.anterior = paciente_encontrado.anterior
        else:
            self.tail = paciente_encontrado.anterior
        self.adicionar_paciente(novo_nome, nova_idade, nova_prioridade)
        print(f"Dados do paciente '{nome_antigo}' alterados.")
        mem_depois = self._monitorar_memoria("Alterar", "depois")
        print(f"Diferença de memória: {mem_depois - mem_antes} bytes\n")

    def exibir_fila(self):
        if not self.head:
            print("Fila vazia.\n")
            return
        cursor = self.head
        fila_str = ""
        while cursor:
            tipo = "(P)" if cursor.prioridade == 2 else "(N)"
            fila_str += f"[ {cursor.nome} {tipo} ] --> "
            cursor = cursor.proximo
        print(fila_str + "FIM\n")

    def exibir_fila_invertida(self):
        if not self.tail:
            print("Fila vazia.\n")
            return
        cursor = self.tail
        fila_str = ""
        while cursor:
            tipo = "(P)" if cursor.prioridade == 2 else "(N)"
            fila_str += f"[ {cursor.nome} {tipo} ] --> "
            cursor = cursor.anterior
        print(fila_str + "INÍCIO\n")

def exibir_ajuda():
    print("--- Comandos Disponíveis ---")
    print("add <nome> <idade> <P/N>         - Adiciona um paciente")
    print("assist                           - Atende (remove) o próximo paciente")
    print("edit <nome> <novo> <idade> <P/N> - Altera os dados de um paciente")
    print("show                             - Exibe a fila atual")
    print("show_inverted                    - Exibe a fila invertida")
    print("help                             - Mostra esta mensagem de ajuda")
    print("exit                             - Encerra o programa")
    print("----------------------------\n")

def main():
    """Função principal que executa o modo interativo."""
    fila = FilaDeAtendimento()
    print("--- Pré-carregando a fila para testes ---\n")
    pacientes_iniciais = [
        ("João", 30, 1), ("Maria", 65, 2), ("Carlos", 25, 1), ("Ana", 70, 2),
        ("Pedro", 40, 1), ("Sofia", 80, 2), ("Lucas", 22, 1), ("Beatriz", 68, 2),
        ("Gabriel", 35, 1), ("Laura", 75, 2)
    ]
    for nome, idade, prioridade in pacientes_iniciais:
        fila.adicionar_paciente(nome, idade, prioridade)
    
    print("--- Fila Inicial ---")
    fila.exibir_fila()
    exibir_ajuda()

    while True:
        try:
            comando_completo = input("Digite o comando: ").strip().split()
            if not comando_completo:
                continue
            
            comando = comando_completo[0].lower()
            mostrar_menu_no_final = True

            if comando == "add":
                if len(comando_completo) == 4:
                    nome, idade_str, p_str = comando_completo[1], comando_completo[2], comando_completo[3]
                    prioridade = 2 if p_str.upper() == 'P' else 1
                    fila.adicionar_paciente(nome, int(idade_str), prioridade)
                else: 
                    print("Uso incorreto. Ex: add Joao 35 P\n")
                    mostrar_menu_no_final = False
            elif comando == "assist":
                fila.remover_paciente()
            elif comando == "edit":
                if len(comando_completo) == 5:
                    nome_antigo, novo_nome, nova_idade_str, nova_p_str = comando_completo[1], comando_completo[2], comando_completo[3], comando_completo[4]
                    nova_prioridade = 2 if nova_p_str.upper() == 'P' else 1
                    fila.alterar_dados(nome_antigo, novo_nome, int(nova_idade_str), nova_prioridade)
                else: 
                    print("Uso incorreto. Ex: edit Maria Mariana 40 N\n")
                    mostrar_menu_no_final = False
            elif comando == "show":
                fila.exibir_fila()
            elif comando == "show_inverted":
                fila.exibir_fila_invertida()
            elif comando == "help":
                exibir_ajuda()
                mostrar_menu_no_final = False
            elif comando == "exit":
                print("Encerrando o programa.")
                break
            else:
                print("Comando inválido. Digite 'help' para ver a lista de comandos.\n")
                mostrar_menu_no_final = False

            if mostrar_menu_no_final:
                exibir_ajuda()

        except (ValueError, IndexError) as e:
            print(f"Erro na entrada de dados: {e}. Verifique os argumentos e tente novamente.\n")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}\n")

if __name__ == "__main__":
    main()