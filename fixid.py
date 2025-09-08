#!/usr/bin/env python3
import json
import sys
from pathlib import Path

def fix_ids(json_file):
    """Fix duplicate IDs in a JSON flashcard file by renumbering cards sequentially."""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, dict) or 'cards' not in data or not isinstance(data['cards'], list):
            print("Error: Invalid JSON structure. Expected a dictionary with a 'cards' array.")
            return False
        
        print("Renumbering cards with sequential IDs...")
        for i, card in enumerate(data['cards'], 1):
            card['id'] = i
            print(f"Card {i}: ID set to {card['id']}")
        
        # Write the fixed JSON back to the file
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Successfully renumbered cards in {json_file}")
        return True
        
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        return False
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_file}'.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fixid.py <json_file>")
        sys.exit(1)
    
    json_file = sys.argv[1]
    
    # Check if file exists
    if not Path(json_file).exists():
        print(f"Error: File '{json_file}' does not exist.")
        sys.exit(1)
    
    # Fix the IDs
    success = fix_ids(json_file)
    sys.exit(0 if success else 1)
