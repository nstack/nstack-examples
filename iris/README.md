## Iris Example

An individual Python-based service that exposes a simple classifier using `scikit-learn` and a built-in data-set. 
The service classifies flower types via distinguishing petal characteristics, _petal width_, _petal length_, _sepal width_, _sepal length_.
It exposes a single function, `predict`, and demonstrates using system dependencies and data-sets within a module.

### Services & Types

```
type PlantInfo = (Double, Double, Double, Double)
type PlantSpecies = Text
predict : PlantInfo -> PlantSpecies
```

This service is used to create specific workflows that expose it over http and wire it up to a Postgres database containing sample data to classify.

### Usage

#### HTTP Source

```bash
$ nstack build
$ nstack start Iris.Classify:0.1.0.fromHttp
> Successfully started as process 5
$ nstack send "/iris" '[1.5, 0.1, 4.9, 3.1]'
$ nstack log 5
> ...
> output : "iris-setosa"
```

#### Postgres Source

```bash
$ nstack build
$ nstack start Iris.Classify:0.1.0.fromDb
> Successfully started as process 5
$ nstack log 5
```

