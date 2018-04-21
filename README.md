# How to use this code

## Requirements
You'll either need:

(1) To have installed Python 3 and Anaconda.

(2) To have installed Docker. In that case you can run the Docker environment `continuumio/anaconda3`, where Python 3 and Anaconda are already installed.

## Then do this
Clone the repo: `git clone https://github.com/JeffreyBenjaminBrown/observatorio-mailing-list`

Copy the `mailing list, private` folder from OneDrive here. Rename it to `private`. (Only a few special people have access to that.)

In the `private/` folder, run `make downloads`. That will download the latest subscription and cancellation data, in .csv format.

In the project's root folder, run `python3 main.py`


# What happens
A new subfolder called `output/` will appear. It includes a data set of all active subscriptions (with a column for each of the many kinds of Latin American names) and a text file with the corresponding email addresses concatenated in a form suitable for use in a BCC field.
