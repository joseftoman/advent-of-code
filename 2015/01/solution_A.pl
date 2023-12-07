#!/usr/bin/perl
use warnings; use strict;

my %a = ('(', 0, ')', 0);
map $a{$_}++, split '', scalar <STDIN>;
print $a{'('} - $a{')'}, "\n";
