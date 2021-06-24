import pandas as pd 
import numpy as np 
import json 
from App_logger.logging import logger_app
import re 

class TrainDataValidation:
    def __init__(self , path):
        self.path = path 
        self.Schema_path = 'Put_SchemaPath_here'
        self.logging = logger_app()

    def get_training_Schema_params(self):
        ''' Method : get_training_Schema_params
            description : This method will read the Training Schemafile And returns it's Parameters..

        '''
        try : 
            with open (self.Schema_path , 'r') as f:
                schema_dict = json.load(f)
                f.close()

            pattern = schema_dict['SampleFileName']
            LengthOfDateStampInFile = schema_dict["LengthOfDateStampInFile"]
            LengthOfTimeStampInFile = schema_dict["LengthOfTimeStampInFile"]
            NumberofColumns     = schema_dict["NumberofColumns"]
            column_names = schema_dict["ColName"]

            logfile_path = 'Training_Logs/valuesfromSchemaValidationLog.txt'
            file_log = open(logfile_path,"a+")
            massage = "LengthOfDateStampInFile:: %s" %LengthOfDateStampInFile + "\t" + "LengthOfTimeStampInFile:: %s" % LengthOfTimeStampInFile +"\t " + "NumberofColumns:: %s" % NumberofColumns + "\n"
            self.logger.log( file_log , massage )
            file_log.close()

        except ValueError:
            log_file_path = "Training_Logs/valuesfromSchemaValidationLog.txt"
            file_log = open(log_file_path ,"a+")
            massage = "ValueError : Value not found inside schema_training.json"
            self.logger.log(file_log , massage)
            file_log.close()
            raise ValueError

        except KeyError:
            log_file_path = "Training_Logs/valuesfromSchemaValidationLog.txt"
            file_log = open(log_file_path, "a+")
            massage = "KeyError:Key value error incorrect key passed"
            self.logger.log(file_log, massage)
            file_log.close()
            raise KeyError

        except Exception as e:
            log_file_path = "Training_Logs/valuesfromSchemaValidationLog.txt"
            file_log = open(log_file_path , 'a+')
            self.logger.log(file_log, str(e))
            file_log.close()
            raise e

        return  LengthOfDateStampInFile, LengthOfTimeStampInFile, column_names, NumberofColumns
        










        except Exception as e:
            raise e 


        















































if __name__ == "__main__":
    a  = TrainDataValidation('Pathishere')
    a.get_training_Schema_params()