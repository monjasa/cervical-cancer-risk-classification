import pickle

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

from classifier import rfc

app = FastAPI(title="Cervical Cancer Risk Classification",
              description="API for a cervical cancer risk classification machine learning model",
              version="1.0")


class InputSample(BaseModel):
    age: int
    number_of_sexual_partners: float
    first_sexual_intercourse: float
    number_of_pregnancies: float
    smokes: bool
    smokes_years: float
    smokes_packs_year: float
    hormonal_contraceptives: bool
    hormonal_contraceptives_years: float
    iud: bool
    iud_years: float
    stds: bool
    stds_number: int
    stds_condylomatosis: bool
    stds_vaginal_condylomatosis: bool
    stds_vulvo_perineal_condylomatosis: bool
    stds_syphilis: bool
    stds_pelvic_inflammatory_disease: bool
    stds_genital_herpes: bool
    stds_molluscum_contagiosum: bool
    stds_hiv: bool
    stds_hepatitis_b: bool
    stds_hpv: bool
    dx_cin: bool
    dx_hpv: bool
    hinselmann: bool
    schiller: bool
    citology: bool


@app.on_event("startup")
async def load_model():
    with open("../models/rfc.pickle", "rb") as f:
        rfc.model = pickle.load(f)


@app.get("/health")
async def health():
    return


@app.post("/predict")
async def predict(input_sample: InputSample):
    x = np.fromiter(input_sample.dict().values(), dtype=float)
    y_pred = rfc.model.predict(x.reshape(1, -1))[0]
    return {"result": bool(y_pred)}
