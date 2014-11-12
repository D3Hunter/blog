CC := gcc
CXX := g++
LD := $(CC)
AR := ar

BASEDIR= ./php_daemon

SOURCEFILES := banner.c cache.c cJSON.c command.c config.c connector.c harvest.c listener.c main.c minIni.c oa_app.c oa_buf.c oa_cond.c oa_errno.c forkdaemon.c log.c oa_json.c oa_mutex.c oa_daemon.c oa_obj.c oa_ssl.c oa_str.c oa_util.c param.c proc.c rpm.c sig.c thread.c

all_source_files := $(SOURCEFILES)
source_obj1 := $(all_source_files:.cpp=.o) #这里是makefile里的替换字符串方法
source_obj2 := $(source_obj1:.c=.o)
source_obj3 := $(source_obj2:.s=.o)
source_objs := $(source_obj3:.S=.o)

CFLAGS := -I/usr/include/x86_64-linux-gnu/ -I$(BASEDIR)
CXXFLAGS :=
ASFLAGS :=
LDFLAGS := -lm -Lthird_part/curl-7.37.1/lib -lcurl -Lthird_part/openssl-1.0.0c/lib -lssl -Lthird_part/openssl-1.0.0c/lib -lcrypto  -Lthird_part/zlib1.2.8/lib -lz  -lrt -ldl -lpthread
EXTERNAL_LIBS=

all_make_files := Makefile

# 使用前置@取消命令写到console
# Print help on no message
all:
	@echo
	@echo "Use the following command:"
	@echo "    make debug32"
	@echo "    make debug64"
	@echo "    make release32"
	@echo "    make release64"
	@echo "    make clean   cleanup everything"
	@echo "To make release version for distribution run:"
	@echo "    make release"
	@echo

release:
	make release32
	make release64

COMMON_FLAGS32=-m32
COMMON_FLAGS64=-m64
##################################################
# debug
##################################################
DEBUG_LDFLAGS= -O0

# 32 bit
DEBUG_FLAGS32=$(COMMON_FLAGS32) -ggdb
debug32_obj_dir=${BASEDIR}/debug-32
debug32_objs := $(addprefix $(debug32_obj_dir)/, $(source_objs)) # addprefix为make内置函数，添加前缀
debug32: CFLAGS += $(DEBUG_FLAGS32) # 相同target会被合并
debug32: CXXFLAGS += $(DEBUG_FLAGS32) # 修改变量值：默认情况下，makefile中的变量都是静态的
debug32: LDFLAGS += $(COMMON_FLAGS32) $(DEBUG_LDFLAGS)
debug32: target=daemon-debug32
debug32: $(debug32_obj_dir) ${debug32_objs} $(EXTERNAL_LIBS)
	$(LD) -o ${target} ${debug32_objs} ${LDFLAGS}

# 64 bit
DEBUG_FLAGS64=$(COMMON_FLAGS64) -ggdb
debug64_obj_dir=${BASEDIR}/debug-64
debug64_objs := $(addprefix $(debug64_obj_dir)/, $(source_objs))
debug64: CFLAGS += $(DEBUG_FLAGS64)
debug64: CXXFLAGS += $(DEBUG_FLAGS64)
debug64: LDFLAGS += $(COMMON_FLAGS64) $(DEBUG_LDFLAGS)
debug64: target=daemon-debug64
debug64: $(debug64_obj_dir) ${debug64_objs} $(EXTERNAL_LIBS)
	$(LD) -o ${target} ${debug64_objs} ${LDFLAGS}

##################################################
# release
##################################################
RELEASE_LDFLAGS= -O3

# 32 bit
RELEASE_FLAGS32=$(COMMON_FLAGS32)
release32_obj_dir=${BASEDIR}/release-32
release32_objs := $(addprefix $(release32_obj_dir)/, $(source_objs))
release32: CFLAGS += $(RELEASE_FLAGS32)
release32: CXXFLAGS += $(RELEASE_FLAGS32)
release32: LDFLAGS += $(COMMON_FLAGS32) $(RELEASE_LDFLAGS)
release32: target=daemon-release32
release32: $(release32_obj_dir) ${release32_objs} $(EXTERNAL_LIBS)
	$(LD) -o ${target} ${release32_objs} ${LDFLAGS}

# 64 bit
RELEASE_FLAGS64=$(COMMON_FLAGS64)
release64_obj_dir=${BASEDIR}/release-64
release64_objs := $(addprefix $(release64_obj_dir)/, $(source_objs))
release64: CFLAGS += $(RELEASE_FLAGS64)
release64: CXXFLAGS += $(RELEASE_FLAGS64)
release64: LDFLAGS += $(COMMON_FLAGS64) $(RELEASE_LDFLAGS)
release64: target=daemon-release64
release64: $(release64_obj_dir) ${release64_objs} $(EXTERNAL_LIBS)
	$(LD) -o ${target} ${release64_objs} ${LDFLAGS}

# other
# 多个target可以使用相同的rule $@会指向正确的target
$(debug32_obj_dir) $(debug64_obj_dir) $(release32_obj_dir) $(release64_obj_dir):
	mkdir -p $@ >/dev/null 2>&1

$(debug32_obj_dir)/%.o $(debug64_obj_dir)/%.o $(release32_obj_dir)/%.o $(release64_obj_dir)/%.o : ${BASEDIR}/%.c $(all_make_files)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(debug32_obj_dir) $(debug64_obj_dir) $(release32_obj_dir) $(release64_obj_dir) > /dev/null 2>&1
	rm -f daemon-debug32 daemon-debug64 daemon-release32 daemon-release64 > /dev/null 2>&1
