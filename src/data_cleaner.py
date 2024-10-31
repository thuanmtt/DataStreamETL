def clean_data(data):
    # Làm sạch dữ liệu ở đây, ví dụ:
    cleaned_data = {
        "data_field1": data.get("field1"),
        "data_field2": data.get("field2", 0.0),
    }
    return cleaned_data
