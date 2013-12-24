set timefmt "%Y-%m-%d"
set xdata time
set datafile separator ","

set yrange [0:110]
set xrange ['2013-10-01':'2013-12-31']

set term pdf size 10in,3in font "Courier,10"
set output 'stress-range.pdf'

set title 'Morning/Evening Stress Scores: 10/2013 - 12/2013'

plot 'stress-range.csv' index 0 using 1:2:3:4:5 with candlesticks lc rgb "#333333" t ''
