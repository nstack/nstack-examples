# Model Training Demonstration

This module illustrates how to train a scikit-learn model within
NStack. The key idea is to initialise the model within the `__init__`
method of the `Service` class. Following that, when data gets passed to
the model, the length of the passed vector is checked: if it is equal to
the number of features, inference mode is assumed and the model's
`predict_proba` method is called. If the length is one more than the
number of features, the extra value is assumed to be a training target,
and the model's `partial_fit` method is called.

The model is smart enough to set the number of features from the first
call to `partial_fit`. All subsequent calls, and all calls to
`predict_proba`, must have the same number of features.
