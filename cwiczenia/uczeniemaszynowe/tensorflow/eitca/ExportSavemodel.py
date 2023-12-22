import tensorflow as tf
import numpy as np

classifier = tf.estimator.LinearClassifier()

feature_spec = {'flower_features': tf.FixedLenFeature(shape=[4], dtype=np.float32)}

serving_fn = tf.estimator.export.build_parsing_serving_input_receiver_fn(feature_spec)
# classifier.train()
# classifier.evaluate()
classifier.export_savedmodel(export_dir_base='/tmp/iris_model' + '/export', serving_input_receiver_fn=serving_fn)
