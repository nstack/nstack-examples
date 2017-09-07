# coding: utf-8

import numpy as np
import pandas as pd
import sklearn as skl
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

print("sklearn version: ", skl.__version__)

# Download the data from the following URL:
# https://s3-eu-west-1.amazonaws.com/yc-rdata/yoochoose-data.7z
# and extract the files into the current directory in order to run
# this script.

print("Loading clicks data")
clicks = pd.read_csv('yoochoose-clicks.dat',
                     header=None,
                     names=['session_id', 'timestamp', 'item_id', 'category'],
                     index_col=[0,1],
                     nrows=None,
                     dtype={'category':'str'})

print("Loading buys data")
buys = pd.read_csv('yoochoose-buys.dat',
                   header=None,
                   names=['session_id', 'timestamp', 'item_id', 'price', 'quantity'],
                   index_col=[0,1],
                   nrows=None)

print("Starting preprocessing")

# In our example project, we will try to predict whether a session
# that contains a view of a given item leads to a purchase of that
# given item, based on the other items viewed in that session.

# We use the third most frequently clicked item, because
# the top two have lots of 'quantity == 0' purchase records, which we
# don't want to worry about (it's not clear what they mean).

top_bought_items = buys.groupby('item_id').size().sort_values(ascending=False)

# The item ID we will try to predict purchases of.
iid = top_bought_items.index[2]

# This is the set of session ids that contain a view of iid
sessions_viewed_iid = set(clicks[clicks['item_id'] == iid].index.get_level_values(0))

# session ids in which iid was purchased
sessions_bought_iid = set(buys[buys['item_id'] == iid].index.get_level_values(0))

#print(len(sessions_bought_iid), len(sessions_viewed_iid),
#      len(sessions_bought_iid.intersection(sessions_viewed_iid)))
# So all sessions where iid was bought also occur in clicks.

# Retain only sessions which viewed the item in question
df_clickstreams = clicks[clicks.index.get_level_values(0).isin(sessions_viewed_iid)]

# As a first pass, the features we will use are views of the most
# frequently viewed items.

df_purchases = clicks[clicks.index.get_level_values(0).isin(sessions_bought_iid)]

# We select the 30 most viewed items to be used as features for our model:
# If the session contains a view of that item, the feature will be set to
# 1.0, otherwise 0.0 .
num_features = 30
item_ids_features = list(df_purchases.groupby('item_id').size().sort_values(ascending=False).index[:num_features])

# Now, for each item_ids_features, and for each session in df_clickstreams,
# populate the relevant element of the feature vector X and label vector y.

viewed_items = {}
for name, group in df_clickstreams.groupby(level=0):
    viewed_items[name] = set(group['item_id'])

num_samples = len(viewed_items)

# Create initial arrays for raw feature vectors and labels.
X_raw = np.zeros((num_samples, num_features))
y_raw = np.zeros(num_samples)

def gen_featurevec(item_set):
    '''
    For a set of viewed items in a given session `item_set`, return a
    list of length `n_features` where each element is 1.0 if item_set
    contains the item corresponding to that feature, and 0.0 otherwise.
    '''
    return [int(item in item_set)for item in item_ids_features]

for i, (key, val) in enumerate(viewed_items.items()):
    fvec = gen_featurevec(val)
    X_raw[i,:] = fvec
    y_raw[i] = float(key in sessions_bought_iid)

# The original dataset is highly imbalanced, i.e. there are roughly 10x
# more negative samples than positive ones. Many ML algorithms can't
# handle that, so we create a balanced dataset by selecting only a subset
# of negative samples.
# First, we split the dataset into positive and negative samples:
X_pos = X_raw[y_raw == 1.0,:]
y_pos = y_raw[y_raw == 1.0]
X_neg = X_raw[y_raw == 0.0,:]
y_neg = y_raw[y_raw == 0.0]

# Create an array of size X_pos.shape[0] containing random indices into
# X_neg. Setting replace=False ensures there will be no duplicates.
ixs = np.random.choice(X_neg.shape[0], X_pos.shape[0], replace=False)

X_balanced = np.concatenate([X_pos, X_neg[ixs,:]], axis=0)
y_balanced = np.concatenate([y_pos, y_neg[ixs]], axis=0)

# Now that we have a balanced dataset, it's good practice to shuffle
# as well.
ixs = np.arange(X_balanced.shape[0])
np.random.shuffle(ixs)
X_shuffled = X_balanced[ixs,:]
y_shuffled = y_balanced[ixs]

# Now we split our balanced, shuffled dataset into train and test sets.
X_train, X_test, y_train, y_test = train_test_split(X_shuffled, y_shuffled, test_size=0.3)

# Now create and train the model.
print("Training model")
rfc = RandomForestClassifier().fit(X_train, y_train)
print("Mean accuracy on test set: ", rfc.score(X_test, y_test))

# Save the trained model to disk.
print("Saving model to disk")
joblib.dump(rfc, 'propensitymodel.pkl')

print("Loading model from disk")
rfc2 = joblib.load('propensitymodel.pkl')
print("Mean accuracy on test set: ", rfc.score(X_test, y_test))

