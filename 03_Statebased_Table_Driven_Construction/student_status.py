from enum import Enum
#state
class studentsstatusstate(Enum):
    Terdaftar  = "Terdaftar"
    Cuti = "Cuti"
    Aktif = "Aktif"
    Lulus = "Lulus"
#trigger input
class triggerinputstate(Enum):
    cetak_ksm = "cetak_ksm"
    menyelesaikan_cuti = "menyelesaikan_cuti"
    lulus = "lulus"
    mengajukan_cuti = "mengajukan_cuti"

#transition
state_transitions = {
    studentsstatusstate.Terdaftar: {
        triggerinputstate.mengajukan_cuti: studentsstatusstate.Cuti,
        triggerinputstate.cetak_ksm: studentsstatusstate.Aktif
    },
    studentsstatusstate.Cuti: {
        triggerinputstate.menyelesaikan_cuti: studentsstatusstate.Terdaftar
    },
    studentsstatusstate.Aktif: {
        triggerinputstate.lulus: studentsstatusstate.Lulus,
        triggerinputstate.mengajukan_cuti: studentsstatusstate.Cuti
    }
}
def change_state(current_state, trigger_input):
    cond_1 = current_state in state_transitions
    cond_2 = trigger_input in state_transitions[current_state]
    if cond_1 and cond_2:
        return state_transitions[current_state][trigger_input]
    return "transition tidak valid"

current_state = studentsstatusstate.Terdaftar
triggerinput = triggerinputstate.mengajukan_cuti
next_state = change_state(current_state, triggerinput)
print(next_state) #studentsstatusstate.Cuti
