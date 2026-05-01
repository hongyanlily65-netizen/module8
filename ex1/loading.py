import sys
from importlib import metadata


DEPENDENCIES = [
    ("pandas", "Data manipulation"),
    ("numpy", "Numerical computation"),
    ("requests", "Network access"),
    ("matplotlib", "Visualization"),
]


def check_dependencies() -> bool:
    missing = []

    for package, _feature in DEPENDENCIES:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)

    if missing:
        print("Missing dependencies:")
        for package in missing:
            print(f"- {package}")

        print("\nInstall with pip:")
        print("  pip install -r requirements.txt")

        print("\nOr install with Poetry:")
        print("  poetry install")

        return False

    return True


def show_package_versions() -> None:
    print("=== Installed package versions ===")

    for package, feature in DEPENDENCIES:
        try:
            version = metadata.version(package)
            print(f"[OK] {package} ({version}) - {feature} ready")
        except metadata.PackageNotFoundError:
            print(f"[MISSING] {package} - {feature} not found")


def compare_pip_poetry() -> None:
    print("\n=== pip vs Poetry ===")
    print("pip:")
    print("- Uses requirements.txt")
    print("- Installs packages directly into the current environment")
    print("- Simple and common")

    print("\nPoetry:")
    print("- Uses pyproject.toml")
    print("- Manages dependencies and virtual environments")
    print("- Creates a lock file for reproducible installs")


def analyze_matrix_data() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    np.random.seed(42)

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    labubu_sales = np.random.randint(20, 120, size=(12, 4))

    df = pd.DataFrame(
        labubu_sales,
        index=months,
        columns=[
            "Labubu Macaron",
            "Labubu Have a Seat",
            "Labubu Big Into Energy",
            "Labubu Fall in Wild",
        ],
    )

    print("\n=== Labubu monthly sales sample ===")
    print(df.head())

    plt.figure()
    for product in df.columns:
        plt.plot(df.index, df[product], marker="o", label=product)
    plt.title("Labubu Monthly Product Sales")
    plt.xlabel("Month")
    plt.ylabel("Units sold")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")

    print("\nVisualization saved as matrix_analysis.png")


def main() -> None:
    print("Welcome to the Real World of Data Engineering\n")

    if not check_dependencies():
        sys.exit(1)

    show_package_versions()
    compare_pip_poetry()
    analyze_matrix_data()


if __name__ == "__main__":
    main()
