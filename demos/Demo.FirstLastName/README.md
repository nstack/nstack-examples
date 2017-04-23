This is a little example demonstrating the environmental configuration feature,
 that are used in a similar manner to OS application environment variables.

It is a module that takes the first name via the a static configuration
argument, last name from the input stream, and concatenates the two.

### Usage

```bash
$ nstack build
$ echo 'import Demo.FirstLastName:0.0.1 as FLN; Sources.http<Text> { http_path = "/fln" } | FLN.full_name { first_name = "John" } | Sinks.log<Text>' | nstack notebook
> Service started successfully as process 5
$ nstack send "/fln" '"Nash"'
```

