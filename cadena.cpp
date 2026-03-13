#include <iostream>
#include <string>
using namespace std;

int main() {
	string nombre, apellidos;

	cout << "Ingresa tu nombre ";
	cin >> nombre;
	cin.ignore();

	cout << "Ingresa tus apellidos ";
	getline(cin, apellidos);//cin >> apellidos;

	cout << "Hola " << nombre << " " << apellidos << " mucho gusto" << endl;

	//CONCATENAR CADENAS
	string descripcion, lugar;
	int tiempo;
	cout << "ingresa el lugar de origen: ";
	getline(cin, lugar);//cin >> lugar;
	cout << "ingresa el tiempo que has vivido ahi: ";
	cin >> tiempo;

	descripcion = "No conozco " + lugar + " pero creo que seria muy bonito visitarlo porque has vivido " + to_string(tiempo) + " anios ahi\n";
	cout << descripcion;

	//LONGITUD DE TEXTO

	cout << "tu nombre " << nombre << " tiene " << nombre.length() << " caracteres\n";
	cout << "tu apellido " << apellidos << " tiene " << apellidos.length() << " caracteres\n";
	cout << "la descripcion " << descripcion << " tiene " << descripcion.length() << " caracteres\n";

	//separar los caracteres de una cadena

	cout << nombre[0] << endl;
	cout << nombre[1] << endl;
	cout << nombre[2] << endl;
	cout << endl;
	//con estructura ciclica

	for (int i = 0; i < lugar.length(); i++) {
		cout << lugar[i] << endl;
	}
	cout << endl;

	//imprimir al reves

	for (int i = lugar.length() - 1; i >= 0; i--) {
		cout << lugar[i] << endl;
	}
	cout << endl;
	return 0;

	
}