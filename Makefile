TOPLEVEL = NES_Mainboard
FILES = **/*.vhd *.vhd
TESTBENCHES = $(wildcard TestBenches/*.vhd)
TESTBENCH_FILES = $(patsubst %,./%,$(TESTBENCHES))
FILES_EXCLUDE = CartridgeROM*.vhd $(TESTBENCHES)

GHDL_CMD = ghdl
GHDL_FLAGS = --std=08 --ieee=synopsys -fsynopsys

YOSYS_CMD = yosys -m ghdl

WORKDIR = work
STOP_TIME = 10us
GHDL_SIM_OPT = --stop-time=$(STOP_TIME) --stop-delta=100000

.PHONY: clean

all: clean compile run

compile: 
	@mkdir -p $(WORKDIR)
	@$(GHDL_CMD) -i $(GHDL_FLAGS) --workdir=$(WORKDIR) --work=work $(TESTBENCH_FILES) $(filter-out $(wildcard $(FILES_EXCLUDE)),$(wildcard $(FILES)))
	@$(GHDL_CMD) -m $(GHDL_FLAGS) --workdir=$(WORKDIR) --work=work $(TOPLEVEL)

clean:
	@rm -rf $(WORKDIR)