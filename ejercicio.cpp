#include <iostream>
using namespace std;
int main() {
	int mdo=8, mdor=0, prod;
	
	cout << "Ingresa un numero: ";
	cin >> mdo;

	while (mdor <= 9) {
		mdor = mdor + 1;
		prod = mdo * mdor;

		cout << mdo << " x " << mdor << " = " << prod << endl;
	}

	return 0;
}