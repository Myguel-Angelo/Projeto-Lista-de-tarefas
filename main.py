from abc import ABC, abstractmethod
from typing import Tuple
import customtkinter as ctk
import time
from datetime import datetime

dia = str(datetime.now().day) 
mes = str(datetime.now().month)
ano = str(datetime.now().year)

# Importando classes
from dados import (
    Frame, 
    Fonte, 
    Botao, 
    FrameSc,
    Texto,
    EntradaTexto,
    Dialogo
)
# Importando funções
from dados import (
    verificar_usuario,
    adicionar_caixa_tarefa,
    desfazer_caixa_tarefa,
    refazer_caixa_tarefa,
    apagar_tudo
)

def esperar(t):
    time.sleep(t)

def validar_input(entrada: str) -> bool:
    cond1 = entrada is None
    cond2 = entrada == ''
    cond3 = entrada.isspace()
    
    if cond1 or cond2 or cond3:
        return False
    return True


class Janela(ctk.CTk, ABC):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
    
    @abstractmethod
    def _estrutura(self): ...
    
    @abstractmethod
    def _posicao(self): ...



class JanelaUsuario(Janela):
    def __init__(self, nome_usuario:str, fg_color: str | Tuple[str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.nome_usuario = nome_usuario
        self._indice = 0
        self._lista_tarefas = []
        self._lista_tarefas_removidas = []
        
        self._estrutura()
        self._posicao()
    
    
    def _estrutura(self):
        self.geometry("500x650")
        self._set_appearance_mode('dark')
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.title(' ÁREA DE USUÁRIO')
        
        # Frames principais
        self.frame_fundo = Frame(master=self, fg_color='#ffffff', corner_radius=20, border_width=30, height=540)
        self.frame_fundo.grid(row=0, column=0, padx=77, pady=100, sticky='nsew')
        
        self.frame_principal = Frame(master=self, fg_color='#ffffff', corner_radius=10, bg_color='transparent')
        self.frame_principal.grid(row=0, column=0, padx=90, pady=90, sticky='nsew')
        self.frame_principal.grid_columnconfigure((0,1,2,3), weight=1)
        
        # Fontes de texto
        self.fonte_titulo = Fonte('Calibri', 27, 'bold', 'roman')
        self.fonte_sub_titulo = Fonte('Calibri', 16, 'bold', 'roman')
        self.fonte_texto1 = Fonte('Arial Black',size=14,weight='bold',slant='roman')
        self.fonte_texto2 = Fonte('Calibri',weight='bold',slant='roman', underline=True)
        
        
        # Atributos de uma janela de Usuário:
        self.texto_titulo = Texto(
            master=self.frame_principal,
            height=70,
            text='Lista de Tarefas',
            font=self.fonte_titulo,
            corner_radius=10,
            text_color= '#606060'
        )
        
        self.frame_lista = FrameSc(
            master=self.frame_principal,
            height=260,
            width=280,
            fg_color='#cccccc',
            corner_radius=20,
            bg_color='#fff'
        )
        self.frame_lista.grid_columnconfigure(0, weight=1)
        
        self.botao_adicionar = Botao(
            master=self.frame_principal,
            height=23,
            width=30,
            text='✚',
            font=self.fonte_texto1,
            command=self._nova_tarefa
        )
        self.botao_desfazer = Botao(
            master=self.frame_principal,
            height=23,
            width=30,
            text='⭯',
            font=self.fonte_texto1,
            command=self._desfazer_tarefa
        )
        self.botao_refazer = Botao(
            master=self.frame_principal,
            height=23,
            width=30,
            text='⭮',
            font=self.fonte_texto1,
            command=self._refazer_tarefa
        )
        self.botao_limpar = Botao(
            master=self.frame_principal,
            height=23,
            width=30,
            text='✖',
            font=self.fonte_texto1,
            command=self._confimar_deletar
        )
        
        self.texto_usuario = Texto(
            master=self.frame_principal,
            font=self.fonte_sub_titulo,
            text=f'{self.nome_usuario} - {dia}/{mes}/{ano}',
            text_color= '#606060'
        )
        
    
    def _posicao(self):
        self.texto_titulo.grid(row=0, column=0, padx=10, pady=(10,0), columnspan=4, sticky='we')
        self.frame_lista.grid(row=1, column=0, padx=15, pady=(5,7), columnspan=4)
        self.botao_adicionar.grid(row=2, column=0, padx=(45,4), pady=(0, 10), sticky='we')
        self.botao_desfazer.grid(row=2, column=1, padx=4, pady=(0, 10), sticky='we')
        self.botao_refazer.grid(row=2, column=2, padx=4, pady=(0, 10), sticky='we')
        self.botao_limpar.grid(row=2, column=3, padx=(4,45), pady=(0, 10), sticky='we')
        self.texto_usuario.grid(row=3, column=0, padx=10, pady=10, sticky='we', columnspan=4)
    
    def _adicionar_tarefa(self, tarefa):
        self._indice = len(self._lista_tarefas) -1
        adicionar_caixa_tarefa(self._lista_tarefas, self.frame_lista, self._indice, tarefa)
        self._indice = len(self._lista_tarefas) -1
        # for i in self._lista_tarefas:
        #     print(i.cget("text"))
    
    def _desfazer_tarefa(self):
        tarefa_desfeita = desfazer_caixa_tarefa(self._lista_tarefas)
        if tarefa_desfeita is not None:
            self._indice = len(self._lista_tarefas)-1
            self._lista_tarefas_removidas.append(tarefa_desfeita)
        
        if self._indice <=0:
            self._indice = 0
        return
    
    def _refazer_tarefa(self):
        self._indice = len(self._lista_tarefas)-1
        refazer_caixa_tarefa(self._lista_tarefas, self._lista_tarefas_removidas, self._indice)
        self._indice = len(self._lista_tarefas)-1
        
    
    def _apagar_tarefas(self):
        apagar_tudo(self._lista_tarefas)
        self._lista_tarefas.clear()
        # self._lista_tarefas_removidas.clear()
        ...
    
    def _nova_tarefa(self):
        dialogo_tarefa = Dialogo(
            title='Nova Tarefa',
            text='Qual tarefa deseja adicionar?',   
        )
        
        nova_tarefa = dialogo_tarefa.get_input()
        if nova_tarefa is None or nova_tarefa == '' or nova_tarefa.isspace():
            return
        self._adicionar_tarefa(nova_tarefa)
    
    def _confimar_deletar(self):
        dialogo_confirmar = Dialogo(
            title=' Apagando todas as tarefas...',
            text='Escreva "CONFIRMAR" para apagar tudo:'
        )
        resposta = dialogo_confirmar.get_input()
        if resposta == 'CONFIRMAR':
            self._apagar_tarefas()
        return


class JanelaLogin(Janela):
    def __init__(self, fg_color: str | Tuple[str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.lista_usuarios = []
        self.user= None
        self.key= None
        
        self._estrutura()
        self._posicao()
    
    def _estrutura(self):
        
        # Configurações da janela de Login
        self.geometry("500x570")
        self._set_appearance_mode('dark')
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.title(' ÁREA DE LOGIN')
        
        # Frames principais
        self.frame_fundo = Frame(master=self, fg_color='#ffffff', corner_radius=20, border_width=30, height=540)
        self.frame_fundo.grid(row=0, column=0, padx=77, pady=100, sticky='nsew')
        
        self.frame_principal = Frame(master=self, fg_color='#ffffff', corner_radius=10, bg_color='transparent')
        self.frame_principal.grid(row=0, column=0, padx=90, pady=90, sticky='nsew')
        
        # Fontes de texto
        self.fonte_titulo = Fonte('Calibri', 27, 'bold', 'roman')
        self.fonte_sub_titulo = Fonte('Calibri', 20, 'bold', 'roman')
        self.fonte_texto1 = Fonte('Calibri',weight='bold',slant='roman')
        self.fonte_texto2 = Fonte('Calibri',weight='bold',slant='roman', underline=True)
        
    
        # Atributos de uma janela de login:
        self.texto_titulo = Texto(
            master=self.frame_principal,
            height=70,
            text='Sistema de Login',
            font=self.fonte_titulo,
            corner_radius=10,
            text_color= '#606060'
        )
        
        self.texto_mensagem = Texto(
            master=self.frame_principal,
            height=0,
            width=0,
            text='',
            font=self.fonte_texto1,
            corner_radius=10,
            text_color='#ff3f3f'
        )
        
        self.texto_usuario = Texto(
            master=self.frame_principal,
            height=10,
            text='Usuário: ',
            font=self.fonte_sub_titulo,
            corner_radius=10,
            text_color='#606060'
        )
        
        self.entrada_usuario = EntradaTexto(
            master=self.frame_principal,
            height=35,
            width=219,
            placeholder_text='Nome de Usuário',
            corner_radius=20,
            border_width=1.5,
            text_color='#606060',
            fg_color='#ffffff'
        )
        
        self.texto_senha = Texto(
            master=self.frame_principal,
            height=10,
            text='Senha: ',
            font=self.fonte_sub_titulo,
            corner_radius=10,
            text_color='#606060'
        )
        
        self.entrada_senha = EntradaTexto(
            master=self.frame_principal,
            height=35,
            width=219,
            placeholder_text='Senha',
            corner_radius=20,
            border_width=1.5,
            text_color='#606060',
            fg_color='#ffffff',show='*'
        )
        
        self.botao_login = Botao(
            master=self.frame_principal,
            height=35, 
            width=219, 
            text='Fazer Login', 
            font=self.fonte_texto1,
            fg_color='#1D69C6',
            command=self._login
        )
        
        self.frame_secundario = Frame(master=self.frame_principal, fg_color='#fff',)
        self.frame_secundario.grid_columnconfigure(1, weight=1)
        
        self.texto_pergunta = Texto(
            width=0,
            height=0,
            master=self.frame_secundario,
            text='Ainda não tem conta? ',
            font=self.fonte_texto1,
            corner_radius=10,
            text_color='#606060'
        )
        
        self.botao_novo_usuario = Botao(
            master=self.frame_secundario,
            height=3, 
            width=0,
            text='Criar novo usuário',
            font=self.fonte_texto2,
            fg_color='#fff',
            text_color='#1D69C6', 
            hover_color='#cfe0ff',
            command=self._criar_usuario
        )
    
    def _posicao(self):
        self.texto_titulo.pack(padx=0, pady=(20,0))
        self.texto_mensagem.pack(padx=0, pady=(0,5))
        self.texto_usuario.pack(padx=0, pady=(0,0)) 
        self.entrada_usuario.pack(padx=0, pady=10)
        self.texto_senha.pack(padx=0, pady=0)
        self.entrada_senha.pack(padx=0, pady=10)
        self.botao_login.pack(padx=0, pady=(5,0))
        self.frame_secundario.pack(pady=0)
        self.texto_pergunta.grid(row=0, column=0, padx=0, pady=0, sticky='nse')
        self.botao_novo_usuario.grid(row=0, column=1, padx=0, pady=0, sticky='nse')
    
    def _login(self):
        esperar(1)
        self.user = self.entrada_usuario.get()
        self.key = self.entrada_senha.get()
        
        # verifica se o usuario não digitou nada:
        if self.user == '' or self.key == '':
            self.texto_mensagem.configure(text='Você esqueceu de preencher\nalguns espaços!', text_color='#ff3f3f')
            return
        self.texto_mensagem.configure(text='')
        
        # verifica o login do usuario
        resposta = verificar_usuario(self.lista_usuarios, self.user, self.key)
        if resposta == 'sucesso':
            esperar(1)
            self.janela_usuario = JanelaUsuario(self.user)
            self.withdraw()
            self.janela_usuario.mainloop()
            
        if resposta == 'falha':
            self.texto_mensagem.configure(text=f'Sua conta não foi encontrada!\nUsuário/Senha inválido', text_color='#ff3f3f')
    
    
    def _definir_usuario(self):
        dialogo_usuario = Dialogo(
            text= 'Insira o seu nome de usuário:',
            title= ' Cadastro de Novo usuário'
        )
        
        novo_usuario = dialogo_usuario.get_input()
        if novo_usuario is None:
            self.texto_mensagem.configure(text='A Criação de um novo usuário\nNão foi realizada!', text_color='#ff3f3f')
            return
        
        if validar_input(novo_usuario): # Verifica se o nome de usuário é válido
            
            criando_senha = self._definir_senha('Insira uma senha de no mínimo\n4 dígitos (Sem espaços):', novo_usuario)
            while True:
                if criando_senha == True:
                    self.user = novo_usuario
                    break
                elif criando_senha == False:
                    criando_senha = self._definir_senha('Insira uma senha válida para seu usuário:', novo_usuario)
                    continue
                else:
                    self.texto_mensagem.configure(text='A Criação de um novo usuário\nNão foi realizada!', text_color='#ff3f3f')
                    break
                
            if criando_senha is True:
                return True
            return
            
        else:
            self.texto_mensagem.configure(text='Você não pode criar uma conta\n com esse nome de usuário', text_color='#ff3f3f')
            return
               
    
    def _definir_senha(self, texto: str, usuario: str):
        dialogo_senha = Dialogo(
            text= texto,
            title= ' Cadastro de Novo usuário'
        )
        nova_senha = dialogo_senha.get_input()
        return self.validar_senha(nova_senha, usuario)
    
    
    def validar_senha(self, senha: str, novo_usuario: str):
        if senha is None:
            return
        
        digitos = len(senha) >=4
        
        if validar_input(senha) and digitos:
            dialogo_confirmar_senha = Dialogo(
                text= f'Confirme seu usuário digitando "CONFIRMAR"\n usuario: {novo_usuario} - senha: {senha}',
                title= ' Cadastro de Novo usuário'
            )
            resposta = dialogo_confirmar_senha.get_input()
            if resposta is None:
                return
            
            elif resposta.strip() == 'CONFIRMAR':
                self.key = senha
                return True
            return
        
        return False
    
    def _criar_usuario(self):
        if self._definir_usuario() is True:
            self.texto_mensagem.configure(text='Criação de um novo usuário\nRealizada com sucesso!', text_color='#1D69C6')
            self.lista_usuarios.append({'user': self.user, 'key': self.key})



janela_login = JanelaLogin()
janela_login.mainloop()