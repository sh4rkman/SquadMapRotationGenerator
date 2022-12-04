#!/usr/bin/python
# -*- coding: utf-8 -*-

# script ecrit par PhiR pour generer une rotation aleatoire a partir d'une liste de layers
# passer le chemin de la liste complete de layers en arguement du script, et un fichier aleatoire sera généré sur la sortie standard
# le fichier de sortie aura exactament une fois chaque map présente dans le fichier d'entrée, quel que soit le nombre de layers présents
# on procède par tirage aléatoire des maps, puis pour chaque map tirage aléatoire parmis les layers disponibles
# attention la version actuelle est case sensitive, il faut respecter les majuscules dans les noms de maps!

import sys

try:
fichier_layer = open(sys.argv[1], 'r')
except:
import traceback
traceback.print_exc()
sys.exit(1)

from collections import defaultdict

maps = set()
layers_par_map = defaultdict(list)
nb_layers = 0

for ligne in fichier_layer.readlines():
ligne = ligne.strip()
if not ligne:
continue
if ligne.startswith('//'):
continue
if ligne.startswith('#'):
continue

map, mode, version = ligne.split('_')

# FIXME case sensitive ?
maps.add(map)
nb_layers += 1
layers_par_map[map].append(ligne)


#print("%d maps" % len(maps))
#print("%d layers" % nb_layers)
#print(layers_par_map)

import random
maps_aleatoire = random.sample(maps, k = len(maps))
#print(maps_aleatoire)

layers_aleatoires = []
for map in maps_aleatoire:
layers_aleatoires.append(random.choice(layers_par_map[map]))

#print(layers_aleatoires)

from datetime import datetime
lignes_sortie = ["// Fichier genere aleatoirement par rotation_random.py le %s" % datetime.now().strftime('%d/%m/%Y a %H:%M'), ]
lignes_sortie.append("// ne pas modifier manuellement car il sera ecrase au prochain lancement")
lignes_sortie.append("// fichier source: %s" % sys.argv[1])
lignes_sortie.append("// %d layers pour %d maps" % (nb_layers, len(maps)))
lignes_sortie.append('')
lignes_sortie += layers_aleatoires
lignes_sortie.append('')

print('\n'.join(lignes_sortie))