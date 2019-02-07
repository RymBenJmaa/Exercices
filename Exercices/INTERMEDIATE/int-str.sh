#!/bin/bash
#Write a script function that determines if an argument passed to it is an integer or a string. The function will return TRUE (0) if passed an integer, and FALSE (1) if passed a string.
Integer () {
case "${1#[+-]}" in
    ''|*[!0-9]*)
        echo "FALSE" ;;
    *)
        echo "TRUE" ;;
esac
}
Integer $1
