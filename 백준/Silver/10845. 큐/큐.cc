#include <iostream>
#include <queue>
using namespace std;

int main(){
	queue<int> q;
	int t;
	cin >> t;
	while(t--){
		string cm; int x;
		cin >> cm;
		if(cm == "push"){
			cin >> x;
			q.push(x);
		}
		else if(cm == "pop"){
			cout << (q.empty()?-1:q.front()) << endl;
			if(q.empty() == false) q.pop();
		}
		else if(cm == "size"){
			cout <<(q.empty()?0:q.size())<< endl;}
		else if(cm == "empty"){cout << (q.empty()?1:0) << endl;}
		else if(cm == "front"){cout << (q.empty()?-1:q.front())<<endl;}
		else if(cm == "back"){cout << (q.empty()?-1:q.back())<<endl;}
	}
	return 0;
}