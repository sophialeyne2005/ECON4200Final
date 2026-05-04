import pandas as pd
pd.__version__

def export_daily_close_onecol(csv_path, out_txt_path, ticker):
    return daily_close

import pandas as pd

def export_daily_close_onecol(csv_path, out_txt_path, ticker):
    usecols_try = ["timestamp", "close", "ticker"]

    try:
        it = pd.read_csv(csv_path, usecols=usecols_try, chunksize=2_000_000, dtype={"ticker": "string"})
        timestamp_col = "timestamp"
    except ValueError:
        usecols_try = ["Unnamed: 0", "close", "ticker"]
        it = pd.read_csv(csv_path, usecols=usecols_try, chunksize=2_000_000, dtype={"ticker": "string"})
        timestamp_col = "Unnamed: 0"

    daily_parts = []

    for chunk in it:
        ts_utc = pd.to_datetime(chunk[timestamp_col], utc=True, errors="coerce")
        ts = ts_utc.dt.tz_convert("America/New_York")

        mask = (chunk["ticker"] == ticker)

        if mask.any():
            daily_parts.append(pd.DataFrame({
                "ts": ts[mask].values,
                "close": chunk.loc[mask, "close"].values
            }))

    if not daily_parts:
        open(out_txt_path, "w").close()
        return pd.Series(dtype="float64")

    df = pd.concat(daily_parts, ignore_index=True).sort_values("ts")
    daily_close = df.groupby(df["ts"].dt.date)["close"].last()

    daily_close.to_csv(out_txt_path, index=False, header=False, float_format="%.6f")
    return daily_close

export_daily_close_onecol

csv_path = "SP500.min.2023Jan.bars.csv"
ticker = "AAPL"
out_path = f"{ticker}_close.txt"

daily = export_daily_close_onecol(csv_path, out_path, ticker)

print("Extracted", len(daily), "daily closing prices.")
daily.head()

import os
os.listdir()

import pandas as pd

daily = pd.read_csv("AAPL_close.txt", header=None)
daily.head()