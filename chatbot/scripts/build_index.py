#!/usr/bin/env python3
"""CLI script to build the ChromaDB index from Blueprint documentation."""

import argparse
import sys
from pathlib import Path

# Add src to path so we can import the package
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from blueprint_chat.indexer import build_index


def main():
    parser = argparse.ArgumentParser(description="Build Blueprint RAG index")
    parser.add_argument(
        "--docs-root",
        type=str,
        default=str(Path(__file__).parent.parent.parent / "docs"),
        help="Path to the docs/ directory",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=str(Path(__file__).parent.parent / "chroma_data"),
        help="Path for ChromaDB storage",
    )
    parser.add_argument(
        "--languages",
        nargs="+",
        default=["nl", "en"],
        help="Languages to index",
    )
    args = parser.parse_args()

    print(f"Building index from: {args.docs_root}")
    print(f"Output directory: {args.output_dir}")
    print(f"Languages: {args.languages}")
    print()

    stats = build_index(
        docs_root=args.docs_root,
        chroma_path=args.output_dir,
        languages=args.languages,
    )

    for lang, count in stats.items():
        print(f"  [{lang.upper()}] {count} chunks indexed")

    total = sum(stats.values())
    print(f"\nTotal: {total} chunks across {len(stats)} languages")


if __name__ == "__main__":
    main()
