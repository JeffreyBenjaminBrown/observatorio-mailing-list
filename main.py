import pandas as pd
import os

# Download
subscribed = pd.read_csv( "downloads/subscribed.csv" ) # collected online, ongoing
canceled = pd.read_csv( "downloads/canceled.csv" ) # collected online, ongoing
first_subscribed = pd.read_csv(
  "downloads/first.csv" # collected once, at the observatorio launch
  , usecols = [ 'Marca temporal', 'Nombres', 'Apellidos'
                , 'Correo electrónico' ] )

# Homogenize
first_subscribed = first_subscribed.rename(
  columns={'Marca temporal':'Timestamp', 'Apellidos':'Primer Apellido'
           , 'Correo electrónico': 'Correo Electrónico'} )
subscribed = subscribed.append( first_subscribed )
canceled = canceled.rename(
  columns={'Correo electrónico': 'Correo Electrónico'})
del(first_subscribed)

# Unify
subscribed['Cancellation']=False
canceled['Cancellation']=True
united = subscribed.append( canceled )
del(subscribed,canceled)

# Limit to active subscriptions
united = united.sort_values(by=['Correo Electrónico','Timestamp'])
united = united.groupby('Correo Electrónico').last()
  # Find the last thing each email address did.
united = united.reset_index()
  # Gruoping turns the email address from a column to an index. Reverse that.
united = united[ ~united['Cancellation'] ].drop(['Cancellation'],axis=1)
  # If the last action from that address was to cancel, remove it.

# Output
if not os.path.exists('output'): os.makedirs('output')
united.to_csv( 'output/active_subscriptions.csv' )
addresses = united['Correo Electrónico'].tolist()
with open("output/addresses.txt", "w") as text_file:
    print(', '.join(addresses), file=text_file)
