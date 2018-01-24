每个线程都有一个jni环境
static函数第二个参数为jclass，成员函数为jobj
java部分，函数标为native
函数命名规则，Java_<full_class_name>_<method>
javah可以为用JNI的class生产header
NewStringUTF创建字符串
创建java中的对象，需要FindClass然后再创建，数组创建如下：
    NewObjectArray，SetObjectArrayElement
JNI自动管理sixteen local references以内的自动释放，超了需要自己释放
JNI函数使用error code和exception提示异常信息，需要native代码处理出现的Exception

jobject NewGlobalRef(JNIEnv *env, jobject obj);
Creates a new global reference to the object referred to by the obj argument. The obj argument may be a global or local reference. Global references must be explicitly disposed of by calling DeleteGlobalRef().
