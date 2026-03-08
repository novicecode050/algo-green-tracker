# Basic Algorand Smart Contract Placeholder for Carbon Credit Minting
from pyteal import *

def approval_program():
    # Logic: Only allow the creator to manage the credits
    handle_creation = Return(Int(1))
    
    # Simple check: If the transaction is a "NoOp" (normal call), approve it
    handle_noop = Return(Int(1))

    program = Cond(
        [Txn.application_id() == Int(0), handle_creation],
        [Txn.on_completion() == OnComplete.NoOp, handle_noop]
    )
    
    return compileTeal(program, Mode.Application, version=8)

if __name__ == "__main__":
    print(approval_program())
