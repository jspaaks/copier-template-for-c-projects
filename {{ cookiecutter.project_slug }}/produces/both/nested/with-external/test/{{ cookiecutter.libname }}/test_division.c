#include <criterion/criterion.h>
#include "{{ cookiecutter.libname }}/division.h"


Test(division, one){
    int actual = divide(2, 3);
    int expected = 0;
    cr_assert(actual == expected);
}

Test(division, two){
    int actual = divide(2, -3);
    int expected = 0;
    cr_assert(actual == expected);
}
