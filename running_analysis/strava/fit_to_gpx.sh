

# gpsbabel -i garmin_fit -f 1642153807.fit -o gpx 1642153807.gpx
cd /Users/rory/data/strava/export_23193264/activities
gunzip *.fit.gz

for file in ./*.fit; do
	gpsbabel -i garmin_fit -f $file -o gpx -F "${file%.fit}.gpx"
done