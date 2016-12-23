## Top level makefile
SRC_DIRS := Movies.GetIMDBScore Movies.GetMoviePoster Movies.FilterHighScores NStack.ImageFilters Movies.Workflows

all: build

build:
	for d in $(SRC_DIRS); do (cd $$d; nstack build); done

start:
	echo $(PATH)
	nstack start Movies.Workflows.w1 --source "postgresql://localhost:5432/movies?query=select+%28f.title%2C+c.name%29+%0D%0Afrom+film_category+fc%0D%0A+++++inner+join+film+f+on+f.film_id+%3D+fc.film_id%0D%0A+++++inner+join+category+c+on+c.category_id+%3D+fc.category_id%0D%0Aorder+by+random%28%29+limit+10%3B" --sink "postgresql://localhost:5432/movies?table=output"

clean:
	for d in $(SRC_DIRS); do (echo "NYI"); done

force_look:
	true

.PHONY: clean build

