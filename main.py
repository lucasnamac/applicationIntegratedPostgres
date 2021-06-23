import psycopg2
import json
import time

DBHOST = "200.131.206.13"
DATABASE = "lucasnm"
USER = "lucasnm"
PASSWORD = "f1g1a5b4c3d2e1"
PORT = "5432"
SCHEMA = "universidade"



def createConnection():
  mydb = psycopg2.connect(
    host= DBHOST,
    database=DATABASE,
    user=USER,
    password=PASSWORD,
    port = PORT,
    options = f'-c search_path={SCHEMA}'
  )
  return mydb

def menu():
    print("----------------")
    print("1 - Inserir")
    print("2 - Deletar")
    print("3 - Consultar")
    print("4 - Alterar")
    print("5 - Transação na tabela faculdade e turma")
    print("6 - Inserir Trigger")
    print("0 - Sair")
    print("----------------")

def insertOption(mydb):
    print("Escolha a opcao que deseja: ")
    print("1 - Inserir um aluno")
    print("2 - Inserir um professor")
    insertOption = int(input())
    if insertOption == 1:
        insertStudent(mydb)
    elif insertOption == 2:
        insertProfessor(mydb)
    else:
        print("Invalid option...")
        time.sleep(1)
        print("Exiting")
        time.sleep(1)
        exit

def deleteOption(mydb):
    print("Escolha a opcao que deseja: ")
    print("1 - Excluir um aluno")
    print("2 - Excluir um professor")
    insertOption = int(input())
    if insertOption == 1:
        deleteStudent(mydb)
    elif insertOption == 2:
        deleteProfessor(mydb)
    else:
        print("Invalid option..")
        time.sleep(1)
        print("Exiting")
        time.sleep(1)
        exit

def updateOption(mydb):
    print("Escolha a opcao que deseja: ")
    print("1 - Alterar uma disciplina")
    print("2 - Alterar uma turma")
    print("3 - Alterar matricula")
    insertOption = int(input())
    if insertOption == 1:
        updateDisciplina(mydb)
    elif insertOption == 2:
        updateTurma(mydb)
    elif insertOption == 3:
        updateMatricula(mydb)
    else:
        print("Invalid option...")
        time.sleep(1)
        print("Exiting")
        time.sleep(1)
        exit

def insertStudent(mydb):
    print("Digite os dados do aluno")
    id_aluno = int(input("ID Aluno: "))
    id_faculdade = int(input("ID Faculdade: "))
    nome_aluno = input("Nome Aluno: ")
    cra_aluno = int(input("CRA Aluno: "))  
    datanasc_aluno = input("Data Nascimento Aluno: ")
    telefone_aluno = input("Telefone Aluno: ")
    
    mycursor = mydb.cursor()
    try:
        query = f"insert into aluno values({id_aluno}, {id_faculdade}, '{nome_aluno}', {cra_aluno},'{datanasc_aluno}', {telefone_aluno})"
        mycursor.execute(query)
        mydb.commit()
        print("------Aluno inserido com sucesso------")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertProfessor(mydb):
    print("Digite os dados do professor")
    id_professor = int(input("ID Professor: "))
    id_faculdade = int(input("ID Faculdade: "))
    nome_prof = input("Nome Professor: ")
    datanasc_prof = input("Data Nascimento Professor: ")
    salario_prof = input("Salario Professor: ")

    mycursor = mydb.cursor()
    try:

        query = f"insert into Professor values ({id_professor}, {id_faculdade}, '{nome_prof}', '{datanasc_prof}', {salario_prof})"      
        mycursor.execute(query)
        mydb.commit()
        print("------Professor inserido com sucesso------")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def deleteStudent(mydb):
    idaluno = int(input("Digite o ID do aluno que deseja excluir: "))
    mycursor = mydb.cursor()
    try:
        query = """Delete from aluno where idaluno = %s"""
        mycursor.execute(query, (idaluno,))
        mydb.commit()
        print("------Aluno removido com sucesso------")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def deleteProfessor(mydb):
    idprofessor = int(input("Digite o ID do professor que deseja excluir: "))
    mycursor = mydb.cursor()
    try:
        query = """Delete from professor where idprofessor = %s"""
        mycursor.execute(query, (idprofessor,))
        mydb.commit()
        print("------Professor removido com sucesso------")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def consultTable(mydb):
    options = ["Aluno", "Professor", "Disciplinas", "Faculdade", "Turma", "Salaaula"]
    print("Selecione qual tabela deseja consultar:")
    print( "1 - Aluno")
    print( "2 - Professor")
    print( "3 - Disciplinas")
    print( "4 - Faculdade")
    print( "5 - Turma")
    print( "6 - Salaaula")

    option = int(input())
    table = options[option-1]
    table.format()

    mycursor = mydb.cursor() 
    try:
        query = f"SELECT * FROM {table}"
        mycursor.execute(query)
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        for tuple in mycursor.fetchall():
            print(tuple)
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print(f"------Tabela {table} consultada com sucesso------")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def updateDisciplina(mydb):
    options = ["sigladisciplina", "nome", "creditos", "prerequisito"]
    id_update = int(input("Informe o ID da disciplina que deseja alterar:"))

    print("Informe os dados que deseja alterar")
    print("1 - Sigla disciplina")
    print("2 - Nome")
    print("3 - Creditos")
    print("4 - Pre requisito") 
    
    option_update = int(input())

    field_update = options[option_update-1]
    field_update.format()
    
    if(option_update ==2 or option_update==1):
        new_value = input("Informe o valor a ser alterado: ")
        query = f"UPDATE disciplinas SET {field_update} = '{new_value}' where iddisciplina ={id_update}"
    else:
        new_value = int(input("Informe o novo valor do campo a ser alterado: "))
        query = f"UPDATE disciplinas SET {field_update} = {new_value} where iddisciplina ={id_update}"


    mycursor = mydb.cursor()
    try:
        

        mycursor.execute(query)
        mydb.commit()
        print("Tabela Disciplinas alterada com sucesso!")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def updateTurma(mydb):
    options = ["ano", "semestre", "localministrado", "nsala"]
    
    id_update = int(input("Informe o ID da turma que deseja alterar:"))

    print("Informe os dados que deseja alterar")
    print("1 - Ano")
    print("2 - Semestre")
    print("3 - Local ministrado")
    print("4 - Numero de sala") 
    
    option_update = int(input())

    field_update = options[option_update-1]
    field_update.format()

    if(option_update == 3):
        new_value = input("Informe o valor a ser alterado: ")
        query = f"UPDATE turma SET {field_update} = '{new_value}' where idturma ={id_update}"
        
    else:
        new_value = int(input("Informe o novo valor do campo a ser alterado: "))
        query = f"UPDATE turma SET {field_update} = {new_value} where idturma ={id_update}"


    mycursor = mydb.cursor()
    try:
        mycursor.execute(query)
        mydb.commit()
        print("Tabela Turma alterada com sucesso!")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


