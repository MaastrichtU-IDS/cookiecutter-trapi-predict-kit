from typing import Optional, List

from openpredict.predict_output import PredictOutput, TrapiRelation

from openpredict import trapi_predict, PredictOptions, PredictOutput

@trapi_predict(path='/predict',
    name="Get predicted targets for a given entity",
    description="Return the predicted targets for a given entity: drug (DrugBank ID) or disease (OMIM ID), with confidence scores.",
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
    # Add the code the load the model and get predictions here
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
    # Example to be run when the script is executed directly
    print(get_predictions("drugbank:DB00002", PredictOptions()))