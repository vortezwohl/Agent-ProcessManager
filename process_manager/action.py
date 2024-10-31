import psutil


def show_all_processes(**kwargs) -> str:
    """
        Retrieves and displays information about all running processes on the system.

        This function iterates over all processes using psutil.process_iter, collecting
        details such as process ID, name, user, status, creation time, CPU usage, and
        memory usage. The collected data is stored in a dictionary and returned as a
        string representation.

        Args:
            **kwargs: Accepts any keyword arguments (currently not used).

        Returns:
            str: A string representation of a dictionary containing process information.

        Note:
            This function assumes that psutil is installed and imported. It also assumes
            that the system has permission to access process information.
    """
    all_processes = dict()
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        all_processes[proc.name()] = {
            'pid': proc.pid,
            'name': proc.name(),
            'user': proc.username(),
            'status': proc.status(),
            'create_time': proc.create_time(),
            'cpu_percent': proc.cpu_percent(),
            'memory_percent': proc.memory_percent()
        }
    return str(all_processes)


def get_process_by_name(name: str) -> str:
    """
        Retrieves process information by name.

        Args:
            name (str): The name of the process to find.

        Returns:
            str: A string representation of the process info dictionary.
    """
    result = dict()
    for proc in psutil.process_iter(['name']):
        if proc.name() == name:
            result[proc.name()] = {
                'pid': proc.pid,
                'name': proc.name(),
                'user': proc.username(),
                'status': proc.status(),
                'create_time': proc.create_time(),
                'cpu_percent': proc.cpu_percent(),
                'memory_percent': proc.memory_percent()
            }
    return str(result)
