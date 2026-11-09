"""Local smoke-test entry point for the gpt-test project."""


def smoke_test_message() -> str:
    """Return a message confirming the local starter is ready."""
    return "GPT test starter is ready."


def main() -> None:
    """Print the local smoke-test message."""
    print(smoke_test_message())


if __name__ == "__main__":
    main()
