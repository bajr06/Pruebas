#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>

#define MAX_NOMBRE 50
#define HORARIO 5
#define MAX_ESTUDIANTE 10

/* 
 * 	Autor: Bryan Andreu Jiménez Rojas.
 *	Curso: Desarrollo de Aplicaciones Multiplataforma 1.
*/ 

typedef struct{
	char nombre[MAX_NOMBRE];
	float calificacion;
	int horarios_disponibles[HORARIO];
} Estudiante;

void organizar(Estudiante *notas){
	for(int i = 0; i < MAX_ESTUDIANTE; i++, turnos++){
		if()
	}
}

void asignar_turnos(Estudiante *turnos){
	for(int j = 0; j < MAX_ESTUDIANTE; j++, turnos++){
		switch(turnos -> calificacion){
			case 10
		}

	}
}

int main(){
	Estudiante Clase[MAX_ESTUDIANTE]={
		{"Alicia", 9.2, {1, 1, 0, 0, 1}},
		{"Bruno", 8.5, {1, 0, 0, 1, 1}},
		{"Carla", 7.8, {0, 1, 1, 1, 0}},
		{"Diego", 6.9, {1, 1, 1, 0, 0}},
		{"Eva", 9.5, {1, 1, 1, 1, 1}},
		{"Felipe", 5.4, {0, 1, 1, 1, 1}},
		{"Gloria", 8.1, {1, 0, 0, 1, 0}},
		{"Hugo", 7.2, {0, 1, 1, 0, 1}},
		{"Isabel", 6.5, {1, 0, 1, 1, 0}},
		{"Jorge", 7.0, {1, 1, 0, 0, 1}},
	};

	asignar_turnos(&Clase);

	return EXIT_SUCCESS;
}
