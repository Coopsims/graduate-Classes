# run.py
from real_estate.load_data.load import RealEstate
from real_estate.helper_functions import calculate_stats


def main():
    file_name = "realtor-data.csv"
    location = "real_estate/load_data/data"
    re_data = RealEstate(file_name, location)

    for group, states in re_data.properties_dict.items():
        for state, properties in states.items():
            print(f"'{state}': {properties[:5]}")

    print("\n \n \n Cheapest in Massachusetts:", re_data.compute_stats("cheapest", "Massachusetts"))
    print("Priciest in Massachusetts:", re_data.compute_stats("priciest", "Massachusetts"))
    print("Absolute cheapest:", re_data.compute_stats("dirt_cheap"))
    print("Best deal in Connecticut for 3 bed and 2 bath:",
          re_data.compute_stats("best_deal", "Connecticut", 3, 2.0))
    print("Budget friendly for 3 bed, 2 bath, under 300000:",
          re_data.compute_stats("budget_friendly", 3, 2.0, 300000))


if __name__ == "__main__":
    main()
