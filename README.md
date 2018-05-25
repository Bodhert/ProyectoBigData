# Proyecto BigData Topicos en Ingenieria de Telematica 
   ### Analisis de sentimientos en texto
  
  Integrantes del grupo:
  * Alejandro Cordoba Bodhert 
  * Juan Pablo Alcaraz Florez 
  * Craig David Cartagena 


  ## Descripcion del proyecto
  El proyecto consiste en analizar un dataset de diferentes comentarios de usuarios respecto a la experiencia en una aerolinea. con esta informacion se debe hacer un analisis de su experiencia e identificar que comentarios son positivos, negativos o neutros.

  ## Como ejecutar

   Para ejecutar localmente se debe correr el siguiente comando:

  ``` spark-submit --master local[1] proyecto.py ```

   El dataset es Learning1.csv

   ## Dependencias

   * TF-IDF (Term frequency – Inverse document frequency): Es un método de vectorización
  de características ampliamente utilizado en la minería de textos para reflejar la
  importancia de un término para un documento

 El calculo del TF es solo contar las ocurrencias de una palabra en un documento.

 Para calcular el IDF se utiliza la sigiente formula:

 ![Tech](/formula.png)

 Después de calcular esto se procede a calcular el TF-IDF de la siguiente manera:
 ![Tech](/tf.png)

## Referencias


http://python-apuntes.blogspot.com.

https://spark.apache.org/docs/2.2.0/mllib-feature-extraction.html

https://machinelearningmastery.com/clean-text-machine-learning-python/

http://web.cs.ucla.edu/~mtgarip/linear.html

http://spark.apache.org/docs/latest/mllib-linear-methods.html#linear-support-vector-machines-svms
