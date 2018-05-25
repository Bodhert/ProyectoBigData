# Proyecto BigData Tópicos en Ingeniería de Telemática 
   ### Análisis de sentimientos en texto
  
  Integrantes del grupo:
  * Alejandro Cordoba Bodhert 
  * Juan Pablo Alcaraz Flórez 
  * Craig David Cartagena 


  ## Descripción del proyecto
  El proyecto consiste en analizar un Dataset de diferentes comentarios de usuarios respecto a la experiencia en una aerolinea. Con esta información se debe hacer un análisis de su experiencia e identificar que comentarios son positivos, negativos o neutros.

  ## Ejecución del Script en Python

   Para ejecutar localmente se debe correr el siguiente comando:

  ``` $ spark-submit --master local[1] proyecto.py ```

   El Dataset se llama Learning1.csv

   ## Dependencias

   Se requiere la instalación por medio del manejador de paquetes de Python, pip; diferentes bibliotecas requeridas para el correcto funcionamiento de la Script.
   
   - $ pip3 install string
   - $ pip3 install nltk
   - $ pip3 install csv
   - $ pip3 install re
   - $ pip3 install pyspark

   ## Funcionamiento

   ### Creación del Corpus

   Se realiza la correspondiente limpieza de los datos suminstrados
   
   - colocar cada una de la setancias en minuscula
   - Eliminar caracteres que no son letras como números, signos de puntuaciones, etc...
   - Realizar Steamming, en donde se busca acortar la busqueda, normalizar oraciones y mejorar los resultados del modelo a entrenar.
   - Eliminar doble espacio entre las palabras.

   Para la correcta eliminación de los Stop-Words y hacer Steamming se requiere hacer la correspondiente tokenización de los datos de entrada.

   ### Vectorización del Dataset

   La transformación del texto en vectores de numeros identificables se realiza una relación entre TF (Time Frecuency) y IDF(Inverse Document Frequency)   

   * TF-IDF (Term Frequency – Inverse Document Frequency): Es un método de vectorización
  de características ampliamente utilizado en la minería de textos para reflejar la
  importancia de un término para un documento

 El calculo del TF es solo contar las ocurrencias de una palabra en un documento.

 Para calcular el IDF se utiliza la sigiente formula:

 ![Tech](/formula.png)

 Después de calcular ésto se procede a calcular el TF-IDF de la siguiente manera:
 ![Tech](/tf.png)

   ### Modelo

   Se utilizó el algoritmo de Random Forest suministrado por la biblioteca MLlib, siendo éste una combinación de árboles predictores, tal que cada árbol depende de los valores de un vector aleatorio probado independientemente y con la misma distribución para cada uno de estos.

   ![Tech](/randomForest.jpg)  

## Referencias

http://python-apuntes.blogspot.com.

https://spark.apache.org/docs/2.2.0/mllib-feature-extraction.html

https://machinelearningmastery.com/clean-text-machine-learning-python/

http://web.cs.ucla.edu/~mtgarip/linear.html

http://spark.apache.org/docs/latest/mllib-linear-methods.html#linear-support-vector-machines-svms
