import argparse
import tiktoken

def main():
    parser = argparse.ArgumentParser(description="Encode a text file using tiktoken's o200k_harmony tokenizer.")
    parser.add_argument("file_path", type=str, help="The path to the text file to encode.")
    args = parser.parse_args()

    try:
        with open(args.file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {args.file_path}")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    encoding = tiktoken.get_encoding("o200k_harmony")
    tokens = encoding.encode(text)

    print(f"Encoded tokens for {args.file_path}:")
    print(tokens)
    print(f"\nTotal tokens: {len(tokens)}")


if __name__ == "__main__":
    main()
