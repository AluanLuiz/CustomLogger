import logging
import os

def create_logger(name, file, level=logging.INFO):
    """
    Creates and returns a custom logger.
    
    'name' - Set the log type for internal separation, 
            for example: Access, error and record.
    'file' - defines which file will be stored;
    'level' - by default INFO, use ERROR, DEBUG or WARNING for other levels;
    """
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    handler_file = logging.FileHandler(specificfile(file))
    
    format= logging.Formatter("%(asctime)s -- %(levelname)s : %(message)s")
    handler_file.setFormatter(format)
    
    logger.addHandler(handler_file)
    
    return logger
    

def specificfile(file):
    """
    Default directory and files.
    'userLog'-  Access logs, movement and records of relevant 
                activities of the active user.
                
    Add or modify at your own risk.
    """
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    if file=="error":
        error_log = os.path.join(log_dir, "errors.log")
        return error_log
    elif file == "user":
        user_log =  os.path.join(log_dir, "userLog.log")
        return user_log
    else:
        others_log = os.path.join(log_dir, "others.log")
        return others_log