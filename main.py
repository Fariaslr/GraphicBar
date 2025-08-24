import matplotlib.pyplot as plt

series = ["6º ano", "6º Filo.","7º ano","7º Filo.", "8º ano", "9º ano"]
mediaTurmas = [7.8, 7.3, 8.3,8.5, 7.3, 7.8]

plt.bar(range(len(series)), mediaTurmas)

plt.title('Média das notas por turma')
plt.ylabel('Notas')

plt.xticks(range(len(series)),series)
plt.ylim(0, 10)
plt.show()
