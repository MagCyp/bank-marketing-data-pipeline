import numpy as np
import pandas as pd

bank_data = pd.read_csv("project/bank_marketing.csv")

# Client data

client_columns = {
    "client_id": "int64",
    "age": "int64",
    "job": "object",
    "marital": "object",
    "education": "object",
    "credit_default": "bool",
    "mortgage": "bool",
}

client_data = bank_data[list(client_columns.keys())].copy()

client_data["job"] = client_data["job"].str.replace(".", "_", regex=False)
client_data["education"] = (
    client_data["education"]
    .str.replace(".", "_", regex=False)
    .replace("unknown", np.nan)
)

bool_columns = ["credit_default", "mortgage"]
client_data[bool_columns] = client_data[bool_columns].eq("yes")

client_data = client_data.astype(client_columns)
client_data.to_csv("project/client.csv", index=False)


# Campaign data

campaign_columns = {
    "client_id": "int64",
    "number_contacts": "int64",
    "contact_duration": "int64",
    "previous_campaign_contacts": "int64",
    "previous_outcome": "bool",
    "campaign_outcome": "bool",
    "last_contact_date": "datetime64[ns]",
}

campaign_source_columns = [
    "client_id",
    "number_contacts",
    "contact_duration",
    "previous_campaign_contacts",
    "previous_outcome",
    "campaign_outcome",
]
campaign_data = bank_data[campaign_source_columns].copy()

campaign_data["previous_outcome"] = campaign_data["previous_outcome"].eq("success")
campaign_data["campaign_outcome"] = campaign_data["campaign_outcome"].eq("yes")

campaign_data["last_contact_date"] = pd.to_datetime(
    bank_data["day"].astype(str) + "-" + bank_data["month"] + "-2022",
    format="%d-%b-%Y",
)

campaign_data = campaign_data.astype(campaign_columns)
campaign_data.to_csv(
    "project/campaign.csv",
    index=False,
    date_format="%Y-%m-%d",
)


# Economics data

economics_columns = {
    "client_id": "int64",
    "cons_price_idx": "float64",
    "euribor_three_months": "float64",
}

economics_data = bank_data[list(economics_columns.keys())].copy()

economics_data = economics_data.astype(economics_columns)
economics_data.to_csv("project/economics.csv", index=False)
