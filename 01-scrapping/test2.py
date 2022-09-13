from bs4 import BeautifulSoup
import  urllib.request
import pandas as pd

web ='https://resultados.as.com/resultados/futbol/primera/clasificacion/'
data = urllib.request.urlopen(web).read().decode()
soup = BeautifulSoup(data)

# puntos
score = soup.find_all('td', class_='destacado')
uscore = []

 # equipos
teams = soup.find_all('span', class_='nombre-equipo')
uteams = []

i = 0
# print(score)
for point in score:
    if i <20:
        uscore.append(point.text)
    else: break
    i += 1

# print(team)
i = 0
for team in teams:
    if i < 20:
        uteams.append(team.text)
    else: break
    i += 1
    
df = pd.DataFrame({'Nombre': uteams,'Puntos': uscore}, index =list(range(1,21)))
print(df)