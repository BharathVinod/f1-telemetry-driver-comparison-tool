from src.data_loader import F1SessionConfig


def main():
    try:
        config = F1SessionConfig(
            2024,
            "Sao Paulo",
            "Q"
        )

        config.display_info()

        print("\nLoading F1 session...")

        session = config.load_session()
        driver_a = "VER"
        driver_b = "LEC"

        lap_a = session.laps.pick_drivers(driver_a).pick_fastest()
        lap_b = session.laps.pick_drivers(driver_b).pick_fastest()

        print(f"\nFastest lap comparison:")

        print(f"{driver_a}: {lap_a['LapTime']}")
        print(f"{driver_b}: {lap_b['LapTime']}")

        time_difference = lap_a["LapTime"] - lap_b["LapTime"]

        print(f"\nTime difference: {time_difference}")

        print("\nSector comparison:")

        sectors = [
            "Sector1Time",
            "Sector2Time",
            "Sector3Time"
        ]
        # Compare sector times for both drivers
        for sector in sectors:
            time_a = lap_a[sector].total_seconds()
            time_b = lap_b[sector].total_seconds()

            difference = time_a - time_b

            if difference < 0:
                faster_driver = driver_a
            elif difference > 0:
                faster_driver = driver_b
            else:
                faster_driver = "Both drivers"

            print(f"\n{sector}")
            print(f"{driver_a}: {time_a:.3f} seconds")
            print(f"{driver_b}: {time_b:.3f} seconds")
            print(f"Difference: {abs(difference):.3f} seconds")
            print(f"Faster driver: {faster_driver}")

        print("\nLap conditions:")

        for driver, lap in [(driver_a, lap_a), (driver_b, lap_b)]:
            print(f"\n{driver}")
            print(f"Compound: {lap['Compound']}")
            print(f"Tyre Life: {lap['TyreLife']}")
            print(f"Fresh Tyre: {lap['FreshTyre']}")
            print(f"Lap Number: {lap['LapNumber']}")
            print(f"Is Accurate: {lap['IsAccurate']}")

        print("Session loaded successfully!")

        print("\nSession information:")
        print(session.event)

        print("\nNumber of laps:")
        print(len(session.laps))

        print("\nAvailable lap data columns:")
        print(session.laps.columns.tolist())

        print("\nDrivers in this session:")

        print(session.results[["Abbreviation", "FullName"]])

    except ValueError as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()