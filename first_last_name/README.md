This is a little silly example demonstrating the new configuration feature
([#112](https://github.com/nstackcom/nstack/issues/112)).

It is a module that takes the first name via the a static configuration
argument, last name from the input stream, and concatenates the two.

Usage:

    nstack build
    echo 'import FirstLastName:0.0.1-SNAPSHOT as FLN; Sources.http : Text { http_path = "fln" } | FLN.full_name { first_name = "John" } | Sinks.log : Text' | nstack notebook
    http PUT localhost:8080/fln params:='"Nash"'
