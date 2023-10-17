import pandas as pd

KEY_OBS_VALUE = "OBS_VALUE"

def parse_data_query(dq: str) -> list:
    if dq is None:
        return []
    dq = dq.strip()
    ret = dq.split(".")
    for i in range(len(ret)):
        ret[i] = ret[i].split("+")
        ret[i] = [c for c in ret[i] if c!=""]

    return ret

def _parse_data_sdmx_json(jdata: dict, labels="both") -> pd.DataFrame:
    series = jdata["data"]["dataSets"][0]["series"]
    struct = jdata["data"]["structure"]

    data = []

    # Loop the series
    for ser_k, ser_v in series.items():

        series_vals = {}
        # Split the keys (1:14:0:1)
        # assign to the series_vals obj[dim_id] the value taken from the structure
        for idx, k in enumerate(ser_k.split(":")):
            if labels == "both":
                dim_val = (
                    struct["dimensions"]["series"][idx]["values"][int(k)]["id"]
                    + ":"
                    + struct["dimensions"]["series"][idx]["values"][int(k)]["name"]
                )
            elif labels == "name":
                dim_val = struct["dimensions"]["series"][idx]["values"][int(k)][
                    "name"
                ]
            elif labels == "id":
                dim_val = struct["dimensions"]["series"][idx]["values"][int(k)][
                    "id"
                ]

            series_vals[struct["dimensions"]["series"][idx]["id"]] = dim_val
        # loop through the observation nodes getting the key (e.g. 1,2...) and the val, the val is another set of keys
        for ser_obs_k, ser_obs_v in ser_v["observations"].items():
            # data_row = series_vals.copy()
            data_row = {}
            for idx, k in enumerate(ser_obs_k.split(":")):
                data_row[struct["dimensions"]["observation"][idx]["id"]] = struct[
                    "dimensions"
                ]["observation"][idx]["values"][int(k)]["name"]

            data_row[KEY_OBS_VALUE] = ser_obs_v[0]

            for idx, attr in enumerate(ser_obs_v[1:]):
                if attr is None:
                    data_row[struct["attributes"]["observation"][idx]["id"]] = None
                else:
                    if labels == "both":
                        data_row[struct["attributes"]["observation"][idx]["id"]] = (
                            struct["attributes"]["observation"][idx]["values"][
                                attr
                            ]["id"]
                            + ":"
                            + struct["attributes"]["observation"][idx]["values"][
                                attr
                            ]["name"]
                        )
                    elif labels == "name":

                        data_row[
                            struct["attributes"]["observation"][idx]["id"]
                        ] = struct["attributes"]["observation"][idx]["values"][
                            attr
                        ][
                            "name"
                        ]
                    elif labels == "id":
                        data_row[
                            struct["attributes"]["observation"][idx]["id"]
                        ] = struct["attributes"]["observation"][idx]["values"][
                            attr
                        ][
                            "id"
                        ]

            # data.append(data_row)
            data.append({**series_vals, **data_row})

    df = pd.DataFrame(data)
    return df

