#!/usr/bin/env python3
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str, default="张三")
    args, _ = parser.parse_known_args()
    print(f"你好，{args.name}今天心情怎么样？")