def updateMatricula(mydb):
    options = ["notas", "faltas"]

    id_matricula = int(input("Digite o ID que deseja alterar: "))

    print("Digite a opção correspondente a que quer alterar")
    print("1 - Notas")
    print("2 - Faltas")
    option_update = int(input())

    field_update = options[option_update-1]
    field_update.format()

    new_value = int(input("Digite o novo valor do campo: "))

    mycursor = mydb.cursor()

    try:
        query = f"UPDATE matricula SET {field_update} = {new_value} WHERE idmatricula = {id_matricula}"

        mycursor.execute(query)
        mydb.commit()

        print("------Dados alterados com sucesso-------")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)




def createTransaction(mydb):
    print("Digite os valores para Faculdade!")
    id_faculdade = int(input("Informe o ID faculdade: "))
    orcamento_faculdade = int(input("Informe o orcamento da faculdade: "))

    print("Digite os valores para Turma")
    id_turma = int(input("Informe o ID Turma: "))
    localministrado_turma = input("Informe o local ministrado: ")
    
    
    mycursor = mydb.cursor()

    try:
        query1 = f" BEGIN; UPDATE faculdade SET orcamento = {orcamento_faculdade} WHERE idfaculdade = {id_faculdade};"
        
        query2 = f"UPDATE turma SET localministrado = '{localministrado_turma}' WHERE idturma = {id_turma}; COMMIT;"

        mycursor.execute(query1)
        mycursor.execute(query2)
        mydb.commit()
        print("Transação Efetuada")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


def insertTrigger(mydb):
    
    mycursor=mydb.cursor()

    try:
        query_procedure = "SET SEARCH_PATH TO universidade; CREATE OR REPLACE FUNCTION cadastramatricula() RETURNS TRIGGER as $$ DECLARE command TEXT;BEGIN command = 'INSERT INTO matricula values' ||'(' || quote_literal(NEW.idaluno) || ',' || quote_literal (NEW.idaluno)||','|| '(SELECT floor(random() * ((0)- (select count(*) from universidade.turma)+1) + (select count(*) from universidade.turma)))' ||')'; EXECUTE command; RETURN NEW; END; $$ LANGUAGE plpgsql;"

        
        mycursor.execute(query_procedure)
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    try:
        query_trigger = "CREATE TRIGGER cadastra AFTER INSERT ON aluno FOR EACH ROW EXECUTE PROCEDURE cadastramatricula();"

        mycursor.execute(query_trigger)
        print("Trigger Inserida")    
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        

def main():
  mydb = createConnection()
  menu()
  opcao = int(input("Digite a opção: "))

  while(opcao!=0):

    if(opcao ==1):
        insertOption(mydb)         
    elif(opcao ==2):
        deleteOption(mydb)
    elif(opcao ==3):
        consultTable(mydb)
    elif(opcao ==4):
        updateOption(mydb)
    elif(opcao == 5):
        createTransaction(mydb)
    elif(opcao == 6):
        insertTrigger(mydb)
    else:
        print("Invalid option...")
        time.sleep(1)
        print("Try again")
        time.sleep(1)
          
    menu()
    opcao = int(input("Digite uma nova opção: "))


  mydb.close()


if __name__ == '__main__':
  main()