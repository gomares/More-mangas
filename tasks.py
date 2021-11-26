from invoke import task, run

@task
def check(c):
    '''
    Comprobador de la sintaxis del proyecto
    '''
    print("Comprobando sintaxis...")
    run("pylint -E manga")

@task
def test(c):
    '''
    Realiza los tests del proyecto
    '''
    print("No hay tests disponibles...")