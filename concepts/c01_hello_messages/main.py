"""c01: first Messages API call via common.llm."""

from common.llm import chat


def main() -> None:
    response = chat(
        messages=[
            {"role": "user", "content": "用一句话解释什么是 agent loop. "},
        ],
    )
    print("content:", response.content)
    print("stop_reason:", response.stop_reason)
    print("usage:", response.usage)


if __name__ == "__main__":
    main()
