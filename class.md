
# class中的语法糖

Python内置的@property装饰器就是负责把一个方法变成属性调用的：

@property
    def stdout(self):
        '''
        Returns an open file handle to the stdout representing the Ansible run
        '''
        stdout_path = os.path.join(self.config.artifact_dir, 'stdout')
        if not os.path.exists(stdout_path):
            raise AnsibleRunnerException("stdout missing")
        return open(os.path.join(self.config.artifact_dir, 'stdout'), 'r')

参见：https://www.liaoxuefeng.com/wiki/1016959663602400/1017502538658208

