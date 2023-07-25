import logging

from trapi_predict_kit.config import settings
from trapi_predict_kit import TRAPI
from {{cookiecutter.module_name}}.predict import get_predictions


log_level = logging.ERROR
if settings.DEV_MODE:
    log_level = logging.INFO
logging.basicConfig(level=log_level)

openapi_info = {
    "contact": {
        "name": "{{cookiecutter.author_name}}",
        "email": "{{cookiecutter.author_email}}",
        # "x-id": "{{cookiecutter.author_orcid}}",
        "x-role": "responsible developer",
    },
    "license": {
        "name": "MIT license",
        "url": "https://opensource.org/licenses/MIT",
    },
    "termsOfService": 'https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_name}}/blob/main/LICENSE.txt',

    "x-translator": {
        "component": 'KP',
        # TODO: update the Translator team to yours
        "team": [ "Clinical Data Provider" ],
        "biolink-version": settings.BIOLINK_VERSION,
        "infores": 'infores:openpredict',
        "externalDocs": {
            "description": "The values for component and team are restricted according to this external JSON schema. See schema and examples at url",
            "url": "https://github.com/NCATSTranslator/translator_extensions/blob/production/x-translator/",
        },
    },
    "x-trapi": {
        "version": settings.TRAPI_VERSION,
        "asyncquery": False,
        "operations": [
            "lookup",
        ],
        "externalDocs": {
            "description": "The values for version are restricted according to the regex in this external JSON schema. See schema and examples at url",
            "url": "https://github.com/NCATSTranslator/translator_extensions/blob/production/x-trapi/",
        },
    }
}

app = TRAPI(
    predict_endpoints=[ get_predictions ],
    info=openapi_info,
    title='{{cookiecutter.package_name_stylized}} TRAPI',
    version='1.0.0',
    openapi_version='3.0.1',
    description="""{{cookiecutter.short_description}}
\n\nService supported by the [NCATS Translator project](https://ncats.nih.gov/translator/about)""",
    # itrb_url_prefix="{{cookiecutter.package_name}}",
    # dev_server_url="https://{{cookiecutter.package_name}}.semanticscience.org",
)

