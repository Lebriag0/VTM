import os  # Módulo para limpar a tela do terminal

# Função para cadastrar as notas musicais em um tom específico
def cadastrar_notas(tom):
    notas = ['C', 'D', 'E', 'F', 'G', 'A', 'B']  # Lista de notas
    notas_tom = []  # Lista para armazenar as notas no tom especificado
    
    # Dicionário de funções para cada tom
    tom_funcs = {
        'C Maior': cadastrar_notas_C,
        'D Maior': cadastrar_notas_D,
        'E Maior': cadastrar_notas_E,
        'F Maior': cadastrar_notas_F,
        'G Maior': cadastrar_notas_G,
        'A Maior': cadastrar_notas_A,
        'B Maior': cadastrar_notas_B
    }
    
    # Cadastrar as notas no tom especificado usando a função correspondente
    notas_tom = tom_funcs[tom]()
    
    return notas_tom

# Funções para cadastrar as notas em um tom específico
def cadastrar_notas_C():
    return ['C', 'D', 'E', 'F', 'G', 'A', 'B']

def cadastrar_notas_D():
    return ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']

def cadastrar_notas_E():
    return ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']

def cadastrar_notas_F():
    return ['F', 'G', 'A', 'A#', 'C', 'D', 'E']

def cadastrar_notas_G():
    return ['G', 'A', 'B', 'C', 'D', 'E', 'F#']

def cadastrar_notas_A():
    return ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']

def cadastrar_notas_B():
    return ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']

# Função para alterar uma nota específica dentro de um tom
def alterar_nota_especifica(notas):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
    nota_antiga = input("Digite a nota que deseja alterar: ")
    if nota_antiga in notas:
        indice = notas.index(nota_antiga)
        nova_nota = input("Digite a nova nota: ")
        notas[indice] = nova_nota
        print("Nota alterada com sucesso.")
    else:
        print("Nota não encontrada.")

# Função principal
def main():
    tom = 'E Maior'  # Definindo o tom inicial
    notas = cadastrar_notas(tom)  # Cadastrar notas no tom inicial
    tom_atual = tom  # Definindo o tom atual
    
    # Lista de funções de cada tom
    funcs_tons = [
        cadastrar_notas_C, 
        cadastrar_notas_D, 
        cadastrar_notas_E, 
        cadastrar_notas_F, 
        cadastrar_notas_G, 
        cadastrar_notas_A, 
        cadastrar_notas_B
    ]
    
    # Loop principal para interação com o usuário
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
        
        # Exibir o tom atual e as notas
        print("\nTom Atual:", tom_atual)
        print("Notas do Tom Atual:", notas)
        
        # Exibir as opções
        print("\nOpções:")
        print("1. Alterar tom")
        print("2. Alterar nota específica")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
            
            print("\nTom Atual:", tom_atual)
            print("Notas do Tom Atual:", notas)
        
            # Exibir as opções de alteração de tom
            print("\nOpções de Alteração de Tom:")
            for i, tom_opcao in enumerate(['C Maior', 'D Maior', 'E Maior', 'F Maior', 'G Maior', 'A Maior', 'B Maior'], start=1):
                print(f"{i}. {tom_opcao}")
            
            # Obter a escolha do usuário
            escolha_tom = int(input("Escolha o novo tom: "))
            tom = ['C Maior', 'D Maior', 'E Maior', 'F Maior', 'G Maior', 'A Maior', 'B Maior'][escolha_tom - 1]
            notas = funcs_tons[escolha_tom - 1]()
            tom_atual = tom
            
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
            print("Tom alterado com sucesso.")
        elif opcao == '2':
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
            alterar_nota_especifica(notas)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Chamada da função principal
if __name__ == "__main__":
    main()