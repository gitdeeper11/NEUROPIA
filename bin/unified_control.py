#!/usr/bin/env python3
"""NEUROPIA - Unified Control Executable"""

import argparse

def main():
parser = argparse.ArgumentParser(description='NEUROPIA Unified Control')
parser.add_argument('--regime', default='full_fusion_plant')
parser.add_argument('--steps', type=int, default=1000)
parser.add_argument('--verbose', action='store_true')
args = parser.parse_args()

if name == "main":
exit(main())
