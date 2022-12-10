# The California Map of Hazardous Waste Sites and Schools
An interactive maps of hazardous waste sites and school locations in California.

This is [Idalmis Vaquero](https://projects.iq.harvard.edu/climatefellowship/people/idalmis-vaquero)'s [Climate Justice Design Fellowship](https://projects.iq.harvard.edu/climatefellowship) 2022 project. The maps and data analysis were implemented by [Jonathan Foster](https://www.gluesolutions.io/jfoster-bio-page) of [GlueSolutions](https://www.gluesolutions.io/home) using [Glue](http://glueviz.org). The website was implemented by [Nathan Sanders](https://projects.iq.harvard.edu/climatefellowship/people/nathan-e-sanders).

## Local Development

This site was built using Pelican, a static site generator, and is hosted from this repository using GitHub Pages.

To run the site locally, clone the repository, create a python virtual environment with the `pip_requirements.txt`, activate that environment, and run `make devserver`.  You can then view the site locally at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Syncing data

This site hosts maps which are dependent on geojson files developed by Glue Solutions. The `bash` script `sync_map_files.sh` can be used to pull the latest versions of these from the Glue Solutions repository.

## Publishing

This Pelican site instance was developed with `make`.  To publish, use `make publish` and then push the changed `docs` files to the repository.
