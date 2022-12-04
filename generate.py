#!/usr/bin/python
# -*- coding: utf-8 -*-

# script ecrit par PhiR pour generer une rotation aleatoire a partir d'une liste de layers
# passer le chemin de la liste complete de layers en arguement du script, et un fichier aleatoire sera généré sur la sortie standard
# le fichier de sortie aura exactament une fois chaque map présente dans le fichier d'entrée, quel que soit le nombre de layers présents
# on procède par tirage aléatoire des maps, puis pour chaque map tirage aléatoire parmis les layers disponibles
# attention la version actuelle est case sensitive, il faut respecter les majuscules dans les noms de maps!

import traceback, random
from datetime import datetime
from collections import defaultdict


inputFile = "source_layers.cfg"
outputFile = "LayerRotation.cfg"
nb_layers = 0
maps = set()
layers_par_map = defaultdict(list)




# -----------------------------------
# OPEN LAYERS SOURCE FILE & LOAD THEM
# -----------------------------------
try:
    fichier_layer = open(inputFile, 'r')
except:
    traceback.print_exc()


for ligne in fichier_layer.readlines():
    ligne = ligne.strip()

    if not ligne:
        continue
    if ligne.startswith('//') or ligne.startswith('#'):
        continue

    map, mode, version = ligne.split('_')
    # FIXME case sensitive ?
    maps.add(map)
    nb_layers += 1
    layers_par_map[map].append(ligne)



# ---------------------
# GENERATE MAP ROTATION
# ---------------------

maps_aleatoire = random.sample(maps, k = len(maps))

layers_aleatoires = []
for map in maps_aleatoire:
    layers_aleatoires.append(random.choice(layers_par_map[map]))


# -------------------------------
# CREATE/OVERIDE MAPROTATION FILE
# -------------------------------
with open(outputFile,"w") as outputFile:
    outputFile.write("// Fichier genere aleatoirement par rotation_random.py le %s\n" % datetime.now().strftime('%d/%m/%Y a %H:%M'))
    outputFile.write("// ne pas modifier manuellement car il sera ecrase au prochain lancement\n")
    outputFile.write("// fichier source: %s\n" % "source_layers.cfg")
    outputFile.write("// %d layers pour %d maps\n" % (nb_layers, len(maps)))
    outputFile.write('\n')
    for layer in layers_aleatoires:
        outputFile.write(f"{layer}\n")
