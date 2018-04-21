import pandas as pd
import os

# Download, merge
subscribed = pd.read_csv( "downloads/subscribed.csv" ) # collected online, ongoing
canceled = pd.read_csv( "downloads/canceled.csv" ) # collected online, ongoing
first_subscribed = pd.read_csv( "downloads/first.csv" # collected once, at the observatorio launch
                     , usecols = [ 'Marca temporal', 'Nombres', 'Apellidos', 'Correo electrónico' ]
)
first_subscribed = first_subscribed.rename(columns={'Marca temporal':'Timestamp', 'Apellidos':'Primer Apellido'
                              , 'Correo electrónico': 'Correo Electrónico'})
subscribed_small = subscribed # TODO: delete
subscribed = subscribed.append( first_subscribed )
del(first_subscribed)
canceled = canceled.rename(
  columns={'Correo electrónico': 'Correo Electrónico'})

# Sort
subscribed = subscribed.sort_values(by=['Correo Electrónico','Timestamp'])
canceled   = canceled  .sort_values(by=['Correo Electrónico','Timestamp'])
subscribed_small = subscribed_small.sort_values( # TODO: delete
                                    by=['Correo Electrónico','Timestamp'])

# Gruop
subscribed = subscribed.groupby('Correo Electrónico').last()
canceled = canceled.groupby('Correo Electrónico').last()
subscribed_small = subscribed_small.groupby( # TODO: delete
  'Correo Electrónico').last()
