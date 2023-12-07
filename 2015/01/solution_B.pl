#!/usr/bin/perl
use warnings; use strict;

my $pos = 0;
my $level = 0;
my %v = ('(', 1, ')', -1);

for my $c (split '', scalar <STDIN>) {
  $pos++;
  $level += $v{$c};
  if ($level < 0) {
    print "$pos\n";
    exit 0;
  }
}
