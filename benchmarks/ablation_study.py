#!/usr/bin/env python3
"""NEUROPIA - Ablation Study"""

def main():
    print("=" * 60)
    print("NEUROPIA - Ablation Study")
    print("=" * 60)
    
    configs = [
        ("Uncontrolled baseline", 0.0),
        ("Classical LQG (per domain)", 58.3),
        ("9 Specialists (no coupling)", 89.3),
        ("O-SFO only (no GCN/UFR)", 91.2),
        ("O-SFO + GCN (no UFR)", 94.1),
        ("FULL NEUROPIA v1.0.0", 96.8),
    ]
    
    print("\n{:<35} {:>12} {:>12}".format("Configuration", "eta (%)", "vs Full"))
    print("-" * 60)
    
    for name, eta in configs:
        diff = eta - 96.8
        print("{:<35} {:>11.1f} {:>+11.1f} pp".format(name, eta, diff))
    
    print("=" * 60)
    return 0

if __name__ == "__main__":
    exit(main())
