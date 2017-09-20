CC := gcc
CXX := g++
LD := $(CC)
AR := ar

BASEDIR= ./build
PROGNAME=program-xxx
SOURCEFILES := a.c b.c c.c

all_source_files := $(SOURCEFILES)
source_obj1 := $(all_source_files:.cpp=.o)
source_obj2 := $(source_obj1:.c=.o)
source_obj3 := $(source_obj2:.s=.o)
SOURCE_OBJS := $(source_obj3:.S=.o)

DEBUG ?= 1
ifeq ($(DEBUG), 1)
	BUILD_TYPE=debug
	PROG_FLAGS=-g -ggdb -rdynamic -Werror
	PROG_LDFLAGS= -O0
	ALL_MAKE_FILES := Makefile
else
	BUILD_TYPE=release
	PROG_FLAGS=-Werror
	PROG_LDFLAGS= -O3
	ALL_MAKE_FILES := Makefile
endif

CFLAGS := $(PROG_FLAGS)
CXXFLAGS := $(PROG_FLAGS)
# -static-libgcc -static-libstdc++ -static
LDFLAGS := $(PROG_LDFLAGS) -lm -lrt -ldl -lpthread

##############################
# x86
##############################
INCLUDE_DIR_X86=-Ithird_part/x86/curl-7.37.1/include -Ithird_part/x86/openssl-1.0.0c/include -Ithird_part/x86/zlib1.2.8/include -I/usr/include/x86_64-linux-gnu/ -I$(BASEDIR)
COMMON_FLAGS_X86=-m32

PROG_FLAGS_X86=$(COMMON_FLAGS_X86) $(INCLUDE_DIR_X86)
LDFLAGS_X86= $(COMMON_FLAGS_X86) -Lthird_part/x86/curl-7.37.1/lib -lcurl -Lthird_part/x86/openssl-1.0.0c/lib -lssl -lcrypto  -Lthird_part/x86/zlib1.2.8/lib -lz -ldl -lrt

PROG_X86_OBJ_DIR=${BASEDIR}/$(BUILD_TYPE)-x86
PROG_X86_OBJS := $(addprefix $(PROG_X86_OBJ_DIR)/, $(SOURCE_OBJS))

##############################
# x64
##############################
INCLUDE_DIR_X64=-Ithird_part/x64/curl-7.37.1/include -Ithird_part/x64/openssl-1.0.0c/include -Ithird_part/x64/zlib1.2.8/include -I/usr/include/x64_64-linux-gnu/ -I$(BASEDIR)
COMMON_FLAGS_X64=-m64

PROG_FLAGS_X64=$(COMMON_FLAGS_X64) $(INCLUDE_DIR_X64)
LDFLAGS_X64= $(COMMON_FLAGS_X64) -Lthird_part/x64/curl-7.37.1/lib -lcurl -Lthird_part/x64/openssl-1.0.0c/lib -lssl -lcrypto  -Lthird_part/x64/zlib1.2.8/lib -lz -ldl -lrt

PROG_X64_OBJ_DIR=${BASEDIR}/$(BUILD_TYPE)-x64
PROG_X64_OBJS := $(addprefix $(PROG_X64_OBJ_DIR)/, $(SOURCE_OBJS))

# Print help on no message
all:
	@echo "Default DEBUG version is build"
	@echo "To build release version add 'DEBUG=0' to the end of the following command"
	@echo "Use the following command:"
	@echo "    make $(PROGNAME)32"
	@echo "    make $(PROGNAME)64"
	@echo "    make clean   cleanup everything"
	@echo
	@echo "To make release version for distribution run:"
	@echo "    make $(PROGNAME) DEBUG=0"
	@echo

$(PROGNAME):$(PROGNAME)32 $(PROGNAME)64

$(PROGNAME)32:prog-x86
$(PROGNAME)64:prog-x64

prog-x86: CFLAGS += $(PROG_FLAGS_X86)
prog-x86: CXXFLAGS += $(PROG_FLAGS_X86)
prog-x86: LDFLAGS += $(LDFLAGS_X86)
prog-x86: target=$(PROGNAME)-$(BUILD_TYPE)-x86
prog-x86: $(PROG_X86_OBJ_DIR) ${PROG_X86_OBJS}
	$(LD) -o ${target} ${PROG_X86_OBJS} ${LDFLAGS}

prog-x64: CFLAGS += $(PROG_FLAGS_X64)
prog-x64: CXXFLAGS += $(PROG_FLAGS_X64)
prog-x64: LDFLAGS += $(LDFLAGS_X64)
prog-x64: target=$(PROGNAME)-$(BUILD_TYPE)-x64
prog-x64: $(PROG_X64_OBJ_DIR) ${PROG_X64_OBJS}
	$(LD) -o ${target} ${PROG_X64_OBJS} ${LDFLAGS}


# other
$(PROG_X86_OBJ_DIR) $(PROG_X64_OBJ_DIR) :
	mkdir -p $@ >/dev/null 2>&1

$(PROG_X86_OBJ_DIR)/%.o $(PROG_X64_OBJ_DIR)/%.o : ${BASEDIR}/%.c $(ALL_MAKE_FILES)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(BASEDIR)/release-x86 $(BASEDIR)/debug-x86 $(BASEDIR)/release-x64 $(BASEDIR)/debug-x64 > /dev/null 2>&1
	rm -f $(PROGNAME)-debug-x86 $(PROGNAME)-debug-x64 $(PROGNAME)-release-x86 $(PROGNAME)-release-x64 > /dev/null 2>&1
