# Neural-Graph
Graph Neural-Style's loss value outputs

The Neural-Style issue: https://github.com/jcjohnson/neural-style/issues/370

The modified neural_style.lua script: https://gist.github.com/ProGamerGov/a8134605c89f01e5bcd88539456675b8

# Requirements

Make sure you Neural-Style command is modified to use the modified Neural-Style script.

Matplotlib is also required: 

`sudo apt-get install python-matplotlib`

# Usage

First run the modified neural_style.lua script with `2>&1 | tee ~/neural-style/loss_values.log` at the end of your Neural-Style command paramters. Example: 

`th neural_style.lua -style_image <image.jpg> -content_image <image.jpg> 2>&1 | tee ~/neural-style/loss_values.log`

Or if you are using multires, then do:

`./multires.sh 2>&1 | tee ~/neural-style/loss_values.log`

After running Neural-Style, you must manually convert the iteration section(s) from the saved terminal log file to their own CSV file. 

Then first modify the graphing script to match your CSV file(s), and run the graphing script: 

`python graph.py`

