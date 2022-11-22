import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg


def CriarBanco(cursor):

    comando = '''CREATE TABLE Alunos(
    id_Alunos INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(30),
    Sexo CHAR(1)
    );'''
    cursor.execute(comando)
    comando = '''CREATE TABLE Eventos(
    id_Eventos INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_Alunos_fk INTEGER NOT NULL,
    Esporte VARCHAR(30),
    FOREIGN KEY(id_Alunos_fk) REFERENCES Alunos (id_Alunos) on update cascade on delete cascade
);'''
    cursor.execute(comando)
    comando = '''CREATE TABLE Turmas(
    id_Turma INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_eventos_fk INTEGER NOT NULL,
    id_Alunos_fk INTEGER NOT NULL,
    Serie CHAR(1),
    Turma CHAR(1),
    FOREIGN KEY(id_eventos_fk) REFERENCES Eventos (id_Eventos) on update cascade on delete cascade, 
    FOREIGN KEY(id_Alunos_fk) REFERENCES Alunos (id_Alunos) on update cascade on delete cascade
    );'''
    cursor.execute(comando)
    comando = '''INSERT INTO Alunos(Nome, Sexo)VALUES
    ("Neymar","M"),
    ("Juliana","F"),
    ("Joselina","F"),
    ("Marta","F");'''
    cursor.execute(comando)
    comando = '''INSERT INTO Eventos(id_Alunos_fk, Esporte)VALUES
    (1,"Futebol"),
    (2,"Volei"),
    (3,"Volei"),
    (4,"Futebol");'''
    cursor.execute(comando)
    comando = '''INSERT INTO Turmas(id_eventos_fk,id_Alunos_fk,Serie,Turma)VALUES
    (1,2,3,"A"),
    (2,1,1,"A"),
    (3,3,2,"B"),
    (4,4,3,"C");'''
    cursor.execute(comando)

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'sephirothFF7'
)

cursor = conexao.cursor()
comando = 'create database semanadejogos;'
cursor.execute(comando)
conexao.database = 'semanadejogos'

Esportes = ["Futebol","Volei"]
Sexo = ["M","F"]
Series = [3,2,1]
Turmas = ["A","B","C"]

CriarBanco(cursor)


