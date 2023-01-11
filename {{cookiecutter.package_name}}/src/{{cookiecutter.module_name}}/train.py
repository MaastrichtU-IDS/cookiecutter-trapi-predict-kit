import logging

import typer
from fairworkflows import FairWorkflow, is_fairstep, is_fairworkflow
from openpredict import save
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

log = logging.getLogger()

cli = typer.Typer(help="Training for models")

@cli.command(help='Train a model')
def train_model(n_jobs = 2):
    model_id = "{{cookiecutter.module_name}}"

    workflow = FairWorkflow.from_function(training_workflow)
    result, prov = workflow.execute(n_jobs)
    # This does not really execute the workflow, only analyzes it

    log.info("Publishing to Nanopub test server")
    workflow.publish_as_nanopub(use_test_server=True, publish_steps=True)
    prov.publish_as_nanopub(use_test_server=True)

    # Actually run the training workflow
    loaded_model = training_workflow(n_jobs)

    workflow._rdf.serialize(f"models/{model_id}.workflow.trig", format="trig")
    prov._rdf.serialize(f"models/{model_id}.prov.trig", format="trig")

    return loaded_model


@is_fairstep(label='Load data', is_script_task=True)
def load_data():
    data, y = load_iris(return_X_y=True, as_frame=True)
    return data
    # return {
    #     "data": data,
    #     "y": y
    # }

@is_fairstep(label='Load data y', is_script_task=True)
def load_data_y():
    # We need to duplicate the use of load_iris because FAIRworkflow
    # doesn't support returning tuples or objects
    data, y = load_iris(return_X_y=True, as_frame=True)
    return y

@is_fairstep(label='Create and fit classifier', is_script_task=True)
def fit_classifier(hyper_params, data, y):
    clf = RandomForestClassifier(
        n_jobs=hyper_params['n_jobs'],
        random_state=hyper_params['random_state'],
    )
    clf.fit(data, y)
    return clf


@is_fairstep(label='Evaluate the trained model', is_script_task=True)
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


@is_fairstep(label='Save the trained model', is_script_task=True)
def save_model(model, path, sample_data, scores, hyper_params):
    loaded_model = save(
        model,
        path,
        sample_data=sample_data,
        scores=scores,
        hyper_params=hyper_params,
    )
    return loaded_model


@is_fairworkflow(label='{{cookiecutter.package_name_stylized}} training workflow')
def training_workflow(n_jobs: int):

    # Define models hyper params
    hyper_params = {
        'n_jobs': n_jobs,
        'random_state': 42
    }

    data = load_data()
    y = load_data_y()

    # Train model (here we use a stub dataset just to make the example clear)
    model = fit_classifier(hyper_params, data, y)

    # Evaluate the model using your own metrics
    scores = evaluate(model)

    # Save the model generated to the models/ folder
    loaded_model = save_model(
        model,
        "models/{{cookiecutter.module_name}}",
        sample_data=data,
        scores=scores,
        hyper_params=hyper_params,
    )
    return loaded_model
    # Optionally you can save other files (dataframes, JSON objects) in the data/ folder


if __name__ == '__main__':
    cli()
