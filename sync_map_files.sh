# Sync a variety of files from the source repo to this one

# geo json files
wget https://gluesolutions.github.io/calenviroscreen.geojson content/extras/calenviroscreen.geojson
wget https://gluesolutions.github.io/hzw_sites.geojson content/extras/hzw_sites.geojson
wget https://gluesolutions.github.io/hzw_near_schools.geojson content/extras/hzw_near_schools.geojson
wget https://gluesolutions.github.io/public_schools.geojson content/extras/public_schools.geojson
wget https://gluesolutions.github.io/charter_schools.geojson content/extras/charter_schools.geojson
wget https://gluesolutions.github.io/private_schools.geojson content/extras/private_schools.geojson

# html files
# The HTML files are synced manually into the gluesolutions.github.io_map_*.html files.

# javascript files
wget https://gluesolutions.github.io/leaflet-heat.js content/extras/leaflet-heat.js
