from data_repo_client import Configuration, ApiClient, SnapshotsApi
import os
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Helper class to make demo analysis easier
class AnalysisUtils:
    def __init__(self, token):
        config = Configuration()
        config.host="https://jade-az.datarepo-dev.broadinstitute.org/"
        config.access_token = token
        self.api_client = ApiClient(configuration=config)
        self.api_client.client_side_validation = False
        plt.rcParams["figure.figsize"] = [6,4]
        os.environ['TERRA_NOTEBOOK_GOOGLE_ACCESS_TOKEN'] = token
        os.environ['WORKSPACE_NAME'] = "ws"
        os.environ['GOOGLE_PROJECT'] = "googleProject"
        logger = logging.getLogger()
        logger.setLevel(logging.CRITICAL)
        
    # Instantiate TDR snapshots API
    def snapshots_api(self): 
        return SnapshotsApi(api_client=self.api_client)
    
    # Visualize distribution with each continuous trait
    def kdPlot(self, data, var):
        sns.set_style("whitegrid")
        sns.set_context("poster", 
                        font_scale = 0.9, 
                        rc={"grid.linewidth": 0.6, 'lines.linewidth': 1.6})
        sns.displot(data[(var)])
    
    # Visualize the distribution between two continuous traits
    def bivariateDistributionPlot(self, data, var1, var2, kind = "scatter"):
        with sns.axes_style("whitegrid"):
            jplot = sns.jointplot(x = data[var1], y = data[var2], kind=kind, color="k", s=1)
            jplot.set_axis_labels(var1, var2)
        
    # Visualize within each continuous trait, organized by dichotomous data
    def boxPlot(self, data, catagorical_var, continuous_var, color_by = None, force_x = False, force_color = False):
        make_plot = True
        if len(data[catagorical_var].unique().tolist()) > 10 and force_x is not True:
            make_plot = False
            print("catagorical_var must be catagorical. If you insist on using these x values, set force_x = True.")
        if color_by is not None:
            if len(data[color_by].unique()) > 5 and force_color is not True:
                make_plot = False
                print("color_by column must be catagorical. If you insist on using these values, set force_color = True.")

        if (make_plot is True):
            sns.set_style("whitegrid")
            sns.set_context("poster", 
                            font_scale = 0.7, 
                            rc={"grid.linewidth": 0.6, 'lines.linewidth': 1.6})
            sns.boxplot(x = catagorical_var, 
                        y = continuous_var, 
                        hue = color_by, 
                        data = data, 
                        palette = ["#275F9A", "#A2C353"],
                        saturation = 1)
            plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        
        
    
    