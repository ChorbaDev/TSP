//
// Created by omar on 14/02/2022.
//

#ifndef TSP_BRUTFORCE_H
#define TSP_BRUTFORCE_H
#include "../../Fichier/fichier.h"

#include <stdbool.h>
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * \struct arrgt
 * \brief Objet Arrangement
 *
 *  Structure stockant tous les arrangements possibles d'une suite de chiffres
 */
typedef struct arrgt {
    int n,    // Le nombre de chiffres différents
    p,    // le nombre de chiffres dans un arrangement
    anp,  // Nombre d'arrangement
    pos,  // Pointeur pour parcourir les arrangement
    **tab; // tableau de "anp" ligne, chaque ligne contient un arrangement
} arrgt;
void recopierTableau(int *t1, int * t2, int taille);
double distanceTrajet(int * tab, Graphe g);
void arrangements(arrgt *arr, int k, int *L, int *t);
void brutForce(Graphe g, int villeDep);
#endif //TSP_BRUTFORCE_H
