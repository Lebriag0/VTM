import os  # Módulo para limpar a tela do terminal
    
# Função para cadastrar as notas musicais em um tom específico
def cadastrar_notas(tom):
    notas = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#']  # Lista de notas
    notas_tom = []  # Lista para armazenar as notas no tom especificado
    
    # Dicionário de funções para cada tom
    tom_funcs = {
        'C Maior': cadastrar_notas_C,
        'D Maior': cadastrar_notas_D,
        'E Maior': cadastrar_notas_E,
        'F Maior': cadastrar_notas_F,
        'G Maior': cadastrar_notas_G,
        'A Maior': cadastrar_notas_A,
        'B Maior': cadastrar_notas_B,
        'C Menor': cadastrar_notas_Cm,
        'D Menor': cadastrar_notas_Dm,
        'E Menor': cadastrar_notas_Em,
        'F Menor': cadastrar_notas_Fm,
        'G Menor': cadastrar_notas_Gm,
        'A Menor': cadastrar_notas_Am,
        'B Menor': cadastrar_notas_Bm
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

def cadastrar_notas_Cm():
    return ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']

def cadastrar_notas_Dm():
    return ['D', 'E', 'F', 'G', 'A', 'A#', 'C']

def cadastrar_notas_Em():
    return ['E', 'F#', 'G', 'A', 'B', 'C', 'D']

def cadastrar_notas_Fm():
    return ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']

def cadastrar_notas_Gm():
    return ['G', 'A', 'A#', 'C', 'D', 'D#', 'F']

def cadastrar_notas_Am():
    return ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def cadastrar_notas_Bm():
    return ['B', 'C#', 'D', 'E', 'F#', 'G', 'A']

# Função para alterar uma nota específica dentro de um tom
def alterar_nota_especifica(notas):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
    nota_antiga = input("Digite a nota que deseja alterar \nEscreva a nota do tom selecionado que deseja alterar: ")
    if nota_antiga in notas:
        indice = notas.index(nota_antiga)
        nova_nota = input("Digite a nova nota que deseja ser colocada no lugar da pré-existente: ")
        notas[indice] = nova_nota
        print("Nota alterada com sucesso!")
    else:
        print("Nota não encontrada...")

# Funções para as progressões de acordes em diferentes tons
def progressao_C():
    return [
        ["I", "II", "III", "IV", "V", "VI", "VII"],
        ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    ]

def progressao_D():
    return [
        ["I", "II", "III", "IV", "V", "VI", "VII"],
        ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']
    ]

def progressao_E():
    return [
        ["I", "II", "III", "IV", "V", "VI", "VII"],
        ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']
    ]

def progressao_F():
    return [
        ["I", "II", "III", "IV", "V", "VI", "VII"],
        ['F', 'G', 'A', 'A#', 'C', 'D', 'E']
    ]

def progressao_G():
    return [
        ["I", "II", "III", "IV", "V", "VI", "VII"],
        ['G', 'A', 'B', 'C', 'D', 'E', 'F#']
    ]

def progressao_A():
    return [
        ["I", "II", "III", "IV", "V", "VI", "VII"],
        ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
    ]

def progressao_B():
    return [
        ["I", "II", "III", "IV", "V", "VI", "VII"],
        ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']
    ]

# Variável global para armazenar a progressão de acordes atual
progressao_atual = [
    ["I", "II", "III", "IV", "V", "VI", "VII"],
    ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']
]

# Função para exibir a progressão de acordes atual
def exibir_progressao():
    if progressao_atual:
        print(f"\nProgressão de Acordes Atual:")
        for linha in progressao_atual:
            print(linha)
    else:
        print("\nNenhuma progressão de acordes definida.")

# Função para manipulação da progressão de acordes
def progressao_de_acordes(progressoes):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
        exibir_progressao()
        
        print("\nOpções de Manipulação de Progressão de Acordes:")
        print("1. Escolher/Modificar progressão de acordes")
        print("2. Adicionar nova progressão de acordes")
        print("3. Listar progressões existentes")
        print("4. Voltar ao menu anterior")

        opcao_manipulacao = input("Escolha uma opção: ")

        if opcao_manipulacao == '1':
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
            global progressao_atual
            
            for i, progressao_opcao in enumerate(['-------- "I", "II", "III", "IV", "V", "VI", "VII"',
                                                  "-------------------------------------------------",
                                                  'C Maior: "C", "D",   "E",  "F",  "G", "A",   "B"',
                                                  "D Maior: 'D', 'E',   'F#', 'G',  'A', 'B',   'C#'" ,
                                                  "E Maior: 'E', 'F#',  'G#', 'A',  'B', 'C#',  'D#'",
                                                  "F Maior: 'F', 'G',   'A',  'A#', 'C', 'D',   'E'", 
                                                  "G Maior: 'G', 'A',   'B',  'C',  'D', 'E',   'F#'", 
                                                  "A Maior: 'A', 'B',   'C#', 'D',  'E', 'F#',  'G#'", 
                                                  "B Maior: 'B', 'C#',  'D#', 'E',  'F#','G#',  'A#'"], start=-1):
                print(f"{i}. {progressao_opcao}")
                
            indice_modificar = int(input("Digite o índice da progressão de acordes que deseja modificar: ")) - 1
            if indice_modificar >= 0 and indice_modificar < len(progressoes):
                progressao_atual = progressoes[indice_modificar]
                print("Progressão de acordes modificada com sucesso!")
            else:
                print("Índice de progressão de acordes inválido.")
        
        elif opcao_manipulacao == '2':
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
            nova_progressao = input("Digite a nova progressão de acordes (separados por espaço): ").split()
            progressoes.append(nova_progressao)
            print("Progressão de acordes adicionada com sucesso!")
        
        elif opcao_manipulacao == '3':
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
            if not progressoes:
                print("Não há progressões de acordes cadastradas.")
            else:
                print("\nLista de Progressões de Acordes:")
                for i, progressao in enumerate(progressoes):
                    print(f"{i+1}. {progressao}")
                input("\nPressione Enter para continuar...")
        
        elif opcao_manipulacao == '4':
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Função para exibir o menu principal e interação com o usuário
def menu_principal():
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
        cadastrar_notas_B,
        cadastrar_notas_Cm, 
        cadastrar_notas_Dm, 
        cadastrar_notas_Em, 
        cadastrar_notas_Fm, 
        cadastrar_notas_Gm, 
        cadastrar_notas_Am, 
        cadastrar_notas_Bm
    ]
    
    # Lista de progressões de acordes
    progressoes = [
        progressao_C(),
        progressao_D(),
        progressao_E(),
        progressao_F(),
        progressao_G(),
        progressao_A(),
        progressao_B()
    ]
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
        
        # Exibir o tom atual e as notas
        print("\nTom Atual:", tom_atual)
        print("Notas do Tom Atual:", notas)
        
        # Exibir as opções
        print("\nOpções:")
        print("1. Alterar tom")
        print("2. Alterar nota específica")
        print("3. Progressão de acordes")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
            
            print("\nTom Atual:", tom_atual)
            print("Notas do Tom Atual:", notas)
        
            # Exibir as opções de alteração de tom
            print("\nOpções de Alteração de Tom:")
            for i, tom_opcao in enumerate(['C Maior', 'D Maior', 'E Maior', 'F Maior', 'G Maior', 'A Maior', 'B Maior'], start=1):
                print(f"{i}. {tom_opcao}")
            
            print("-----------------")
            
            for i, tom_opcao2 in enumerate(['C Menor', 'D Menor', 'E Menor', 'F Menor', 'G Menor', 'A Menor', 'B Menor'], start=8):
                print(f"{i}. {tom_opcao2}")
            
            # Obter a escolha do usuário
            escolha_tom = int(input("Escolha o novo tom: "))
            tom = ['C Maior', 'D Maior', 'E Maior', 'F Maior', 'G Maior', 'A Maior', 'B Maior', 'C Menor', 'D Menor', 'E Menor', 'F Menor', 'G Menor', 'A Menor', 'B Menor'][escolha_tom - 1]
            notas = funcs_tons[escolha_tom - 1]()
            tom_atual = tom
            
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
            print("Tom alterado com sucesso.")
        
        elif opcao == '2':
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
            alterar_nota_especifica(notas)
        
        elif opcao == '3':
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
            progressao_de_acordes(progressoes)
        
        elif opcao == '4':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Chamada da função principal
