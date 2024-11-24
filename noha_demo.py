# noha_demo.py
import argparse
from transformers import pipeline

# Initialize the NLP engine (example: using a text-generation model)
def initialize_noha_engine():
    print("Initializing Noha engine...")
    return pipeline("text-generation", model="gpt2")

# Handle a basic command to generate code
def run_command(engine, command):
    print(f"Processing command: {command}")
    response = engine(command, max_length=50, num_return_sequences=1)
    print("Generated Code:")
    print(response[0]['generated_text'])

# Run pre-defined tests
def run_tests(engine):
    print("Running Noha demo tests...")
    test_commands = [
        "Create a Python function to add two numbers",
        "Generate a for loop to print numbers 1 to 10",
        "Write HTML for a simple webpage"
    ]
    for cmd in test_commands:
        print(f"Test Command: {cmd}")
        run_command(engine, cmd)

# Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Noha Demo Script")
    parser.add_argument("--run", type=str, help="Run a Noha command")
    parser.add_argument("--test", action="store_true", help="Run pre-defined Noha tests")

    args = parser.parse_args()
    noha_engine = initialize_noha_engine()

    if args.run:
        run_command(noha_engine, args.run)
    elif args.test:
        run_tests(noha_engine)
    else:
        print("Noha Demo: Use --run or --test to see Noha in action.")
