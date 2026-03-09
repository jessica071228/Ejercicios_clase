#include <iostream>
using namespace std;
int main() {
	int mdo = 8, mdor = 0, prod;
	cout << "ingresa un numero: ";
	cin >> mdo;
	do {
		mdor++;
		prod = mdo * mdor;
		cout << mdo << " x " << mdor << " = " << prod << endl;

	} while (mdor <= 9);
	return 0;
}