import unittest

import plotly.graph_objects as go
import pandas as pd
import numpy as np
from tests.hash_table.visualization.data.hash_distribution import get_all_data


class CollisionTest(unittest.TestCase):

    def test_collision(self):
        min_hash_table_size = 20
        max_hash_table_size = 400
        elements = 300
        data = get_all_data(min_hash_table_size, max_hash_table_size, elements)

        hash_collisions = np.asarray(data[0])
        hash_salt_collisions = np.asarray(data[1])
        sha_salt_collisions = np.asarray(data[2])

        x_axis = [i for i in range(min_hash_table_size, max_hash_table_size + 1)]

        fig = go.Figure(layout=go.Layout(
            title="Hash collisions test",
            updatemenus=[dict(type="buttons", direction="right", x=0.9, y=1.16), ],
        ))

        init = 0

        fig.add_trace(
            go.Scatter(x=x_axis[:init],
                       y=hash_collisions[:init],
                       name="Hash",
                       visible=True,
                       line=dict(color="#261218", dash="dash")))

        fig.add_trace(
            go.Scatter(x=x_axis[:init],
                       y=hash_salt_collisions[:init],
                       name="Salt hash",
                       visible=True,
                       line=dict(color="#c91839", dash="dash")))

        fig.add_trace(
            go.Scatter(x=x_axis[:init],
                       y=sha_salt_collisions[:init],
                       name="Sha hash with salt",
                       visible=True,
                       line=dict(color="#18c930", dash="dash")))

        fig.update(frames=[
            go.Frame(
                data=[
                    go.Scatter(x=x_axis[:k], y=hash_collisions[:k]),
                    go.Scatter(x=x_axis[:k], y=hash_salt_collisions[:k]),
                    go.Scatter(x=x_axis[:k], y=sha_salt_collisions[:k])
                ]
            )
            for k in range(max_hash_table_size - min_hash_table_size + 1)])

        # Buttons
        fig.update_layout(
            updatemenus=[
                dict(
                    buttons=list([
                        dict(label="Play",
                             method="animate",
                             args=[None, {"frame": {"duration": 100}}])
                    ]))],
            autosize=True
        )

        fig.show()