def CadastrarAluno(id):
    if id == 0:
        layout = [
            [sg.Text('Digite o nome do Aluno e seu genero')],
            [sg.Text('Nome: ', size=(10, 1)), sg.Input(key='nome')],
            [sg.Combo(values=Sexo, key="sexo", size=(20, 1))],
            [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
        ]

        janela = sg.Window('Cadastro de Aluno', layout, element_justification='center')
        evento, dados = janela.read()
        nome = dados['nome']
        sexo = dados['sexo']
        comando = f'INSERT INTO Alunos(Nome, Sexo)VALUES("{nome}","{sexo}")'
        cursor.execute(comando)
        conexao.commit()
        janela.close()
    else:
        layout = [
            [sg.Text('Digite o nome do Aluno e seu genero')],
            [sg.Text('Nome: ', size=(10, 1)), sg.Input(key='nome')],
            [sg.Combo(values=Sexo, key="sexo", size=(20, 1))],
            [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
        ]

        janela = sg.Window('Cadastro de Aluno', layout, element_justification='center')
        evento, dados = janela.read()
        nome = dados['nome']
        sexo = dados['sexo']
        comando = f'UPDATE Alunos SET Nome = "{nome}", sexo="{sexo}" where id_Alunos={id}'
        cursor.execute(comando)
        conexao.commit()
        janela.close()




def CadastrarEvento(id):
    if id == 0:
          layout = [
             [sg.Text('Digite o id do aluno e o nome do esporte')],
             [sg.Text('id: ', size=(10, 1)), sg.Input(key='id')],
             [sg.Combo(values=Esportes, key="esporte", size=(20, 1))],
             [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
         ]

          janela = sg.Window('Cadastro de Aluno', layout, element_justification='center')
          evento, dados = janela.read()
          id = dados['id']
          Esporte = dados['esporte']
          comando = f'INSERT INTO Eventos(id_Alunos_fk, Esporte)VALUES({id},"{Esporte}")'
          cursor.execute(comando)
          conexao.commit()
          janela.close()
    else:
        layout = [
            [sg.Text('Digite o id do aluno e o nome do esporte')],
            [sg.Text('id: ', size=(10, 1)), sg.Input(key='id')],
            [sg.Combo(values=Esportes, key="esporte", size=(20, 1))],
            [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
        ]

        janela = sg.Window('Cadastro de Aluno', layout, element_justification='center')
        evento, dados = janela.read()
        id_cadastro = dados['id']
        Esporte = dados['esporte']
        comando = f'UPDATE Eventos SET id_Alunos_fk = {id_cadastro}, Esporte="{Esporte}" where id_Eventos={id}'
        cursor.execute(comando)
        conexao.commit()
        janela.close()


def CadastrarTurma(id):
    if id == 0:
        layout = [
            [sg.Text('Digite o id do evento, id do aluno, Serie e Turma')],
            [sg.Text('id_Evento: ', size=(10, 1)), sg.Input(key='id_evento')],
            [sg.Text('id_aluno', size=(10, 1)), sg.Input(key='id_aluno')],
            [sg.Combo(values=Series, key="serie", size=(20, 1))],
            [sg.Combo(values=Turmas, key="turma", size=(20, 1))],
            [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
        ]

        janela = sg.Window('Cadastro de Aluno', layout, element_justification='center')
        evento, dados = janela.read()
        id_evento = dados['id_evento']
        id_aluno = dados['id_aluno']
        Serie = dados['serie']
        Turma = dados['turma']
        comando = f'INSERT INTO Turmas(id_eventos_fk,id_Alunos_fk,Serie,Turma)VALUES({id_evento},{id_aluno},"{Serie}","{Turma}")'
        cursor.execute(comando)
        conexao.commit()
        janela.close()
    else:
        layout = [
            [sg.Text('Digite o id do evento, id do aluno, Serie e Turma')],
            [sg.Text('id_Evento: ', size=(10, 1)), sg.Input(key='id_evento')],
            [sg.Text('id_aluno', size=(10, 1)), sg.Input(key='id_aluno')],
            [sg.Combo(values=Series, key="serie", size=(20, 1))],
            [sg.Combo(values=Turmas, key="turma", size=(20, 1))],
            [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
        ]

        janela = sg.Window('Cadastro de Aluno', layout, element_justification='center')
        evento, dados = janela.read()
        id_evento = dados['id_evento']
        id_aluno = dados['id_aluno']
        Serie = dados['serie']
        Turma = dados['turma']
        comando = f'UPDATE Turmas SET id_Eventos_fk = {id_evento},id_Alunos_fk = {id_aluno},Serie={Serie},Turma={Turma} where id_Turma={id}'
        cursor.execute(comando)
        conexao.commit()
        janela.close()



def Grafico_Genero_Esporte():
    Qtd_Masculino_Futebol = 0
    Qtd_Masculino_Volei = 0
    Qtd_Futebol = 0
    Qtd_Volei = 0


    Comando = f'''SELECT Sexo, Esporte FROM Alunos, Eventos
     where id_Alunos = id_Alunos_fk;'''
    cursor.execute(Comando)
    resultado = cursor.fetchall()
    i = 0
    for i in range(len(resultado)):
        if resultado[i][1] == "Futebol":
            if resultado[i][0] == "M":
                Qtd_Masculino_Futebol+=1
            Qtd_Futebol += 1
        elif resultado[i][1] == "Volei":
            if resultado[i][0] == "M":
                Qtd_Masculino_Volei+=1
            Qtd_Volei+=1
    Cont_Genero = [Qtd_Masculino_Futebol,Qtd_Masculino_Volei]
    Qtd_Incrito_por_Esporte = [Qtd_Futebol,Qtd_Volei]

    plt.bar(Esportes,Qtd_Incrito_por_Esporte,color='pink', label="Quantidade de Menina")
    plt.bar(Esportes,Cont_Genero,color='b',label="Quantidade de Menino")
    plt.legend()
    plt.show()


def Grafico_Genero_Turma():
    Qtd_Masculino_3 = 0
    Qtd_Masculino_2 = 0
    Qtd_Masculino_1 = 0

    Qtd_3 = 0
    Qtd_2 = 0
    Qtd_1 = 0



    Comando = f'''SELECT Sexo, Serie FROM Alunos, Turmas
     where id_Alunos = id_Alunos_fk;'''
    cursor.execute(Comando)
    resultado = cursor.fetchall()
    i = 0
    print(resultado)
    for i in range(len(resultado)):
        if resultado[i][1] == '3':
            if resultado[i][0] == "M":
                Qtd_Masculino_3+=1
            Qtd_3 += 1
        elif resultado[i][1] == '2':
            if resultado[i][0] == "M":
                Qtd_Masculino_2+=1
            Qtd_2+=1
        elif resultado[i][1] == '1':
            if resultado[i][0] == "M":
                Qtd_Masculino_1 += 1
            Qtd_1 += 1

    Cont_Genero = [Qtd_Masculino_3,Qtd_Masculino_2,Qtd_Masculino_1]
    Qtd_Incrito_por_Turma = [Qtd_3,Qtd_2,Qtd_1]

    plt.bar(Series,Qtd_Incrito_por_Turma,color='pink', label="Quantidade de Menina")
    plt.bar(Series,Cont_Genero,color='b',label="Quantidade de Menino")
    plt.legend()
    plt.show()

def Grafico_Esporte_MaisEcolhido():
    Contagem_Futebol = 0
    Contagem_Volei = 0

    Comando = f'''SELECT Esporte FROM Eventos'''
    cursor.execute(Comando)
    resultado = cursor.fetchall()
    i = 0
    for i in range(len(resultado)):
        if resultado[i][0] == "Futebol":
            Contagem_Futebol +=1
        else:
            Contagem_Volei +=1


    Apuração = [Contagem_Futebol,Contagem_Volei]
    plt.pie(Apuração,labels=Esportes,autopct='%1.0f%%')
    plt.legend()
    plt.show()

def Atualizar():
    layout = [
        [sg.Text('Digite o nome do que você quer mudar(Nome, Evento, Turma) e o ID')],
        [sg.Text('Nome: ', size=(10, 1)), sg.Input(key='nome')],
        [sg.Text('ID:', size=(10, 1)), sg.Input(key='id')],
        [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
    ]
    janela = sg.Window('Cadastro de Aluno', layout, element_justification='center')
    evento, dados = janela.read()
    nome_Atualizar = dados['nome']
    id_atualizar = dados['id']

    if nome_Atualizar == 'Evento':
        CadastrarEvento(id_atualizar)
    elif nome_Atualizar == 'Turma':
        CadastrarTurma(id_atualizar)
    else:
        CadastrarAluno(id_atualizar)
    janela.close()

def Listar():
    comando = 'SELECT Nome,Sexo,Esporte FROM Alunos, Eventos where id_Alunos = id_Alunos_fk;'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    layout = [
        [sg.Listbox(values=resultado, size=(30, 6), key='esc')],
        [sg.Button('OK')]
    ]
    janela = sg.Window('esc', layout)
    evento, dados = janela.read()
    janela.close()

def Deletar():
    layout = [
        [sg.Text('Digite o nome do que você quer Deletar(Nome, Evento, Turma) e o ID')],
        [sg.Text('Nome: ', size=(10, 1)), sg.Input(key='nome')],
        [sg.Text('ID:', size=(10, 1)), sg.Input(key='id')],
        [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
    ]
    janela = sg.Window('Cadastro de Aluno', layout, element_justification='center')
    evento, dados = janela.read()
    nome_Atualizar = dados['nome']
    id_atualizar = dados['id']

    if nome_Atualizar == 'Evento':
        comando = f'DELETE from Eventos where id_Eventos= {id_atualizar}'
        cursor.execute(comando)
        conexao.commit()
    elif nome_Atualizar == 'Turma':
        comando = f'DELETE from Turmas where id_Turma= {id_atualizar}'
        cursor.execute(comando)
        conexao.commit()
    else:
        comando = f'DELETE from Alunos where id_Alunos= {id_atualizar}'
        cursor.execute(comando)
        conexao.commit()

    janela.close()


escolha = ''
while escolha != '8 - Sair':

    opções = ['1 - Cadastrar', '2 - Atualizar', '3 - Listar', '4 - Deletar',
              '5 - Gráfico Relação Gênero Turma', '6 - Grafico Esporte mais escolhido', '7 - Grafico Relação Gênero Eventos', '8 - Sair']

    layout = [
        [sg.Listbox(values=opções, size=(30, 10), key='esc')],
        [sg.Button('OK')]
    ]
    janela = sg.Window('Menu principal', layout)
    evento, dados = janela.read()


    escolha = dados['esc'][0]
    janela.close()


    if escolha == '1 - Cadastrar':
          CadastrarAluno(0)
          CadastrarEvento(0)
          CadastrarTurma(0)


    if escolha == '2 - Atualizar':
        Atualizar()
    if escolha == '3 - Listar':
        Listar()

    if escolha == '4 - Deletar':
        Deletar()
    if escolha == '5 - Gráfico Relação Gênero Turma':
        Grafico_Genero_Turma()
    if escolha ==  '6 - Grafico Esporte mais escolhido':
        Grafico_Esporte_MaisEcolhido()
    if escolha == '7 - Grafico Relação Gênero Eventos':
        Grafico_Genero_Esporte()
