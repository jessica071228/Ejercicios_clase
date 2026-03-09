#include < iostream>
using namespace std;
int main() {
	int mdo = 8, mdor = 0, prod;
	cout << "ingresa un numero: ";
	cin >> mdo;
	for (mdor = 1; mdor <= 10; mdor++) {
		prod = mdo * mdor;
		cout << mdo << " x " << mdor << " = " << prod << endl;
	}
}