import pandas as pd
import os

subscribed = pd.read_csv( "downloads/subscribed.csv" ) # collected online, ongoing
canceled = pd.read_csv( "downloads/canceled.csv" ) # collected online, ongoing
first_subscribed = pd.read_csv( "downloads/first.csv" # collected once, at the observatorio launch
                     , usecols = [ 'Marca temporal', 'Nombres', 'Apellidos', 'Correo electrónico' ]
)
first_subscribed = first_subscribed.rename(columns={'Marca temporal':'Timestamp', 'Apellidos':'Primer Apellido'
                              , 'Correo electrónico': 'Correo Electrónico'})
subscribed = subscribed.append( first_subscribed )
del(first_subscribed)

