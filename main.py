import argparse

from src.text_stats import analyze_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Анализ текста: слова, предложения, средняя длина слова."
    )
    parser.add_argument(
        "--text",
        required=True,
        help="Текст для анализа",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    result = analyze_text(args.text)

    print("Результаты анализа:")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
