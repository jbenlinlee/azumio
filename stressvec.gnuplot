set timefmt "%Y-%m-%d"
set xdata time
set datafile separator ","

set yrange [0:110]

#set term png size 1000,500
#set output 'stressvec.png'

set term pdf size 10.5in,5.25in font "Courier,10"
set output 'stressvec.pdf'

plot 'stressvec.csv' index 0 using 1:2:3:4 with vec nohead lc rgb 'red' t 'incr', \
'stressvec.csv' index 1 using 1:2:3:4 with vec nohead lc rgb '#007700' t 'decr', \
'stressvec.csv' index 2 using 1:2 with p lc rgb '#000077' t 'stay/1pt'
