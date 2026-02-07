#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int tamanyoCadena(char * palabra) {
	int contador = 0;

	while(palabra[contador] != '\0') {
		contador++;
	}

	return contador;
}

char * invertirCadena(char * palabra) {
	int tamanyo = tamanyoCadena(palabra) - 1;
	int limite = tamanyo / 2;
	int contador = 0;
	char temporal;

	while(contador <= limite) {
		temporal = palabra[contador];
		palabra[contador] = palabra[tamanyo - contador];
		palabra[tamanyo - contador] = temporal;

		contador++;
	}

	return palabra;
}

int main() {
	char palabra[10] = "Mujer";

	printf("Palabra antes: %s\n", palabra);

	invertirCadena(palabra);

	printf("Palabra después: %s\n", palabra);

	return EXIT_SUCCESS;
}
