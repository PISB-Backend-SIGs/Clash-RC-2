// C++ code declaring a global 1-D
// array of size 10^8
#include <bits/stdc++.h>
using namespace std;

// Variable N is initialized
const int N = 1e8;

// Global array is declared
int a[N];

// Driver Code
int main()
{
	for (int i = 0; i < N; ++i) {
		a[i] = i;
	}
	cout << a[N - 1];
	return 0;
}