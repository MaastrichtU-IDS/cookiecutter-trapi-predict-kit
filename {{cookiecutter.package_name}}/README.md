# 🔮 {{cookiecutter.package_name_stylized}}

[![Tests](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}/actions/workflows/test.yml/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}/actions/workflows/test.yml)

{{cookiecutter.short_description}}

## 📥️ Setup

You will need Python >=3.8 and <3.11

1. Clone the repository:

   ```bash
   git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}
   cd {{cookiecutter.package_name}}
   ```

2. Install [`hatch`](https://hatch.pypa.io) to manage the project if not already done

   ```bash
   pip install --upgrade hatch
   ```

3. Use hatch to install the dependencies, this will also pull the data required to run the models in the `data` folder with [`dvc`](https://dvc.org/):

   ```bash
   hatch -v env create
   ```

4. See below to setup [`dvc`](https://dvc.org) for data version control. It helps you to easily store datasets used by your machine learning workflows, and keep track of changes in a way similar to git. Like git, with dvc you will need to choose a platform to publish your data, such as [DagsHub](https://dagshub.com/docs/integration_guide/dvc/) or [HuggingFace](https://dvc.org/doc/dvclive/api-reference/ml-frameworks/huggingface).

### Create a new project on DagsHub

Here we document the process using [DagsHub](https://dagshub.com/docs/integration_guide/dvc/) to publish data related to a ML experiment, but you could choose to use a different platform for your project if you wish.

⚠️ Open source projects on DagsHub using the free plan have a 10G storage limit.

1. Go to [dagshub.com](https://dagshub.com/user/login), and login with GitHub or Google

2. Create a new project in DagsHub by connecting it to the GitHub repository with the code for the experiment (this repository)

3. Set your DagsHub credentials in your local terminal (add these commands to your `~/.bashrc` or `~/.zshrc` to enable it automatically on boot):

   ```bash
   export DAGSHUB_USER="{{cookiecutter.github_username}}"
   export DAGSHUB_TOKEN="TOKEN"
   ```

4. Link your local repository to the created DagsHub project:

   ```bash
   hatch run dvc remote add origin https://dagshub.com/$DAGSHUB_USER/openpredict-model.dvc
   hatch run dvc remote default origin
   hatch run dvc remote modify origin --local auth basic
   hatch run dvc remote modify origin --local user $DAGSHUB_USER
   hatch run dvc remote modify origin --local password $DAGSHUB_TOKEN
   ```

### Push data

⚠️ Put all data files required to train the model, and the files generated by the training to the `data/` folder and publish this data to a public repository on a platform like DagsHub or HuggingFace

First add the changes made to the `data/` folder:

```bash
hatch run dvc add data
```

Then push the added data:

```bash
hatch run dvc push
```

Alternatively you can use this shortcut to add changes and push in one command:

```bash
hatch run push-data
```

### Pull data

```bash
hatch run dvc pull
```

You can check the status `dvc` in the current repository with:

```bash
hatch run dvc status
```

## 🪄 Usage

You are free to setup your development workflow as you wish, consider those instructions as recommendations which work out-of-the-box with the code generated by the template.

### Deploy TRAPI

Deploy  your prediction function as a Translator Reasoner API on http://localhost:8808:

```bash
hatch -v run dev
```

### Train

Run the training function to train the model:

```bash
hatch run train
```

### Predict

Run the prediction function providing an input ID:

```bash
hatch run predict drugbank:DB00002
```

### Test

Run the tests locally:

```bash
hatch run test -s
```

### Add dependencies

Add dependencies directly in the `pyproject.toml`. Try to keep the main dependencies minimal: just what is needed to run the predictions functions. And add all dependencies required for training in the `train` optional dependencies.

Hatch will automatically update the virtual environment the next time you use it to run a script.

If you are facing issue with the dependencies (e.g. not updated properly), you can reset the environment with:

```bash
hatch env prune
```

## 🐳 Docker

Start the TRAPI API:

```bash
docker-compose up
```

## 🙏 Acknowledgments

Project bootstrapped with https://github.com/MaastrichtU-IDS/cookiecutter-trapi-predict-kit
