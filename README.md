# What running this code does

A new subfolder called `output/` will appear. It includes a data set of all active subscriptions (with a column for each of the many kinds of Latin American names) and a text file with the corresponding email addresses concatenated in a form suitable for use in a BCC field.


# The input data, and how it is interpreted

We have two sets of subscription data. One was collected at the Observatorio's initial launch, when people signed up to attend the event. If they indicated on that form that they were interested in receiving more information from us on an ongoing basis, they should be subscribed. In one case, two people used the same email address; one asked to be subscribed, the other not. This code subscribes that address.

The other set of subscription data is collected on an ongoing basis, online, from a Google Form. Cancellation data is collected in the same manner, from another form. Those two forms feed into a Google (spread)Sheet that also contains the initial signup information.

If the last action associated with an email in that collection was to unsubscribe, they are unsubscribed. Otherwise they are subscribed.


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

