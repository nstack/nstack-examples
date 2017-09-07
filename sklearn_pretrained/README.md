# Introduction

Building an accurate Machine Learning or statistical model is hard
enough, but Data Scientists know that getting a trained model into
production is often a far greater challenge. Internal process involving
IT, Engineering and other business units mean it can take months for a
model to make it into production, leaving the Data Science team
frustrated and unable to demonstrate their value-add to the
organisation.

In an ideal world, Data Science teams would be able to independently
take trained models and produce scalable, robust, production-grade
applications for internal or external consumption. Unfortunately this
requires Data Engineering and DevOps skills that aren't always present
within Data Science teams.

# The NStack Solution

At NStack, having conversations with dozens of Data Science teams
has given us a deep understanding of the problems Data Science
practitioners encounter in their day-to-day work.

Building on our market insights, we have built systems that help Data
Scientists address these issues. By building existing functions and
models into NStack workflows, Data Scientists gain the ability to create
APIs that push or pull data from a wide variety of datastores and
perform the analytics function in streaming or batch mode, scheduled
or on-demand.

Within an organisation, this functionality can be used to create a tool
belt of reusable, composable standard modules that would otherwise be
spread out across different teams and therefore unavailable for
sharing and building upon. Another internal use case is the quick setup
of prototypes for consumption or testing by nontechnical teams. In both
cases, there is no need for involvement of IT or Engineering
departents.

For external use cases, such as deploying a model to production that
deterines properties of a customer-facing product component, NStack's
architecture based on the Kubernetes orchestration system makes it
easy and seamless for IT to install and monitor on-premesis, while
presenting the exact same user interface to the Data Scientists.

Whether for internal or external consumption, NStack's system of
reusable, composable modules and workflows empowers Data Scientists to
rapidly iterate their projects, work towards their vision and
demonstrate impact to management.

In the rest of this white paper, we will walk through an example use
case of NStack: deploying a trained Machine Learning model as an HTTP
API. A repository containing all the code necessary to run the example
yourself can be found [here](https://github.com/nstack/XXX).

# Example: Introduction

Propensity modeling is a common way to use Machine Learning models
to make business decisions. For example, if the question is which
out of a number of offers to present to a given customer, a
propensity model can be used to present the offer which has the
highest expected rate of return for the company.

Here we will illustrate how to deploy a propensity model written
in python using [the scikit-learn library](scikit-learn.org) to
NStack, allowing you to seamlessly connect it to the rest of your
organisation's infrastructure.

We will use a dataset from the [RecSys 2015][recsys] recommender
systems competition. The dataset contains anonymized clickstreams
from an online retailer's website, and the task is to predict which
sessions will lead to a purchase. Once the data is downloaded, the
code linked to above will locally train a model which takes as input
a simple set of features describing a web session, and outputs the
probability that a certain item will be purchased by that user. This
model will then be saved to a file called `propensitymodel.pkl`.

[recsys]: http://recsys.yoochoose.net/challenge.html

From this point, deploying the model to NStack can be achieved in a
few simple steps:

# Example: Building a Module

To build, simply run `nstack build` on the command line. This uploads
the `service.py` file, which describes how to load the model and obtain
predictions from it, along with the model file and the workflow
specification to the NStack cloud.

# Example: Starting the NStack Workflow

Running `nstack build` results in an NStack module which is configured
by reading the files `nstack.yaml` and `module.nml`. Modules can
contain multiple workflows, but in this case there is only one, named
`w` (defined in `module.nml`). Before running data through the workflow,
we need to start it, this can be done by running
`nstack start Propensity:0.0.1-SNAPSHOT w`.

If successful, this will print a process number for the now deployed
model.

## Example: Running the Workflow

Send data to the workflow as follows (the list of ones and zeros is
just a random feature vector for testing):
```
nstack send '/get_propensity' '[1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0]'
```

and then the results can be viewed by viewing the logs of the process:
```
nstack log X
```
where `X` is the process number.

# Example: Scheduling and DMP Integration
This example kept things simple, reading inputs from an HTTP request
and writing outputs to NStack's log (inspect `module.nml` to see how
this workflow is defined). NStack supports much more complicated
workflows, with arbitrary numbers of processing stages and a
variety of sources and sinks (e.g. SQL database, data warehouse,
etc.)

A more realistic example workflow involves a scheduled daily loading of
cookie data followed by an analytics pipeline, and finally storing the
processed results in a DMP such as Krux (now Salesforce DMP) for
subsequent analysis by the marketing team. A simple parameter in the
workflow's configuration turns on scheduling with an arbitrary
repetition time, and scheduled jobs can be viewed both from the command
line interface and using the web UI.

At any time during development if anything goes wrong, the NStack
process logs will contain useful information, including the output of
any print statements inserted in the module code, so troubleshooting is
a straightforward process. 

# Conclusion: NStack core benefits
As demonstrated above, NStack helps Data Science teams tackle their
most important problem: disseminating their work. With NStack, Data
Scientists can independently produce shareable, composable,
production-ready modules that integrate with a wide variery of data
platforms.

In addition, here are some features we are currently working on which
will make it into the product in the next 12-18 months:

* R support: The NStack module system, with its sophisticated type
  system, makes it possible to seamlessly connect R functions with
  all other NStack functions, including those written in Python. This
  will provide a good way for teams working in different languages to
  share their work, and to manage language migrations.
* Model Training: We are working on allowing models to maintain
  internal state, which will enable the training of models within
  NStack, as well as the running of so-called online models, which
  generate predictions and learn incrementally from their inputs at the
  same time.
* Stream Windows: Currently, streams are presented to NStack workflows
  one record at a time, but for many applications multiple records need
  to be considered simultaneously. A future release of NStack will
  include a variety of windowing schemes to allow for sophisticated
  trend analysis, anomaly detection, etc.
* Model Building in the Web UI: Many NStack operations can already be
  performed from our web UI, but work currently in progress will enable
  the whole model building process, including composing functions, to
  be done from a browser. This will open up the benefits of NStack to a
  much larger audience within an organisation, making it possile to
  build an entire workflow (using both pre-packaged and custom-built
  functions) without writing a single line of code.

That's it! For more information on how to build more complex workflows
with NStack, see [docs.nstack.com](docs.nstack.com), or email
info@nstack.com with any questions!
