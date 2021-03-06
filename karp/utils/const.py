# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'tchen'

MATCH_TEXT = r'(?P<text>[\-_0-9a-zA-Z]+)'
MATCH_TEXT1 = r'(?P<text1>[\-_0-9a-zA-Z]+)'
MATCH_PK = r'(?P<pk>[0-9]+)'

CASE_TYPE_CODING = 0
CASE_TYPE_DEBUG = 1
CASE_TYPE_DATA_STRUCTURE = 2
CASE_TYPE_PROBLEM_SOLVING = 3

CASE_TYPE_CHOICES = (
    (CASE_TYPE_CODING, 'Coding Skill'),
    (CASE_TYPE_DEBUG, 'Debug Skill'),
    (CASE_TYPE_DATA_STRUCTURE, 'Data Structure Skill'),
    (CASE_TYPE_PROBLEM_SOLVING, 'Problem Solving Skill'),
)


CASE_LEVEL_NOVICE = 1
CASE_LEVEL_ADVANCED_BEGINNER = 2
CASE_LEVEL_COMPETENT = 3
CASE_LEVEL_PROFICIENT_PRACTITIONER = 4
CASE_LEVEL_EXPERT = 5

CASE_LEVEL_CHOICES = (
    (CASE_LEVEL_NOVICE, 'Novice'),
    (CASE_LEVEL_ADVANCED_BEGINNER, 'Advanced Beginner'),
    (CASE_LEVEL_COMPETENT, 'Competent'),
    (CASE_LEVEL_PROFICIENT_PRACTITIONER, 'Proficient Practitioner'),
    (CASE_LEVEL_EXPERT, 'Expert'),
)

CASE_CATEGORY_GENERAL = 0
CASE_CATEGORY_TCPIP = 1
CASE_CATEGORY_SECURITY = 2
CASE_CATEGORY_DRIVER = 3
CASE_CATEGORY_APPLICATION = 4
CASE_CATEGORY_PERFORMANCE = 5

CASE_CATEGORY_CHOICES = (
    (CASE_CATEGORY_GENERAL, 'General'),
    (CASE_CATEGORY_TCPIP, 'TCP/IP Stack'),
    (CASE_CATEGORY_SECURITY, 'Security'),
    (CASE_CATEGORY_DRIVER, 'Device Driver'),
    (CASE_CATEGORY_APPLICATION, 'Application'),
    (CASE_CATEGORY_PERFORMANCE, 'Performance'),
)

CASE_LANG_C = 0
CASE_LANG_TCL = 1
CASE_LANG_SHELL = 2
CASE_LANG_PYTHON = 3
CASE_LANG_PERL = 4
CASE_LANG_JAVA = 5
CASE_LANG_RUBY = 6
CASE_LANG_ERLANG = 7
CASE_LANG_JAVASCRIPT = 8

CASE_LANG_CHOICES = (
    (CASE_LANG_C, 'C/C++'),
    (CASE_LANG_TCL, 'TCL'),
    (CASE_LANG_SHELL, 'Shell'),
    (CASE_LANG_PYTHON, 'Python'),
    (CASE_LANG_PERL, 'Perl'),
    (CASE_LANG_JAVA, 'Java'),
    (CASE_LANG_RUBY, 'Ruby'),
    (CASE_LANG_ERLANG, 'ERLang'),
    (CASE_LANG_JAVASCRIPT, 'Javascript'),
)

CASE_LANG_EXTENTIONS = [
    ['.c', '.h', '.cpp', '.cc'],
    ['.tcl'],
    ['.sh'],
    ['.py'],
    ['.java'],
    ['.ruby'],
    ['.erl'],
    ['.js'],
]
