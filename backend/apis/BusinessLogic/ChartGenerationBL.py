import os
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

"""
References:
1. Private methods in python classes
        https://www.geeksforgeeks.org/private-methods-in-python/
"""


class ChartGenerationBL:

    def __init__(self):
        self.generated_images_list: list = []

    def __read_and_preprocess_data(self, input_file_path, fps):
        # Read the CSV file
        data = pd.read_csv(input_file_path)

        # Calculate the center of the bounding box
        data['x_center'] = (data['bbox_x_min'] + data['bbox_x_max']) / 2
        data['y_center'] = (data['bbox_y_min'] + data['bbox_y_max']) / 2

        # Sort the data by frame_id
        data = data.sort_values(by='frame_id')

        # Create a unique identifier for each instrument
        data['instrument_id'] = data['class'] + '_' + data['id'].astype(str)

        # Calculate the difference in x_center and y_center for each unique
        # instrument between frames
        data['x_diff'] = data.groupby('instrument_id')['x_center'].diff()
        data['y_diff'] = data.groupby('instrument_id')['y_center'].diff()

        # Calculate the velocity (Euclidean distance between position vectors at two consecutive frames / time difference)
        # Time difference between frames is 1/30 seconds as fps = 30

        data['velocity'] = ((data['x_diff'] ** 2 + data['y_diff'] ** 2) ** 0.5) * fps

        # Calculate the unique number of frames for each instrument_id
        unique_frames_counts = data.groupby('instrument_id')['frame_id'].nunique()

        # Get the instrument_id's with fewer than 30 unique frames
        instruments_to_drop = unique_frames_counts[unique_frames_counts < 30].index

        # Drop the instrument_id's from the DataFrame
        filtered_df = data[~data['instrument_id'].isin(instruments_to_drop)]
        return filtered_df

    def __create_instrument_confidence_histogram(self, filtered_data, output_storage_path):
        # Create a histogram for each instrument type
        fig = px.histogram(filtered_data, x='conf', color='class', barmode='group',
                           title='Confidence Histogram for Each Instrument Type')

        # Update layout and axis labels
        fig.update_layout(xaxis_title='Confidence', yaxis_title='Count')

        # Remove the first y-tick near the x-axis
        fig.update_yaxes(ticks="outside", tick0=None, showticklabels=True)

        # Adjust the figure size
        fig.update_layout(height=400, width=800)

        # Update title
        fig.update_layout(
            title={
                'text': 'Instruments confidence histogram',
                'font': {'size': 20, 'family': 'Arial', 'color': 'white'},
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

        # Display the figure
        # fig.show()

        # Save the figure as a PNG file
        name: str = "instruments_confidence_histogram.png"
        pio.write_image(fig, f'{output_storage_path}/{name}')
        self.generated_images_list.append(name)

    def __create_average_velocity_radar_plot(self, filtered_df, output_storage_path):
        # Create a mask for rows where confidence is greater than 0.7
        mask = filtered_df['conf'] > 0.7

        # Calculate the average velocity for each instrument using the mask
        average_velocity = filtered_df.loc[mask].groupby('instrument_id')[
            'velocity'].mean()

        # Create radar plot
        fig = go.Figure(data=go.Scatterpolar(
            r=average_velocity.values,
            theta=average_velocity.index,
            fill='toself'
        ), layout=go.Layout(width=600))  # Adjust the plot width

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, average_velocity.max()]
                )),
            showlegend=False,
            title={
                'text': "Average Velocity for Instruments with high mean confidence",
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            template='plotly_dark'
        )

        # Save the figure as a PNG file
        name: str = "Instruments_average_velocity_radar_plot.png"
        pio.write_image(fig, f'{output_storage_path}/{name}')
        self.generated_images_list.append(name)

        # fig.show()

    def __create_merged_instrument_trajectories_over_time(
            self,
            filtered_total_distance_df, output_storage_path):
        '''
        This function creates a single plot with the trajectories of all the instrument instances and shows them in a single plot.
        '''

        # Trajectory plot
        fig = px.line(
            filtered_total_distance_df,
            x="x_center",
            y="y_center",
            color="instrument_id",
            title="Instrument Trajectories Over Time",
            line_group="instrument_id",
            hover_name="instrument_id",
            template="plotly_dark")
        fig.update_layout(
            title={
                'text': "Instrument Trajectories Over Time",
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
        # Reverse y-axis due to image coordinate system convention
        fig.update_yaxes(autorange="reversed")

        # Save the figure as a PNG file
        name: str = "all_instruments_trajectory.png"
        pio.write_image(fig, f'{output_storage_path}/{name}')
        self.generated_images_list.append(name)
        # fig.show()

    def generate(self, input_file_path: str, fps: int, output_storage_path: str):
        if not os.path.isdir(output_storage_path):
            os.makedirs(output_storage_path)
            # print('All plots will be saved here : ', output_storage_path)

        # Read and preprocess the data
        filtered_data = self.__read_and_preprocess_data(input_file_path, fps)

        # Set the theme for Plotly express
        px.defaults.template = 'plotly_dark'

        # Set dark theme
        pio.templates.default = "plotly_dark"

        # Create the instrument confidence histogram
        self.__create_instrument_confidence_histogram(filtered_data, output_storage_path)

        # Create the average velocity radar plot
        self.__create_average_velocity_radar_plot(filtered_data, output_storage_path)

        # Create the merged trajectories plot for all instrument instances
        self.__create_merged_instrument_trajectories_over_time(
            filtered_data, output_storage_path)

        return self.generated_images_list
