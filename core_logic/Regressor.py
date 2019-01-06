from models.forward_models.SVRModel import SVRModel
from models.forward_models.NearestDataPointModel import NearestDataPointModel
from models.forward_models.RidgeRegressor import RidgeRegressor
from models.forward_models.LassoRegressor import LassoRegressor
from models.forward_models.RandomForestModel import RandomForestModel
from models.forward_models.LinearModel import LinearModel
from models.forward_models.NeuralNetModel import NeuralNetModel
from models.forward_models.NeuralNetModel_keras import NeuralNetModel_keras
from helper_scripts.ModelHelper import ModelHelper

load_model = True	# Load the file from disk

class Regressor:
	"""
	Small adapter class that handles training and usage of the underlying models
	"""

	regression_model = None

	def __init__(self, output_name, regime):
		self.MH = ModelHelper.get_instance() # type: ModelHelper

		regime_indices = self.MH.regime_indices[regime]
		regime_feature_data = [self.MH.train_features_dat[x] for x in regime_indices]
		regime_label_data = [self.MH.train_labels_dat[output_name][x] for x in regime_indices]

		#self.regression_model = NeuralNetModel(regime_feature_data, regime_label_data)
		if load_model:
			self.regression_model = NeuralNetModel_keras()
			self.regression_model.load_model(output_name, regime)
		else:
			self.regression_model = NeuralNetModel_keras()
			self.regression_model.train_model(output_name, regime, regime_feature_data, regime_label_data)

	def predict(self,features):
		return self.regression_model.predict(features)
