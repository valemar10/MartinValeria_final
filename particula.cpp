#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
void leapfrog(float tini, float tfin, float dt);
int main()
{
    float tini=0;
    float tfin=10;
    float dt=0.1;
    leapfrog(tini,tfin,dt);
    return(0);
    
}

void leapfrog(float tini, float tfin, float dt)
{
    float vxnuevo=0;
    float xnuevo=1;
    float vynuevo=1;
    float ynuevo=0; 
    float m=7294.29;
    float q=2;
    float vxviejo=0;
    float xviejo=0;
    float vyviejo=1;
    float yviejo=0;
    float Ex=0;
    float Ey=0;
    ofstream outfile;
    outfile.open("datoslp.dat");
    while(tini<tfin)
    {
        
        if(tini<3)
        {
            Ex=0;
            Ey=0;
        }
        if (tini>7)
        {
            Ex=0;
            Ey=0;
        }
        if(3<tini<7)
        {
            Ex=0;
            Ey=3;
		}
        vxviejo=vxnuevo;
        vyviejo=vynuevo;
        xviejo=xnuevo;
        yviejo=ynuevo;
        outfile<<tini<<" "<<xnuevo<<" "<<ynuevo<<endl;
        vxviejo= vxviejo-(dt/2)*(q*Ex/m);
        vyviejo= vyviejo-(dt/2)*(q*Ey/m);
        vxnuevo= vxviejo+dt*(q*Ex/m);
        vynuevo=vyviejo+dt*(q*Ey/m);
        xnuevo= xviejo+dt*vxnuevo;
        ynuevo=yviejo+dt*vyviejo;
        tini= tini+dt;
        
            

        
    }
    outfile.close();
}