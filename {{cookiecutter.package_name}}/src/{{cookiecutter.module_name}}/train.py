import typer
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

from openpredict import save


cli = typer.Typer(help="Training for models")

@cli.command(help='Train a model')
def train_model(n_jobs: int = 2):
    # Define models hyper params
    hyper_params = {
        'n_jobs': n_jobs,
        'random_state': 42
    }

    # Train model (here web use a stub dataset just to make the example clear)
    data, y = load_iris(return_X_y=True, as_frame=True)
    model = RandomForestClassifier(
        n_jobs=hyper_params['n_jobs'],
        random_state=hyper_params['random_state'],
    )
    model.fit(data, y)

    # Evaluate the model using your own metrics
    scores = evaluate(model)

    # Save the model generated to the models/ folder
    save(
        model,
        "models/{{cookiecutter.module_name}}",
        sample_data=data,
        scores=scores,
        hyper_params=hyper_params,
    )

    # Optionally you can save other files (dataframes, JSON objects) in the data/ folder


def evaluate(model):
    # Evaluate the quality of your model using custom metrics
    # cf. https://scikit-learn.org/stable/modules/model_evaluation.html
    return {
        'precision': 0.85,
        'recall': 0.80,
        'accuracy': 0.85,
        'roc_auc': 0.90,
        'f1': 0.75,
        'average_precision': 0.85,
    }


if __name__ == '__main__':
    cli()