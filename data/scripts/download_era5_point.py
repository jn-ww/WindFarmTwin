#!/usr/bin/env python3
"""
Download ERA5 hourly 100-m winds for a single lat/lon and year.
"""
import argparse, pathlib, cdsapi

def fetch(lat, lon, year, out_dir):
    c = cdsapi.Client()
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"era5_{lat:.2f}_{lon:.2f}_{year}.nc"
    area = f"{lat+0.25}/{lon-0.25}/{lat-0.25}/{lon+0.25}"  # N/W/S/E
    c.retrieve(
        "reanalysis-era5-single-levels",
        {
            "product_type": "reanalysis",
            "variable": [
                "100m_u_component_of_wind",
                "100m_v_component_of_wind",
            ],
            "year": str(year),
            "month": [f"{m:02d}" for m in range(1, 13)],
            "day": [f"{d:02d}" for d in range(1, 32)],
            "time": [f"{h:02d}:00" for h in range(24)],
            "area": area,    # small 0.5° box around the site
            "format": "netcdf",
        },
        str(target),
    )

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--lat", type=float, required=True)
    p.add_argument("--lon", type=float, required=True)
    p.add_argument("--year", type=int, required=True)
    p.add_argument("--out", default="data/raw")
    args = p.parse_args()
    fetch(args.lat, args.lon, args.year, args.out)

