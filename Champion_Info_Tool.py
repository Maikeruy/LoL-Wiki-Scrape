import requests
import PySimpleGUI
from bs4 import BeautifulSoup


layout = [[PySimpleGUI.Text('Champion:'), PySimpleGUI.InputText()],
          [PySimpleGUI.Button('Ok'), PySimpleGUI.Button('Cancel')],
          [PySimpleGUI.Text('Health: '),PySimpleGUI.Text('', key='Health'), PySimpleGUI.Text('Mana: '),PySimpleGUI.Text('', key='Mana')]]
window = PySimpleGUI.Window('LoL-Tool', layout)

while True:
    event, values = window.read()
    if event == 'Ok':
        try:
            response = requests.get('https://leagueoflegends.fandom.com/wiki/'+values[0]+'/LoL')
            soup = BeautifulSoup(response.content, 'html.parser')
            class champion_Info:  # Contains Chamion info
                Health = soup.find(id='Health_'+values[0])
                Mana = soup.find(id='ResourceBar_'+values[0])
                Armor = soup.find(id='Armor_'+values[0])
                magic_Resist = soup.find(id='MagicResist_'+values[0])
                attack_Damage = soup.find(id='AttackDamage_'+values[0])
            window['Health'].update(champion_Info.Health.text.strip())
            window['Mana'].update(champion_Info.Mana.text.strip())
        except:
            window['status'].update('Make sure that you insert a Youtube link')
            continue
    elif event == "Cancel" or event == PySimpleGUI.WIN_CLOSED:
        window.close()
        break
