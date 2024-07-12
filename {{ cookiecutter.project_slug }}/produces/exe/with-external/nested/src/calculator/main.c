#include <stdio.h>
#include <math.h>
{% if cookiecutter.external_directory != "My project doesn't have external dependencies" -%}
#include "addition.h"
{%- endif  %}
#include "division.h"
#include "multiplication.h"
{% if cookiecutter.external_directory != "My project doesn't have external dependencies" -%}
#include "subtraction.h"
{%- endif  %}


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


    fprintf(stdout, "-- test c2x / c23 features\n");
    constexpr int n = 5;
    int arr[n] = {0, 1, 2, 3, 4};
    fprintf(stdout, "   ");
    for (size_t i = 0; i < n; i++) {
        fprintf(stdout, "%d%s", arr[i], i < n - 1 ? " " : "\n");
    }
    fprintf(stdout, "\n");

    fprintf(stdout, "-- test own functions\n");
    fprintf(stdout, "   multiply(2, 3) = %d\n", multiply(2, 3));
    fprintf(stdout, "   divide(2, 3) = %d\n", divide(2, 3));
    fprintf(stdout, "\n");

    {% if cookiecutter.external_directory != "My project doesn't have external dependencies" -%}
    fprintf(stdout, "-- test external library\n");
    fprintf(stdout, "   add(2, 3) = %d\n", add(2, 3));
    fprintf(stdout, "   subtract(2, 3) = %d\n", subtract(2, 3));
    fprintf(stdout, "\n");
    {%- endif %}

    return 0;
}
