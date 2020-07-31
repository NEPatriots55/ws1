import requests 
import pandas as pd 
from bs4 import BeautifulSoup as BS
from sys import argv
import json
import numpy as np

url = requests.get('http://se7en.ws/cod-warzone-guns-weapon-stats-damage-stats-dropoff-graphs-recoil-patterns-best-guns-in-warzone/?lang=en')


soup = BS(url.content, 'html.parser')
table = soup.find_all(class_='tablepress')
table_df = str(table)

df = pd.read_html(table_df)

weapons_df = np.array(df, dtype=object)


df1 = weapons_df[0]
assault_rifle_df = pd.DataFrame(df1)
assault_rifle_df.set_index('Name', inplace=True)
columns_to_drop = ['Recoil Patterns (Screenshots supply: TheXclusiveAce)', 'Damage Dropoffs (Bodyshots to kill at 100HP) (Data supply: TheXclusiveAce)']
columns_to_drop1 = ['Shots To Kill.1', 'Shots To Kill.2', 'Shots To Kill.3']
assault_rifle_df.drop(columns_to_drop, axis=0, inplace=True)
assault_rifle_df.drop(columns_to_drop1, axis=1, inplace=True)


df2 = weapons_df[1]
smg_df = pd.DataFrame(df2)
smg_df.set_index('Name', inplace=True)
columns_to_drop = ['Recoil Patterns (Screenshots supply: TheXclusiveAce)', 'Damage Dropoffs (Bodyshots to kill at 100HP) (Data supply: TheXclusiveAce)']
columns_to_drop1 = ['Shots To Kill.1', 'Shots To Kill.2', 'Shots To Kill.3']
smg_df.drop(columns_to_drop, axis=0, inplace=True)
smg_df.drop(columns_to_drop1, axis=1, inplace=True)


df3 = weapons_df[2]
lmg_df = pd.DataFrame(df3)
lmg_df.set_index('Name', inplace=True)
columns_to_drop = ['Recoil Patterns (Screenshots supply: TheXclusiveAce)', 'Damage Dropoffs (Bodyshots to kill at 100HP) (Data supply: TheXclusiveAce)']
columns_to_drop1 = ['Shots To Kill.1', 'Shots To Kill.2', 'Shots To Kill.3']
lmg_df.drop(columns_to_drop, axis=0, inplace=True)
lmg_df.drop(columns_to_drop1, axis=1, inplace=True)


df4 = weapons_df[3]
marksman_rifle_df = pd.DataFrame(df4)
marksman_rifle_df.set_index('Name', inplace=True)
columns_to_drop = ['Damage Dropoffs (Bodyshots to kill at 100HP) (Data supply: TheXclusiveAce)']
columns_to_drop1 = ['Shots To Kill.1', 'Shots To Kill.2', 'Shots To Kill.3']
marksman_rifle_df.drop(columns_to_drop, axis=0, inplace=True)
marksman_rifle_df.drop(columns_to_drop1, axis=1, inplace=True)


df5 = weapons_df[4]
sniper_df = pd.DataFrame(df5)
sniper_df.set_index('Name', inplace=True)
columns_to_drop1 = ['Shots To Kill.1', 'Shots To Kill.2', 'Shots To Kill.3', 'Move %']
sniper_df.drop(columns_to_drop1, axis=1, inplace=True)


df6 = weapons_df[5]
shotgun_df = pd.DataFrame(df6)
shotgun_df.set_index('Name', inplace=True)
columns_to_drop1 = ['Shots To Kill.1', 'Shots To Kill.2', 'Shots To Kill.3']
shotgun_df.drop(columns_to_drop1, axis=1, inplace=True)


df6 = weapons_df[-1]
pistol_df = pd.DataFrame(df6)
pistol_df.set_index('Name', inplace=True)
columns_to_drop1 = ['Shots To Kill.1', 'Shots To Kill.2', 'Shots To Kill.3']
pistol_df.drop(columns_to_drop1, axis=1, inplace=True)

weapon_type = input(' What type of weapon is it? (Assault Rifle, SMG, LMG, Marksman Rifle, Sniper Rifle, Shotgun, or Pistol) ')

if weapon_type == 'Assault Rifle':
    weapon_model = input(' What model assualt rifle is it? (FAL, M4A1, FR 5.56, Oden, M13, FN Scar, AK-47, RAM-7, Grau 5.56)    ')
    ar_weapon_stats = assault_rifle_df.loc[weapon_model] 
    print(ar_weapon_stats)
    

if weapon_type == 'SMG':
    weapon_model = input(' What model SMG is it? (AUG, P90, MP5, Uzi, Bizon, MP7, Striker 45)    ')
    smg_weapon_stats = smg_df.loc[weapon_model] 
    print(smg_weapon_stats)


if weapon_type == 'LMG':
    weapon_model = input(' What model LMG is it? (PKM, SA87, M91, MG34, Holger-26)    ')
    lmg_weapon_stats = lmg_df.loc[weapon_model] 
    print(lmg_weapon_stats)


if weapon_type == 'Marksman Rifle':
    weapon_model = input(' What model marksman rifle is it? (EBR, Carbine, Kar98Ok)    ')
    marksman_weapon_stats = marksman_rifle_df.loc[weapon_model] 
    print(marksman_weapon_stats)


if weapon_type == 'Sniper Rifle':
    weapon_model = input(' What model sniper rifle is it? (Dragunov, HDR, AX-50)    ')
    sniper_weapon_stats = sniper_df.loc[weapon_model] 
    print(sniper_weapon_stats)


if weapon_type == 'Shotgun':
    weapon_model = input(' What model shotgun is it? (Model 680, R9-0, 725, Origin 12, VLK Rogue)    ')
    shotgun_weapon_stats = shotgun_df.loc[weapon_model] 
    print(shotgun_weapon_stats)


if weapon_type == 'Pistol':
    weapon_model = input(' What model Pistol is it? (X16, 1911, .357, M19, .50 GS)    ')
    pistol_weapon_stats = pistol_df.loc[weapon_model] 
    print(pistol_weapon_stats)



#weapon_stats = 'FAL'
#assault_rifle_df.to_csv('ws3.csv')

