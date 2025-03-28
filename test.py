from flask import Flask, render_template_string
import plotly.graph_objs as go
import plotly.offline as pyo

app = Flask(__name__)

# Example Plotly graph
def create_plot():
    # Create a simple scatter plot
    trace = go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[10, 15, 13, 17, 21],
        mode='lines+markers',
        name='Example Data'
    )

    layout = go.Layout(
        title='Example Plotly Graph',
        xaxis=dict(title='X-axis'),
        yaxis=dict(title='Y-axis')
    )

    fig = go.Figure(data=[trace], layout=layout)
    return pyo.plot(fig, output_type='div', include_plotlyjs=False)

@app.route('/')
def index():
    # Generate the Plotly graph
    plot_div = create_plot()
    
    # Render the HTML template with the Plotly graph
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Plotly in Flask</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
        <body>
            <h1>Plotly Graph in Flask</h1>
            {{ plot_div|safe }}
        </body>
        </html>
    ''', plot_div=plot_div)

if __name__ == '__main__':
    app.run(debug=True)