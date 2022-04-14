# Cervical Cancer Risk Classification

The project repository of a machine learning model deployment for solving the problem of Risk Classification of Cervical Cancer developed with FastAPI framework and Docker.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

The setups steps expect following tools installed on the system.

* [Docker Desktop](https://www.docker.com/get-started/)

## Installing

### Clone the repository

```
git@github.com:monjasa/cervical-cancer-risk-classification.git
cd cervical-cancer-risk-classification
```

### Build the Docker image

```
docker build -t cervical-cancer-image .
```

## Serve

### Run the Docker container

```
docker run -d -p 80:80 --name cervical-cancer cervical-cancer-image 
```

And now you can visit the Swagger documentation with the URL http://localhost/docs.

### Try out the POST /predict endpoint

```
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 21,
  "number_of_sexual_partners": 3,
  "first_sexual_intercourse": 17,
  "number_of_pregnancies": 1,
  "smokes": true,
  "smokes_years": 1.33,
  "smokes_packs_year": 10,
  "hormonal_contraceptives": false,
  "hormonal_contraceptives_years": 0,
  "iud": false,
  "iud_years": 0,
  "stds": true,
  "stds_number": 1,
  "stds_condylomatosis": false,
  "stds_vaginal_condylomatosis": false,
  "stds_vulvo_perineal_condylomatosis": false,
  "stds_syphilis": true,
  "stds_pelvic_inflammatory_disease": false,
  "stds_genital_herpes": false,
  "stds_molluscum_contagiosum": false,
  "stds_hiv": false,
  "stds_hepatitis_b": false,
  "stds_hpv": false,
  "dx_cin": false,
  "dx_hpv": false,
  "hinselmann": true,
  "schiller": false,
  "citology": false
}'
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
