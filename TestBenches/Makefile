# vhdl files
TESTBENCH = NES_Framebuffer_TB
FILES = $(wildcard ../**/*vhd) $(wildcard ../*.vhd)
FILES_EXCLUDE = ../CartridgeROM_Coregen.vhd #$(wildcard ../CartridgeROM*.vhd)# $(wildcard ../TestBenches/*)
FILES_FINAL = $(filter-out $(wildcard $(FILES_EXCLUDE)),$(wildcard $(FILES)))
VHDLEX = .vhd

VIEW = $(TESTBENCH)

YOSYS = yosys

# testbench
# TESTBENCHFILES = $(wildcard *.vhd)

#roms
ROM = ../roms/smb

#GHDL CONFIG
GHDL_CMD = ghdl
GHDL_FLAGS  = -fsynopsys

SIMDIR = ../work
STOP_TIME = 1000us
GHDL_SIM_OPT = --stop-time=$(STOP_TIME) --stop-delta=100000

WAVEFORM_VIEWER = gtkwave

#$(foreach v, $(.VARIABLES), $(info $(v) = $($(v))))

.PHONY: clean

all: clean rom compile run


compile:
	@mkdir -p $(SIMDIR)
	@$(GHDL_CMD) -i $(GHDL_FLAGS) --workdir=$(SIMDIR) --work=work $(TESTBENCHFILES) $(FILES_FINAL)
	@$(GHDL_CMD) -m $(GHDL_FLAGS) --workdir=$(SIMDIR) --work=work $(TESTBENCH)

synth_vhdl: $(FILES_FINAL)
	$(YOSYS) -mghdl -p 'ghdl --warn-no-binding -C --ieee=synopsys $^ -e $(TESTBENCH); synth_gatemate -top $(TESTBENCH) -nomx8 -vlog net/$(TESTBENCH)_synth.v'

run:
	@$(GHDL_CMD) -r --time-resolution=auto $(GHDL_FLAGS) --workdir=$(SIMDIR) --work=work $(TESTBENCH) --wave=$(patsubst %,$(SIMDIR)/%.ghw, $(TESTBENCH)) $(GHDL_SIM_OPT) --ieee-asserts=disable

view:
	$(WAVEFORM_VIEWER) --dump=$(SIMDIR)/$(VIEW).ghw --save ./$(VIEW).gtkw

clean:
	@rm -rf $(SIMDIR)
	@-rm $(ROM)_chr.dat
	@-rm $(ROM)_prg.dat

rom:
	@python2 ../tools/romconv.py $(ROM).nes