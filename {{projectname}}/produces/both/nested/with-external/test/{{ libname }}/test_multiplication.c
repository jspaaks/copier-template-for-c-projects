#include <criterion/criterion.h>
#include "{{ libname }}/multiplication.h"


Test(multiplication, one){
    int actual = multiply(2, 3);
    int expected = 6;
    cr_assert(actual == expected);
}

Test(multiplication, two){
    int actual = multiply(2, -3);
    int expected = -6;
    cr_assert(actual == expected);
}
