import os
import subprocess

print("hello world")

path_to_java = os.path.join("C:", os.sep, "Program Files (x86)", "Java", "jre6", "bin", "java.exe")

print(subprocess.call([path_to_java, '-jar', 'query_shire.jar', '20-00']))
