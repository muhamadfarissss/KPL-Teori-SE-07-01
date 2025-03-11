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