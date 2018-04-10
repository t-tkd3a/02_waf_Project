#! /usr/bin/env python
# encoding: utf-8

def hello(ctx):
	print('waf. hello world.')

def ping(ctx):
	print('-> ping from ' + ctx.path.abspath())

def options(opt):
        opt.load('compiler_cxx')

def configure(conf):
        conf.load('compiler_cxx')

def build(bld):
        bld.program(
                source       = 'main.cpp', 
                target       = 'appname', 

                includes     = ['.'], 
                defines      = ['LINUX=1', 'BIDULE'],

                lib          = ['m'], 
                libpath      = ['/usr/lib'],
                linkflags    = ['-g'], 

                install_path = None, 
                cflags       = ['-O2', '-Wall'], 
                cxxflags     = ['-O0', '-g' , '-Wall'],

        )
