import sys
from typing import Optional, List

from openpredict import trapi_predict, PredictOptions, PredictOutput, load


# Define additional metadata to integrate this function in TRAPI
@trapi_predict(path='/predict',
    name="Get predicted targets for a given entity",
    description="Return the predicted targets for a given entity: drug (DrugBank ID) or disease (OMIM ID), with confidence scores.",
    # Define which relations can be predicted by this function in a TRAPI query
    relations=[
        {
            'subject': 'biolink:Drug',
            'predicate': 'biolink:treats',
            'object': 'biolink:Disease',
        },
        {
            'subject': 'biolink:Disease',
            'predicate': 'biolink:treated_by',
            'object': 'biolink:Drug',
        },
    ]
)
def get_predictions(
        input_id: str, options: PredictOptions
    ) -> PredictOutput:
    # You can easily load previously stored models
    loaded_model = load("models/{{cookiecutter.module_name}}")

    # Add the code to generate predicted associations for the provided input
    # loaded_model.model.predict_proba(x)

    # Predictions results should be a list of entities
    # for which there is a predicted association with the input entity
    predictions = {
        "hits": [
            {
                "id": "DB00001",
                "type": "biolink:Drug",
                "score": 0.12345,
                "label": "Leipirudin",
            }
        ],
        "count": 1,
    }
    return predictions


if __name__ == '__main__':
    # To be run when the script is executed directly
    input_id = "drugbank:DB00002"
    if sys.argv[1]:
        input_id = sys.argv[1]
    print(get_predictions(input_id, PredictOptions()))