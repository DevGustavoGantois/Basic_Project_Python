print("<--------------------------->")
print("LIST OF TASKS")
print("<-------------------------->")
print("Hello User. Welcome!")

#Criei uma função principal para o meu programa.
def main():
#Criei uma lista tasks na função principal, pois usarei ela em todo o meu projeto.
    tasks = []
#Criei um loop de repetição infinito, caso o usuário digite 'exit the program' o programa irá sair.
    while True:
#Adicionando todas as opções de listas de tarefas:
        print("1 => Add Tasks.")
        print("2 => List Tasks.")
        print("3 => Mark tasks as completed.")
        print("4 => Display tasks by priority.")
        print("5 => Remove tasks. ")
        print("6 => Enter 'exit the program' to exit.")
        print("<---------------------------------------->")
#Criando a variável opções para escolher entre uma dessas acima.
        option = input("Enter a option of tasks:")

        if option == 'exit the program':
            print("Finish the program, thank you User!!")
            break
         
        if option == '1':
#Se opção for igual ao número 1 ele vai chamar a função add_tasks(tasks)
            add_tasks(tasks)
        elif option == '2':
#Se a opção for igual ao número 2 ele vai chamar a função list_tasks(tasks)
            list_tasks(tasks)
        elif option == '3':
#Se a opção for igual ao número 3 ele vai chamar a função mark_Tasks_completed(tasks)
            mark_Tasks_completed(tasks)
        elif option == '4':
#Se a opção for igual ao número 4 ele vai chamar a função display_tasks_by_Priority(tasks)
            display_Tasks_by_Priority(tasks)
        elif option == '5':
#Se a opção for igual ao número 5 ele vai chamar a função remove_tasks(tasks)
            remove_tasks(tasks)
        else:
#Caso outro número for digitado ele vai mostrar uma mensagem de erro, e vai reiniciar o programa.
            print("Invalid option. Please select the option (1-5).")


#Criei uma função adicionar tarefas => add_tasks(tasks) atribuindo a lista da minha função principal
def add_tasks(tasks):
    #Criei um input para cada especificidade das tarefas:
    name = input("Add name for task:")
    description = input("Describe the task:")
    priority = input("What level the priority of the task:")
    category = input("What is the category of the task:")
    add_task = {'name': name, 'description': description, 'priority': priority, 'category': category, 'Completed': False  }
    tasks.append(add_task)
    #Adicionando todas as tarefas ao dicionário tasks.
    #Depois adiciono a lista.

def list_tasks(tasks):
#Listando as tarefas através do loop de repetição for:
    for task in tasks:
        print(task)

def mark_Tasks_completed(tasks):
#Utilizando o input para o usuário marcar a tarefa que ele quiser completa.
    task_name = input("Enter the name of the task to mark as completed:")
    #Criando um laço de repetição for task in tasks na "lista global". 
    for task in tasks:
    #Se a tarefa localizada no nome for igual a 'completed' ela será verdadeira e validada
        if task['name'] == task_name:
            task['Completed'] = True
            #Mostraremos no programa que a tarefa foi validada através do print e depois utilizando um return
            print(f"Task '{task_name}' marked as completed.")
            return
        #Se task['Completed'] não for = True ela será constada como "Task not found"
        print("Task not found.")

def display_Tasks_by_Priority(tasks):
        #Criei um input novamente para o usuário caso o usuário digitar que a tarefa é prioridade ela irá ser destacada.
        priority_level = input("Is there a task you want to mark as a priority:")
        #Criei um laço de repetição for percorrendo a lista tasks:
        for task in tasks:
            #Se tarefa for prioridade ele irá utilizar este input
            if task['priority'] == priority_level:
            #Mostrando a tarefa e o nome da tarefa através do dicionário.
                print(task['name'])

def remove_tasks(tasks):
        #Criei um input para interação do usuário caso ele queira remover alguma tarefa
        remove_task = input("Dou you have any activity you want to remove:")
        #Criei um laço de repetição for para percorrer toda a lista tasks na função principal.
        for task in tasks:
            #Se tasks['name'] for igual a remove_task ele irá remover o nome da tarefa na lista.
            if task['name'] == remove_task:
                task.remove(tasks)
            #Depois ele mostrara que a task em questão foi removida com sucesso.
                print(f"Task '{remove_task}' removed successfully.")
                return
            #Retornando a função, caso ela for falsa irá mostrar como no print("Task not found")
            print("Task not found.")

#Criei um if __name__ == '__main__': para dar prioridade a essa função como a função principal que irá mover o meu projeto.        
if __name__ == '__main__':
    main()

#CRIEI VÁRIAS FUNÇÕES REUTILIZAVEIS PARA CASO PRECISE AJUSTAR O CÓDIGO FEITO.
    

#OBS: Sei que o uso de comentários excessivos não é uma prática do CLEAN CODE, porém utilizei comentários excessivos para fixar meu aprendizado neste projeto.