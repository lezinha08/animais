class ListaDeAnimais:
    def __init__(self):
        self.animais = []
    
    def adicionar_animal(self, nome):
        self.animais.append(nome)
        print(f'{nome} foi adicionado à lista.')
    
    def remover_animal(self, nome):
        if nome in self.animais:
            self.animais.remove(nome)
            print(f'{nome} foi removido da lista.')
        else:
            print(f'{nome} não encontrado na lista.')
    
    def listar_animais(self):
        if self.animais:
            print("Lista de Animais:")
            for animal in self.animais:
                print(f'- {animal}')
        else:
            print("A lista está vazia.")
    
    def salvar_lista(self, filename):
        with open(filename, 'w') as file:
            for animal in self.animais:
                file.write(animal + '\n')
        print(f'A lista foi salva no arquivo {filename}')
    
    def carregar_lista(self, filename):
        try:
            with open(filename, 'r') as file:
                self.animais = [line.strip() for line in file]
            print(f'A lista foi carregada do arquivo {filename}')
        except FileNotFoundError:
            print(f'O arquivo {filename} não foi encontrado.')

# Exemplo de uso
lista = ListaDeAnimais()
lista.adicionar_animal("Cachorro")
lista.adicionar_animal("Gato")
lista.listar_animais()
lista.remover_animal("Gato")
lista.listar_animais()
lista.salvar_lista("animais.txt")
lista.carregar_lista("animais.txt")
