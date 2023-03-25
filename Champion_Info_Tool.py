import requests
from bs4 import BeautifulSoup

print('Champion: ')
search = input()

response = requests.get(
    'https://leagueoflegends.fandom.com/wiki/'+search+'/LoL')
soup = BeautifulSoup(response.content, 'html.parser')

class champion_Info: #Contains Chamion info
    Health = soup.find(id='Health_'+search)
    Mana = soup.find(id='ResourceBar_'+search)
    Armor = soup.find(id='Armor_'+search)
    magic_Resist = soup.find(id='MagicResist_'+search)
    attack_Damage = soup.find(id='AttackDamage_'+search)


print("Health: "+champion_Info.Health.text.strip())
print("Mana: "+champion_Info.Mana.text.strip())
print("Armor: "+champion_Info.Armor.text.strip())
print("Magic Resist: "+champion_Info.magic_Resist.text.strip())
print("Attack Damage: "+champion_Info.attack_Damage.text.strip())
