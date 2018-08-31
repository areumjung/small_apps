
# coding: utf-8

# In[ ]:


#Importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data
x = [1,2,3,4,5]
y = [6,7,8,9,10]

#prepare the output file
output_file("line.html")

#create a figure object
f = figure()

#create line plot
f.line(x, y)

#write the plot in the figure object
show(f)


# In[ ]:


dir(f)


# In[ ]:


#Importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data
x = [1,2,3,4,5]
y = [6,7,8,9,10]

#prepare the output file
output_file("line.html")

#create a figure object
f = figure()

#create line plot
f.triangle(x, y)

#write the plot in the figure object
show(f)


# In[ ]:


#Importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data
x = [1,2,3,4,5]
y = [6,7,8,9,10]

#prepare the output file
output_file("line.html")

#create a figure object
f = figure()

#create line plot
f.circle(x, y)

#write the plot in the figure object
show(f)


# In[ ]:


#using pandas

from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

#prepare data
df = pd.read_csv("data.csv")
x = df['x']
y = df['y']

output_file("line_from_csv.html")

f = figure()
f.line(x, y)
show(f)


# In[ ]:


from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

df = pd.read_csv("bachelors.csv")
x = df['Year']
y = df['Engineering']

output_file("bachelor_engin.html")

f = figure()
f.line(x, y)
show(f)


# In[ ]:


import pandas
from bokeh.plotting import figure, output_file, show

p = figure(plot_width=500, plot_height=400, tools='pan', logo=None)

p.title.text = "Cool Data"
p.title.text_color = "Gray"
p.title.text_font = "times"
p.title.text_font_style = "bold"
p.xaxis.minor_tick_line_color = None
p.yaxis.minor_tick_line_color = None
p.xaxis.axis_label = "Date"
p.yaxis.axis_label = "Intensity"

p.line([1,2,3],[4,5,6])
output_file("graph.html")
show(p)


# In[ ]:


import pandas as pd
df = pd.read_excel("verlegenhuken.xlsx")
df.head()


# In[ ]:


from bokeh.plotting import figure, output_file, show
import pandas as pd

df = pd.read_excel("verlegenhuken.xlsx")
p = figure(plot_width=500, plot_height=400, tools='pan, reset', logo=None)

x = df['Temperature']/10
y = df['Pressure']/10

p.title.text = "Temperature and Air Pressure"
p.title.text_color = "gray"
p.title.text_font = "arial"
p.title.text_font_size = "20pt"
p.title.text_font_style = "bold"
p.xaxis.minor_tick_line_color = None
p.yaxis.minor_tick_line_color = None
p.xaxis.axis_label = "Temperature"
p.xaxis.axis_label_text_font_size = "15pt"
p.yaxis.axis_label = "Pressure (hPa)"
p.yaxis.axis_label_text_font_size = "15pt"

p.circle(x, y, size=[i/1000 for i in y], color='red', alpha=0.5)
output_file("weather.html")
show(p)


# In[ ]:


from bokeh.plotting import figure, output_file, show
import pandas as pd

df=pd.read_csv("adbe.csv")
df.head()


# In[ ]:


from bokeh.plotting import figure, output_file, show
import pandas as pd

df = pd.read_csv("adbe.csv", parse_dates=["Date"])

p = figure(width=500, height=250, x_axis_type="datetime", sizing_mode='scale_width')
p.line(df['Date'], df['Close'], color="Orange", alpha=0.5)

output_file("timeseries.html")
show(p)


# In[ ]:


from bokeh.plotting import figure, output_file, show
import pandas as pd

df = pd.read_excel("verlegenhuken.xlsx")
p = figure(plot_width=500, plot_height=400, tools='pan, reset', logo=None)

p.title.text='Earthquake'
p.title.text_color='Orange'
p.title.text_font='times'
p.title.text_font_style='italic'

p.yaxis.minor_tick_line_color='Yellow'

p.xaxis.axis_label='Times'
p.yaxis.axis_label='Value'

p.line([1,2,3,4,5],[5,6,5,5,3],line_width=2,color='red',alpha=0.5)
p.circle([i*2 for i in [1,2,3,4,5]],[5,6,5,5,3],size=8,color='blue',alpha=0.5)

output_file("Scatter_plotting.html")
show(p)

