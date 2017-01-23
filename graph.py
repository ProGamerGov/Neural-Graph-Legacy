from matplotlib import pyplot, dates
from csv import reader

with open('out1.csv', 'r') as f: #Change out1.csv to the name of your CSV file
    data = list(reader(f))

iterations = [i[0] for i in data[1::]]
content_1_loss = [i[1] for i in data[1::]]
style_1_loss = [i[2] for i in data[1::]]
style_2_loss = [i[3] for i in data[1::]]
style_3_loss = [i[4] for i in data[1::]]
style_4_loss = [i[5] for i in data[1::]]
style_5_loss = [i[6] for i in data[1::]]
total_loss = [i[7] for i in data[1::]]

pyplot.title('Loss Values') #Graph tile
pyplot.xlabel('Iterations')
pyplot.ylabel('Loss')
pyplot.grid()

#Change marker='o' to marker=',' to remove the dots on the line graphs.
pyplot.plot(iterations, content_1_loss, label='Content 1 loss', lw=2, marker=',')
pyplot.plot(iterations, style_1_loss, label='Style 1 loss', lw=2, marker=',')
pyplot.plot(iterations, style_2_loss, label='Style 2 loss', lw=2, marker=',')
pyplot.plot(iterations, style_3_loss, label='Style 3 loss', lw=2, marker=',')
pyplot.plot(iterations, style_4_loss, label='Style 4 loss', lw=2, marker=',')
pyplot.plot(iterations, style_5_loss, label='Style 5 loss', lw=2, marker=',')
pyplot.plot(iterations, total_loss, label='Total loss', lw=2, marker=',')

#The position of the legend
pyplot.legend(loc='upper right')
pyplot.show()
