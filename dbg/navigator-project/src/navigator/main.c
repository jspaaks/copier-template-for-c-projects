#include <stdio.h>
#include <math.h>
#include "operations/division.h"
#include "operations/multiplication.h"

int main (void) {
    fprintf(stdout, "-- test compile definitions\n");
#ifndef DEBUG
    fprintf(stdout, "   DEBUG compile definition has not been defined.\n");
#else
    fprintf(stdout, "   DEBUG compile definition has been defined.\n");
#endif
    fprintf(stdout, "\n");

    fprintf(stdout, "-- test whether math library was linked\n");
    fprintf(stdout, "   sqrt(144) = %f\n", sqrt(144));
    fprintf(stdout, "\n");

    fprintf(stdout, "-- test own library\n");
    fprintf(stdout, "   operations_divide(2, 3) = %d\n", operations_divide(2, 3));
    fprintf(stdout, "   operations_multiply(2, 3) = %d\n", operations_multiply(2, 3));
    fprintf(stdout, "\n");

    return 0;
}
