# Cuadro de mados de las 100 canciones más escuchadas de Spotify #

La base de datos ha sido recogida de la web: https://www.kaggle.com/datasets/amaanansari09/top-100-songs

## Los parametros de la base de datos son:

* id: Es un número único que identifica cada canción en Spotify.

* name: Es el nombre de la canción.

* duration: Es la duración de la canción en minutos.

* energy: Es una medida que va de 0.0 a 1.0 y representa una medida perceptual de la intensidad y actividad de una canción. Las canciones energéticas suelen ser más rápidas, fuertes y ruidosas, como el death metal, mientras que las canciones menos energéticas suelen ser más suaves, como una preludio de Bach. Esto se determina por varias características de la canción, como su rango dinámico, su volumen percibido, su timbre, la velocidad de inicio de las notas y su entropía general.

* key: Es la clave en la que se encuentra la canción. Los números se relacionan con las notas usando la notación de clase de tono estándar. Por ejemplo, el 0 es un C, el 1 es un C♯/D♭, el 2 es un D, y así sucesivamente. Si no se detectó la clave, el valor es -1.

* loudness: Es el volumen general de la canción en decibelios (dB). Los valores de volumen se promedian en toda la canción y son útiles para comparar la relativa intensidad de las canciones. Los valores de volumen típicamente van de -60 a 0 dB.

* mode: Indica la modalidad (mayor o menor) de la canción, que se refiere al tipo de escala de la que se deriva su contenido melódico. Mayor se representa por 1 y menor por 0.

* speechiness: Detecta la presencia de palabras habladas en la canción. Los valores cercanos a 1.0 describen canciones que consisten exclusivamente de palabras habladas, como un programa de entrevistas o un audiolibro. Los valores entre 0.33 y 0.66 describen canciones que pueden contener tanto música como palabras habladas, como en el caso del rap. Los valores por debajo de 0.33 probablemente representan canciones que no tienen palabras habladas.

* acousticness: Es una medida de confianza que va de 0.0 a 1.0 sobre si la canción es acústica. 1.0 representa una alta confianza de que la canción es acústica.

* instrumentalness: Predice si una canción no tiene voces. Los sonidos de "ooh" y "aah" se consideran instrumentales en este contexto. El rap o el canto sin letra no se consideran instrumentales. Los valores cercanos a 1.0 describen canciones que probablemente no tienen voces, mientras que los valores cercanos a 0.0 describen canciones que probablemente sí tienen voces.

