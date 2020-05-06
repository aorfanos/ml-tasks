# Task report/comments

### task 1
Decided to go with `sysctl` rather than the `pam_limits` module, because of persistence in the OS.
When attempted using pam_limits and '\*' domain, the change did not persist through `vagrant ssh` sessions.

### task 2
Sample `vagrant up --provision` run:
```
Bringing machine 'pam_limits' up with 'virtualbox' provider...
==> pam_limits: Checking if box 'generic/centos7' version '2.0.6' is up to date...
==> pam_limits: A newer version of the box 'generic/centos7' for provider 'virtualbox' is
==> pam_limits: available! You currently have version '2.0.6'. The latest is version
==> pam_limits: '3.0.0'. Run `vagrant box update` to update.
==> pam_limits: Running provisioner: ansible...
    pam_limits: Running ansible-playbook...
 [WARNING]: Found variable using reserved name: hosts


PLAY [pam_limits] **************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ulimit.test]

TASK [shell] *******************************************************************
changed: [ulimit.test]

TASK [Display initial ulimit -n value] *****************************************
ok: [ulimit.test] => {
    "msg": "Current ulimit -n is :4000"
}

TASK [Update ulimit] ***********************************************************
ok: [ulimit.test]

TASK [shell] *******************************************************************
changed: [ulimit.test]

TASK [Display changed value] ***************************************************
ok: [ulimit.test] => {
    "msg": "Ulimit for open files (-n) option is: 256000"
}

PLAY RECAP *********************************************************************
ulimit.test                : ok=6    changed=2    unreachable=0    failed=0   

```

### task 3
- [Demo](https://asciinema.org/a/Km7gxpWi7ZaACgmu6ij7sEath)
- Output:
```
(u'1588796622', u'85.75.14.126', u'Athens', u'I', u'Attica', u'Europe/Athens', 23.7353, 37.9842, 0.0, u'GR', u'Greece', u'')
```

### task 4
- [Demo](https://asciinema.org/a/DxEMS2hu4sw6OdCn3rd8f1HWo)
- docker image size: 60.6MB
```
REPOSITORY                       TAG                 IMAGE ID            CREATED             SIZE
aorfanos/fetch_ip_info           latest              1e7830c9eb14        11 seconds ago      60.6 MB
```