if __name__ == "__main__":
    menu_principal()

    
    
'''# Variável global para armazenar a progressão de acordes atual
progressao_atual = [
    ["I", "II", "III", "IV", "V", "VI", "VII"],
    ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']
]

# Função para exibir a progressão de acordes atual
def exibir_progressao():
    if progressao_atual:
        print(f"\nProgressão de Acordes Atual:")
        for linha in progressao_atual:
            print(linha)
    else:
        print("\nNenhuma progressão de acordes definida.")

# Função para manipulação da progressão de acordes
def manipular_progressao(progressoes):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
        exibir_progressao()
        
        print("\nOpções de Manipulação de Progressão de Acordes:")
        print("1. Escolher/Modificar progressão de acordes")
        print("2. Adicionar nova progressão de acordes")
        print("3. Listar progressões existentes")
        print("4. Voltar ao menu anterior")

        opcao_manipulacao = input("Escolha uma opção: ")

        if opcao_manipulacao == '1':
            global progressao_atual
            indice_modificar = int(input("Digite o índice da progressão de acordes que deseja modificar: ")) - 1
            if indice_modificar >= 0 and indice_modificar < len(progressoes):
                progressao_atual = progressoes[indice_modificar]
                print("Progressão de acordes modificada com sucesso!")
            else:
                print("Índice de progressão de acordes inválido.")
        
        elif opcao_manipulacao == '2':
            nova_progressao = input("Digite a nova progressão de acordes (separados por espaço): ").split()
            progressoes.append(nova_progressao)
            print("Progressão de acordes adicionada com sucesso!")
        
        elif opcao_manipulacao == '3':
            if not progressoes:
                print("Não há progressões de acordes cadastradas.")
            else:
                print("\nLista de Progressões de Acordes:")
                for i, progressao in enumerate(progressoes):
                    print(f"{i+1}. {progressao}")
                input("\nPressione Enter para continuar...")
        
        elif opcao_manipulacao == '4':
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Função principal para gerenciar a progressão de acordes
def progressao_de_acordes(progressoes):
    global progressao_atual
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela
        exibir_progressao()
        
        print("\nOpções de Progressão de Acordes:")
        print("1. Manipular progressões de acordes")
        print("2. Voltar ao menu anterior")
        
        opcao_progressao = input("Escolha uma opção: ")
        
        if opcao_progressao == '1':
            manipular_progressao(progressoes)
        
        elif opcao_progressao == '2':
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Função principal
def main():
    progressoes = []  # Lista para armazenar progressões de acordes
    
    # Chamada da função para gerenciar a progressão de acordes
    progressao_de_acordes(progressoes)

# Execução do programa
if __name__ == "__main__":
    main()
    
    
    para a segunda opção, faça como um esquema de opções também, tendo os algarismos romanos como opções.
Ele teria opções em cima e em embaixo, sendo em cima a progressão de acorde atual e a opção de baixo sendo as opções de algarismo para ser selecionados. quando é selecionado o algarismo da progressao atual e depois o algarismo das opções, o algarismo das opçoes troca de lugar com a atual.
desse jeito, eliminaria o fato do usuario ter que digitar exatamente a progressão que quer fazer.
como um bonus, poderia ter a opção de limpar todos os espaços dos algarismos, para deixar livre para o usuario criar a propria progressao. Use "()" para separar os algarismos, faça a exibição em string.'''