import requests
import webbrowser
import time

class Pokemon:
    def __init__(self, nome, tipo, descricao, ataquebase, defesabase, ataqueespecial, defesaespecial, velocidade, peso):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.ataque_base = ataquebase
        self.defesa_base = defesabase
        self.ataque_especial = ataqueespecial
        self.defesa_especial = defesaespecial
        self.velocidade = velocidade
        self.peso = peso

    def __str__(self):
        return f"Nome: {self.nome} Tipo: {self.tipo} Ataque Base: {self.ataque_base} Defesa Base: {self.defesa_base} Ataque Especial: {self.ataque_especial} Defesa Especial: {self.defesa_especial} Velocidade: {self.velocidade} Peso: {self.peso}"
    
    def informações(self):
        api = f'https://pokeapi.co/api/v2/pokemon/{self.nome}'
        res = requests.get(api)
        if res.status_code == 200:
            dados_pokemon = res.json()
            self.tipo = dados_pokemon['types'][0]['type']['name']
            self.ataque_base = dados_pokemon['stats'][1]['base_stat']
            self.defesa_base = dados_pokemon['stats'][2]['base_stat']
            self.ataque_especial = dados_pokemon['stats'][3]['base_stat']
            self.defesa_especial = dados_pokemon['stats'][4]['base_stat']
            self.velocidade = dados_pokemon['stats'][5]['base_stat']
            self.peso = dados_pokemon['weight']
        else:
            print(f"Não temos informações do pokemon: {self.nome}.")

    def programa():       
        a = input("Nome do Pokemon: ")
        pokemon = Pokemon(a, '', '', '', '',' ', '','','')
        pokemon.informações()
        print(pokemon)
        time.sleep(8)
        Pokemon.menu()
        

    def lista():
        print('Redirecionando para a Lista de Todos os Pokemons...')
        time.sleep(3)
        webbrowser.open('https://psverso.com.br/listas/lista-todos-pokemon/')
        return Pokemon.menu()
    
    def desenvolvedor():

        print('Se você deseja ir para o Portfolio')
        print('')
        print('Digite "1" para continuar')
        print('')
        print('Caso não queira, pressione "Enter" para retornar ao menu')

        user_input = input('')

        if user_input == '1':
           print('Redirecionando...')
           time.sleep(3)
           webbrowser.open('https://github.com/nevesntc')
           Pokemon.menu()
        else:
           print('Retornando ao menu...')
           time.sleep(2)
           Pokemon.menu()

    
    def sair():
        print('Obrigado por Utilizar o Programa')
        print('')
        print('Creditos: Bruno Neves')
        exit()
    
    def menu(): # esse codigo \033[1;1m é para deixar tudo em branco em negrito para poder visualizar melhor. Utilizei codigo ANSI de cores: referência: http://raccoon.ninja/pt/dev-pt/utilizando-cores-para-escrever-no-terminal-python/
        print('\033[1;1mBem vindo ao Banco de Dados do Pokemon')
        print('')
        print('1- Escolher o Pokemon')
        print('')
        print('2- Ver a Lista de Pokemons Existentes')
        print('')
        print('3- Desenvolvedor')
        print('')
        print('4- Sair')
        b = int(input(''))
        if b == 1:
            Pokemon.programa()
        elif b == 2:
            Pokemon.lista()
        elif b == 3:
            Pokemon.desenvolvedor()
        elif b == 4:
            Pokemon.sair()
        else:
            print('Não é uma opção válida')
            print('')
            print('Tente Novamente')
            return Pokemon.menu
        
Pokemon.menu()


    

    


    
    




