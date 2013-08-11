# Include this to enable self-documentation in Makefiles.
# Source: http://www.cmcrossroads.com/article/self-documenting-makefiles
#
help:
	@echo $(if $(need-help),,Type \'$(MAKE)$(dash-f) help\' to get help)

need-help := $(filter help,$(MAKECMDGOALS))

define print-help
$(if $(need-help),$(info make $1 -- $2))
endef

define last-element
$(word $(words $1),$1)
endef

this-makefile := $(call last-element,$(MAKEFILE_LIST))
other-makefiles := $(filter-out $(this-makefile),$(MAKEFILE_LIST))
parent-makefile := $(call last-element,$(other-makefiles))

dash-f := $(if $(filter-out Makefile makefile GNUmakefile,\
$(parent-makefile)), -f $(parent-makefile))
