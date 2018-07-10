    #include <stdio.h>
    #include <stdlib.h>
    #include <math.h>
    #include <assert.h>
    #include <unistd.h>
    #include <sys/time.h>
     
    #define M 2048
    #define N 2048
    #define K 2048
     
    /*#define M 1000
    #define N 1000
    #define K 1000*/
     
     
    #define alpha 1
    #define beta 1
    double A[M][K];
    double B[K][N];
    double C[M][N];
    //double newB[N][K]; //added line for transposed array B
     
    #define IF_TIME(foo) foo;
     
    void init_array()
    {
        int i, j;
     
        for (i=0; i<N; i++) {
            for (j=0; j<N; j++) {
                A[i][j] = (i + j);
                B[i][j] = (double)(i*j);
                C[i][j] = 0.0;
                //newB[i][j]=0.0;
            }
        }
    }
     
     
    void print_array()
    {
        int i, j;
     
        for (i=0; i<N; i++) {
            for (j=0; j<N; j++) {
                fprintf(stdout, "%lf ", C[i][j]);
                if (j%80 == 79) fprintf(stdout, "\n");
            }
            fprintf(stdout, "\n");
        }
    }
     
    double rtclock()
    {
        struct timezone Tzp;
        struct timeval Tp;
        int stat;
        stat = gettimeofday (&Tp, &Tzp);
        if (stat != 0) printf("Error return from gettimeofday: %d",stat);
        return(Tp.tv_sec + Tp.tv_usec*1.0e-6);
    }
     
    double t_start, t_end;
     
    int main()
    {
        int i, j, k;
        register double s;
     
        init_array();
     
        IF_TIME(t_start = rtclock());
     
        /* Code to be optimized - start */
        /*
        //transposing matrix B
        for(i=0;i<K;i++){
            for(j=0;j<N;j++){
                newB[j][i]=B[i][j];
            }
        }
        */
        //Add the pragma line here
        #pragma omp parallel for private(j,k)
        for(i=0; i<M; i++)
            for(k=0; k<K; k++)
                for(j=0; j<N; j++)  
                    C[i][j] = beta*C[i][j] + alpha*A[i][k] * B[k][j];
        /* Code to be optimized - end */
     
        IF_TIME(t_end = rtclock());
        IF_TIME(fprintf(stderr, "%0.6lfs\n", t_end - t_start));
     
        if (fopen(".test", "r")) {
            print_array();
        }
     
        return 0;
    }
     