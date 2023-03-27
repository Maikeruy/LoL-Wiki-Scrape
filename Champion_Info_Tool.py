import requests
import PySimpleGUI
from bs4 import BeautifulSoup

def get_champion_info(champion_name):
    url = 'https://leagueoflegends.fandom.com/wiki/'+champion_name+'/LoL'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    champion_info = {
        'Health': soup.find(id='Health_'+champion_name),
        'Mana': soup.find(id='ResourceBar_'+champion_name),
        'Armor': soup.find(id='Armor_'+champion_name),
        'Magic_Resist': soup.find(id='MagicResist_'+champion_name),
        'Attack_Damage': soup.find(id='AttackDamage_'+champion_name)
    }
    return champion_info

layout = [[PySimpleGUI.Text('Champion:'), PySimpleGUI.InputText()],
          [PySimpleGUI.Button('Ok'), PySimpleGUI.Button('Cancel')],
          [PySimpleGUI.Text('Health: '),PySimpleGUI.Text('', key='Health'), 
           PySimpleGUI.Text('Mana: '),PySimpleGUI.Text('', key='Mana')],
          [PySimpleGUI.Text('Armor: '),PySimpleGUI.Text('', key='Armor'), 
           PySimpleGUI.Text('Magic Resist: '),PySimpleGUI.Text('', key='magic_Resist')],
          [PySimpleGUI.Text('Attack Damage: '),PySimpleGUI.Text('', key='attack_Damage')],
          [PySimpleGUI.Text('', key='status')]]

window = PySimpleGUI.Window('LoL-Tool', layout)

while True:
    event, values = window.read()
    window['status'].update('')
    if event == 'Ok':
        try:
            champion_Info = get_champion_info(values[0])
            window['Health'].update(champion_Info["Health"].text.strip())
            window['Mana'].update(champion_Info["Mana"].text.strip())
            window['Armor'].update(champion_Info["Armor"].text.strip())
            window['magic_Resist'].update(champion_Info["Magic_Resist"].text.strip())
            window['attack_Damage'].update(champion_Info["Attack_Damage"].text.strip())
        except:
            window['status'].update('Make sure you typed the champions name correct')
            continue
    elif event == "Cancel" or event == PySimpleGUI.WIN_CLOSED:
        window.close()
        break
