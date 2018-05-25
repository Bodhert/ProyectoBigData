# Proyecto BigData Tópicos en Ingeniería de Telemática 
   ### Análisis de sentimientos en texto
  
  Integrantes del grupo:
  * Alejandro Cordoba Bodhert 
  * Juan Pablo Alcaraz Flórez 
  * Craig David Cartagena 


  ## Descripción del proyecto
  El proyecto consiste en analizar un Dataset de diferentes comentarios de usuarios respecto a la experiencia en una aerolinea. con esta información se debe hacer un análisis de su experiencia e identificar que comentarios son positivos, negativos o neutros.

  ## Ejecución del Script en Python

   Para ejecutar localmente se debe correr el siguiente comando:

  ``` $ spark-submit --master local[1] proyecto.py ```

   El Dataset se llama Learning1.csv

   ## Dependencias

   * TF-IDF (Term Frequency – Inverse Document Frequency): Es un método de vectorización
  de características ampliamente utilizado en la minería de textos para reflejar la
  importancia de un término para un documento

 El calculo del TF es solo contar las ocurrencias de una palabra en un documento.

 Para calcular el IDF se utiliza la sigiente formula:

 ![Tech](/formula.png)

 Después de calcular ésto se procede a calcular el TF-IDF de la siguiente manera:
 ![Tech](/tf.png)

## Referencias

http://python-apuntes.blogspot.com.

https://spark.apache.org/docs/2.2.0/mllib-feature-extraction.html

https://machinelearningmastery.com/clean-text-machine-learning-python/

http://web.cs.ucla.edu/~mtgarip/linear.html

http://spark.apache.org/docs/latest/mllib-linear-methods.html#linear-support-vector-machines-svms
