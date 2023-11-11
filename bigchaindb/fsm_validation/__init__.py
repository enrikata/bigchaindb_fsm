from transitions import Machine
from bigchaindb.fsm_validation.thermostat_fsm import FSM

fsm = FSM()

thermostat = Machine(model=fsm, states=list(fsm.states.keys()), initial=fsm.initial_state, transitions=fsm.transitions)
