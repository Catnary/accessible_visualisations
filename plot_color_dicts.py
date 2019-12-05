'''
Two sets of colors for graphing. Subsets derived from the following references:
 
Robert M. Boynton. (1989)
Eleven Colors That Are Almost Never Confused.
Proc. SPIE 1077, Human Vision, Visual Processing, and Digital Display, 322-332.
http://doi.org/10.1117/12.952730
 
Kelly, K. L. (1965).
Twenty-two colors of maximum
contrast. Color Engineering, 3(26), 26–27.
 
Paul Green-Armytage (2010)
A colour alphabet and the limits of colour coding.
Colour: Design & Creativity, 5:1–23.
https://eleanormaclure.files.wordpress.com/2011/03/colour-coding.pdf
 
'''
 
 #Subset of Boynton's list of "11 colors that are almost never confused"
 boynton_cmap = {'Blue':(0.0, 0.0, 1.0),
                'Red':(1.0, 0.0, 0.0),
                'Green':(0.0, 1.0, 0.0),
                'Yellow':(1.0, 1.0, 0.0),
                'Magenta':(1.0, 0.0, 1.0),
                'Pink':(1.0, 0.5, 0.5),
                'Gray':(0.5, 0.5, 0.5),
                'Brown':(0.5, 0.0, 0.0),
                'Orange':(1.0, 0.5, 0.0),}
 
#Subset of Kelly's "22 colors of maximum contrast"
kelly_cmap = {'Vivid Yellow':'#FFB300',
              'Strong Purple':'#803E75',
              'Vivid Orange':'#FF6800',
              'Very Light Blue':'#A6BDD7',
              'Vivid Red':'#C10020',
              'Grayish Yellow':'#CEA262',
              'Medium Gray':'#817066'}
              
#The eight colors I use most often for simple plots on a white background
color_map = ["#0000FF","#FF0000","#FFB300","#808080", "#803E75", "#FF6800", "#CEA262", "#A6BDD7"]

#Plot the colors using matplotlib
import matplotlib.pyplot as plt

fig,ax = plt.subplots(1,figsize=(8, 1), dpi=40) 
xdat = range(0,(len(color_map)))
ydat = [1 for x in xdat]
plt.scatter(xdat, ydat, color=color_map, s=1e3)
ax.set_yticklabels([])
print("color_map")
plt.show()
