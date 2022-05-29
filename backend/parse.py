def parse(form_data):
    user_data = [
        form_data.age.data * 365,
        int(form_data.sex.data),
        form_data.height.data,
        form_data.weight.data,
        form_data.systolic_blood_pressure.data,
        form_data.diastolic_blood_pressure.data,
        int(form_data.cholestrol.data),
        int(form_data.gluc_level.data),
        int(form_data.smoking_Status.data),
        int(form_data.alcohol.data),
        int(form_data.active.data)
    ]

    return user_data