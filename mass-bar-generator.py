import os
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Use a dark template
pio.templates.default = "plotly_dark"

# Reads the CSV that contains the data
data = pd.read_csv('data.csv')

# Sets ID column as the index
data.set_index('ID', inplace=True)

# Check if path 'images' exists - if not, create it
if not os.path.exists("images"):
    os.mkdir("images")

# Creates an array from the ID column
rowID = data.index

# Loops through all the unique IDs
for i in rowID:

	fig = go.Figure()

	# Draw the consumption bar chart
	fig.add_trace(
		go.Bar(
			# X axis values created from the header row of the CSV
			x = list(data),
			# Y axis values created from the rows, based on the unique IDs
			y = data.loc[i],
			name = 'Value',
			# Shows the Y axis values
			text = data.loc[i],
			# Displays the Y axis values inside the bars
			textposition='outside',
			#Bar color
			marker_color='#2eafc9'
		))

	# Layout settings, all optional
	fig.update_layout(
        # Unique ID as chart title
		title='ID %s' % i,
		#width=1920, height=1080,
		showlegend=True,
        # Rotate the X axis ticks
		xaxis_tickangle=-45,
		yaxis_title='Y axis title',
		#margin=dict(l=200, r=200, t=100, b=100,pad=10),
		#font=dict(family='Arial, Helvetica, sans-serif', size=24, color='#303030')
		)

	# Writes the image file(s), uses the unique ID as the file name.
	fig.write_image("images/{0}.png".format(i))
