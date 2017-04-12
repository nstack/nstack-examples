## Movies Example

A more complex set of indiviudal services that we compose together to build a complex data pipeline.
In this case we create a reusable workflow that takes a stream of movie titles as text, obtains their IMDB score, filters low-ranking movies, and for those that remain, get and process their movie poster image.

This partial workflow of type `Text -> MovieImage` is then reused to create specific workflows that expose it over http and wire it up to a postgres databse, whilst output the eventual data image to an S3 bucket.

### Services & Types

```haskell
type Title = Text
type MovieRecord = (Text, Double)
type MovieImage = {title: Text, data: [Byte]}

GetIMDBScore.getIMDBScore : Title -> MovieRecord
FilterHighScores.filterHighScores : MovieRecord -> [MovieRecord]
GetMoviePoster.getMoviePoster : MovieRecord -> MovieImage

def moviePosters = GetIMDBScore.getIMDBScore
                   | FilterHighScores.filterHighScores { score = "7.5" } * 
                   | GetMoviePoster.getMoviePoster *
                   | Image.applyFilter { filtertype = "random" };
```

### Usage

#### HTTP Source

```bash
$ nstack build # depends on common modules found in ../nstack
$ nstack start Movies.Workflows:0.1.2.fromHttp
> Successfully started as process 5
$ nstack send "/movies" '"Toy Story"'
$ nstack log 5
```

#### Postgres Source

```bash
$ nstack build # depends on common modules found in ../nstack
$ nstack start Movies.Workflows:0.1.2.fromDb
> Successfully started as process 5
$ nstack log 5
```

