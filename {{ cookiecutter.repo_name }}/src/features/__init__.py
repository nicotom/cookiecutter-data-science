import logging
from sklearn.pipeline import FeatureUnion
from sklearn_pandas import DataFrameMapper
from sklearn.preprocessing import StandardScaler


logger = logging.getLogger(__file__)


features_by_name = {
    'example_feature': lambda: DataFrameMapper([(['example_column'], StandardScaler())]),
}


def get_features(*features):
    names = [f for f in features if isinstance(f, str)]
    rest = [f for f in features if not isinstance(f, str)]

    # validate that names exists
    if any(n not in features_by_name for n in names):
        raise KeyError("Valid features are: {}".format(', '.join(sorted(features_by_name.keys()))))

    # if no features were given, all features by name are included
    if len(features) == 0:
        names = features_by_name.keys()

    named_features = [(name, features_by_name[name]()) for name in names]

    # make a big union
    return FeatureUnion(transformer_list=named_features + rest)