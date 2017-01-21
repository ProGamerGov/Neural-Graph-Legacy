from matplotlib import pyplot, dates
from csv import reader

with open('out1.csv', 'r') as f:
    data = list(reader(f))

iterations = [i[0] for i in data[1::]]
content_1_loss = [i[1] for i in data[1::]]
style_1_loss = [i[2] for i in data[1::]]
style_2_loss = [i[3] for i in data[1::]]
style_3_loss = [i[4] for i in data[1::]]
style_4_loss = [i[5] for i in data[1::]]
style_5_loss = [i[6] for i in data[1::]]
total_loss = [i[7] for i in data[1::]]

pyplot.title('Loss Values')
pyplot.xlabel('Iterations')
pyplot.ylabel('Loss')
pyplot.grid()

pyplot.plot(iterations, content_1_loss, label='Content 1 loss', lw=2, marker='o')
pyplot.plot(iterations, style_1_loss, label='Style 1 loss', lw=2, marker='o')
pyplot.plot(iterations, style_2_loss, label='Style 2 loss', lw=2, marker='o')
pyplot.plot(iterations, style_3_loss, label='Style 3 loss', lw=2, marker='o')
pyplot.plot(iterations, style_4_loss, label='Style 4 loss', lw=2, marker='o')
pyplot.plot(iterations, style_5_loss, label='Style 5 loss', lw=2, marker='o')
pyplot.plot(iterations, total_loss, label='Total loss', lw=2, marker='o')

pyplot.legend(loc='upper right')
pyplot.show()
