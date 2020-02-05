from sklearn.utils.validation import check_is_fitted

import functools


def add_class_name(func):
    @functools.wraps(func)
    def wrapper_add_class_name(*args, **kwargs):
        value = func(*args, **kwargs)
        return value.add_suffix("__" + args[0].__class__.__name__)

    return wrapper_add_class_name


class FeatureMixin:
    """Mixin class for all feature extraction estimators in giotto-time."""

    _estimator_type = "feature_extractor"

    def get_feature_names(self):
        """Return feature names for output features.

        Returns
        -------
        output_feature_names : ndarray, shape (n_output_features,)
            Array of feature names.

        """
        check_is_fitted(self)

        return [f"{name}__{self.__class__.__name__}" for name in self.columns_]
