#include <iostream> //注意头文件的使用方法
using namespace std;
int main()
{
    int rows,n,a;
    cin>>rows;
    while(rows--){
    	cin>>n;
    	int sum=0;
    	for(int i=0;i<n;i++){
    		cin>>a;
			sum=sum+a;
		}
		cout << sum << endl;
		cout << endl;
	}
	return 0;
}
