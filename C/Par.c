#include <stdio.h>
#include <stdlib.h>

int main() {
	int numero;

	puts("Introduzca un número cualquiera:");
	scanf("%d", &numero);

	do {
		if(numero % 2 == 0) {
			printf("Es un número par.\n");
		} else {
			printf("Es un número inpar.\n");
		}

		puts("");
		puts("Introduzca un número cualquiera:");
		scanf("%d", &numero);
	} while(numero >= 1);
	
	return EXIT_SUCCESS;
}
