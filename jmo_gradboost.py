import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.model_selection import train_test_split

# pns = pd.read_csv('DHSlbr.csv')
# df = pd.read_csv("jmo_final/hightops_data.csv")
df = pd.read_csv("hightops_data.csv")
df = df.dropna()

df.dtypes

df = df.rename(columns = {"Retail Price": "retail_price",
                          "Sale Price":"sale_price",
                          "Shoe Size": "shoe_size",
                          "Buyer Region": "state",
                          "Brand": "brand",
                          "Sneaker Name": "sneaker_name"})

df['retail_price'] = df.retail_price.str.replace('$','')
df['sale_price'] = df.sale_price.str.replace('$','')
df['sale_price'] = df.sale_price.str.replace(',','')

df['retail_price'] = df['retail_price'].astype(int)
df['sale_price'] = df['sale_price'].astype(int)

df['shoe_size'] = df['shoe_size'].astype(int)
df['state'] = df['state'].astype(str)
df['brand'] = df['brand'].astype(str)

# df['sale_price'].plot(kind='hist')
# plt.show()

sale_index = pd.cut(df.sale_price,bins=[0,500,4500],labels=[0,1])
# sale_index = pd.cut(df.sale_price,bins=[-0.5,10000,40000],labels=[0,1])
# sale_index = pd.cut(df.sale_price,bins=[-0.5,20000,40000],labels=[0,1])
# sale_index = pd.cut(df.sale_price,bins=[-0.5,30000,40000],labels=[0,1])

# sale_index = pd.cut(df.sale_price,bins=[-0.5,10000,20000,40000],labels=[0,1,0], ordered=False)
# sale_index = pd.cut(df.sale_price,bins=[-0.5,20000,30000,40000],labels=[0,1,0], ordered=False)

df.insert(1,'sale_price_index', sale_index)

# df = df[['sale_price_index','retail_price', 'shoe_size', 'state', 'brand']]
df = df[['sale_price_index','retail_price', 'shoe_size']]

df = df.dropna()

X_train, X_test = train_test_split(df, test_size=0.25)
y_train = X_train.pop('sale_price_index')
y_test = X_test.pop('sale_price_index')

# CATEGORICAL_COLUMNS = ['shoe_size', 'state', 'brand']
CATEGORICAL_COLUMNS = ['shoe_size']
NUMERIC_COLUMNS = ['retail_price']

def one_hot_cat_column(feature_name, vocab):
  return tf.feature_column.indicator_column(
      tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocab))

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
  # Need to one-hot encode categorical features.
  vocabulary = X_train[feature_name].unique()
  feature_columns.append(one_hot_cat_column(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
      feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

example = dict(X_train.head(1))
example = dict(X_train.head())
example = dict(X_train)
# class_fc = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_vocabulary_list('brand', (0, 1)))
# print('Feature value: "{}"'.format(example['brand'].iloc[0]))
# print('One-hot encoded: ', tf.keras.layers.DenseFeatures([class_fc])(example).numpy())

tf.keras.layers.DenseFeatures(feature_columns)(example).numpy()

NUM_EXAMPLES = len(y_train)

def make_input_fn(X, y, n_epochs=None, shuffle=True):
  def input_fn():
    dataset = tf.data.Dataset.from_tensor_slices((dict(X), y))
    if shuffle:
      dataset = dataset.shuffle(NUM_EXAMPLES)
    # For training, cycle thru dataset as many times as need (n_epochs=None).
    dataset = dataset.repeat(n_epochs)
    # In memory training doesn't use batching.
    dataset = dataset.batch(NUM_EXAMPLES)
    return dataset
  return input_fn

train_input_fn = make_input_fn(X_train, y_train)
eval_input_fn = make_input_fn(X_test, y_test, shuffle=False, n_epochs=1)

linear_est = tf.estimator.LinearClassifier(feature_columns) #logistic regression model

linear_est.train(train_input_fn, max_steps=100)

# Evaluation.
result = linear_est.evaluate(eval_input_fn)
# clear_output()
print(pd.Series(result))

# Since data fits into memory, use entire dataset per layer. It will be faster.
# Above one batch is defined as the entire dataset.
n_batches = 1
est = tf.estimator.BoostedTreesClassifier(feature_columns, n_batches_per_layer=n_batches)

# The model will stop training once the specified number of trees is built, not
# based on the number of steps.
est.train(train_input_fn, max_steps=100)

# result = est.evaluate(eval_input_fn)
# clear_output()
# print(pd.Series(result))

# logistic regression
# pred_dicts = list(linear_est.predict(eval_input_fn))
# probs_l = pd.Series([pred['probabilities'][1] for pred in pred_dicts])
# probs_l.plot(kind='hist', bins=20, title='predicted probabilities')
# plt.show()

# boosted tree
pred_dicts = list(est.predict(eval_input_fn))
probs = pd.Series([pred['probabilities'][1] for pred in pred_dicts])
probs.plot(kind='hist', bins=20, title='predicted probabilities')
plt.show()

# pdfs
# probs_l.plot(kind='kde')
probs.plot(kind='kde', title='predicted probabilities')
plt.show()

from sklearn.metrics import roc_curve

fpr, tpr, _ = roc_curve(y_test, probs)
plt.plot(fpr, tpr)
plt.title('ROC curve')
plt.xlabel('false positive rate')
plt.ylabel('true positive rate')
plt.xlim(0,)
plt.ylim(0,)
plt.show()