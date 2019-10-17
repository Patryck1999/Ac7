import sqlite3
from model.disciplina import Disciplina
from contextlib import closing

db_name = "disciplinas.db"
model_name = "disciplina"
model_name_relationship = "disciplina_aluno"

def con():
    return sqlite3.connect(db_name)

def listar():
        with closing(con()) as connection, closing(connection.cursor()) as cursor:
                cursor.execute(f"SELECT id, nome, id_professor FROM {model_name}")
                rows = cursor.fetchall()
                registros = []
                for (id, nome, id_professor) in rows:
                        disciplina = Disciplina.criar_com_id(id, nome, id_professor)
                if disciplina != None:
                        registros.append(disciplina)
                return registros

def consultar(id):
        with closing(con()) as connection, closing(connection.cursor()) as cursor:
                cursor.execute(f"SELECT id, nome, id_professor FROM {model_name} WHERE id = ?", (id,))
                row = cursor.fetchone()
                if row == None:
                        return None
                return Professor.criar_com_id(row[0],row[1],row[2])

def consultar_por_nome(nome):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT id, nome, id_professor FROM {model_name} WHERE nome = ?", (nome,))
        pass

def cadastrar(disciplina):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (nome, id_professor) VALUES (?, ?)"
        result = cursor.execute(sql, (disciplina.nome, disciplina.id_professor))
        connection.commit()
        if cursor.lastrowid:
            disciplina.associar_id(cursor.lastrowid)
            return disciplina
        else:
            return None

def alterar(disciplina):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET nome = ?, id_professor = ? WHERE id = ?"
        result = cursor.execute(sql, (disciplina.nome, disciplina.id_professor, disciplina.id))
        connection.commit()
        return result

def remover(disciplina):
    pass

#Disciplina-aluno

def cadastrar_aluno(disciplina, aluno_id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name_relationship} (disciplina_id, aluno_id) VALUES (?, ?)"
        result = cursor.execute(sql, (disciplina.id, aluno_id))
        pass
            
def remover_aluno(disciplina, aluno_id):
    pass
    
def consultar_alunos(disciplina):
    pass
    