#include <iostream> //注意头文件的使用方法
using namespace std;
int main()
{
	int n,a;
    while(cin>>n){
    	if(n==0){
    		break;
		}
    	int sum=0;
		for(int i=0;i<n;i++){
			cin>>a;
			sum=sum+a;
		}
		cout << sum << endl;
	}   
	return 0;   
}
