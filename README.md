# Galactic Cargo Management System (GCMS)

## Overview
This project implements a Galactic Cargo Management System (GCMS) that efficiently packs cargo into space bins using different algorithms based on cargo color. Developed as part of the COL106 Data Structures and Algorithms course at IIT Delhi under Professor Parag Singla, this system demonstrates advanced AVL tree implementations to meet strict time and space complexity requirements.

## Problem Statement
Interstellar shipping companies face the challenge of efficiently packing differently sized cargo items into bins with specific capacities. The GCMS system categorizes cargo by color, each requiring a specialized packing algorithm:
- **Blue Cargo**: Compact Fit (smallest sufficient capacity, least ID)
- **Yellow Cargo**: Compact Fit (smallest sufficient capacity, greatest ID)
- **Red Cargo**: Largest Fit (largest remaining capacity, least ID)
- **Green Cargo**: Largest Fit (largest remaining capacity, greatest ID)

## Technical Specifications
- **Time Complexity**: 
  - O(log n + log m) for add_bin, add_object, delete_object, object_info
  - O(log n + S) for bin_info (S = objects in bin)
- **Space Complexity**: O(n + m)
- **Constraints**: No use of Python dictionaries/sets, pure AVL tree implementation

## Implementation Details

### Core Components
1. **AVL Trees** (`avl.py`):
   - Custom comparison functions for different sorting criteria
   - Specialized search methods for each cargo color
   - Balanced insertion/deletion operations

2. **Bin Management** (`bin.py`):
   - Stores bin ID and capacity
   - Maintains objects in an AVL tree sorted by object ID
   - Handles object addition/removal

3. **Object Management** (`object.py`):
   - Object properties: ID, size, color, bin assignment
   - Color enum (BLUE, YELLOW, RED, GREEN)

4. **GCMS Controller** (`gcms.py`):
   - Maintains 5 AVL trees:
     - 4 trees for different cargo algorithms (blue, yellow, red, green)
     - 1 tree for bin ID lookups
   - Implements all required operations:
     - `add_bin()`, `add_object()`
     - `delete_object()`, `object_info()`
     - `bin_info()`

### Key Algorithms
- **Compact Fit Algorithm**: Selects bin with smallest sufficient capacity
- **Largest Fit Algorithm**: Selects bin with largest remaining capacity
- **Tie-breaking**: Uses bin ID (least/greatest) per color specification

## How to Run
1. Execute `main.py` for sample operations:
```bash
python main.py
```

2. Sample output:
```python
(0, [3283, 8983])  # Bin 1234: 0 capacity, objects 3283 & 8983
(5, [8989, 4839])   # Bin 4321: 5 capacity, objects 8989 & 4839
(7, [2892])         # Bin 1111: 7 capacity, object 2892
```

## File Structure
```
├── avl.py           # AVL tree implementation
├── bin.py           # Bin class and operations
├── exceptions.py    # Custom exceptions (NoBinFoundException)
├── gcms.py          # Main GCMS system logic
├── main.py          # Test/demo script
├── node.py          # AVL tree node definition
└── object.py        # Object class and color enum
```

## Developer
**Amber Agarwal**  
IIT Delhi - COL106 Data Structures and Algorithms  
