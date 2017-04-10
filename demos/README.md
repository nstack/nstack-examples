## Demos

A collection of basic example services.


### Demo.NumChars

The nstack version _HelloWorld_, this service is created by default when initialising an empty python project (i.e. `nstack init python`)
It exports a single function, 

```
numChars : Text -> Integer
```

that simply returns the number of characters in a input text message. Build using `nstack build`.


### Demo.Workflow

A sample workflow module that uses the service above (`Demo.NumChars`) and exposes over HTTP. Similarly, this service is created by default when initialising an empty python project (i.e. `nstack init workflow`).

It exports this single workflow, exposing the service over HTTP and sending the result to the service log

```
def w = Sources.http<Text> { http_path = "/demo" } | D.numChars | Sinks.log<Integer>;
```

Build using `nstack build`, and run using `nstack start Demo.Workflow.0.0.1.w`. From here you can use the `nstack send` command to send messages to the running workflow as follows and view the output using `nstack log`,

```bash
$ nstack build
$ nstack start Demo.Workflow.0.0.1.w
> Service started successfully as process 5
$ nstack send "/demo" '"HelloWorld"'
> Event sent successfully
$ nstack log 5
> ...
> Output : 10
```

### Demo.Classify

A trivial _classifier_ that demonstrates sending data into an nstack service

You can build and run this service in a single step using the `nstack notebook` feature that provides a mini-REPL (you can also redirect a file/stream into the notebook command to provide for rapid service testing and development),

```
$ cd Demo.Classify
$ nstack build
$ nstack notebook
import Demo.Classify:0.0.3 as D;
Sources.http<Text> { http_path = "/classify" } | D.numChars | Sinks.log<Text>
<Ctrl-D>
> Service started successfully as process 5
$ nstack send "/classify" '"orange"'
```

### Demo.FirstLastName

This is a little example demonstrating the environmental configuration feature,
 that are used in a similar manner to OS application environment variables.

It is a module that takes the first name via the a static configuration
argument, last name from the input stream, and concatenates the two.

As mentioned above, this example demonstrates piping input into the `nstack notebook` command to start an ad-hoc workflow,

```bash
$ cd Demo.FirstLastName
$ nstack build
$ echo 'import FirstLastName:0.0.1 as FLN; Sources.http<Text> { http_path = "/fln" } | FLN.full_name { first_name = "John" } | Sinks.log<Text>' | nstack notebook
> Service started successfully as process 5
$ nstack send "/fln" '"Nash"'
```

