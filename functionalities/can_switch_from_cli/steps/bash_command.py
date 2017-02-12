import subprocess


class BashCommand():

    def __init__(self, command_body='', v=0, r=None, command_pipe_in=''):
        self.command = command_body

        self.command_pipe_in = command_pipe_in
        self.verbose = v
        self.return_parameter = r

    def check_for_pipes(self):
        if '|' in self.command:
            self.command_pipe_in = self.command[self.command.find('|')+1:]
            self.command = self.command[:self.command.find('|')]
        
    def run(self):
        self.check_for_pipes()
        proc1 = subprocess.Popen(self.command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        self.return_code = proc1.wait()
        pipe_return_code = 0
        if self.command_pipe_in:
            proc2 = subprocess.Popen(self.command_pipe_in.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=proc1.stdout)
            pipe_return_code = proc2.wait()
        self.return_code = self.return_code + pipe_return_code
        self.execution_stdout = proc1.stdout.read()
        self.execution_stderr = proc1.stderr.read()
        if self.command_pipe_in:
            self.execution_stdout = proc2.stdout.read()
            self.execution_stderr = proc2.stderr.read()
        if self.return_parameter == 'output':
            self.handle_results()
            return self.execution_stdout
        elif self.return_parameter == 'error':
            self.handle_results(raise_on_error=False)
            return self.return_code
        else:
            self.handle_results()
            return self.return_code
        
    def handle_results(self, raise_on_error=True):
        if self.verbose >= 2:
            print(self.execution_stdout)
        if self.verbose >= 1:
            print(self.execution_stderr)
        try:
            assert self.return_code == 0
        except AssertionError:
            Prompt.write_to_prompt('!!!Something went wrong there!!!')
            if raise_on_error:
                raise
            else:
                return 1
        return 0
