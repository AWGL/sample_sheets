import os

encoding = 'utf-8'
path_to_java = os.path.join("jre", "bin", "java.exe")  # Place jre in same directory as code for testing- relative path
#path_to_java = os.path.join("M:", os.sep, "Pyrosequencing", "Pyrosequencing Service", "PCR & PYRO spreadsheets",
                            #"Log", "IT", "PyroService Worklist Program", "jre", "bin", "java.exe")  # for live- abspath