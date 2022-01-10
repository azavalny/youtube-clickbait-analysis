class YouTube_Classifier_Ensemble():
     """This is a custom Scikit-Learn based Ensemble classifier using two of my own custom classifiers for YouTube Video 
     Clickbait Classification"""

     def __init__(self, title_filepath, stats_filepath):
       self.title = keras.models.load_model(title_filepath)
       stats_clf = pickle.load(open(stats_filepath, 'rb'))
       self.stats = stats

     def predict_probabilities(self, title_data, stats_data):
      """Returns an array of probabilities of whether the title and stats of a YouTube video are clickbait"""
      y_pred_title = self.title.predict(title_data)
      
      y_pred_stats = self.stats.predict_proba(stats_data)


      final_predictions = []

      for p in range(len(y_pred_title)):
        final_predictions.append((y_pred_title*0.75) + (y_pred_stats*0.25))

      return final_predictions