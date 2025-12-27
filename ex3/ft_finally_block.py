def water_plants(plant_list):
    success = False
    try:
        print("Opening watering system")
        i = 0
        while i < len(plant_list):
            print(f"Watering {plant_list[i]}")
            i += 1
        success = True
    except Exception:
        print("Error: Cannot water None - invalid plant!")
        success = False
    finally:
        print("Closing watering system (cleanup)")
        if success:
            print("Watering completed successfully!")


def test_watering_system():
    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])

    print("\nTesting with error...")
    water_plants(["tomato", None])


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
