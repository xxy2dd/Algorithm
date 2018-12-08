#include <iostream> //注意头文件的使用方法
#include <windows.h>
using namespace std;
int main()
{
	DWORD s=GetTickCount();
    int n,a;
    while(cin>>n){
    	int sum=0;
    	for(int i=0;i<n;i++){
    		cin>>a;
			sum=sum+a;
		}	
		cout << sum << endl;
	}
	DWORD e=GetTickCount();
	cout<<e-s<<endl;
	return 0;
   
}
