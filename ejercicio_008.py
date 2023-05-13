#Notas aprobados
notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5,
'Luis': 5}

sort_notas = sorted(notas.items(), key=lambda x: x[1], reverse=True)

for i in sort_notas:
	if i[1] >= 6:
		print(i[0], i[1])