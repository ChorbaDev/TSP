#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "../C/BruteForce/BruteForce.c"
#include "../C/NearestNeighbour/NearestNeighbour.c"
#include "../C/Random/Random.c"
typedef int ** Graphe;

// lecture des données dans un fichier et construction du graphe
int lire_data(char * nom, Graphe * g, int *n, int *m);

// affichage du graphe, i.e. du tableau des distances
void affiche_km(int ** g, int n);
void affiche_path(int * path, int n);
int main()
{
    clock_t t1, t2;
    double cpu_boucle;
    unsigned long i, yam=0;
	char nom[30];
	Graphe G = NULL;
	int n, m;
	int err;
		
	do
	{
		printf("saisir le nom de fichier de données : ");
		scanf("%s", nom); while(getchar() != '\n');
        char *ch= malloc(sizeof(char)*100);
        strcat(ch,"../../../communes/communes/");
        strcat(ch,nom);
		err = lire_data(ch, &G, &n, &m);
	}
	while(err == 0);
    affiche_km(G, n);
    int path[n];
    for (int i = 0; i < n-1; ++i) {
        path[i]=-1;
    }

    t1 = clock();
    printf("Vous voulez utiliser quelle algo?\n"
           "1-Plus proche voisin\n"
           "2-Aléatoire\n"
           "3-Brute Force\n");
    int reponse;
    do {
        scanf("%d",&reponse);
    }while(reponse<1 || reponse>3);
    switch (reponse) {
        case 1:NearestNeighbour(G,n,0,path);break;
        case 2:randomPath(G,0,n,path,10000);
        case 3:BruteForce(G,n,0,path);
        default:break;
    }
    t2 = clock();
    printf("nombre de ticks d'horloge avant la boucle : %lu\n", t1);
    printf("nombre de ticks d'horloge après la boucle : %lu\n", t2);
    cpu_boucle = (double)(t2-t1)/(double)(CLOCKS_PER_SEC);
    printf("temps cpu de la boucle en secondes %f\n", cpu_boucle);
    affiche_path(path,n);
    printf("\n%d", routeLength(G,n,path));
}

int lire_data(char * nom, Graphe * g, int *n, int *m)
{
	char str[15];
	int i, s1, s2, km;
	FILE * f = fopen(nom, "r");
	
	if (f == NULL) return 0; // le fichier n'existe pas
	
	// la première ligne contient le nombre de sommets n et le nombre d'arêtes m
	fgets(str, 15, f);
	sscanf(str, "%d %d", n, m);
	
	// allocation dynamique d'un tableau n x n rempli de 0
	*g = (int **)calloc(sizeof(int *), *n);
	for (i = 0; i < *n; i++) (*g)[i] = (int *)calloc(sizeof(int), *n);

	// lecture du fichier et remplissage du tableau G
	for (i = 0; i < *m; i++)
	{
		fgets(str, 15, f);
		sscanf(str, "%d %d %d", &s1, &s2, &km);
		(*g)[s1][s2] = km;
		(*g)[s2][s1] = km;
	}
	fclose(f);
	return 1;
}

void affiche_km(Graphe g, int n)
{
	int i, j;

	for(i = 0; i < n; i++)
	{
		for(j = 0; j < n; j++)
            printf("%5d ", g[i][j]);
		printf("\n");
	}
}