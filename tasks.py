from invoke import task, run

@task
def check(c):
    '''
    Comprobador de la sintaxis del proyecto
    '''
    print("Comprobando sintaxis...")
    run("pyflakes code") # El directorio con todo el código de la aplicación

@task
def test(c):
    '''
    Realiza los tests del proyecto
    '''
    print("Realizando los tests...")
    run("pytest")