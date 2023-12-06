from sklearn.preprocessing import MinMaxScaler

class DataPreprocessing:
    def __init__(self):
        self.scaler_x = MinMaxScaler()

    def user_data(self, data):
        data = self.scaler_x.fit_transform(data)
        user_data_scaled = self.scaler_x.transform(data)
        return user_data_scaled
