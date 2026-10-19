from dotenv import load_dotenv
import os
from contracts.enum.Etype_export import EtypeExport
from contracts.enum.Etype_period_of_day import EtypePeriodOfDay
from contracts.enum.Etype_split_pattern import EtypeSplitPattern

class Settings:
    """
        Define the main config for the worker
    """

    def __init__(self):
        """
            Main constructor
            Some variables only use a reference from a enumarate

            file_path => is the path for the csv folder
            type_split_pattern => is the type of split for the csv file, for example  | ; ,
            days_before_the_message => the numbers of days needed, before send a message
            include_preparation => if is necessary include the preparation text
            type_period_of_day => 1 is Morning, 2 is afternoon, 3 is evening, 4 is nigth
            generate_export => use true if you want to generate a export file, you must active the next flag and edit output_export
            type_export => the type of file to export
            output_export => the file to generate the export
        """
        load_dotenv()
        self.app_name:str                            = os.getenv("APP_NAME")
        self.app_version:str                         = os.getenv("APP_VERSION")
        self.file_path:str                           = os.getenv("FILE_PATH")
        self.type_split_pattern: EtypeSplitPattern   = int(os.getenv("TYPE_SPLIT_PATTERN"))
        self.days_before_the_message: int            = int(os.getenv("DAYS_BEFORE_THE_MESSAGE"))
        self.include_preparation: bool               = bool(os.getenv("INCLUDE_PREPARATION"))
        self.type_period_of_day: EtypePeriodOfDay    = int(os.getenv("TYPE_PERIOD_OF_DAY"))
        self.generate_export: bool                   = bool(os.getenv("GENERATE_EXPORT"))
        self.type_export: EtypeExport                = int(os.getenv("TYPE_EXPORT"))
        self.output_export: str                      = os.getenv("OUTPUT_EXPORT")
        self.process_batch_limit: int                = int(os.getenv("PROCESS_BATCH_LIMIT", 50))
