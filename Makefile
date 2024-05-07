TOPLEVEL = NES_Mainboard
FILES = **/*.vhd *.vhd
FILES_EXCLUDE = HDMI/HDMIController.vhd CartridgeROM*.vhd TestBenches/*

GHDL_CMD = ghdl
GHDL_FLAGS = -g

YOSYS_CMD = yosys -m ghdl

SYNDIR = synthesis
STOP_TIME = 10us
GHDL_SIM_OPT = --stop-time=$(STOP_TIME) --stop-delta=100000

.PHONY: clean

all: clean compile

compile: 
	@mkdir -p $(SYNDIR)
	@$(GHDL_CMD) -i $(GHDL_FLAGS) --workdir=$(SYNDIR) --work=work $(filter-out $(wildcard $(FILES_EXCLUDE)),$(wildcard $(FILES)))
	@$(GHDL_CMD) -m $(GHDL_FLAGS) --workdir=$(SYNDIR) --work=work $(TOPLEVEL)

clean:
	@rm -rf $(SYNDIR)