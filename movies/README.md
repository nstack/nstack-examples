# Services & Types

```haskell
type Title = Text
type Category = Text
type MovieRecord = (Text, Text, Integer)
type MovieRecordImage = {title: Text, category: Text, score: Integer, poster: ByteString}

getIMDBScore : (Title, Category) -> MovieRecord
filterHighScores : MovieRecord -> Maybe MovieRecord -- currently returns [MovieRecord]
getMoviePoster : MovieRecord -> MovieRecordImage
processPoster : MovieRecordImage -> MovieRecordImage -- currently returns Title
```

# Remaining tasks
* Hook up to postgres source/sink
* Update processPoster to return full record
* Remove debugging print stmts

# Issues

## Need streaming rather than RPC

* Often need to return only a single value for a range of values coming int
  * e.g. filterHighScores should take the entire dataframe and return a subset of values
  * Filtering is a partial stop-gap atm

## Poor method reuse due inability to access data within DSL

*  No abilty to wrangle the data/types of the stream means we have the pass the entire data stream into each method
* e.g. getMoviePoster should have the type `Title -> Image` but currently needs to take in the stream-specific type, meaning it can't be reused elsewhere
* We ideally want some way to either split and merge data within the DSL (and split/merge streams), or some type narrowing/eplanding capability (perhaps row types/structural subtyping)

## Require windowing/batching

* We can't determine the total highest score for each category without either,
  * passing the entire dataframe inside the `filterHighScores` service
  * or having stateful services and a stop signal that is sent to a service so it knows when it has recevied the entire streamed dataframe
* currently we have a klduge where filter is based on a stic threashold rather than the max score per category
  
## Verbosity

* We have to repeat the same type alaises within each API, 
  * move to the DSL?
  
## No Maybe so filter can't be used

## Need a local testing/debug story during development of a service 
* Ideally see where a message is within a workflow, at what stage, etc.
* see where the last error occured in the pipeline

## Need somewhere to store query, pref in DSL
```
select (f.title, c.name) 
from film_category fc
     inner join film f on f.film_id = fc.film_id
     inner join category c on c.category_id = fc.category_id
order by random() limit 10;
```

## Way to build all dependent services easily

* Maybe a build tool
* IDE
* Project

