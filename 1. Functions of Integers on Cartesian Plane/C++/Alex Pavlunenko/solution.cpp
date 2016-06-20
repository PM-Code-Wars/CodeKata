/******************
Alex Pavlunenko
20 June 2016
Kata 1 Functions of Integers on Cartesian Plane
*/
using namespace std;
class Funij
{

  public:
  static unsigned long long sumin(unsigned long long n)
  {
    unsigned long long result = 0;
    unsigned long long diff = 0;
    
    for(unsigned long long i = 1; i <= n; i++)
    {      
      result += (i * n) - diff;
      diff += i;      
    } 
    return result;
  }
  static unsigned long long sumax(unsigned long long n)
  {    
   
    unsigned long long diff = 0;
    unsigned long long product = n*n;
    unsigned long long result = product;
    
    for(unsigned long long i = (n-1); i >= 1; i--)
    {
      diff += i;  
      result += product - diff;          
    } 
    return result;
  }
  
  static unsigned long long sumsum(unsigned long long n)
  {
    return sumin(n) + sumax(n);
  }
};
