��    c      4  �   L      p     q  8   �  D   �  8   	  4   ?	  >   t	  <   �	  I   �	  9   :
  ?   t
  7   �
     �
  /     /   <  1   l     �  3   �  ,   �  !     $   5  $   Z       $   �  .   �  &   �  '         @  	   a  $   k  j   �  _   �     [  &   r  d   �  8   �  3   7  #   k  "   �  #   �     �  $   �  /        I     i  "   �     �     �  (   �  '   	  *   1  )   \  !   �     �  #   �     �            )   8     b  )     &   �  %   �  ,   �     #     +     E     `  4   h  6   �     �  $   �           5     V     q     �     �     �     �     �     �     �          $     3  /   N     ~     �     �     �     �     �          %     =  %   O     u  	   �  �  �     1  =   H  @   �  4   �  4   �  :   1  7   l  C   �  4   �  =     ;   [     �  %   �  %   �  2   �     0  $   A  0   f     �  .   �  /   �  *     )   <  8   f  )   �  2   �  +   �     (     1  _   N  J   �     �  *     L   8  ?   �  9   �  $   �     $  !   B     d     {  %   �     �     �     �           +   "   A      d   %   �   !   �      �      �      !      !     6!     L!  4   h!  "   �!  #   �!  "   �!     "  '   &"     N"     W"     h"  
   �"  /   �"  7   �"     �"  "   #     0#  !   L#     n#     �#     �#     �#     �#     �#     �#     �#     �#     $      $     .$  )   D$     n$     �$     �$     �$     �$     �$     �$     %     !%  $   1%     V%     r%     U   ;   E                            -                (   :              R      *   %               ]   B       Z   Q   I      !   7       '           #   \   c   G                               "       H   W   `   ^   &   C   )             D   1       /   Y   O                           V   ?   L   0   N   T       J          5       @   4          9   X                  $      M   .   [       a   2   S   6   <       	   8       3   +   _   K              
   b   A   F       ,       P            >          =    
Report bugs to <%s>.
   -?, --help                  show this help, then exit
   -V, --version               output version information, then exit
   -e, --exit-on-error         exit immediately on error
   -i, --ignore=RELATIVE_PATH  ignore indicated path
   -m, --manifest-path=PATH    use specified path for manifest
   -n, --no-parse-wal          do not try to parse WAL files
   -q, --quiet                 do not print any output, except for errors
   -s, --skip-checksums        skip checksum verification
   -w, --wal-directory=PATH    use specified path for WAL files
 "%s" has size %lld on disk but size %zu in the manifest "%s" is not a file or directory "%s" is present in the manifest but not on disk "%s" is present on disk but not in the manifest "\u" must be followed by four hexadecimal digits. %s home page: <%s>
 %s verifies a backup against the backup manifest.

 Character with value 0x%02x must be escaped. Escape sequence "\%s" is invalid. Expected "," or "]", but found "%s". Expected "," or "}", but found "%s". Expected ":", but found "%s". Expected JSON value, but found "%s". Expected array element or "]", but found "%s". Expected end of input, but found "%s". Expected string or "}", but found "%s". Expected string, but found "%s". Options:
 The input string ended unexpectedly. The program "%s" is needed by %s but was not found in the
same directory as "%s".
Check your installation. The program "%s" was found by "%s"
but was not the same version as %s.
Check your installation. Token "%s" is invalid. Try "%s --help" for more information.
 Unicode escape values cannot be used for code point values above 007F when the encoding is not UTF8. Unicode high surrogate must not follow a high surrogate. Unicode low surrogate must follow a high surrogate. Usage:
  %s [OPTION]... BACKUPDIR

 WAL parsing failed for timeline %u \u0000 cannot be converted to text. backup successfully verified
 both path name and encoded path name cannot duplicate null pointer (internal error)
 checksum mismatch for file "%s" checksum without algorithm could not close directory "%s": %m could not close file "%s": %m could not decode file name could not finalize checksum of file "%s" could not finalize checksum of manifest could not initialize checksum of file "%s" could not initialize checksum of manifest could not open directory "%s": %m could not open file "%s": %m could not parse backup manifest: %s could not parse end LSN could not parse start LSN could not read file "%s": %m could not read file "%s": read %d of %lld could not stat file "%s": %m could not stat file or directory "%s": %m could not update checksum of file "%s" could not update checksum of manifest duplicate path name in backup manifest: "%s" error:  expected at least 2 lines expected version indicator fatal:  file "%s" has checksum of length %d, but expected %d file "%s" should contain %zu bytes, but read %zu bytes file size is not an integer invalid checksum for file "%s": "%s" invalid manifest checksum: "%s" last line not newline-terminated manifest checksum mismatch manifest ended unexpectedly manifest has no checksum missing end LSN missing path name missing size missing start LSN missing timeline no backup directory specified out of memory out of memory
 timeline is not an integer too many command-line arguments (first is "%s") unexpected WAL range field unexpected array end unexpected array start unexpected file field unexpected manifest version unexpected object end unexpected object field unexpected object start unexpected scalar unrecognized checksum algorithm: "%s" unrecognized top-level field warning:  Project-Id-Version: pg_verifybackup (PostgreSQL) 14
Report-Msgid-Bugs-To: pgsql-bugs@lists.postgresql.org
POT-Creation-Date: 2021-08-14 05:45+0000
PO-Revision-Date: 2021-08-15 16:00+0800
Last-Translator: Jie Zhang <zhangjie2@fujitsu.com>
Language-Team: Chinese (Simplified) <zhangjie2@fujitsu.com>
Language: zh_CN
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
 
臭虫报告至<%s>.
   -?, --help                  显示此帮助，然后退出
   -V, --version               输出版本信息，然后退出
   -e, --exit-on-error         出错时立即退出
   -i, --ignore=RELATIVE_PATH  忽略指定的路径
   -m, --manifest-path=PATH    使用清单的指定路径
   -n, --no-parse-wal          不试图解析WAL文件
   -q, --quiet                 不打印任何输出，错误除外
   -s, --skip-checksums        跳过校验和验证
   -w, --wal-directory=PATH    对WAL文件使用指定路径
 "%s"在磁盘上有大小%lld，但在清单中有大小%zu "%s"不是文件或目录 清单中有"%s"，但磁盘上没有 磁盘上有"%s"，但清单中没有 "\u" 后必须紧跟有效的十六进制数数字 %s 主页: <%s>
 %s 根据备份清单验证备份.

 值为 0x%02x 的字符必须进行转义处理. 转义序列 "\%s" 无效. 期望是"," 或 "]"，但发现结果是"%s". 期望是 "," 或 "}"，但发现结果是"%s". 期望得到 ":"，但发现结果是"%s". 期望是JSON值, 但结果发现是"%s". 期望为数组元素或者"]"，但发现结果是"%s". 期望输入结束，结果发现是"%s". 期望是字符串或"}"，但发现结果是"%s". 期望是字符串, 但发现结果是"%s". 选项:
 输入字符串意外终止. %2$s需要程序"%1$s"
但在与"%3$s"相同的目录中找不到该程序.
检查您的安装. 程序"%s"是由"%s"找到的
但与%s的版本不同.
检查您的安装. 令牌 "%s" 无效. 请用 "%s --help" 获取更多的信息.
 当编码不是UTF8时，大于007F的码位值不能使用Unicode转义值. Unicode 的高位代理项不能紧随另一个高位代理项. Unicode 代位代理项必须紧随一个高位代理项. 用法:
  %s [选项]... BACKUPDIR

 时间线%u的WAL解析失败 \u0000不能被转换为文本。 备份已成功验证
 路径名和编码路径名 无法复制空指针 (内部错误)
 文件"%s"的校验和不匹配 校验和没有算法 无法关闭目录 "%s": %m 无法关闭文件 "%s": %m 无法解码文件名 无法完成文件"%s"的校验和 无法完成清单的校验和 无法初始化文件"%s"的校验和 无法初始化清单的校验和 无法打开目录 "%s": %m 无法打开文件 "%s": %m 清单校验和不匹配: %s 无法解析结束LSN 无法解析起始LSN 无法读取文件 "%s": %m 无法读取文件"%1$s"：读取了%3$lld中的%2$d 无法取文件 "%s" 的状态: %m 无法统计文件或目录"%s": %m 无法更新文件"%s"的校验和 无法更新清单的校验和 备份清单中的路径名重复: "%s" 错误:  至少需要2行 预期的版本指示器 致命的: 文件"%s"的校验和长度为%d，但应为%d 文件"%s"应包含%zu到字节，但读取到%zu字节 文件大小不是整数 文件"%s"的校验和无效: "%s" 清单校验和无效: "%s" 最后一行未以换行符结尾 清单校验和不匹配 清单意外结束 清单没有校验和 缺少结束LSN 缺少路径名 缺少大小 缺少起始LSN 缺少时间线 未指定备份目录 内存不足 内存不足
 时间线不是整数 命令行参数太多 (第一个是 "%s") 意外的WAL范围字段 意外的数组结束 意外的数组开始 意外的文件字段 意外的清单版本 意外的对象结束 意外的对象字段 意外的对象开始 意外的标量 无法识别的校验和算法: "%s" 无法识别的顶层字段 警告:  