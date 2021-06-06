import psycopg2
import json

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
  print("1 - Inclusão de um aluno")
  print("2 - Inclusão de um professor")
  print("2 - Deleção")
  print("3 - Consultar")
  print("4 - Alteração")
  print("0 - Sair")

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
    query = f"insert into Aluno values({id_aluno}, {id_faculdade}, {nome_aluno}, {cra_aluno},{datanasc_aluno}, {telefone_aluno}"

    #res_insert_query ="""insert into Aluno values(%s, %s, %s, %s, %s, %s)"""
    #d_to_insert=(id_aluno, id_faculdade, nome_aluno, cra_aluno, datanasc_aluno, telefone_aluno)
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

    query = f"insert into Professor values ({id_professor}, {id_faculdade}, {nome_prof}, {datanasc_prof}, {salario_prof})"

    #res_insert_query ="""insert into Professor values(%s, %s, %s, %s, %s)"""
    #d_to_insert=(id_professor, id_faculdade, nome_prof, datanasc_prof, salario_prof)
    
    mycursor.execute(query)
    mydb.commit()
    print("------Professor inserido com sucesso------")
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


  new_value = int(input("Informe o novo valor do campo a ser alterado"))

  mycursor = mydb.cursor()
  try:
    query = f"UPDATE disciplinas SET {field_update} = {new_value} where iddisciplina ={id_update}"

    mycursor.execute(query)
    mydb.commit()
  except(Exception, psycopg2.DatabaseError) as error:
    print(error)
    
    



def delete():
  print('a')
def consult():
  print('a')



'''
conter inclusão, alteração, exclusão e consulta 

'''

#print(mydb)
def main():
  mydb = createConnection()
  menu()
  opcao = int(input("Digite a opção: "))

  while(opcao!=0):
    if(opcao ==1):
      insertStudent(mydb)
    if(opcao ==2):
      insertProfessor(mydb)
    if(opcao ==4):
      updateDisciplina(mydb)
    menu()
    opcao = int(input("Digite uma nova opção: "))


  mydb.close()


if __name__ == '__main__':
  main()