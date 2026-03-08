# Basic Algorand Smart Contract Placeholder for Carbon Credit Minting
from pyteal import *

def approval_program():
    return Approve()

def clear_state_program():
    return Approve()

if __name__ == "__main__":
    print(compileTeal(approval_program(), Mode.Application, version=8))
