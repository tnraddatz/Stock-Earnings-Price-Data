from matplotlib import pyplot as plt

class CreateGraph:

    def __init__(self, data_hash):
        self.data_hash = data_hash

    def generate_scatter_plot(self):
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        plt.xlabel('Actual Return')
        plt.ylabel('Expected Return +/- ')
        #plt.scatter([-4,-3,-2,-1,0,1, 2, 3, 4], [-4,-3,-2,-1,0,1, 2, 3, 4])
        
        good_data_x = []#This is the data that we expect and will label green
        good_data_y = [] 
        bad_data_x = [] #This is the data we did not expect and will label red 
        bad_data_y = []

        #[datetime.datetime(2005, 5, 6, 0, 0), '77.730003', ['77.330002', '77.470001', '77.349998', '76.760002', '76.879997', '76.470001', '75.230003', '76.599998', '76.129997', '77.510002', '77.059998']]
        while len(self.data_hash) > 0:
            key, value = self.data_hash.popitem()
            plt.title(key)
            for data in value: 
                after_report_price = data[1]
                gain_or_loss_prior = (data[2][0] - data[2][-1]) / data[2][-1] #return % over 10 days
                gain_or_loss_after = (after_report_price - data[2][0]) / data[2][0] #return % (after - before / before)
                #IF BAD DATA
                if (gain_or_loss_prior > 0 and gain_or_loss_after < 0) or (gain_or_loss_prior < 0 and gain_or_loss_after > 0 ):
                    bad_data_x.append(gain_or_loss_after)
                    bad_data_y.append(gain_or_loss_prior)
                else: #If Good Data 
                    good_data_x.append(gain_or_loss_after)
                    good_data_y.append(gain_or_loss_prior)

        plt.scatter(good_data_x, good_data_y, color = "green")
        plt.scatter(bad_data_x, bad_data_y, color = "red")
        plt.show()