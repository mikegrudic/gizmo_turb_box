BOX_PERIODIC # gives periodic boundary conditions
MAGNETIC # enables MHD
MHD_CONSTRAINED_GRADIENT=1 # enables Hopkins 2016 constrained-gradient scheme for beating down divB errors
EOS_GAMMA=1.001 # effectively isothermal EOS
EOS_ENFORCE_ADIABAT=0.04 # sets isothermal EOS P = (0.2 km/s)^2 * density
TURB_DRIVING # enables turbulence driving
NOGRAVITY # disable self-gravity
ADAPTIVE_GRAVSOFT_FORGAS
