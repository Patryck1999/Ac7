# Exceção lançada quando se tenta associar um ID a uma entidade que já possui um.
class NaoTransienteException(Exception):
    pass

class AlunoJaInclusoException(Exception):
    pass

class Disciplina():
    
    def __init__(self, nome, professor_id):
        self.id = None
        self.nome = nome
        self.professor_id = professor_id
        self.alunos = []
    
    def associar_id(self, id):
        if self.id != None:
            raise NaoTransienteException
        self.id = id
    
    def incluir_aluno(self, aluno_id):
        try:
            for aluno in range self.alunos:
                if aluno == aluno_id:
                    raise AlunoJaInclusoException

            self.alunos.append(aluno_id)
        except Exception as e:
            print("Problema ao incluir aluno na disciplina!")
            print(e)
    
    def associar_alunos(self, alunos):
        if self.alunos != None:
            raise NaoTransienteException
        self.alunos = alunos
    
    def remover_aluno(self, aluno_id):
        try:
            self.alunos.remove(aluno_id)
        except Exception as e:
            print("Problema ao remover aluno da disciplina!")
            print(e)
    
    def verificar_transiente(self):
        if self.id != None:
            return False
        return True
    
    def validar(self):
        if self.nome != None and self.professor_id != None:
            return True
        return False
    
    def atualizar(self, dados):
        try:
            nome = dados["nome"]
            professor_id = dados["professor_id"]
            self.nome, self.professor_id = nome, professor_id
            return self
        except Exception as e:
            print("Problema ao atualizar!")
            print(e)

    def __dict__(self):
        d = dict()
        d['id'] = self.id
        d['nome'] = self.nome
        d['professor_id'] = self.professor_id
        return d

    @staticmethod
    def criar(dados):
        try:
            nome = dados["nome"]
            professor_id = dados["professor_id"]
            return Professor(nome=nome, professor_id=professor_id)
        except Exception as e:
            print("Problema ao criar nova disciplina!")
            print(e)
    
    @staticmethod    
    def criar_com_id(id, nome, professor_id):
        try:
            disciplina = Disciplina(nome=nome, professor_id=professor_id)
            disciplina.associar_id(id)
            return disciplina
        except Exception as e:
            print("Problema ao criar nova disciplina!")
            print(e)