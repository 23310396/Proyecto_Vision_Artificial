from pathlib import Path
from collections import Counter


NAMES = [
    "audi", "chevrolet", "citroen", "dacia", "ford", "hyundai", "mercedes",
    "nissan", "peugeot", "renault", "seat", "skoda", "suzuki", "toyota", "volkswagen"
]


def main():
    total = Counter()
    for split in ["train", "valid", "test"]:
        labels_dir = Path(split) / "labels"
        split_count = Counter()
        for label_file in labels_dir.glob("*.txt"):
            for line in label_file.read_text(encoding="utf-8").splitlines():
                parts = line.split()
                if parts:
                    split_count[int(parts[0])] += 1
        total.update(split_count)
        print(f"\n{split.upper()}")
        for class_id, count in sorted(split_count.items()):
            print(f"{class_id:02d} - {NAMES[class_id]}: {count}")

    print("\nTOTAL")
    for class_id, count in sorted(total.items()):
        print(f"{class_id:02d} - {NAMES[class_id]}: {count}")


if __name__ == "__main__":
    main()
