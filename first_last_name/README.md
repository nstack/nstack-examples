This is a little silly example demonstrating the new configuration feature
([#112](https://github.com/nstackcom/nstack/issues/112)).

It is a module that takes the first name via the a static configuration
argument, last name from the input stream, and concatenates the two.

Usage:

    nstack build
    nstack start 'source(http:///full_name : Text) |
      args_example.full_name { first_name = "John" } |
      sink(log:// : Text)'
    http PUT localhost:8080/full_name params:='"Nash"'
