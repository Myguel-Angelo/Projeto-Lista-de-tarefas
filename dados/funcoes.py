# Verificar Login
from dados.classes import Frame
from dados.classes import CaixaMarcar

def verificar_usuario(lista: list[dict[str, str]], usuario: str, senha: str):
    for item in lista:
        if usuario == item['user'] and senha == item['key']:
            print(f'Logando com {usuario}')
            return 'sucesso'
    print('Usuário não encontrado!')
    return 'falha'


def adicionar_caixa_tarefa(lista: list[CaixaMarcar], local:Frame, indice:int, tarefa:str):
    lista.append(
        CaixaMarcar(
            master=local, 
            text=tarefa,
            text_color= '#000',
        )
    )
    lista[indice+1].grid(row=indice+1, column=0, padx=5, pady=5, sticky='we')

def desfazer_caixa_tarefa(lista: list[CaixaMarcar]):
    if len(lista) == 0:
        print('Lista Vazia!!')
        return
    tarefa_removida = lista.pop()
    tarefa_removida.grid_remove()
    return tarefa_removida

def refazer_caixa_tarefa(lista_principal: list, lista_removidas: list, indice:int):
    if len(lista_removidas) == 0:
        print('Não a nenhuma tarefa pare ser refeita')
        return
    
    tarefa_removida = lista_removidas.pop()
    lista_principal.append(tarefa_removida)
    
    tarefa_removida.grid(row=indice+1, column=0, padx=5, pady=5, sticky='we')
    return


def apagar_tudo(lista: list[CaixaMarcar]):
    for tarefa in lista:
        tarefa.grid_remove()