# vhdl files
TESTBENCHES = $(patsubst %.vhd, % , $(wildcard *.vhd))
FILES = $(wildcard ../**/*vhd) $(wildcard ../*.vhd)
FILES_EXCLUDE = $(wildcard ../CartridgeROM*.vhd) $(wildcard ../TestBenches/*)
FILES_FINAL = $(filter-out $(wildcard $(FILES_EXCLUDE)),$(wildcard $(FILES)))
VHDLEX = .vhd

VIEW =

# testbench
TESTBENCHFILES = $(wildcard *.vhd)


#GHDL CONFIG
GHDL_CMD = ghdl
GHDL_FLAGS  = -fsynopsys

SIMDIR = ../work
STOP_TIME = 100us
GHDL_SIM_OPT = --stop-time=$(STOP_TIME) --stop-delta=100000

WAVEFORM_VIEWER = gtkwave

#$(foreach v, $(.VARIABLES), $(info $(v) = $($(v))))

.PHONY: clean

all: clean compile run


compile:
	@mkdir -p $(SIMDIR)
	@$(GHDL_CMD) -i $(GHDL_FLAGS) --workdir=$(SIMDIR) --work=work $(TESTBENCHFILES) $(FILES_FINAL)
	@$(foreach testbench, $(TESTBENCHES), $(GHDL_CMD) -m $(GHDL_FLAGS) --workdir=$(SIMDIR) --work=work $(testbench);)


run:
	@$(foreach testbench, $(TESTBENCHES), $(GHDL_CMD) -r $(GHDL_FLAGS) --workdir=$(SIMDIR) --work=work $(testbench) --wave=$(patsubst %,$(SIMDIR)/%.ghw, $(testbench))  $(GHDL_SIM_OPT);)

view:
	$(WAVEFORM_VIEWER) --dump=$(SIMDIR)/$(VIEW).ghw --save ./$(VIEW).gtkw

clean:
	@rm -rf $(SIMDIR)