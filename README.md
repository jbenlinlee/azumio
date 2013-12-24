## stress.py
This is a script that processes data from the Azumio Stress Check
app and outputs data in the form:

	<date>,<morning score>,0,<score delta>

This output can then be used by gnuplot using the `stressvec.gnuplot`
gnuplot script. This gnuplot script will generate a plot of stress
data with red vectors indicating days where stress increased from
morning to evening, blue vectors indicating when stress decreased
from morning to evening, and points indicating days with only one
measurement or where the stress score did not change.
