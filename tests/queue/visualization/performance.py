import unittest

import plotly.graph_objects as go

from src.queue.operations.time import get_queue_push_time


class TestQueuePerformance(unittest.TestCase):

    def test_performance_vs_queue(self):
        sample: int = 1000
        data = [get_queue_push_time(10, i) for i in range(sample)]

        queue_times = [i[0].values[0] for i in data]
        heap_times = [i[1].values[0] for i in data]

        times = [i for i in range(sample)]

        fig = go.Figure(layout=go.Layout(
            title="Queue performance",
            updatemenus=[dict(type="buttons", direction="right", x=0.9, y=1.16), ],
        ))

        init = 1

        fig.add_trace(
            go.Scatter(x=times[:init],
                       y=queue_times[:init],
                       name="Queue",
                       visible=True,
                       line=dict(color="#33CFA5", dash="dash")))

        fig.add_trace(
            go.Scatter(x=times[:init],
                       y=heap_times[:init],
                       name="Custom Heap",
                       visible=True,
                       line=dict(color="#000000", dash="dash")))

        fig.update(frames=[
            go.Frame(
                data=[
                    go.Scatter(x=times[:k], y=queue_times[:k]),
                    go.Scatter(x=times[:k], y=heap_times[:k])]
            )
            for k in range(0, sample)])

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