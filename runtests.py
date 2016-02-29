#!/usr/bin/env python
import sys
import subprocess


FLAKE8_ARGS = ['coreapidocs/', 'tests/', '--ignore=E501']
NOSETESTS_ARGS = ['--with-coverage', '--cover-package=coreapidocs', '--cover-erase', '--cover-html']


def exit_on_failure(command, message=None):
    if command:
        sys.exit(command)


def flake8_main(args):
    print('Running: flake8 %s' % " ".join(FLAKE8_ARGS))
    command = subprocess.call(['flake8'] + args)
    print("\n" if command else "Success. flake8 passed.\n")
    return command


def run_tests(args):
    print('Running: nosetests %s' % " ".join(NOSETESTS_ARGS))
    command = subprocess.call(['nosetests'] + args)
    return command

exit_on_failure(flake8_main(FLAKE8_ARGS))
exit_on_failure(run_tests(NOSETESTS_ARGS))
